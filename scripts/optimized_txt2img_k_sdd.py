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
from einops import rearrange
from ldm.util import instantiate_from_config
from omegaconf import OmegaConf
from PIL import Image
from pytorch_lightning import seed_everything
from torch import autocast
from torchvision.utils import make_grid
from tqdm import tqdm, trange
from transformers import logging
from pathlib import Path

from scripts.optimUtils import logger, split_weighted_subprompts

logging.set_verbosity_error()

def txt2img_opti_predict(prompt, steps, iterations, batch, seed, precision, rows, outpath, scale, width, height, set_sampler, turbo):

    configy_path=(os.path.dirname(os.path.realpath(__file__)))

    # config = '/home/pigeondave/gits/stable-diffusion-ret2/sd_dreamer/scripts/v1-inference.yaml'
    # ckpt = "/mnt/ext4_data0/trinart2_step60000.ckpt"

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ddim_eta",
        type=float,
        default=0.0,
        help="ddim eta (eta=0.0 corresponds to deterministic sampling",
    )
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
        "--format",
        type=str,
        help="output image format",
        choices=["jpg", "png"],
        default="png",
    )

    parser.add_argument(
        "--plms",
        action='store_true',
        help="Enables PLMS sampler.",
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
    logger(vars(opt), log_csv="logs/txt2img_logs.csv")

    from scripts.launcher_opti import model, modelCS, modelFS

    if turbo:
        print('turbo on')
    else:
        print('turbo off')

    # As the model no longer self-seeds on initialization, we must do this should we
    # reject the built-in sampling method.
    if set_sampler != 'plms' and set_sampler!= 'ddim':
        model.make_schedule(ddim_num_steps=steps,
                            ddim_eta=opt.ddim_eta, verbose=False)

    model_wrap = K.external.CompVisDenoiser(model)
    sigma_min, sigma_max = model_wrap.sigmas[0].item(
    ), model_wrap.sigmas[-1].item()

    model.half()
    modelCS.half()

    start_code = None

    batch_size = batch
    n_rows = rows if rows > 0 else batch_size
    prompt = prompt
    assert prompt is not None
    data = [batch_size * [prompt]]

    if precision == "autocast" and opt.device != "cpu":
        precision_scope = autocast
    else:
        precision_scope = nullcontext

    seeds = ""
    with torch.no_grad():

        all_samples = list()
        for n in trange(iterations, desc="Sampling"):
            for prompts in tqdm(data, desc="data"):

                sample_path = os.path.join(outpath, "txt2img_samples")
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

                    shape = [opt.C, height // opt.f, width // opt.f]

                    if opt.device != "cpu":
                        mem = torch.cuda.memory_allocated() / 1e6
                        modelCS.to("cpu")
                        while torch.cuda.memory_allocated() / 1e6 >= mem:
                            time.sleep(1)

                    # samples_ddim = None
                    # sampler_str = "k_lms"

                    if set_sampler != 'plms' and set_sampler!= 'ddim':
                        # We adapt from the original DDIM setup to k_lms here.
                        sigmas = model_wrap.get_sigmas(steps)
                        from scripts.launcher_opti import CFGDenoiser
                        model_wrap_cfg = CFGDenoiser(model_wrap)

                        torch.manual_seed(seed)

                        x = torch.randn([batch, *shape],
                                        device=opt.device) * sigmas[0]
                        extra_args = {'cond': c,
                                      'uncond': uc, 'cond_scale': scale}

                        samples_ddim = sampler(
                            model_wrap_cfg, x, sigmas, extra_args=extra_args, disable=False)
                    else:
                        sampler_str = "plms"
                        samples_ddim = model.sample(S=steps,
                                                    conditioning=c,
                                                    batch_size=batch,
                                                    seed=seed,
                                                    shape=shape,
                                                    verbose=False,
                                                    unconditional_guidance_scale=scale,
                                                    unconditional_conditioning=uc,
                                                    eta=opt.ddim_eta,
                                                    x_T=start_code)

                    modelFS.to(opt.device)

                    print(samples_ddim.shape)
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

import threading

def txt2img_opti(*txt2img_args):
    t1 = threading.Thread(target=txt2img_opti_predict, args=(txt2img_args))
    t1.start()
    t1.join()