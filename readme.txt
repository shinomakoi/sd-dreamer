- Have a working Stable Diffusion install (tested on the default CompVis and basujindal version)
- Run 'conda activate ldm' to init SD (in Windows, from inside the Anaconda prompt)
- Run 'pip install -r <path-to-sd-dreamer-folder>/requirements.txt' to install dependencies
- Run 'python <path-to-sd-dreamer-folder>\main.py

- Run the program and set the necessary paths. The 'stable diffusion install folder' is the main base folder of your existing stable diffusion install.

- For inpainting, download the model from https://ommer-lab.com/files/latent-diffusion/inpainting_big.zip and put in the 'stable-diffusion\models\ldm\inpainting_big' folder and rename to last.ckpt

- For upscaling, download real-esrgan-vulkan from https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0, extract the zip then set the paths in the settings tab of the app.

- Use the custom scripts in the 'optimizedSD' folder if you wish. Put the folder in SD base directory
--small_batch only works with the 'optimizedSD/optimized_txt2img.py'. You can also use other modified txt2img and img2img scripts. txt2img_clean_half and img2img_clean_half are recommended. The included inpaint.py is recommended for inpainting if you run out of VRAM.