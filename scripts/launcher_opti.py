import configparser
import os
from itertools import islice
from pathlib import Path
from ldm.util import instantiate_from_config
from omegaconf import OmegaConf

import torch
import torch.nn as nn
from omegaconf import OmegaConf

settings_path=(os.path.dirname(os.path.realpath(__file__)))
settings_path=(Path(settings_path).parent/'settings.ini')

config = configparser.ConfigParser()
settings_file = (settings_path)
config.read(settings_path)
chkpt_ini=config.get('Settings', 'ckpt_path')


configy_path=(os.path.dirname(os.path.realpath(__file__)))
config = Path(configy_path)/'v1-inference.yaml'
config = OmegaConf.load(f"{config}")
# config = OmegaConf.load(f"{opt.config}")
# model = load_model_from_config(config, f"{chkpt_ini}")

print(chkpt_ini)

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def load_model_from_config(chkpt_ini, verbose=False):
    print(f"Loading model from {chkpt_ini}")
    pl_sd = torch.load(chkpt_ini, map_location="cpu")
    if "global_step" in pl_sd:
        print(f"Global Step: {pl_sd['global_step']}")
    global sd
    sd = pl_sd["state_dict"]
    return sd

# Not entirely certain as to the purpose of this; however, looking at existing code, it's
# necessary to adapt Stable Diffusion's inputs to k_lms.

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

sd = load_model_from_config(f"{chkpt_ini}")
li, lo = [], []

for key, value in sd.items():
    sp = key.split(".")
    if (sp[0]) == "model":
        if "input_blocks" in sp:
            li.append(key)
        elif "middle_block" in sp:
            li.append(key)
        elif "time_embed" in sp:
            li.append(key)
        else:
            lo.append(key)
for key in li:
    sd["model1." + key[6:]] = sd.pop(key)
for key in lo:
    sd["model2." + key[6:]] = sd.pop(key)


model = instantiate_from_config(config.modelUNet)
_, _ = model.load_state_dict(sd, strict=False)
model.eval()
# model.unet_bs = opt.unet_bs
# model.cdevice = opt.device
# model.turbo = turbo
device='cuda'
modelCS = instantiate_from_config(config.modelCondStage)
_, _ = modelCS.load_state_dict(sd, strict=False)
modelCS.eval()
modelCS.cond_stage_model.device = device

modelFS = instantiate_from_config(config.modelFirstStage)
_, _ = modelFS.load_state_dict(sd, strict=False)
modelFS.eval()

del sd

def torch_gc():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
        print('Torch cache cleaned')
torch_gc()

from scripts.optimized_txt2img_k_sdd import txt2img_opti
from scripts.optimized_img2img_k_sdd import img2img_opti

def txt2img_opti_main(*txt2img_args):
    txt2img_opti(*txt2img_args)
    torch_gc()

def img2img_opti_main(*img2img_args):
    img2img_opti(*img2img_args)
    torch_gc()