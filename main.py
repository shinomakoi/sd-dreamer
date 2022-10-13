################### BETA 0.5 ###################
################### Work in progress ###################

########## to do ##########
# expand img2img
# clean up code
# moar comments
# vram, ram view
# save more settings
# add drag and drop for images
# progress bar
# fix unicode prompt error on win with chinese characters, emojis etc
# add config yaml path option
# image viewer not loading with 1 image
# batch img2img
# img2img upscale with esrgan
# use metadata to set fields
# random artists
# batch img2img processing
# prompts from file
# image thumbnails

# add highres fix, perlin noise, threshold, outpainting, codeformer, change full
# precision, free_gpu_mem, new precision options, !fix, !fetch, outcrop, prompt blending
# session_peakmem

from ldm.invoke.restoration import Restoration
import configparser
import glob
import os
import random
import shutil
import sys
from pathlib import Path

import PIL
from ldm.generate import Generate
from PIL import Image, ImageFilter, ImageOps
from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtCore import QUrl  # , QPropertyAnimation
from PySide6.QtCore import QProcess
from PySide6.QtGui import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QFileDialog

from inpainter import inpainter_window
from painter import paintWindow
from ui import Ui_sd_dreamer_main

global loaded_model
loaded_model = False

home_dir_path = os.path.dirname(os.path.realpath(__file__))
sd_folder_path = Path(home_dir_path).parent

print('SD Dreamer home directory: ', home_dir_path)
print('SD install working directory:', sd_folder_path)

# load settings.ini file
config = configparser.ConfigParser()
settings_file = (Path(home_dir_path)/'settings.ini')

config.read(Path(home_dir_path)/'settings.ini')

inpainting_dir = Path(home_dir_path)/'inpainting'
latent_sr_path = Path(home_dir_path)/'scripts'/'predict_sr.py'
sd_output_folder = Path(sd_folder_path)/'outputs'/'sd_dreamer'
esrgan_out_path = Path(sd_output_folder)/'upscales'/'esrgan_out'

os.chdir('..')
gfpgan, codeformer = None, None
restoration = Restoration()
gfpgan, codeformer = restoration.load_face_restore_models()


class Load_Images_Class:
    def __init__(self):
        print('Load_Images_Class')

    def load_images(self, img_path, cust_load, img_mode):
        print('load_images variables loaded:', img_path, cust_load, img_mode)
        global images_path

        if cust_load == True:
            images_path = str(Path(img_path))
            print('custom folder load')
        else:
            print('not custom folder load')
            images_path = str(Path(img_path)/img_mode)

        images_path = str(Path(images_path)/'*.png')
        global image_list
        image_list = []
        image_list = glob.glob(images_path, recursive=True)

        image_list.sort(reverse=True)
        image_count = len(image_list)
        image_index = image_count-image_count

        print(image_count, 'images in folder')
        print('image_index=', image_index)

        # global image_to_display
        image_to_display = image_list[0]
        print('image_to_display', image_to_display)
        return image_to_display, image_index, images_path


# load settings from settings.ini
py_bin_path_ini = config.get('Settings', 'py_bin_path')
first_run_ini = config.get('Settings', 'first_run')
chkpt_ini = config.get('Settings', 'ckpt_path')

print('First run: ', first_run_ini)


