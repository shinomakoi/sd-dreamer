import configparser
import os
from itertools import islice
from pathlib import Path

import torch
import torch.nn as nn
from ldm.util import instantiate_from_config
from omegaconf import OmegaConf


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


settings_path = (os.path.dirname(os.path.realpath(__file__)))
settings_path = (Path(settings_path).parent/'settings.ini')

config = configparser.ConfigParser()
settings_file = (settings_path)
config.read(settings_path)
chkpt_ini = config.get('Settings', 'ckpt_path')

config = 'configs/stable-diffusion/v1-inference.yaml'
config = OmegaConf.load(f"{config}")
model = load_model_from_config(config, f"{chkpt_ini}")

model = model.half()

# def txt2img_main(*txt2img_args):
#     from scripts.txt2img_k_sdd import txt2img
#     txt2img(*txt2img_args)
#     torch_gc()

# def img2img_main(*img2img_args):
#     from scripts.img2img_k_sdd import img2img
#     img2img(*img2img_args)
#     torch_gc()

# def txt2imghd_main(*txt2imghd_args):
#     txt2imghd(*txt2imghd_args)
#     torch_gc()