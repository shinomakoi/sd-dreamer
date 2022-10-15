# sd-dreamer
Qt based Linux/Windows/Mac GUI for Stable Diffusion (Invoke-AI 2.0)

Features txt2img, img2img, inpainting, paint app for img2img, upscaling, textual inversion embedding, k-diffusion samplers and more.

Note: the current version is designed to work with the Invoke-AI repo only. The old version is in the 'old-generic' branch.

- Have a working Stable Diffusion install from the Invoke-Ai repo (https://github.com/invoke-ai/stable-diffusion)
- IMPORTANT: Place the SD Dreamer folder in the base of your Invoke-AI folder (e.g. in 'InvokeAI' folder), so to launch, for example - 'python InvokeAI\sd-dreamer-main\main.py'
- Run 'conda activate <invokeai/ldm>' or whatever your SD conda environment is (in Windows, from inside the Anaconda/Miniconda prompt)
- Run 'pip install -r requirements.txt' to install dependencies
- Run 'python main.py' to start the app (inside the SD Dreamer folder)

- LatentSR requires download of https://ommer-lab.com/files/latent-diffusion/sr_bsr.zip - put the model.ckpt file from sr_bsr.zip in the models/ldm/bsr_sr/ folder. Probably bugged currently with the invoke-ai environment.

- For external upscaling with ESRGAN, you can download models (.pth) and place them in the 'ESRGAN/models' folder. There's a large selection here: https://upscale.wiki/wiki/Model_Database
 
 - ESRGAN and LatentSR upscales are in 'outputs/sd_dreamer/upscales' folder
 
 ![sdd9](https://user-images.githubusercontent.com/112139428/191869406-b37a0c84-991d-46ac-8c8c-93b5575e975b.png)

Credit to stability.ai/CompVis et al for Stable Diffusion, Invoke-ai, jquesnelle, richservo, joeyballentine and anons
