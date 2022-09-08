import argparse
import os
import time
from contextlib import nullcontext

import k_diffusion as K
import numpy as np
import torch
from einops import rearrange
from ldm.models.diffusion.ddim import DDIMSampler
from ldm.models.diffusion.plms import PLMSSampler
from PIL import Image
from torch import autocast
from torchvision.utils import make_grid
from tqdm import tqdm, trange

from scripts.txt2img_k_sdd_batch import (CFGDenoiser, create_random_tensors,
                                         model)

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
    help="downsampling factor",
)

opt = parser.parse_args()


def txt2img_predict(prompt, steps, iterations, batch, seed, precision, rows, outpath, scale, width, height, set_sampler):
    if set_sampler == 'k_lms' or set_sampler == 'k_euler' or set_sampler == 'k_euler_a' or set_sampler == 'k_dpm_2' or set_sampler == 'k_dpm_2_a' or set_sampler == 'k_heun':
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
        sampler = ksamplers[set_sampler]

        print('arguments: ', prompt, steps, iterations,
              batch, seed, precision, rows, outpath, scale, width, height, set_sampler)

        batch_size = batch
        n_rows = rows if rows > 0 else batch_size

        prompt = prompt
        assert prompt is not None
        data = batch_size * [prompt]

        sample_path = os.path.join(outpath, 'samples')
        os.makedirs(sample_path, exist_ok=True)
        base_count = len(os.listdir(sample_path))
        grid_count = len(os.listdir(outpath)) - 1

        precision_scope = autocast if precision == "autocast" else nullcontext
        with torch.no_grad(), precision_scope("cuda"), model.ema_scope():
            all_samples = list()
            for n in trange(iterations, desc="Sampling"):
                seeds = list(seed + n*batch_size +
                             i for i in range(batch_size))
                uc = None
                if scale != 1.0:
                    uc = model.get_learned_conditioning(batch_size * [""])
                if isinstance(data, tuple):
                    data = list(data)
                c = model.get_learned_conditioning(data)

                shape = [opt.C, height // opt.f, width // opt.f]

                sigmas = model_wrap.get_sigmas(steps)
                x = create_random_tensors(
                    shape, seeds, device=device) * sigmas[0]
                model_wrap_cfg = CFGDenoiser(model_wrap)
                extra_args = {'cond': c, 'uncond': uc, 'cond_scale': scale}

                samples_ddim = sampler(
                    model_wrap_cfg, x, sigmas, extra_args=extra_args, disable=False)
                x_samples_ddim = model.decode_first_stage(samples_ddim)
                x_samples_ddim = torch.clamp(
                    (x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)

                for x_sample in x_samples_ddim:
                    x_sample = 255. * \
                        rearrange(x_sample.cpu().numpy(), 'c h w -> h w c')
                    Image.fromarray(x_sample.astype(np.uint8)).save(
                        os.path.join(sample_path, f"{base_count:05}.png"))
                    base_count += 1

                all_samples.append(x_samples_ddim)

            # additionally, save as grid
            grid = torch.stack(all_samples, 0)
            grid = rearrange(grid, 'n b c h w -> (n b) c h w')
            grid = make_grid(grid, nrow=n_rows)

            # to image
            grid = 255. * rearrange(grid, 'c h w -> h w c').cpu().numpy()
            Image.fromarray(grid.astype(np.uint8)).save(
                os.path.join(outpath, f'grid-{grid_count:04}.png'))
            grid_count += 1

        print(f"Your samples are ready and waiting for you here: \n{outpath} \n"
              f" \nEnjoy.")

    else:
        if set_sampler == 'plms':
            sampler = PLMSSampler(model)
        else:
            sampler = DDIMSampler(model)

        os.makedirs(outpath, exist_ok=True)
        outpath = outpath

        batch_size = batch
        n_rows = rows if rows > 0 else batch_size

        assert prompt is not None
        data = [batch_size * [prompt]]

        sample_path = os.path.join(outpath, 'samples')
        os.makedirs(sample_path, exist_ok=True)
        base_count = len(os.listdir(sample_path))
        grid_count = len(os.listdir(outpath)) - 1

        start_code = None

        opt.ddim_eta = 0.0
        precision = 'autocast'

        precision_scope = autocast if precision == "autocast" else nullcontext
        with torch.no_grad():
            with precision_scope("cuda"):
                with model.ema_scope():
                    tic = time.time()
                    all_samples = list()
                    for n in trange(iterations, desc="Sampling"):
                        for prompts in tqdm(data, desc="data"):
                            uc = None
                            if scale != 1.0:
                                uc = model.get_learned_conditioning(
                                    batch_size * [""])
                            if isinstance(prompts, tuple):
                                prompts = list(prompts)
                            c = model.get_learned_conditioning(prompts)
                            shape = [opt.C, height // opt.f, width // opt.f]
                            samples_ddim, _ = sampler.sample(S=steps,
                                                             conditioning=c,
                                                             batch_size=batch,
                                                             shape=shape,
                                                             verbose=False,
                                                             unconditional_guidance_scale=scale,
                                                             unconditional_conditioning=uc,
                                                             eta=opt.ddim_eta,
                                                             x_T=start_code)

                            x_samples_ddim = model.decode_first_stage(
                                samples_ddim)
                            x_samples_ddim = torch.clamp(
                                (x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)

                            for x_sample in x_samples_ddim:
                                x_sample = 255. * \
                                    rearrange(x_sample.cpu().numpy(),
                                              'c h w -> h w c')
                                Image.fromarray(x_sample.astype(np.uint8)).save(
                                    os.path.join(sample_path, f"{base_count:05}.png"))
                                base_count += 1

                            all_samples.append(x_samples_ddim)

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


def txt2img(*txt2img_args):

    txt2img_predict(*txt2img_args)