class WorkerSignals(QObject):

    finished = Signal()
    # error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    Slot()

    def run(self):

        print("Thread start")
        (mode, mode_args, g) = self.args
        print('Dream mode:', mode)

        if mode == 'txt2img':
            load_mode = 'txt2img_samples'
            txt2img_args = mode_args
            print('txt2img args:', txt2img_args)

            results = g.txt2img(
                prompt=txt2img_args["prompt"],
                steps=txt2img_args["steps"],
                iterations=txt2img_args["iterations"],
                seed=txt2img_args["seed"],
                width=txt2img_args["width"],
                height=txt2img_args["height"],
                cfg_scale=txt2img_args["scale"],
                sampler_name=txt2img_args["sampler"],
                outdir=txt2img_args["outdir"],

                facetool=txt2img_args["facetool"],
                gfpgan_strength=txt2img_args["gfpgan_strength"],
                codeformer_fidelity=txt2img_args["codeformer_fidelity"],

                grid=txt2img_args["grid"],
                seamless=txt2img_args["seamless"],
                variation_amount=txt2img_args["variation_amount"],
                upscale=txt2img_args["upscale"],

                threshold=txt2img_args["threshold"],
                perlin=txt2img_args["perlin_value"],
                hires_fix=txt2img_args["hires_fix"],
                free_gpu_mem=txt2img_args["free_gpu_mem"],
            )

        if mode == 'img2img':
            load_mode = 'img2img_samples'
            img2img_args = mode_args
            print('img2img args:', img2img_args)

            results = g.img2img(
                prompt=img2img_args["prompt"],
                steps=img2img_args["steps"],
                iterations=img2img_args["iterations"],
                seed=img2img_args["seed"],
                width=img2img_args["width"],
                height=img2img_args["height"],
                cfg_scale=img2img_args["scale"],
                sampler_name=img2img_args["sampler"],
                outdir=img2img_args["outdir"],
                strength=img2img_args["strength"],
                init_img=img2img_args["init_img"],

                facetool=img2img_args["facetool"],
                gfpgan_strength=img2img_args["gfpgan_strength"],
                codeformer_fidelity=img2img_args["codeformer_fidelity"],

                grid=img2img_args["grid"],
                seamless=img2img_args["seamless"],
                upscale=img2img_args["upscale"],
                threshold=img2img_args["threshold"],
                perlin_value=img2img_args["perlin_value"],
                embiggen=img2img_args["embiggen"],
                free_gpu_mem=img2img_args["free_gpu_mem"],
            )

        if mode == 'inpaint':
            load_mode = 'inpaint_samples'
            inpaint_args = mode_args
            print('inpaint args:', inpaint_args)

            results = g.img2img(
                prompt=inpaint_args["prompt"],
                steps=inpaint_args["steps"],
                iterations=inpaint_args["iterations"],
                seed=inpaint_args["seed"],
                width=inpaint_args["width"],
                height=inpaint_args["height"],
                cfg_scale=inpaint_args["scale"],
                sampler_name=inpaint_args["sampler"],
                outdir=inpaint_args["outdir"],
                strength=inpaint_args["strength"],

                facetool=inpaint_args["facetool"],
                gfpgan_strength=inpaint_args["gfpgan_strength"],
                codeformer_fidelity=inpaint_args["codeformer_fidelity"],

                # grid=inpaint_args["grid"],
                # seamless=inpaint_args["seamless"],
                init_img=inpaint_args["init_img"],
                init_mask=inpaint_args["init_mask"],
                upscale=inpaint_args["upscale"],

                threshold=inpaint_args["threshold"],
                perlin=inpaint_args["perlin_value"],
                free_gpu_mem=inpaint_args["free_gpu_mem"],
            )

        # if mode == 'outpaintcrop':
        #     load_mode = 'inpaint_samples'
        #     outpaintcrop_args = mode_args
        #     print('outpaintcrop args:', outpaintcrop_args)

        #     results = g.apply_postprocessor(
        #         tool='outcrop',
        #         outcrop={'top': 64},
        #         image_path='',
        #         # top=outpaintcrop_args["top_crop"],
        #         # bottom=outpaintcrop_args["bottom_crop"],
        #         # left=outpaintcrop_args["left_crop"],
        #         # right=outpaintcrop_args["right_crop"],
        #     )
        #     print('outpaintcropresults:', results)

        if mode == 'fix':
            load_mode = 'txt2img_samples'
            fix_args = mode_args
            print('fix args:', fix_args)

            results = g.apply_postprocessor(
                image_path=fix_args["image_path"],
                tool=fix_args["tool"],
                codeformer_fidelity=fix_args["codeformer_fidelity"],
            )
            print('fixres', results)

        print("Thread complete")

        self.signals.finished.emit()
        self.signals.result.emit(load_mode)
        # print('results content', results)


