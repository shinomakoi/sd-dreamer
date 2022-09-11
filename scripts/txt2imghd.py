import argparse
import os
import shutil
from typing import List, Optional
import cv2
import torch
import cv2
import PIL
import gc
import numpy as np
import subprocess
from omegaconf import OmegaConf
from PIL import Image, ImageDraw
from tqdm import tqdm, trange
#from imwatermark import WatermarkEncoder
from einops import rearrange, repeat
from itertools import islice
from einops import rearrange
import time
from pytorch_lightning import seed_everything
from torch import autocast

from ldm.util import instantiate_from_config
from ldm.models.diffusion.ddim import DDIMSampler


def load_img(path):
    image = Image.open(path).convert("RGB")
    w, h = image.size
    print(f"loaded input image of size ({w}, {h}) from {path}")
    # resize to integer multiple of 32
    w, h = map(lambda x: x - x % 32, (w, h))
    image = image.resize((w, h), resample=PIL.Image.Resampling.LANCZOS)
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.*image - 1.


def convert_pil_img(image):
    w, h = image.size
    # resize to integer multiple of 32
    w, h = map(lambda x: x - x % 32, (w, h))
    image = image.resize((w, h), resample=PIL.Image.Resampling.LANCZOS)
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.*image - 1.


def addalpha(im, mask):
    imr, img, imb, ima = im.split()
    mmr, mmg, mmb, mma = mask.split()
    # we want the RGB from the original, but the transparency from the mask
    im = Image.merge('RGBA', [imr, img, imb, mma])
    return(im)

# Alternative method composites a grid of images at the positions provided


def grid_merge(source, slices):
    source.convert("RGBA")
    for slice, posx, posy in slices:  # go in reverse to get proper stacking
        source.alpha_composite(slice, (posx, posy))
    return source


def grid_coords(target, original, overlap):
    # generate a list of coordinate tuples for our sections, in order of how they'll be rendered
    # target should be the size for the gobig result, original is the size of each chunk being rendered
    center = []
    target_x, target_y = target
    center_x = int(target_x / 2)
    center_y = int(target_y / 2)
    original_x, original_y = original
    x = center_x - int(original_x / 2)
    y = center_y - int(original_y / 2)
    center.append((x, y))  # center chunk
    uy = y  # up
    uy_list = []
    dy = y  # down
    dy_list = []
    lx = x  # left
    lx_list = []
    rx = x  # right
    rx_list = []
    while uy > 0:  # center row vertical up
        uy = uy - original_y + overlap
        uy_list.append((lx, uy))
    while (dy + original_y) <= target_y:  # center row vertical down
        dy = dy + original_y - overlap
        dy_list.append((rx, dy))
    while lx > 0:
        lx = lx - original_x + overlap
        lx_list.append((lx, y))
        uy = y
        while uy > 0:
            uy = uy - original_y + overlap
            uy_list.append((lx, uy))
        dy = y
        while (dy + original_y) <= target_y:
            dy = dy + original_y - overlap
            dy_list.append((lx, dy))
    while (rx + original_x) <= target_x:
        rx = rx + original_x - overlap
        rx_list.append((rx, y))
        uy = y
        while uy > 0:
            uy = uy - original_y + overlap
            uy_list.append((rx, uy))
        dy = y
        while (dy + original_y) <= target_y:
            dy = dy + original_y - overlap
            dy_list.append((rx, dy))
    # calculate a new size that will fill the canvas, which will be optionally used in grid_slice and go_big
    last_coordx, last_coordy = dy_list[-1:][0]
    # outer bottom edge of the render canvas
    render_edgey = last_coordy + original_y
    render_edgex = last_coordx + original_x  # outer side edge of the render canvas
    scalarx = render_edgex / target_x
    scalary = render_edgey / target_y
    if scalarx <= scalary:
        new_edgex = int(target_x * scalarx)
        new_edgey = int(target_y * scalarx)
    else:
        new_edgex = int(target_x * scalary)
        new_edgey = int(target_y * scalary)
    # now put all the chunks into one master list of coordinates (essentially reverse of how we calculated them so that the central slices will be on top)
    result = []
    for coords in dy_list[::-1]:
        result.append(coords)
    for coords in uy_list[::-1]:
        result.append(coords)
    for coords in rx_list[::-1]:
        result.append(coords)
    for coords in lx_list[::-1]:
        result.append(coords)
    result.append(center[0])
    return result, (new_edgex, new_edgey)


