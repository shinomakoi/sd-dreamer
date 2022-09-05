# sd-dreamer
Qt based Linux/Windows GUI for Stable Diffusion

Features txt2img, img2img, inpainting, paint app for img2img, upscaling with Real-ESRGAN, LatentSR, txt2imgHD and and k-diffusion samplers.

- Have a working Stable Diffusion install (tested on the default CompVis and the basujindal, hlky versions) 
- IMPORTANT: Place the SD Dreamer folder in the base of your stable diffusion folder (e.g. in stable-diffusion-main folder, where environment.yaml file is), so to launch, for example - 'python stable-diffusion-main\sd-dreamer\main.py'
- Run 'conda activate <ldm/ldp>' or whatever your conda environment is to init SD (in Windows, from inside the Anaconda prompt)
- Run 'pip install -r requirements.txt' to install any dependencies
- Run 'python main.py' to start the app

- LatentSR requires download of https://ommer-lab.com/files/latent-diffusion/sr_bsr.zip - put the model.ckpt file in the models/ldm/bsr_sr/ folder.

- k_ samplers require k-diffusion installed (already included in most forks)

- For inpainting, download the model from https://ommer-lab.com/files/latent-diffusion/inpainting_big.zip and put in the 'stable-diffusion\models\ldm\inpainting_big' folder and rename to last.ckpt

- For upscaling, download real-esrgan-vulkan-ncnn from https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0, extract the zip then set the paths in the settings tab of the app.

![sdd6](https://user-images.githubusercontent.com/112139428/188335306-9d61624c-6cdd-49bb-becd-41b56c6ef070.png)


Credit to stability.ai et al for Stable Diffusion, basujindal, nights192, jquesnelle, richservo and anons
