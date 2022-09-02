import PIL
import os
import argparse
import random
import sys
import torch
import torch.nn as nn
import numpy as np
from omegaconf import OmegaConf
from PIL import Image, ImageDraw, ImageMath, ImageFilter
from tqdm import tqdm, trange
from itertools import islice
from einops import rearrange, repeat
from pytorch_lightning import seed_everything
from torch import autocast
from pathlib import Path

# import accelerate
import k_diffusion as K
from ldm.util import instantiate_from_config

# some of those options should not be changed at all because they would break the model,
# so I removed them from options.
opt_C = 4
opt_f = 8
os.chdir(os.path.dirname(sys.argv[0]))
outdir = Path(__file__).resolve().parents[2] 
outdir = Path(outdir/'outputs'/'sd_dreamer')

origWidth = 0
origHeight = 0
print(outdir)

parser = argparse.ArgumentParser()

parser.add_argument(
        "--prompt",
        type=str,
        nargs="?",
        default="",
        help="description of your image to help guide the sampler"
    )

parser.add_argument(
        "--seed",
        type=int,
        default=random.randint(0,4294967295),
        help="the seed (for reproducible sampling). default is randomly generated",
    )
parser.add_argument(
        "--strength",
        type=float,
        help="strength of the upsampling effect/amount of detail, works best with values around 0.25-0.3, higher values tend to get incoherent",
        default=0.25
    )

parser.add_argument(
        "--img_path",
        type=str,
        help="path  of images",
        default=""
    )

opt = parser.parse_args()

# if not opt.image: raise SystemExit('Error: You must provide an image file to upscale using --image')
# if not opt.prompt: raise SystemExit('Error: You must provide a prompt describing your image to help guide the sampler using --prompt')

def load_model_from_config(config, ckpt, verbose=False):
    print(f"Loading model from {ckpt}")
    pl_sd = torch.load(ckpt, map_location="cpu")
    if "global_step" in pl_sd:
        print(f"Global Step: {pl_sd['global_step']}")
    sd = pl_sd["state_dict"]
    model = instantiate_from_config(config.model)
    m, u = model.load_state_dict(sd, strict=False)
    if len(m) > 0 and verbose:
        print("missing keys:")
        print(m)
    if len(u) > 0 and verbose:
        print("unexpected keys:")
        print(u)

    model.cuda()
    model.eval()
    return model


config = OmegaConf.load("../../configs/stable-diffusion/v1-inference.yaml")
model = load_model_from_config(config, "../../models/ldm/stable-diffusion-v1/model.ckpt")

# device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
assert torch.cuda.is_available()
device = torch.device("cuda")
model = model.half().to(device)