def get_resampling_mode():
    try:
        from PIL import __version__, Image
        major_ver = int(__version__.split('.')[0])
        if major_ver >= 9:
            return Image.Resampling.LANCZOS
        else:
            return Image.LANCZOS
    except Exception as ex:
        return 1  # 'Lanczos' irrespective of version.

# Chop our source into a grid of images that each equal the size of the original render


def grid_slice(source, overlap, og_size, maximize=False):
    width, height = og_size  # size of the slices to be rendered
    coordinates, new_size = grid_coords(source.size, og_size, overlap)
    if maximize == True:
        # minor concern that we're resizing twice
        source = source.resize(new_size, get_resampling_mode())
        # re-do the coordinates with the new canvas size
        coordinates, new_size = grid_coords(source.size, og_size, overlap)
    # loc_width and loc_height are the center point of the goal size, and we'll start there and work our way out
    slices = []
    for coordinate in coordinates:
        x, y = coordinate
        slices.append(((source.crop((x, y, x+width, y+height))), x, y))
    global slices_todo
    slices_todo = len(slices) - 1
    return slices, new_size


class Options:
    C: int
    f: int
    strength: float
    from_file: bool
    config: str
    ckpt: str
    passes: int
    wm: str
    gobig_overlap: int
    generated: Optional[List[str]]
    img: str


def realesrgan2x(executable: str, input: str, output: str):
    process = subprocess.Popen([
        executable,
        '-i',
        input,
        '-o',
        output,
        '-n',
        'realesrgan-x4plus'
    ])
    process.wait()

    final_output = Image.open(output)
    final_output = final_output.resize(
        (int(final_output.size[0] / 2), int(final_output.size[1] / 2)), get_resampling_mode())
    final_output.save(output)


