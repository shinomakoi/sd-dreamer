import argparse
import os
from contextlib import nullcontext
from itertools import islice
from pathlib import Path

import k_diffusion as K
import numpy as np
import torch
import torch.nn as nn
from einops import rearrange
from ldm.util import instantiate_from_config
from omegaconf import OmegaConf
from PIL import Image
from torch import autocast
from torchvision.utils import make_grid
from tqdm import trange
import sys
import configparser


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def load_model_from_config(config, ckpt, verbose=False):
    print(f"Loading model from {ckpt}")
    pl_sd = torch.load(ckpt, map_location="cpu")
    if "global_step" in pl_sd:
        print(f"Global Step: {pl_sd['global_step']}")
    sd = pl_sd["state_dict"]
    model = instantiate_from_config(config.model)
    _, _ = model.load_state_dict(sd, strict=False)
    model.cuda()
    model.eval()
    return model


class CFGDenoiser(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.inner_model = model

    def forward(self, x, sigma, uncond, cond, cond_scale):
        x_in = torch.cat([x] * 2)
        sigma_in = torch.cat([sigma] * 2)
        cond_in = torch.cat([uncond, cond])
        uncond, cond = self.inner_model(x_in, sigma_in, cond=cond_in).chunk(2)
        return uncond + (cond - uncond) * cond_scale


def create_random_tensors(shape, seeds, device):
    xs = []
    for seed in seeds:
        torch.manual_seed(seed)
        xs.append(torch.randn(shape, device=device))
    x = torch.stack(xs, 0)
    return x


parser = argparse.ArgumentParser()

parser.add_argument(
    "--prompt",
    type=str,
    nargs="?",
    default="a painting of a virus monster playing guitar",
    help="the prompt to render"
)
parser.add_argument(
    "--outdir",
    type=str,
    nargs="?",
    help="dir to write results to",
    default="outputs/txt2img-samples"
)
parser.add_argument(
    "--skip_grid",
    action='store_true',
    help="do not save a grid, only individual samples. Helpful when evaluating lots of samples",
)
parser.add_argument(
    "--skip_save",
    action='store_true',
    help="do not save individual samples. For speed measurements.",
)
parser.add_argument(
    "--ddim_steps",
    type=int,
    default=50,
    help="number of ddim sampling steps",
)
parser.add_argument(
    "--fixed_code",
    action='store_true',
    help="if enabled, uses the same starting code across samples ",
)
parser.add_argument(
    "--ddim_eta",
    type=float,
    default=0.0,
    help="ddim eta (eta=0.0 corresponds to deterministic sampling",
)
parser.add_argument(
    "--n_iter",
    type=int,
    default=2,
    help="sample this often",
)
parser.add_argument(
    "--H",
    type=int,
    default=512,
    help="image height, in pixel space",
)
parser.add_argument(
    "--W",
    type=int,
    default=512,
    help="image width, in pixel space",
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
    "--n_samples",
    type=int,
    default=3,
    help="how many samples to produce for each given prompt. A.k.a. batch size",
)
parser.add_argument(
    "--n_rows",
    type=int,
    default=0,
    help="rows in the grid (default: n_samples)",
)
parser.add_argument(
    "--scale",
    type=float,
    default=7.5,
    help="unconditional guidance scale: eps = eps(x, empty) + scale * (eps(x, cond) - eps(x, empty))",
)
parser.add_argument(
    "--dyn",
    type=float,
    help="dynamic thresholding from Imagen, in latent space (TODO: try in pixel space with intermediate decode)",
)
parser.add_argument(
    "--from-file",
    type=str,
    help="if specified, load prompts from this file",
)
parser.add_argument(
    "--config",
    type=str,
    default="configs/stable-diffusion/v1-inference.yaml",
    help="path to config which constructs model",
)
parser.add_argument(
    "--ckpt",
    type=str,
    default="models/ldm/stable-diffusion-v1/model.ckpt",
    help="path to checkpoint of model",
)
parser.add_argument(
    "--seed",
    type=int,
    default=None,
    help="the seed (for reproducible sampling)",
)
parser.add_argument(
    "--sampler",
    type=str,
    help="Choose the sampler used",
    choices=["lms", "euler", "euler_a", "dpm", "dpm_a", "heun"],
    default="lms"
)
parser.add_argument(
    "--precision",
    type=str,
    help="evaluate at this precision",
    choices=["full", "autocast"],
    default="autocast"
)
opt = parser.parse_args()

# if opt.seed is None:
#     opt.seed = hash(opt)

config = configparser.ConfigParser()
settings_file = ('sd_dreamer/settings.ini')
config.read('sd_dreamer/settings.ini')
chkpt_ini=config.get('Settings', 'ckpt_path')

config = OmegaConf.load(f"{opt.config}")
model = load_model_from_config(config, f"{chkpt_ini}")
print(chkpt_ini)

if opt.precision == "autocast":
    model = model.half()

os.makedirs(opt.outdir, exist_ok=True)
outpath = opt.outdir

from scripts.txt2img_k_sdd import txt2img
from scripts.img2img_k_sdd import img2img
from scripts.txt2imghd import txt2imghd


def torch_gc():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
torch_gc()

def txt2img_main(*txt2img_args):
    txt2img(*txt2img_args)
    torch_gc()

def img2img_main(*img2img_args):

    img2img(*img2img_args)
    torch_gc()

def txt2imghd_main(*txt2imghd_args):
    txt2imghd(*txt2imghd_args)
    torch_gc()