def batch_upscaler(imgz):
    opt.image=imgz
    # opt.prompt='ice queen'

    def i2np(i):
        return np.array(i).astype(np.float32) / 255.0


    def np2i(n):
        return Image.fromarray(np.uint8(n * 255.0))


    def grayscale(n):
        # Y' = 0.2989 R + 0.5870 G + 0.1140 B
        return n[..., 0] * 0.2989 + n[..., 1] * 0.5870 + n[..., 2] * 0.1140


    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))


    def make_gradient(width, height, rot):
        base = Image.linear_gradient("L")
        base = base.rotate(rot)
        base = base.resize((width, height))
        return base


    # a, b = -1 or 1, determine mask location
    def create_2_corner_mask(w, h, m, a, b):
        mask = np.ones((w, h), dtype=np.float32)
        for i in range(m):
            mask[:, i * a] = i / m
        for i in range(m):
            mask[i * b, :] *= i / m
        mask = np.clip(mask, 0.0, 1.0)
        return mask


    def chunk(it, size):
        it = iter(it)
        return iter(lambda: tuple(islice(it, size)), ())


    def load_img_pil(img_pil):
        image = img_pil.convert("RGB")
        w, h = image.size
        print(f"loaded input image of size ({w}, {h})")
        w, h = map(lambda x: x - x % 64, (w, h))  # resize to integer multiple of 64
        image = image.resize((w, h), resample=PIL.Image.LANCZOS)
        print(f"cropped image to size ({w}, {h})")
        image = np.array(image).astype(np.float32) / 255.0
        image = image[None].transpose(0, 3, 1, 2)
        image = torch.from_numpy(image)
        return 2.0 * image - 1.0


    def load_img(path):
        return load_img_pil(Image.open(path))


    def convert_input_image(img, width, height):
        img = img.convert("RGB")
        w, h = map(lambda x: x - x % 32, (width, height))  # resize to integer multiple of 32
        img = img.resize((w, h), resample=PIL.Image.Resampling.LANCZOS)
        img = np.array(img).astype(np.float32) / 255.0
        return img


    def make_extra_args(cfg_scale, batch_size, prompts):
        uc = None
        if cfg_scale != 1.0:
            uc = model.get_learned_conditioning(batch_size * [""])
        if isinstance(prompts, tuple):
            prompts = list(prompts)
        c = model.get_learned_conditioning(prompts)
        return {"cond": c, "uncond": uc, "cond_scale": cfg_scale}


    def directory_setup():
        os.makedirs(outdir, exist_ok=True)
        outpath = outdir
        sample_path = os.path.join(outpath, "anon_upscales")
        os.makedirs(sample_path, exist_ok=True)
        base_count = len(os.listdir(sample_path))
        return base_count, sample_path


    def seeds_setup(seed):
        torch.cuda.empty_cache()
        rng_seed = seed_everything(seed)
        seeds = torch.randint(-(2**63), 2**63 - 1, [1])
        torch.manual_seed(seeds[0].item())
        return rng_seed


    def name_gen(prompt, sample_path, base_count, seed):
        return os.path.join(
            sample_path,
            f"{base_count:05}-{seed}_" f"{prompt.replace(' ', '_')[:128]}.png",
        )


    def masked_blend(imageA, imageB, amask, style=1, strength=24.0, overdrive=0.1, clrs="RGB"):
        blendM = i2np(amask)
        blendA = i2np(imageA)
        blendB = i2np(imageB)

        if style == 0:
            blended = (blendA.T * (1.0 - blendM.T) + blendB.T * blendM.T).T
        elif style == 1:
            blendAL = grayscale(blendA)
            blendBL = grayscale(blendB)

            blogic = blendAL * (1.0 - blendM) - blendBL * blendM
            blogic = sigmoid(blogic * strength) * (1.0 + overdrive) - overdrive / 2.0
            blended = ((blendA.T * blogic.T) + (blendB.T * (1.0 - blogic.T))).T
            blended = np.clip(blended, 0.0, 1.0)

        return np2i(blended).convert(clrs)


    def ESR_upscale(img, upscale=2):
        # Instructions HOWTO install lib in GFPGAN GH repo
        from basicsr.archs.rrdbnet_arch import RRDBNet
        from realesrgan import RealESRGANer

        # default tile = 400
        tile = 400
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        bg_upsampler = RealESRGANer(
            scale=4,
            model_path="https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/"
            "RealESRGAN_x4plus.pth",
            model=model,
            tile=tile,
            tile_pad=10,
            pre_pad=0,
            half=True,
        )
        npi = i2np(img)
        res = bg_upsampler.enhance(npi * 255.0, outscale=upscale)
        return np2i(res[0] / 255.0)


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


    def dream(prompt, ddim_steps, cfg_scale, seed, height, width, sampler, skip_save=True):
        rng_seed = seeds_setup(seed)
        base_count, sample_path = directory_setup()
        model_wrap = K.external.CompVisDenoiser(model)
        with torch.no_grad(), autocast("cuda"), model.ema_scope():
            torch.manual_seed(rng_seed)
            x = torch.randn([1, opt_C, height // opt_f, width // opt_f], device=device)

            sigmas = model_wrap.get_sigmas(ddim_steps)
            x *= sigmas[0]
            ea = make_extra_args(cfg_scale, 1, prompt)
            samples_ddim = sampler(CFGDenoiser(model_wrap), x, sigmas, extra_args=ea)

            x_samples_ddim = model.decode_first_stage(samples_ddim)
            x_samples_ddim = torch.clamp((x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
            x_sample = 255.0 * rearrange(x_samples_ddim[0].cpu().numpy(), "c h w -> h w c")
            made_image = Image.fromarray(x_sample.astype(np.uint8))
            if not skip_save:
                made_image.save(name_gen(prompt, sample_path, base_count, rng_seed))
            return made_image


    def translation(prompt, init_img, dsteps, cfg_scale, dns, seed, height, width, skip_save=True):
        rng_seed = seeds_setup(seed)
        base_count, sample_path = directory_setup()
        model_wrap = K.external.CompVisDenoiser(model)

        image = convert_input_image(init_img, width, height)
        image = image[None].transpose(0, 3, 1, 2)
        image = torch.from_numpy(image)
        with torch.no_grad(), autocast("cuda"):
            init_image = 2.0 * image - 1.0
            init_image = init_image.to(device)
            init_image = repeat(init_image, "1 ... -> b ...", b=1)
            init_latent = model.get_first_stage_encoding(model.encode_first_stage(init_image))
            x0 = init_latent

            assert 0.0 <= dns <= 1.0, "can only work with strength in [0.0, 1.0]"
            with model.ema_scope():
                torch.manual_seed(rng_seed)
                t_enc = int(dns * dsteps)
                sigmas = model_wrap.get_sigmas(dsteps)
                samples_ddim = K.sampling.sample_euler(
                    CFGDenoiser(model_wrap),
                    x0 + torch.randn_like(x0) * sigmas[dsteps - t_enc - 1],
                    sigmas[dsteps - t_enc - 1 :],
                    extra_args=make_extra_args(cfg_scale, 1, prompt),
                )

                x_samples_ddim = model.decode_first_stage(samples_ddim)
                x_samples_ddim = torch.clamp((x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                x_sample = 255.0 * rearrange(x_samples_ddim[0].cpu().numpy(), "c h w -> h w c")
                made_image = Image.fromarray(x_sample.astype(np.uint8))
                if not skip_save:
                    made_image.save(name_gen(prompt, sample_path, base_count, rng_seed))
                return made_image


    def run_blending():
        imageA = dream(prompt, 40, 7.0, 557, 512, 512, skip_save=False).convert("RGBA")
        imageB = dream(prompt, 40, 7.0, 558, 512, 512, skip_save=True).convert("RGBA")

        amask = Image.new("L", (256, 512))
        amask.paste(make_gradient(256, 512, 90.0), (0, 0))

        blended = masked_blend(
            imageA.crop((256, 0, 512, 512)),
            imageB.crop((0, 0, 256, 512)),
            make_gradient(256, 512, 90.0),
            strength=16.0,
        )

        tbld = translation(
            prompt, blended.crop((0, 0, 256, 512)), 40, 7.0, 0.5, -1, 512, 256, skip_save=True
        ).convert("RGBA")

        total = Image.new("RGBA", (512 + 256, 512))
        total.paste(imageA, (0, 0))
        total.paste(imageB, (256, 0))
        total.paste(tbld, (256, 0))
        total.show()


    def make_big(S, seed, margin, totS, sampler=K.sampling.sample_euler_ancestral):
        # sample_lms
        # sample_euler
        # sample_euler_ancestral
        # sample_dpm_2
        # sample_dpm_2_ancestral
        # sample_heun

        assert margin % 64 == 0
        totS2 = totS * 2
        crpS = totS + margin
        crpSE = totS2 - crpS

        crops = [
            (0, 0, crpS, crpS),
            (crpSE, 0, totS2, crpS),
            (0, crpSE, crpS, totS2),
            (crpSE, crpSE, totS2, totS2),
        ]

        corners = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

        imageA = Image.open(opt.image)
        global origWidth, origHeight
        origWidth, origHeight = imageA.size
        imageA = imageA.resize((512, 512))
        esr = ESR_upscale(imageA)

        for n in range(4):
            image0Z = esr.crop(crops[n])
            image0 = translation(prompt, image0Z, 59, 7.5, S, seed, crpS, crpS)
            mask = create_2_corner_mask(crpS, crpS, margin * 2, *corners[n])
            esr.paste(masked_blend(image0Z, image0, mask * 255.0, style=0), crops[n][:2])
        return esr, imageA

    if __name__ == "__main__":
        prompt = opt.prompt
        seed = opt.seed
        esr, orig = make_big(opt.strength, seed, 64, 512)
        base_count, sample_path = directory_setup()
        # if the input file wasn't square, restore it to its original aspect ratio and the warn user their results will probably suck
        if ((origWidth / origHeight) != 1):
            esr = esr.resize(((origWidth * 2), (origHeight * 2)))
            print ('Input image was not a square aspect ratio, so results are likely to be poor.')
        for r in ((">", ""), ("<", ""),("/", ""),("<", ""),("?", ""),("*", ""),("\\", ""),('"', ""),(',', ""),('.', ""),('\n', "")):
            prompt = prompt.replace(*r).strip()
        for r in ((">", ""), ("<", ""),("<", ""),("|", ""),("?", ""),("*", ""),('"', ""),(' ', "_"),(',', ""),('.', ""),('\n', "")):
            sample_path = sample_path.replace(*r).strip()
        esr.save(name_gen(prompt, sample_path, base_count, seed))
        print('Prompt=',prompt, 'Path saved to:',sample_path, seed)

def scale_list():
    i = 0
    image_list = os.listdir(opt.img_path)
    image_count=len(image_list)
    while i < image_count:
        print('Image count is:',image_count)
        imgz=image_list[i]
        imgz=(Path(opt.img_path)/(imgz))
        print('imgz =', imgz)
        batch_upscaler(imgz)
        i += 1
scale_list()