def text2img2(prompt, steps, iterations, seed, outpath, scale, width, height, detail_steps, detail_scale, realesrgan, strength, img=None):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--generated",
        type=str,
        nargs="?",
        help="only do detailing, using these base filenames in output dir"
    )
    parser.add_argument(
        "--img",
        type=str,
        nargs="?",
        help="only do detailing, using this path (will be copied to output dir)"
    )
    parser.add_argument(
        "--outdir",
        type=str,
        nargs="?",
        help="dir to write results to",
        default="outputs/txt2imghd_samples"
    )

    parser.add_argument(
        "--ddim",
        action='store_true',
        help="use ddim sampling",
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
        "--passes",
        type=int,
        default=1,
        help="number of upscales/details",
    )
    parser.add_argument(
        "--gobig_overlap",
        type=int,
        default=128,
        help="overlap size for GOBIG",
    )
    opt = parser.parse_args()

    from scripts.launcher import model

    seed_everything(seed)

    device = torch.device(
        "cuda") if torch.cuda.is_available() else torch.device("cpu")
    model = model.to(device)

    sampler = DDIMSampler(model)

    os.makedirs(outpath, exist_ok=True)
    outpath = outpath

    sample_path = os.path.join(outpath, 'txt2imghd_samples')
    os.makedirs(sample_path, exist_ok=True)

    #wm_encoder = WatermarkEncoder()
    #wm_encoder.set_watermark('bytes', widthm.encode('utf-8'))

    batch_size = 1
    precision_scope = autocast
    base_count = len(os.listdir(sample_path))

    assert prompt is not None
    data = [batch_size * [prompt]]

    generated = opt.generated
    if generated is None and img is not None:
        shutil.copyfile(img, os.path.join(sample_path, f"{base_count:05}.png"))
        generated = [f"{base_count:05}"]
    elif isinstance(generated, str):
        generated = [generated]

    if generated is None:
        generated = []
        with torch.inference_mode():
            with precision_scope("cuda"):
                with model.ema_scope():
                    for _ in trange(iterations, desc="Sampling"):
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
                                                             batch_size=batch_size,
                                                             shape=shape,
                                                             verbose=False,
                                                             unconditional_guidance_scale=scale,
                                                             unconditional_conditioning=uc,
                                                             eta=0,
                                                             x_T=None)

                            x_samples_ddim = model.decode_first_stage(
                                samples_ddim)
                            x_samples_ddim = torch.clamp(
                                (x_samples_ddim + 1.0) / 2.0, min=0.0, max=1.0)
                            x_samples_ddim = x_samples_ddim.cpu().permute(0, 2, 3, 1).numpy()

                            x_checked_image = x_samples_ddim

                            x_checked_image_torch = torch.from_numpy(
                                x_checked_image).permute(0, 3, 1, 2)

                            for x_sample in x_checked_image_torch:
                                x_sample = 255. * \
                                    rearrange(x_sample.cpu().numpy(),
                                              'c h w -> h w c')
                                img = Image.fromarray(
                                    x_sample.astype(np.uint8))
                                output_path = os.path.join(
                                    sample_path, f"{base_count:05}.png")
                                img.save(output_path)
                                generated.append(f"{base_count:05}")
                                base_count += 1

        torch.cuda.empty_cache()
        gc.collect()

    sampler = DDIMSampler(model)

    for base_filename in generated:
        for _ in trange(opt.passes, desc="Passes"):
            realesrgan2x(realesrgan, os.path.join(sample_path, f"{base_filename}.png"), os.path.join(
                sample_path, f"{base_filename}u.png"))
            base_filename = f"{base_filename}u"

            source_image = Image.open(os.path.join(
                sample_path, f"{base_filename}.png"))
            og_size = (height, width)
            slices, _ = grid_slice(
                source_image, opt.gobig_overlap, og_size, False)

            betterslices = []
            for _, chunk_w_coords in tqdm(enumerate(slices), "Slices"):
                chunk, coord_x, coord_y = chunk_w_coords

                init_image = convert_pil_img(chunk).to(device)
                init_image = init_image.half()
                init_image = repeat(init_image, '1 ... -> b ...', b=batch_size)
                init_latent = model.get_first_stage_encoding(
                    model.encode_first_stage(init_image))  # move to latent space

                sampler.make_schedule(
                    ddim_num_steps=detail_steps, ddim_eta=0, verbose=False)

                assert 0. <= strength <= 1., 'can only work with strength in [0.0, 1.0]'
                t_enc = int(strength * detail_steps)

                with torch.inference_mode():
                    with precision_scope("cuda"):
                        with model.ema_scope():
                            for prompts in tqdm(data, desc="data"):
                                uc = None
                                if detail_scale != 1.0:
                                    uc = model.get_learned_conditioning(
                                        batch_size * [""])
                                if isinstance(prompts, tuple):
                                    prompts = list(prompts)
                                c = model.get_learned_conditioning(prompts)

                                # encode (scaled latent)
                                z_enc = sampler.stochastic_encode(
                                    init_latent, torch.tensor([t_enc]*batch_size).to(device))
                                # decode it
                                samples = sampler.decode(z_enc, c, t_enc, unconditional_guidance_scale=detail_scale,
                                                         unconditional_conditioning=uc,)

                                x_samples = model.decode_first_stage(samples)
                                x_samples = torch.clamp(
                                    (x_samples + 1.0) / 2.0, min=0.0, max=1.0)

                                for x_sample in x_samples:
                                    x_sample = 255. * \
                                        rearrange(
                                            x_sample.cpu().numpy(), 'c h w -> h w c')
                                    resultslice = Image.fromarray(
                                        x_sample.astype(np.uint8)).convert('RGBA')
                                    betterslices.append(
                                        (resultslice.copy(), coord_x, coord_y))

            alpha = Image.new('L', og_size, color=0xFF)
            alpha_gradient = ImageDraw.Draw(alpha)
            a = 0
            i = 0
            overlap = opt.gobig_overlap
            shape = (og_size, (0, 0))
            while i < overlap:
                alpha_gradient.rectangle(shape, fill=a)
                a += 4
                i += 1
                shape = ((og_size[0] - i, og_size[1] - i), (i, i))
            mask = Image.new('RGBA', og_size, color=0)
            mask.putalpha(alpha)
            finished_slices = []
            for betterslice, x, y in betterslices:
                finished_slice = addalpha(betterslice, mask)
                finished_slices.append((finished_slice, x, y))
            # # Once we have all our images, use grid_merge back onto the source, then save
            final_output = grid_merge(source_image.convert(
                "RGBA"), finished_slices).convert("RGB")
            final_output.save(os.path.join(
                sample_path, f"{base_filename}d.png"))
            base_filename = f"{base_filename}d"

            torch.cuda.empty_cache()
            gc.collect()
        for r in ((">", ""), ("<", ""), ("<", ""), ("|", ""), ("?", ""), ("*", ""), ('"', ""), (',', ""), ('.', ""), ('\n', ""), (' ', '_')):
            prompt = prompt.replace(*r).strip()
        final_output.save(os.path.join(sample_path, f"{base_count:05}_{str(seed)}_{prompt[:120]}.png"))
        seed+= 1
        base_count += 1

def txt2imghd(*txt2imghd_args):

    text2img2(*txt2imghd_args)