class sd_dreamer_main(QtWidgets.QFrame, Ui_sd_dreamer_main):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.generator_process = None
        self.w = None
        self.art_win = None
        self.threadpool = QThreadPool()

        icon = QIcon()
        icon.addFile(str(Path(home_dir_path)/"appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        pixmap = QPixmap(str(Path(home_dir_path)/('view_default.png')))
        self.imageView.setPixmap(pixmap)

        self.pyBinPath.setText(py_bin_path_ini)
        self.custCheckpointLine.setText(chkpt_ini)

        self.outputFolderLine.setText(
            str(Path(sd_folder_path)/'outputs'/'sd_dreamer'))

        def art_op():
            art_source = self.imgFilename.text().replace('Filename: ', '')
            art_source = str(art_source)
            art(art_source, 0, 0)

        def read_metadata_op():
            filename = self.imgFilename.text().replace('Filename: ', '')
            im = Image.open(filename)
            im.load()
            self.processOutput.appendPlainText(
                'Metadata: '+im.info['Dream'])

        def openMenu(position):

            img_menu = QMenu()

            esrganAction = img_menu.addAction("Upscale: ESRGAN")
            ldsrAction = img_menu.addAction("Upscale: LDSR")
            artAction = img_menu.addAction("Paint edit")
            metadataAction = img_menu.addAction("Get metadata")
            inpaintAction = img_menu.addAction("Inpaint")
            img2imgAction = img_menu.addAction("img2img")
            favouriteAction = img_menu.addAction("Send to favourites")
            # codeformerAction = img_menu.addAction("Codeformer")

            action = img_menu.exec(self.imageView.mapToGlobal(position))

            check_image = Path(
                self.imgFilename.text().replace('Filename: ', ''))
            try:
                assert os.path.isfile(check_image)
            except AssertionError or NameError:
                print("No image")
                return

            if action == esrganAction:
                esrgan_launch_process(True)

            if action == ldsrAction:
                ldsr_launch_process(True)

            if action == artAction:
                art_op()

            if action == metadataAction:
                read_metadata_op()

            if action == img2imgAction:
                img2img_dream(True)

            if action == inpaintAction:
                inpaint(True)

            if action == favouriteAction:
                source = self.imgFilename.text().replace('Filename: ', '')
                file_stripped = Path(source).name
                target = Path(sd_output_folder)/'favourites'
                os.makedirs(Path(sd_output_folder)/'favourites', exist_ok=True)
                shutil.copyfile(source, Path(target/file_stripped))
                self.errorMessages.setText(f'Sent image to {target}')

            # if action == codeformerAction:
            #     fix_dream('codeformer')

        self.imageView.customContextMenuRequested.connect(openMenu)

        def first_run():
            if first_run_ini == '0':

                self.custCheckpointLine.setText(
                    str(Path(sd_folder_path)/'models'/'ldm'/'stable-diffusion-v1'/'model.ckpt'))

                config.set('Settings', 'first_run', '1')
                config.set('Settings', 'ckpt_path', str(
                    Path(sd_folder_path)/'models'/'ldm'/'stable-diffusion-v1'/'model.ckpt'))
                with open(settings_file, 'w') as configfile:
                    config.write(configfile)
        first_run()

        def check_install():
            check_install = os.path.exists(
                Path(sd_folder_path)/'environment.yml')
            if check_install == False:
                self.errorMessages.setText(
                    "WARNING: SD install folder seems incorrect. SD Dreamer folder must be in SD install folder")
                print(
                    "WARNING: SD install folder seems incorrect. SD Dreamer folder must be in SD install folder")
                return

            try:
                os.chdir(sd_folder_path)
            except:
                print("SD FOLDER NOT FOUND")
                self.errorMessages.setText("SD FOLDER NOT FOUND")
                return
        check_install()

        def cycle_images(button):
            try:
                image_count = len(image_list)
            except:
                print('Image list is empty')
                return
            image_index = int(int(self.imgIndex.text()))

            if button == 'next' and int(image_index) < image_count-1:
                image_index = int(int(self.imgIndex.text())) + 1
                image_to_display = image_list[image_index]
                self.imgFilename.setText('Filename: '+image_to_display)
                pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
                self.imageView.setPixmap(pixmap)
                # print('next to',image_to_display)
                self.imgIndex.setText(str(image_index))

            if button == 'previous' and int(image_index) > 0:
                image_index = int(int(self.imgIndex.text()))-1
                image_to_display = image_list[image_index]
                self.imgFilename.setText('Filename: '+image_to_display)
                pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
                self.imageView.setPixmap(pixmap)
                # print('next to',image_to_display)
                self.imgIndex.setText(str(image_index))

        self.nextImageButton.clicked.connect(lambda: cycle_images('next'))
        self.previousImgButton.clicked.connect(
            lambda: cycle_images('previous'))

        self.cancelButton.pressed.connect(self.stop_process)

        def gen_random_seed():
            if self.seedCheck.isChecked():
                self.seedVal.setText(str(random.randint(0, 1632714927)))
        gen_random_seed()

        def esrgan_models_func():
            try:
                # generate ESRGAN model list
                for x in os.listdir(Path(home_dir_path)/'ESRGAN'/'models'):
                    if x.endswith(".pth"):
                        self.rnvModelSelect.addItem(x)
            except:
                print('ESRGAN models not found')
        esrgan_models_func()

        def dream_rename():
            if self.mainTab.currentIndex() == 0:
                self.generateButton.setText('Dream (txt2img)')
            elif self.mainTab.currentIndex() == 1:
                self.generateButton.setText('Dream (img2img)')
            elif self.mainTab.currentIndex() == 2:
                self.generateButton.setText('Dream (inpaint)')

        self.mainTab.currentChanged.connect(dream_rename)

# saving the paths to the ini file
        def refresh_images():
            if len(self.operationFolder.text()) > 0:
                loady = Load_Images_Class()
                loady.load_images(self.operationFolder.text(), True, 'custom')
                self.nextImageButton.click()

        self.imageLoadButton.clicked.connect(refresh_images)

        def operationFolderSelect_select():
            opf = (QFileDialog.getExistingDirectory(
                self, ("Select images folder")))
            if len(opf) > 0:
                self.operationFolder.setText(opf)
                # self.load_images(opf, True, '')
                loady = Load_Images_Class()
                loady.load_images(self.operationFolder.text(), True, 'custom')
                self.nextImageButton.click()

        self.operationFolderSelect.clicked.connect(
            operationFolderSelect_select)

        def py_binSelect_select():
            py_bin_path = (QFileDialog.getOpenFileName(
                self, 'Open file', '', "All files (*.*)")[0])
            if len(py_bin_path) > 0:
                self.pyBinPath.setText(py_bin_path)
                config.set('Settings', 'py_bin_path', py_bin_path)
            with open(settings_file, 'w') as configfile:
                config.write(configfile)
        self.pyBinSelect.clicked.connect(py_binSelect_select)

        def custCheckpointSelect_select():
            ckpt_path = (QFileDialog.getOpenFileName(
                self, 'Open file', '', "Checkpoints (*.ckpt*)")[0])
            if len(ckpt_path) > 0:
                self.custCheckpointLine.setText(ckpt_path)
                config.set('Settings', 'ckpt_path', ckpt_path)
            with open(settings_file, 'w') as configfile:
                config.write(configfile)
        self.custCheckpointSelect.clicked.connect(custCheckpointSelect_select)

 # add prompts and remove duplicates
        def load_prompts():
            prompt_list = []
            try:
                for old_prompt in reversed(list(open(Path(home_dir_path)/"sdd_prompt_archive.txt"))):
                    if len(old_prompt) > 0:
                        prompt_list.append(old_prompt.strip())
                    prompt_list = list(dict.fromkeys(prompt_list))
            except:
                print("SD prompt archive not found")

            for old_prompt in prompt_list:
                self.promptVal.addItem(old_prompt)
        load_prompts()

        def load_prompt_tags():
            prompt_tag_list = []
            try:
                for old_prompt_tag in reversed(list(open(Path(home_dir_path)/"prompt_tags.txt"))):
                    if len(old_prompt_tag) > 0:
                        prompt_tag_list.append(old_prompt_tag.strip())
                    prompt_tag_list = list(dict.fromkeys(prompt_tag_list))
            except:
                print("SD prompt archive not found")

            for old_prompt in prompt_tag_list:
                self.promptTag.addItem(old_prompt)
        load_prompt_tags()

        def select_img2imgimg():
            file_x = (QFileDialog.getOpenFileName(self, 'Open file',
                      '', "Images (*.png *.jpg *.bmp *.webp)")[0])
            if len(file_x) > 0:
                self.img2imgFile.setText(file_x)
        self.imgFileSelect.clicked.connect(select_img2imgimg)

        def select_outputFolder():
            file_y = (QFileDialog.getExistingDirectory(
                self, ("Select output folder")))
            if len(file_y) > 0:
                self.outputFolderLine.setText(file_y)
        self.outputFolderSelect.clicked.connect(select_outputFolder)

        def select_inpaint_image():
            global inpaint_source
            inpaint_source = (QFileDialog.getOpenFileName(
                self, 'Open file', '', "Images (*.png *.jpg *.bmp *.webp)")[0])
            if len(inpaint_source) > 0:
                self.inpaint_img.setText(inpaint_source)
                print('Inpaint source: ', type(inpaint_source))
        self.inpaint_img_select.clicked.connect(select_inpaint_image)

        def select_embedding():
            file_z = (QFileDialog.getOpenFileName(self, 'Open file',
                      '', "Embedding files (*.bin *.pt)")[0])
            if len(file_z) > 0:
                self.embeddingInputFile.setText(file_z)
        self.embeddingSelect.clicked.connect(select_embedding)

        def inpaint(image_view=False):
            print('Launching inpaint')

            if image_view == True:
                inpaint_source = self.imgFilename.text().replace('Filename: ', '')
            else:
                inpaint_source = self.inpaint_img.text()

            if len(inpaint_source) > 0:
                self.mainTab.setCurrentIndex(2)
                self.w = inpainter_window(inpaint_source)
                self.w.show()
        self.inpaintButton.pressed.connect(inpaint)

        def art(art_source, width, height):
            print('Launching art')
            self.img2imgFile.setText(str(Path(sd_output_folder)/'art.png'))
            self.mainTab.setCurrentIndex(1)
            self.art_win = paintWindow(
                sd_folder_path, art_source, int(width), int(height))
            self.art_win.show()
        self.artButton.pressed.connect(lambda: art(
            False, self.widthThing.value(), self.heightThing.value()))

        def add_prompt_tag():

            setattr(self.promptTag, "allItems", lambda: [
                    self.promptTag.itemText(i) for i in range(self.promptTag.count())])

            if len(self.promptTag.currentText()) > 0:
                self.promptVal.setCurrentText(
                    self.promptVal.currentText()+', '+self.promptTag.currentText())

                if self.promptTag.currentText() not in self.promptTag.allItems():
                    if len(self.promptTag.currentText()) > 0:
                        self.promptTag.addItem(self.promptTag.currentText())
                    with open(Path(home_dir_path)/"prompt_tags.txt", "a", encoding='utf-8') as f:
                        f.write('\n'+self.promptTag.currentText())

        self.promptTagAdd.clicked.connect(add_prompt_tag)

        def operations_hub():
            print("Launched operations hub")
            try:
                images_path
            except NameError:
                print('Image folder is empty')
                return

            def op_launcher(op_type):
                print("OP launcher")
                self.start_process(op_type)

            def esrgan_upscale_op():
                print("ESRGAN op")
                esrgan_launch_process()

            def latent_sr():
                print("LatentSR op")
                ldsr_launch_process()

            if self.operationBox.currentIndex() == 0:
                esrgan_upscale_op()

            if self.operationBox.currentIndex() == 1:
                latent_sr()

        self.operationsGoButton.pressed.connect(operations_hub)

        def thread_result(dream_images_to_load):
            print('Thread result function')

            if self.seedCheck.isChecked():
                self.seedVal.setText(str(random.randint(1, 1632714927)))

            self.promptVal.addItem(self.promptVal.currentText())

            with open(Path(home_dir_path)/"sdd_prompt_archive.txt", "a", encoding='utf-8') as f:
                f.write('\n'+self.promptVal.currentText())

            mode_load_images = Load_Images_Class()
            load_img_things = mode_load_images.load_images(
                sd_output_folder, False, dream_images_to_load)
            (image_to_display, image_index, images_path) = load_img_things

            # self.cancelButton.setEnabled(False)
            self.errorMessages.setText(f"SD Dreamer: Finished")
            self.imgFilename.setText('Filename: '+image_to_display)
            pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
            self.imageView.setPixmap(pixmap)
            self.imgIndex.setText(str(image_index))

        # def thread_result(s):
        #     print(s)

        def dreamer_new():

            if self.mainTab.currentIndex() > 2:
                return

            global loaded_model
            global g
            model_ckpt = self.custCheckpointLine.text()

            if loaded_model == False:
                if self.precisionToggle.isChecked() and self.embeddingCheck.isChecked() == False:
                    g = Generate(weights=model_ckpt, gfpgan=gfpgan,
                                 codeformer=codeformer, precision='float32')
                elif self.embeddingCheck.isChecked():
                    g = Generate(weights=model_ckpt, gfpgan=gfpgan,
                                 codeformer=codeformer, precision='float32',
                                 embedding_path=self.embeddingInputFile.text())
                else:
                    g = Generate(weights=model_ckpt, gfpgan=gfpgan,
                                 codeformer=codeformer, precision='auto')

                self.errorMessages.setText(f"SD Dreamer: Loading model...")
                loaded_model = True

            pos_prompt = str(self.promptVal.currentText())
            neg_prompt = str(self.negPromptVal.text())

            if len(neg_prompt) > 0:
                prompt = pos_prompt+', ['+neg_prompt+']'
            else:
                prompt = pos_prompt

            steps = int(self.stepsVal.value())
            iterations = int(self.itsVal.value())
            seed = int(self.seedVal.text())
            outpath = Path(sd_output_folder)/'txt2img_samples'
            width = int(self.widthThing.value())
            height = int(self.heightThing.value())
            scale = float(self.scaleVal.value())
            set_sampler = str(self.samplerToggle.currentText())
            init_img = self.img2imgFile.text()
            strength = float(self.img2imgStrength.value())
            gfpgan_strength = float(self.gfpganStrength.value())
            codeformer_fidelity = float(self.codeformerValue.value())
            facetool = None

            if self.mainTab.currentIndex() == 2:
                outpath = Path(sd_output_folder)/'inpaint_samples'

            if self.gfpganCheck.isChecked():
                facetool = 'gfpgan'

            if self.codeformerCheck.isChecked():
                facetool = 'codeformer'

            if self.gridCheck.isChecked():
                grid = True
            else:
                grid = False

            if self.seamlessCheck.isChecked():
                seamless = True
            else:
                seamless = False

            if self.variantAmountCheck.isChecked():
                variation_amount = float(self.variantAmountValue.value())
            else:
                variation_amount = False

            if self.builtUpscaleCheck.isChecked():
                upscale = [int(self.builtUpscaleScale.currentText()), float(
                    self.builtUpscaleStrength.value())]
            else:
                upscale = None
## new 2.0

            if self.thresholdCheck.isChecked():
                threshold = int(self.thresholdValue.value())
            else:
                threshold = False

            if self.perlinCheck.isChecked():
                perlin_value = float(self.perlinValue.value())
            else:
                perlin_value = False

            if self.memFreeCheck.isChecked():
                free_gpu_mem = True
            else:
                free_gpu_mem = False
##
            dream_base_args = {
                'prompt': '"'+prompt+'"',
                'steps': steps,
                'iterations': iterations,
                'seed': seed,
                'width': width,
                'height': height,
                'scale': scale,
                'sampler': set_sampler,
                'outdir': outpath,
                'gfpgan_strength': gfpgan_strength,
                'grid': grid,
                'seamless': seamless,
                'variation_amount': variation_amount,
                'upscale': upscale,
## new
                'codeformer_fidelity': codeformer_fidelity,
                'threshold': threshold,
                'perlin_value': perlin_value,
                'free_gpu_mem': free_gpu_mem,
                'facetool': facetool,
            }
            return (dream_base_args, prompt, steps, seed, scale,
                    set_sampler, width, height, strength, init_img)

        def txt2img_dream():
            (dream_base_args, prompt, steps, seed, scale,
             set_sampler, *args) = dreamer_new()

            txt2img_args = dream_base_args
            print(dream_base_args)

            if self.hiresfixCheck.isChecked():
                hires_fix = True
            else:
                hires_fix = False
            txt2img_args["hires_fix"] = hires_fix

            msgy = (
                f'Prompt: "{prompt}" Steps: {steps}, Seed: {seed}, Scale: {scale}, Sampler: {set_sampler}')
            self.processOutput.appendPlainText(msgy)

            def launch_txt2img():
                worker = Worker('txt2img', txt2img_args, g)
                self.errorMessages.setText(
                    f"SD Dreamer: Dreaming (txt2img)...")
                worker.signals.result.connect(thread_result)
                self.threadpool.start(worker)
            launch_txt2img()

        def img2img_dream(context_menu_op=False):
            (dream_base_args, prompt, steps, seed, scale,
             set_sampler, width, height, strength, init_img) = dreamer_new()

            outpath = Path(sd_output_folder)/'img2img_samples'
            img2img_args = dream_base_args

            if context_menu_op == True:
                init_img = self.imgFilename.text().replace('Filename: ', '')

            if self.img2imgUpscaleCheck.isChecked():
                image = Image.open(init_img).convert("RGB")
                image = image.resize(
                    (width, height), resample=PIL.Image.Resampling.LANCZOS)
                image.save(Path(outpath.parent)/'upscaled.png')
                init_img = Path(outpath.parent)/'upscaled.png'

            if self.embiggenCheck.isChecked():
                embiggen_scale = int(self.embiggenScale.value())
                embiggen_strength = float(self.embiggenStrength.value())
                embiggen_overlap = float(self.embiggenOverlap.value())
                img2img_args["embiggen"] = embiggen_scale, embiggen_strength, embiggen_overlap
            else:
                img2img_args["embiggen"] = None

            img2img_args["outdir"] = outpath
            img2img_args["strength"] = strength
            img2img_args["init_img"] = str(init_img)

            print('img2imgargs:', img2img_args)

            msgy = (
                f'Prompt: "{prompt}" Steps: {steps}, Seed: {seed}, Scale: {scale}, Sampler: {set_sampler}')
            self.processOutput.appendPlainText(msgy)

            def launch_img2img():
                self.errorMessages.setText(
                    f"SD Dreamer: Dreaming (img2img)...")
                worker = Worker('img2img', img2img_args, g)
                worker.signals.result.connect(thread_result)
                self.threadpool.start(worker)
            launch_img2img()

        def inpaint_dream():
            (dream_base_args, init_img, strength, *args) = dreamer_new()

            # outpath = Path(sd_output_folder)/'inpaint_samples'
            inpaint_args = dream_base_args
            init_img = Path(inpainting_dir)/'masking'/'image.png'
            init_mask = Path(inpainting_dir)/'masking' / \
                'out'/'init_mask.png'
            inpaint_args["init_img"] = str(init_img)
            inpaint_args["init_mask"] = init_mask
            inpaint_args["strength"] = float(self.img2imgStrength.value())

            def gen_masks():
                im_a = Image.open(Path(inpainting_dir) /
                                  'masking'/'image_mask.png').convert('RGB')
                if self.invertMaskCheck.isChecked():
                    im_invert = ImageOps.invert(im_a)
                    im_a_blur = im_invert.filter(
                        ImageFilter.GaussianBlur(self.maskBlurVaue.value()))
                else:
                    im_a_blur = im_a.filter(
                        ImageFilter.GaussianBlur(self.maskBlurVaue.value()))

                im_a = im_a_blur.convert('L')
                im_rgb = Image.open(init_img)
                im_rgba = im_rgb.copy()
                im_rgba.putalpha(im_a)
                im_rgba.save(init_mask)
            gen_masks()

            def launch_inpaint():
                self.errorMessages.setText(
                    f"SD Dreamer: Dreaming (inpaint)...")
                worker = Worker('inpaint', inpaint_args, g)
                worker.signals.result.connect(thread_result)
                self.threadpool.start(worker)
            launch_inpaint()

        def fix_dream(fix_type):
            (dream_base_args, init_img, *args) = dreamer_new()

            fix_args = {}

            init_img = self.imgFilename.text().replace('Filename: ', '')
            fix_args["image_path"] = str(init_img)

            if fix_type == 'codeformer':
                fix_args["tool"] = 'codeformer'
                fix_args["codeformer_fidelity"] = 0.75

            self.errorMessages.setText(
                f"SD Dreamer: Dreaming (fix)...")
            worker = Worker('fix', fix_args, g)
            worker.signals.result.connect(thread_result)
            self.threadpool.start(worker)

        # def outpaintcrop_dream():
        #     (dream_base_args, init_img, *args) = dreamer_new()

        #     outpaintcrop_args = dream_base_args

        #     # outpaintcrop_args = {}

        #     outpaintcrop_args["image_path"] = str(init_img)
        #     outpaintcrop_args["top_crop"] = self.topCrop.value()
        #     outpaintcrop_args["bottom_crop"] = self.bottomCrop.value()
        #     outpaintcrop_args["left_crop"] = self.leftCrop.value()
        #     outpaintcrop_args["right_crop"] = self.rightCrop.value()

        #     print(outpaintcrop_args)

        #     def launch_outpaintcrop():
        #         worker = Worker('outpaintcrop', outpaintcrop_args, g)
        #         self.errorMessages.setText(
        #             f"SD Dreamer: Dreaming (outcrop/outpaint)...")
        #         worker.signals.result.connect(thread_result)
        #         self.threadpool.start(worker)
        #     launch_outpaintcrop()

        def dream_launcher():
            if self.mainTab.currentIndex() == 0:
                txt2img_dream()
            if self.mainTab.currentIndex() == 1:
                img2img_dream()
            if self.mainTab.currentIndex() == 2:
                inpaint_dream()
            # if self.mainTab.currentIndex() == 3:
            #     outpaintcrop_dream()

        self.generateButton.clicked.connect(dream_launcher)

        def esrgan_launch_process(context_menu_op=False):

            if context_menu_op == True:
                single_image = self.imgFilename.text().replace('Filename: ', '')
                op_input_path = Path(images_path)/(single_image)
            else:
                op_input_path = Path(images_path.replace('*.png', ''))

            esrgan_out_path = Path(
                self.outputFolderLine.text())/'upscales'/'esrgan_out'
            os.makedirs(esrgan_out_path, exist_ok=True)
            print('Upscaling, folder in: ', op_input_path)
            print('Upscaling, folder out ', esrgan_out_path)

            esrgan_args = [str(Path(home_dir_path)/'ESRGAN'/'upscale.py'), str(Path(home_dir_path)/'ESRGAN'/'models'/self.rnvModelSelect.currentText(
            )), '--input', str(op_input_path), '--output', str(esrgan_out_path)]

            if context_menu_op == True:
                os.makedirs(Path(esrgan_out_path.parent) /
                            ('inputs'), exist_ok=True)
                one_op_path = Path(esrgan_out_path.parent)/('inputs')
                single_image = Path(single_image).name
                shutil.copyfile(op_input_path, Path(one_op_path/single_image))
                esrgan_args[-3] = str(Path(one_op_path))
                esrgan_args.append('--delete-input')

            print('ESRGAN args:', esrgan_args)

            self.start_process(esrgan_args)

        def ldsr_launch_process(context_menu_op=False):

            if context_menu_op == True:
                single_image = self.imgFilename.text().replace('Filename: ', '')
                op_input_path = Path(images_path)/(single_image)
            else:
                op_input_path = Path(images_path.replace('*.png', ''))

            print('Latent-SR: path to images:', op_input_path)
            latent_sr_out = Path(
                self.outputFolderLine.text())/'upscales'/'latent_sr'
            os.makedirs(latent_sr_out, exist_ok=True)

            latent_sr_args = [str(latent_sr_path), '--img_path', str(op_input_path),
                              '--steps', self.latentSRSteps.text(), '--out_path', str(latent_sr_out)]

            if context_menu_op == True:
                latent_sr_args[1] = "--single"
            print('latent_sr_args:', latent_sr_args)

            self.start_process(latent_sr_args)

    def start_process(self, process_args):

        self.cancelButton.setEnabled(True)

        self.processOutput.appendPlainText("Starting external process")
        self.generator_process = QProcess()
        self.generator_process.stateChanged.connect(self.handle_state)
        self.generator_process.finished.connect(
            lambda: self.process_finished)
        self.generator_process.readyReadStandardOutput.connect(
            self.handle_stdout)
        self.generator_process.readyReadStandardError.connect(
            self.handle_stderr)

        self.generator_process.start(self.pyBinPath.text(), process_args)

    def handle_stderr(self):
        data = self.generator_process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr.strip())

    def handle_stdout(self):
        data = self.generator_process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout.strip())

    def message(self, s):
        self.processOutput.appendPlainText(s)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Idle',
            QProcess.Starting: 'Initialising...',
            QProcess.Running: 'Running...',
        }
        state_name = states[state]
        self.processOutput.appendPlainText(f"SD Dreamer: {state_name}")
        self.errorMessages.setText(f"SD Dreamer: {state_name}")

    def process_finished(self):

        self.processOutput.appendPlainText("Operation finished.")
        self.generator_process = None
        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(1, 1632714927)))
        # self.cancelButton.setEnabled(False)
        self.generateButton.setEnabled(True)

    def stop_process(self):
        print('Terminated process')
        # self.cancelButton.setEnabled(False)
        self.generateButton.setEnabled(True)

        if self.generator_process != None:
            self.generator_process.terminate()
            self.processOutput.appendPlainText("Procesing has been ended.")
            # self.cancelButton.setEnabled(False)
            self.generateButton.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = sd_dreamer_main()
    window.show()
    app.exec()
