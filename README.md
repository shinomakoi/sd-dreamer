# sd-dreamer
Qt based Linux/Windows GUI for Stable Diffusion (invoke-ai version). Requires NVIDIA GPU

Features txt2img, img2img, inpainting, paint app for img2img, upscaling, textual inversion embedding, k-diffusion samplers and more.

Note: the current version is designed to work with the invoke-ai repo only. The old version is in the 'old-generic' branch.

- Have a working Stable Diffusion install from the invoke-ai repo (https://github.com/invoke-ai/stable-diffusion)
- IMPORTANT: Place the SD Dreamer folder in the base of your Stable Diffusion folder (e.g. in stable-diffusion-invoke-ai folder, where environment.yaml file is), so to launch, for example - 'python stable-diffusion-invoke-ai\sd-dreamer-main\main.py'
- Run 'conda activate <ldm/ldp>' or whatever your SD conda environment is (in Windows, from inside the Anaconda prompt)
- Run 'pip install -r requirements.txt' to install dependencies
- Run 'python main.py' to start the app

- LatentSR requires download of https://ommer-lab.com/files/latent-diffusion/sr_bsr.zip - put the model.ckpt file from sr_bsr.zip in the models/ldm/bsr_sr/ folder.

- For external upscaling, you can download real-esrgan-vulkan-ncnn from https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0, extract the zip then set the paths to them in the settings tab of the app.
 
 - ESRGAN and LatentSR upscales are in 'outputs/sd_dreamer/upscales' folder
 
![sddd8](https://user-images.githubusercontent.com/112139428/191080074-5ea33a79-0949-4e46-afed-dbf8c5ea843c.png)

Credit to stability.ai/CompVis et al for Stable Diffusion, lstein, jquesnelle, richservo and anons
