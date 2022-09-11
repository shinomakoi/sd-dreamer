import argparse
import os
import re
import time
from contextlib import contextmanager, nullcontext
from itertools import islice
from random import randint

import k_diffusion as K
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from einops import rearrange, repeat
from ldm.util import instantiate_from_config
from omegaconf import OmegaConf
from PIL import Image
from pytorch_lightning import seed_everything
from torch import autocast
from torchvision.utils import make_grid
from tqdm import tqdm, trange
from transformers import logging
from pathlib import Path
from ldm.models.diffusion.ddim import DDIMSampler

from scripts.optimUtils import logger, split_weighted_subprompts

logging.set_verbosity_error()


def load_img(path, h0, w0):

    image = Image.open(path).convert("RGB")
    w, h = image.size

    print(f"loaded input image of size ({w}, {h}) from {path}")
    if h0 is not None and w0 is not None:
        h, w = h0, w0

    # resize to integer multiple of 32
    w, h = map(lambda x: x - x % 64, (w, h))

    print(f"New image size ({w}, {h})")
    image = image.resize((w, h), resample=Image.LANCZOS)
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.0 * image - 1.0


def img2img_opti_predict(prompt, steps, iterations, batch, seed, precision, rows, outpath, scale, width, height, set_sampler, init_img, strength, turbo):
    configy_path=(os.path.dirname(os.path.realpath(__file__)))

    config = Path(configy_path)/'v1-inference.yaml'

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--skip_grid",
        action="store_true",
        help="do not save a grid, only individual samples. Helpful when evaluating lots of samples",
    )

    parser.add_argument(
        "--ddim_eta",
        type=float,
        default=0.0,
        help="ddim eta (eta=0.0 corresponds to deterministic sampling",
    )

    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        help="CPU or GPU (cuda/cuda:0/cuda:1/...)",
    )
    parser.add_argument(
        "--unet_bs",
        type=int,
        default=1,
        help="Slightly reduces inference time at the expense of high VRAM (value > 1 not recommended )",
    )
    parser.add_argument(
        "--turbo",
        action="store_true",
        help="Reduces inference time on the expense of 1GB VRAM",
    )

    parser.add_argument(
        "--plms",
        action='store_true',
        help="Enables PLMS sampler.",
    )
    parser.add_argument(
        "--sampler",
        type=str,
        help="Choose the sampler used",
        choices=["lms", "euler", "euler_a", "dpm", "dpm_a", "heun"],
        default="lms"
    )

    opt = parser.parse_args()

    if set_sampler != 'plms' and set_sampler!= 'ddim':

        ksamplers = {'k_lms': K.sampling.sample_lms,
                    'k_euler': K.sampling.sample_euler,
                    'k_euler_a': K.sampling.sample_euler_ancestral,
                    'k_dpm_2': K.sampling.sample_dpm_2,
                    'k_dpm_2_a': K.sampling.sample_dpm_2_ancestral,
                    'k_heun': K.sampling.sample_heun}

        sampler = ksamplers[set_sampler]

    tic = time.time()
    os.makedirs(outpath, exist_ok=True)
    outpath = outpath
    grid_count = len(os.listdir(outpath)) - 1

    # if seed == None:
    #     seed = randint(0, 1000000)
    # seed_everything(seed)

    # Logging
    logger(vars(opt), log_csv="logs/img2img_logs.csv")
    from scripts.launcher_opti import model, modelCS, modelFS


    assert os.path.isfile(init_img)
    init_image = load_img(init_img, height, width).to(opt.device)


    # As the model no longer self-seeds on initialization, we must do this should we
    # reject the built-in sampling method.
    if set_sampler != 'plms' or 'ddim':
        model.make_schedule(ddim_num_steps=steps,
                            ddim_eta=opt.ddim_eta, verbose=False)
    from scripts.launcher_opti import CFGDenoiser


    model_wrap = K.external.CompVisDenoiser(model)
    sigma_min, sigma_max = model_wrap.sigmas[0].item(
    ), model_wrap.sigmas[-1].item()


    if opt.device != 'cpu' and precision == "autocast":
        model.half()
        modelCS.half()
        modelFS.half()
        init_image = init_image.half()

    batch_size = batch
    n_rows = rows if rows > 0 else batch_size
    assert prompt is not None
    data = [batch_size * [prompt]]

    modelFS.to(opt.device)

    init_image = repeat(init_image, "1 ... -> b ...", b=batch_size)
    init_latent = modelFS.get_first_stage_encoding(
        modelFS.encode_first_stage(init_image))  # move to latent space

    if opt.device != "cpu":
        mem = torch.cuda.memory_allocated() / 1e6
        modelFS.to("cpu")
        while torch.cuda.memory_allocated() / 1e6 >= mem:
            time.sleep(1)

    assert 0.0 <= strength <= 1.0, "can only work with strength in [0.0, 1.0]"
    t_enc = int(strength * steps)
    print(f"target t_enc is {t_enc} steps")

    if precision == "autocast" and opt.device != "cpu":
        precision_scope = autocast
    else:
        precision_scope = nullcontext

    seeds = ""
    with torch.no_grad():

        all_samples = list()
        for n in trange(iterations, desc="Sampling"):
            for prompts in tqdm(data, desc="data"):

                sample_path = os.path.join(outpath, "img2img_samples")
                os.makedirs(sample_path, exist_ok=True)
                base_count = len(os.listdir(sample_path))
                grid_count = len(os.listdir(outpath)) - 1

                with precision_scope("cuda"):
                    modelCS.to(opt.device)
                    uc = None
                    if scale != 1.0:
                        uc = modelCS.get_learned_conditioning(
                            batch_size * [""])
                    if isinstance(prompts, tuple):
                        prompts = list(prompts)

                    subprompts, weights = split_weighted_subprompts(prompts[0])
                    if len(subprompts) > 1:
                        c = torch.zeros_like(uc)
                        totalWeight = sum(weights)
                        # normalize each "sub prompt" and add it
                        for i in range(len(subprompts)):
                            weight = weights[i]
                            # if not skip_normalize:
                            weight = weight / totalWeight
                            c = torch.add(c, modelCS.get_learned_conditioning(
                                subprompts[i]), alpha=weight)
                    else:
                        c = modelCS.get_learned_conditioning(prompts)

                    if opt.device != "cpu":
                        mem = torch.cuda.memory_allocated() / 1e6
                        modelCS.to("cpu")
                        while torch.cuda.memory_allocated() / 1e6 >= mem:
                            time.sleep(1)

                    samples_ddim = None

                    if set_sampler != 'plms' and set_sampler!= 'ddim':
                        sigmas = model_wrap.get_sigmas(steps)
                        # changes manual seeding procedure
                        torch.manual_seed(seed)
                        # sigmas = K.sampling.get_sigmas_karras(steps, sigma_min, sigma_max, device=device)
                        noise = torch.randn_like(
                            init_latent) * sigmas[steps - t_enc - 1]  # for GPU draw
                        xi = init_latent + noise
                        sigma_sched = sigmas[steps - t_enc - 1:]
                        # x = torch.randn([batch, *shape]).to(device) * sigmas[0] # for CPU draw
                        model_wrap_cfg = CFGDenoiser(model_wrap)
                        extra_args = {'cond': c,
                                      'uncond': uc, 'cond_scale': scale}
                        samples_ddim = sampler(
                            model_wrap_cfg, xi, sigma_sched, extra_args=extra_args, disable=False)

                    else:
                        sampler = DDIMSampler(model)

                        z_enc = model.stochastic_encode(init_latent, torch.tensor(
                            [t_enc]*batch_size).to(opt.device), seed, opt.ddim_eta, steps)
                        samples_ddim = model.decode(z_enc, c, t_enc, unconditional_guidance_scale=scale,
                                                    unconditional_conditioning=uc,)

                    modelFS.to(opt.device)
                    print("saving images")
                    for i in range(batch_size):

                        x_samples_ddim = modelFS.decode_first_stage(
                            samples_ddim[i].unsqueeze(0))
                        x_sample = torch.clamp(
                            (x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                        x_sample = 255.0 * \
                            rearrange(
                                x_sample[0].cpu().numpy(), "c h w -> h w c")
                        for r in ((">", ""), ("<", ""), ("<", ""), ("|", ""), ("?", ""), ("*", ""), ('"', ""), (',', ""), ('.', ""), 
                                ('\n', ""), (' ', '_'),('/', '_'),('\\', '_'),(':', '_')):
                            prompt = prompt.replace(*r).strip()
                        Image.fromarray(x_sample.astype(np.uint8)).save(
                                os.path.join(sample_path, f"{base_count:05}_{str(seed)}_{prompt[:120]}.png"))
                        seeds += str(seed) + ","
                        seed += 1
                        base_count += 1

                    if opt.device != "cpu":
                        mem = torch.cuda.memory_allocated() / 1e6
                        modelFS.to("cpu")
                        while torch.cuda.memory_allocated() / 1e6 >= mem:
                            time.sleep(1)

                    del samples_ddim
                    print("memory_final = ", torch.cuda.memory_allocated() / 1e6)

    toc = time.time()

    time_taken = (toc - tic) / 60.0

    print(
        (
            "Samples finished in {0:.2f} minutes and exported to "
            + sample_path
            + "\n Seeds used = "
            + seeds[:-1]
        ).format(time_taken)
    )


def img2img_opti(*img2img_args):

    img2img_opti_predict(*img2img_args)
