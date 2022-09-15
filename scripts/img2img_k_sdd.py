"""make variations of input image"""

import argparse
import os
import threading
import time
from contextlib import nullcontext

import accelerate
import k_diffusion as K
import numpy as np
import PIL
import torch
from einops import rearrange, repeat
from PIL import Image
from pytorch_lightning import seed_everything
from torch import autocast
from torchvision.utils import make_grid
from tqdm import tqdm, trange

from scripts.launcher import CFGDenoiser, model

def torch_gc():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
    print('Finished. Torch cache cleaned')

parser = argparse.ArgumentParser()

parser.add_argument(
    "--C",
    type=int,
    default=4,
    help="latent channels",
)
parser.add_argument(
    "--f",
    type=int,
    default=8,
    help="downsampling factor, most often 8 or 16",
)


def img2img_predict(prompt, steps, iterations, batch, seed, precision, rows, outpath, scale, width, height, set_sampler, init_img, strength, turbo):

    device = torch.device(
        "cuda") if torch.cuda.is_available() else torch.device("cpu")
    #model = model.to(device)
    ksamplers = {'k_lms': K.sampling.sample_lms,
                 'k_euler': K.sampling.sample_euler,
                 'k_euler_a': K.sampling.sample_euler_ancestral,
                 'k_dpm_2': K.sampling.sample_dpm_2,
                 'k_dpm_2_a': K.sampling.sample_dpm_2_ancestral,
                 'k_heun': K.sampling.sample_heun}

    model_wrap = K.external.CompVisDenoiser(model)

    if set_sampler == 'ddim' or set_sampler == 'plms':
        set_sampler = 'k_lms'
        print('ddim and plms currently not available')

    sampler = ksamplers[set_sampler]

    print('arguments: ', prompt, steps, iterations, batch, seed, precision,
          rows, outpath, scale, width, height, set_sampler, init_img, strength)

    batch_size = batch
    n_rows = rows if rows > 0 else batch_size
    prompt = prompt
    assert prompt is not None
    data = [batch_size * [prompt]]

    def load_img(path):
        image = Image.open(path).convert("RGB")
        w, h = image.size
        print(f"loaded input image of size ({w}, {h}) from {path}")
        w, h = map(lambda x: x - x % 64, (w, h))  # lmao, it's 64 not 32
        image = image.resize(
            (width, height), resample=PIL.Image.Resampling.LANCZOS)
        image = np.array(image).astype(np.float32) / 255.0
        image = image[None].transpose(0, 3, 1, 2)
        image = torch.from_numpy(image).half()
        return 2.*image - 1.

    accelerator = accelerate.Accelerator()
    device = accelerator.device
    seed_everything(seed)
    seeds = torch.randint(-2 ** 63, 2 ** 63 - 1, [accelerator.num_processes])
    torch.manual_seed(seeds[accelerator.process_index].item())

    sample_path = os.path.join(outpath, 'img2img_samples')
    os.makedirs(sample_path, exist_ok=True)
    base_count = len(os.listdir(sample_path))
    grid_count = len(os.listdir(outpath)) - 1

    assert os.path.isfile(init_img)
    init_image = load_img(init_img).to(device)
    init_image = repeat(init_image, '1 ... -> b ...', b=batch_size)
    init_latent = model.get_first_stage_encoding(
        model.encode_first_stage(init_image))  # move to latent space
    x0 = init_latent

    assert 0. <= strength <= 1., 'can only work with strength in [0.0, 1.0]'
    t_enc = int(strength * steps)
    print(f"target t_enc is {t_enc} steps")

    precision_scope = autocast if precision == "autocast" else nullcontext
    with torch.no_grad():
        with precision_scope("cuda"):
            with model.ema_scope():
                tic = time.time()
                all_samples = list()
                for n in trange(iterations, desc="Sampling", disable=not accelerator.is_main_process):
                    for prompts in tqdm(data, desc="data", disable=not accelerator.is_main_process):
                        uc = None
                        if scale != 1.0:
                            uc = model.get_learned_conditioning(
                                batch_size * [""])
                        if isinstance(prompts, tuple):
                            prompts = list(prompts)
                        c = model.get_learned_conditioning(prompts)

                        sigmas = model_wrap.get_sigmas(steps)
                        # torch.manual_seed(seed) # changes manual seeding procedure
                        # sigmas = K.sampling.get_sigmas_karras(steps, sigma_min, sigma_max, device=device)
                        noise = torch.randn_like(
                            x0) * sigmas[steps - t_enc - 1]  # for GPU draw
                        xi = x0 + noise
                        sigma_sched = sigmas[steps - t_enc - 1:]
                        # x = torch.randn([batch, *shape]).to(device) * sigmas[0] # for CPU draw
                        model_wrap_cfg = CFGDenoiser(model_wrap)
                        extra_args = {'cond': c, 'uncond': uc,
                                      'cond_scale': scale}
                        samples_ddim = sampler(
                            model_wrap_cfg, xi, sigma_sched, extra_args=extra_args, disable=not accelerator.is_main_process)
                        x_samples = model.decode_first_stage(samples_ddim)
                        x_samples = torch.clamp(
                            (x_samples + 1.0) / 2.0, min=0.0, max=1.0)
                        x_samples = accelerator.gather(x_samples)

                        if accelerator.is_main_process:
                            for x_sample in x_samples:
                                x_sample = 255. * \
                                    rearrange(x_sample.cpu().numpy(),
                                              'c h w -> h w c')
                                for r in ((">", ""), ("<", ""), ("<", ""), ("|", ""), ("?", ""), ("*", ""), ('"', ""), (',', ""), ('.', ""),
                                          ('\n', ""), (' ', '_'), ('/', '_'), ('\\', '_'), (':', '_')):
                                    prompt = prompt.replace(*r).strip()
                                Image.fromarray(x_sample.astype(np.uint8)).save(
                                    os.path.join(sample_path, f"{base_count:05}_{str(seed)}_{prompt[:120]}.png"))
                                seed += 1
                                base_count += 1

                        if accelerator.is_main_process:
                            all_samples.append(x_samples)

                # additionally, save as grid
                grid = torch.stack(all_samples, 0)
                grid = rearrange(grid, 'n b c h w -> (n b) c h w')
                grid = make_grid(grid, nrow=n_rows)

                # to image
                grid = 255. * \
                    rearrange(grid, 'c h w -> h w c').cpu().numpy()
                Image.fromarray(grid.astype(np.uint8)).save(
                    os.path.join(outpath, f'grid-{grid_count:04}.png'))
                grid_count += 1

                toc = time.time()

    print(f"Your samples are ready and waiting for you here: \n{outpath} \n"
          f" \nEnjoy.")


def img2img(*img2imgargs):
    t1 = threading.Thread(target=img2img_predict, args=(img2imgargs))
    t1.start()
    t1.join()
    torch_gc()