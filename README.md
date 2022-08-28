# sd-dreamer
Qt based Linux/Windows GUI for Stable Diffusion

- Have a working Stable Diffusion install (tested on the default CompVis and the basujindal, hlky versions)
- IMPORTANT: Place the SD Dreamer folder in the base of your stable diffusion folder (e.g. in stable-diffusion-compvis folder), so to launch, for example - 'python stable-diffusion-main\sd-dreamer\main.py'
- Run 'conda activate <ldm/ldp>' or whatever your conda environment is to init SD (in Windows, from inside the Anaconda prompt)
- Run 'pip install -r requirements.txt' to install any dependencies
- Run 'python <path-to-sd-dreamer-folder>main.py to start'
- k_ samplers require k-diffusion installed
- k_euler_a and k_dpm_2_a samplers only supported for txt2img currently, will default to k_lms for img2img

- For inpainting, download the model from https://ommer-lab.com/files/latent-diffusion/inpainting_big.zip and put in the 'stable-diffusion\models\ldm\inpainting_big' folder and rename to last.ckpt

- For upscaling, download real-esrgan-vulkan-ncnn from https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0, extract the zip then set the paths in the settings tab of the app.

- 'small_batch' only works with 'optimized_*' scripts. You can also use other modified txt2img and img2img scripts. The included inpaint.py is recommended for inpainting if you run out of VRAM.
