################### BETA 0.3 ###################
################### Work in progress ###################

########## to do ##########
# inpaint fix clear
# fint inpainter save, only saves mask?
# expand img2img
# prompt tags
# clean up code
# moar comments
# vram, ram view
# appicon fix
# prevent changing size after paint saved
# save more settings
# add drag and drop for images
# add img2img to op center
# fix art paint using view image from img2img
# make art paint refresh load images
# fix painting make 2 images instead of 1
# progress bar
# fix unicode prompt error on win with chinese characters etc
# add config yaml path option
# allow open ,inpaint, other formats than PNG
# image viewer not loading with 1 image

import configparser
import glob
import os
import random
import sys
from pathlib import Path
import shutil

import PIL
import png
from ldm.generate import Generate
from PIL import Image, ImageFilter, ImageOps
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtCore import QUrl  # , QPropertyAnimation
from PySide2.QtCore import QProcess
from PySide2.QtGui import *
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QFileDialog

from painter import paintWindow
from ui import Ui_sd_dreamer_main

global loaded_model
loaded_model = False

# print('working dir=',os.getcwd())
home_dir_path = os.path.dirname(os.path.realpath(__file__))
print('SD Dreamer home directory: ', home_dir_path)

# load settings.ini file
config = configparser.ConfigParser()
settings_file = (Path(home_dir_path)/'settings.ini')

config.read(Path(home_dir_path)/'settings.ini')

inpainting_dir = Path(home_dir_path)/'inpainting'

sd_folder_path = Path(home_dir_path)
sd_folder_path = str(sd_folder_path.parent)

latent_sr_path = Path(home_dir_path)/'scripts'/'predict_sr.py'
sd_output_folder = Path(sd_folder_path)/'outputs'/'sd_dreamer'
esrgan_out_path = Path(sd_output_folder)/'upscales'/'real_esrgan_out'


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


class inpainter_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.inpainter_process = None

        print('Inpaint image: ', inpaint_source)

        r = png.Reader(inpaint_source)
        png_w = (r.read()[0])
        png_h = (r.read()[1])
        os.chdir(sd_folder_path)

        # setting title
        self.setWindowTitle("Inpainter")

        self.setMaximumHeight(png_h)
        self.setMaximumWidth(png_w)
        self.setMinimumHeight(png_h)
        self.setMinimumWidth(png_w)

        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)

        # making image color to black
        self.image.fill(Qt.white)

        # variables
        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 24
        # default color
        self.brushColor = Qt.black

        # QPoint object to tract the point
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()

        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")

        # adding brush size to main menu
        b_size = mainMenu.addMenu("Brush Size")

        b_color = mainMenu.addMenu("Brush")

        black = QAction("Select", self)
        b_color.addAction(black)
        black.triggered.connect(self.blackColor)

        white = QAction("Erase", self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)

        inpaintAction = QAction("Save", self)

        fileMenu.addAction(inpaintAction)

        inpaintAction.triggered.connect(self.inpy)
        # saveAction.triggered.connect(self.save)

        # creating clear action
        clearAction = QAction("Clear", self)
        # adding short cut to the clear action
        clearAction.setShortcut("Ctrl + C")
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(self.clear)

        pix_6 = QAction("6px", self)
        # adding this action to the brush size
        b_size.addAction(pix_6)
        # adding method to this
        pix_6.triggered.connect(self.Pixel_6)

        pix_12 = QAction("12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        pix_24 = QAction("24px", self)
        b_size.addAction(pix_24)
        pix_24.triggered.connect(self.Pixel_24)

        pix_32 = QAction("32px", self)
        b_size.addAction(pix_32)
        pix_32.triggered.connect(self.Pixel_32)

        pix_48 = QAction("48px", self)
        b_size.addAction(pix_48)
        pix_48.triggered.connect(self.Pixel_48)

        # similarly repeating above steps for different color
        white = QAction("White", self)
        white.triggered.connect(self.whiteColor)

        self.load_img(False)

    def load_img(self, inpainted):

        if inpainted == True:
            im_rgb = Image.open(Path(str(inpainting_dir)) /
                                'masking'/'out'/'image.png')
        else:
            im_rgb = Image.open(inpaint_source)
            im_rgb.save(Path(str(inpainting_dir))/'masking'/'image.png')
            # im_rgb.save(Path(str(inpainting_dir))/'masking'/'out'/'image.png')

            im_rgba = im_rgb.copy()
            im_rgba.putalpha(215)
            im_rgba.save(Path(str(inpainting_dir))/'inpaint_view.png')

        label = QLabel(self)
        pixy = Path(inpainting_dir)/'inpaint_view.png'
        pixmap = QPixmap(str(pixy))
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    # method for checking mouse cicks
    def mousePressEvent(self, event):

        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            # make drawing flag true
            self.drawing = True
            # make last point to the point of cursor
            self.lastPoint = event.pos()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):

        # checking if left button is pressed and drawing flag is true
        if (event.buttons() & Qt.LeftButton) & self.drawing:

            # creating painter object
            painter = QPainter(self.image)

            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()

    # method for mouse left button release
    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False

    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)

        # draw rectangle  on the canvas
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def inpy(self):
        img_mask_s = (str(Path(inpainting_dir)/'masking'/'image_mask.png'))
        self.image.save(img_mask_s)
        # self.inpaint_process()
        print(sd_dreamer_main().promptVal.currentText())

        self.setWindowTitle("Saved. Press 'Dream (inpaint)' to inpaint")

    def clear(self, inpainted=True):
        # make the whole canvas white
        self.image.fill(Qt.white)
        self.load_img(inpainted)
        # update
        self.update()

    def Pixel_6(self):
        self.brushSize = 6

    def Pixel_12(self):
        self.brushSize = 12

    def Pixel_24(self):
        self.brushSize = 24

    def Pixel_32(self):
        self.brushSize = 32

    def Pixel_48(self):
        self.brushSize = 48

    def whiteColor(self):
        self.brushColor = Qt.white

    def blackColor(self):
        self.brushColor = Qt.black


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
        print('mode is', mode)
        # print('args is:', mode_args)

        if mode == 'txt2img':
            load_mode = 'txt2img_samples'
            txt2img_args = mode_args

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
                gfpgan_strength=txt2img_args["gfpgan_strength"],
                grid=txt2img_args["grid"],
                seamless=txt2img_args["seamless"],
                variation_amount=txt2img_args["variation_amount"],
                upscale=txt2img_args["upscale"],
            )

            print('txt2img args:', txt2img_args)

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
                gfpgan_strength=img2img_args["gfpgan_strength"],
                grid=img2img_args["grid"],
                seamless=img2img_args["seamless"],
                upscale=img2img_args["upscale"]
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
                # gfpgan_strength=inpaint_args["gfpgan_strength"],
                # grid=inpaint_args["grid"],
                # seamless=inpaint_args["seamless"],
                init_img=inpaint_args["init_img"],
                init_mask=inpaint_args["init_mask"],
                upscale=inpaint_args["upscale"]
            )

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

        # image_list=[]
        pixmap = QPixmap(str(Path(home_dir_path)/('view_default.png')))
        self.imageView.setPixmap(pixmap)

        def cycle_images(button):
            try:
                image_count = len(image_list)
            except:
                print('image list is empty')
                image_count = 0
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

        check_install = os.path.exists(
            Path(sd_folder_path) / 'environment.yaml')
        if check_install == False:
            self.errorMessages.setText(
                "WARNING: SD install folder seems incorrect. SD Dreamer folder must be in SD install folder")
            print(
                "WARNING: SD install folder seems incorrect. SD Dreamer folder must be in SD install folder")

        try:
            os.chdir(sd_folder_path)
        except:
            print("SD FOLDER NOT FOUND")
            self.errorMessages.setText("The SD folder not found")

        print('SD install working directory: ', sd_folder_path)

        # self.generateButton.pressed.connect(
        #     lambda: self.start_process('dream'))
        self.cancelButton.pressed.connect(self.stop_process)

        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(0, 1632714927)))


        self.pyBinPath.setText(py_bin_path_ini)
        self.custCheckpointLine.setText(chkpt_ini)

        if first_run_ini == '0':

            self.custCheckpointLine.setText(
                str(Path(sd_folder_path)/'models'/'ldm'/'stable-diffusion-v1'/'model.ckpt'))

            config.set('Settings', 'first_run', '1')
            config.set('Settings', 'ckpt_path', str(
                Path(sd_folder_path)/'models'/'ldm'/'stable-diffusion-v1'/'model.ckpt'))
            with open(settings_file, 'w') as configfile:
                config.write(configfile)

        self.outputFolderLine.setText(
            str(Path(sd_folder_path)/'outputs'/'sd_dreamer'))

        try:
            for x in os.listdir(Path(home_dir_path)/'ESRGAN'/'models'):  # generate ESRGAN model list
                if x.endswith(".pth"):
                    self.rnvModelSelect.addItem(x)
        except:
            print('ESRGAN models not found')

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
        prompt_list = []
        try:
            for old_prompt in reversed(list(open(Path(home_dir_path)/"sdd_prompt_archive.txt"))):
                prompt_list.append(old_prompt.strip())
                prompt_list = list(dict.fromkeys(prompt_list))
        except:
            print("SD prompt archive not found")

        for old_prompt in prompt_list:
            self.promptVal.addItem(old_prompt)

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
                self, 'Open file', '', "Images (*.png)")[0])
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

        def inpaint():
            global inpaint_source
            if self.inpaintingDisplayedCheck.isChecked():
                inpaint_source = self.imgFilename.text().replace('Filename: ', '')
            else:
                inpaint_source = self.inpaint_img.text()

            if len(inpaint_source) > 0:
                self.w = inpainter_window()
                self.w.show()
        self.inpaintButton.pressed.connect(inpaint)

        def art(art_source, width, height):
            self.img2imgFile.setText(str(Path(sd_output_folder)/'art.png'))
            self.mainTab.setCurrentIndex(1)
            self.img2imgDisplayed.setChecked(False)
            self.art_win = paintWindow(
                sd_folder_path, art_source, int(width), int(height))
            self.art_win.show()
            print('art finished')
        self.artButton.pressed.connect(lambda: art(
            False, self.widthThing.currentText(), self.heightThing.currentText()))

        def operations_hub():
            print("Operations hub started")

            try:
                images_path
            except NameError:
                print('Image folder is empty')
                if self.customFolderCheck.isChecked() == False:
                    return

            def op_launcher(op_type):
                print("OP launcher")
                self.start_process(op_type, op_enable=True)

            def esrgan_upscale_op():
                # images_path
                print("ESRGAN op")
                op_launcher('esrgan_upscale_op', )

            def latent_sr():
                print("LatentSR op")
                op_launcher('latent_sr_op')

            # def inpaint_op():
            #     global inpaint_source
            #     inpaint_source = Path(
            #         images_path)/self.imgFilename.text().replace('Filename: ', '')
            #     inpaint_source = str(inpaint_source)
            #     print(inpaint_source)
            #     inpaint()
            #     print("Inpaint op")
            #     # op_launcher('inpaint_op')

            def art_op():
                art_source = self.imgFilename.text().replace('Filename: ', '')
                art_source = str(art_source)
                art(art_source, 0, 0)

            def read_metadata_op():
                print('Get metadata')
                filename = self.imgFilename.text().replace('Filename: ', '')
                im = Image.open(filename)
                im.load()  # Needed only for .png EXIF data (see citation above)
                self.processOutput.appendPlainText(
                    'Metadata: '+im.info['Dream'])

            def art_op():
                art_source = Path(
                    images_path)/self.imgFilename.text().replace('Filename: ', '')
                art_source = str(art_source)
                art(art_source, 0, 0)

            if self.operationBox.currentIndex() == 0:
                esrgan_upscale_op()

            if self.operationBox.currentIndex() == 1:
                latent_sr()

            # if self.operationBox.currentIndex() == 2:
            #     inpaint_op()

            if self.operationBox.currentIndex() == 2:
                art_op()

            if self.operationBox.currentIndex() == 3:
                read_metadata_op()

        self.operationsGoButton.pressed.connect(operations_hub)

        def thread_result(dream_images_to_load):
            print('thread result function')

            if self.seedCheck.isChecked():
                self.seedVal.setText(str(random.randint(1, 1632714927)))

            self.promptVal.addItem(self.promptVal.currentText())
            f = open(Path(home_dir_path)/"sdd_prompt_archive.txt", "a")
            f.write('\n'+self.promptVal.currentText())
            f.close()

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
                    g = Generate(weights=model_ckpt, full_precision=True)
                if self.embeddingCheck.isChecked():
                    g = Generate(weights=model_ckpt, full_precision=True,
                                 embedding_path=self.embeddingInputFile.text())
                else:
                    g = Generate(weights=model_ckpt)

                self.errorMessages.setText(f"SD Dreamer: Loading model...")
                loaded_model = True

            prompt = str(self.promptVal.currentText())
            steps = int(self.stepsVal.value())
            iterations = int(self.itsVal.value())
            seed = int(self.seedVal.text())
            outpath = Path(sd_output_folder)/'txt2img_samples'
            width = int(self.widthThing.currentText())
            height = int(self.heightThing.currentText())
            scale = float(self.scaleVal.value())
            set_sampler = str(self.samplerToggle.currentText())
            init_img = self.img2imgFile.text()
            strength = float(self.img2imgStrength.value())

            if self.mainTab.currentIndex() == 2:
                outpath = Path(sd_output_folder)/'inpaint_samples'

            if self.gfpganCheck.isChecked():
                gfpgan_strength = float(self.gfpganStrength.value())
            else:
                gfpgan_strength = False

            if self.gridCheck.isChecked():
                grid = False
            else:
                grid = True

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
            }

            if self.mainTab.currentIndex() == 0:
                txt2img_args = dream_base_args
                # print(dream_base_args)

                msgy = (
                    f'Prompt: "{prompt}" Steps: {steps}, Seed: {seed}, Scale: {scale}, Sampler: {set_sampler}')
                self.processOutput.appendPlainText(msgy)

                def txt2img_go():
                    worker = Worker('txt2img', txt2img_args, g)
                    self.errorMessages.setText(
                        f"SD Dreamer: Dreaming (txt2img)...")
                    worker.signals.result.connect(thread_result)
                    self.threadpool.start(worker)
                txt2img_go()

            if self.mainTab.currentIndex() == 1:

                # check if an image is loaded in the viewer before img2img
                if self.img2imgDisplayed.isChecked() and self.imgFilename.text() == 'Filename: ':
                    print('No image in viewer')
                    return
                elif self.img2imgDisplayed.isChecked() and self.imgFilename.text() != 'Filename: ':
                    try:
                        assert os.path.isfile(init_img)
                    except AssertionError or NameError:
                        print("INVALID INIT IMAGE")

                    print('initimg:', init_img)
                    init_img = Path(
                        self.imgFilename.text().replace('Filename: ', ''))

                if self.img2imgUpscaleCheck.isChecked():
                    image = Image.open(init_img).convert("RGB")
                    image = image.resize(
                        (width, height), resample=PIL.Image.Resampling.LANCZOS)
                    image.save(Path(outpath.parent)/'upscaled.png')
                    init_img = Path(outpath.parent)/'upscaled.png'

                outpath = Path(sd_output_folder)/'img2img_samples'
                img2img_args = dream_base_args
                img2img_args["outdir"] = outpath
                img2img_args["strength"] = strength
                img2img_args["init_img"] = str(init_img)

                print('img2imgargs', img2img_args)

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

            if self.mainTab.currentIndex() == 2:

                outpath = Path(sd_output_folder)/'inpaint_samples'
                inpaint_args = dream_base_args
                init_img = Path(inpainting_dir)/'masking'/'image.png'
                init_mask = Path(inpainting_dir)/'masking' / \
                    'out'/'init_mask.png'
                inpaint_args["init_img"] = str(init_img)
                inpaint_args["init_mask"] = init_mask

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

        self.generateButton.clicked.connect(dreamer_new)

    def start_process(self, process_type, op_enable=False):

        self.cancelButton.setEnabled(True)

        if self.customFolderCheck.isChecked() and op_enable is True:
            global images_path
            images_path = self.operationFolder.text()
            'Operation images input path:', images_path

        self.processOutput.appendPlainText("Starting process")
        self.generator_process = QProcess()
        self.generator_process.stateChanged.connect(self.handle_state)
        self.generator_process.finished.connect(
            lambda: self.process_finished(process_type))
        self.generator_process.readyReadStandardOutput.connect(
            self.handle_stdout)
        self.generator_process.readyReadStandardError.connect(
            self.handle_stderr)

        if self.operationOne.isChecked():
            single_image = self.imgFilename.text().replace('Filename: ', '')
            op_input_path = Path(images_path)/(single_image)
        if self.operationalAll.isChecked():
            op_input_path = Path(images_path.replace('*.png', ''))

        if process_type == 'esrgan_upscale_op':
            esrgan_out_path = Path(
                self.outputFolderLine.text())/'upscales'/'esrgan_out'
            os.makedirs(esrgan_out_path, exist_ok=True)
            print('Upscaling, folder in: ', op_input_path)
            print('Upscaling, folder out ', esrgan_out_path)

            esrgan_args = [str(Path(home_dir_path)/'ESRGAN'/'upscale.py'), str(Path(home_dir_path)/'ESRGAN'/'models'/self.rnvModelSelect.currentText(
            )), '--input', str(op_input_path), '--output', str(esrgan_out_path)]

            if self.operationOne.isChecked():
                one_op_path = Path(esrgan_out_path.parent)/('inputs')
                single_image = Path(single_image).name
                shutil.copyfile(op_input_path, Path(one_op_path/single_image))
                esrgan_args[-3] = str(Path(one_op_path))
                esrgan_args.append('--delete-input')

            print('ESRGAN args: ', esrgan_args)
                
            self.generator_process.start(self.pyBinPath.text(), esrgan_args)
            return

        if process_type == 'latent_sr_op':
            print('Latent-SR: path to images:', op_input_path)
            latent_sr_out = Path(
                self.outputFolderLine.text())/'upscales'/'latent_sr'
            os.makedirs(latent_sr_out, exist_ok=True)

            latent_sr_args = [str(latent_sr_path), '--img_path', str(op_input_path),
                              '--steps', self.latentSRSteps.text(), '--out_path', str(latent_sr_out)]

            if self.operationOne.isChecked():
                latent_sr_args[1] = "--single"
            print('latent_sr_args:', latent_sr_args)

            self.generator_process.start(self.pyBinPath.text(), latent_sr_args)
            return

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
            QProcess.Running: 'Dreaming...',
        }
        state_name = states[state]
        self.processOutput.appendPlainText(f"SD Dreamer: {state_name}")
        self.errorMessages.setText(f"SD Dreamer: {state_name}")

    def process_finished(self, process_type):
        if process_type == 'dream':
            print('proc fin, dream')

        self.processOutput.appendPlainText("Generation finished.")
        self.generator_process = None
        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(1, 1632714927)))
        # self.cancelButton.setEnabled(False)
        self.generateButton.setEnabled(True)

    def stop_process(self):
        print('cancelled')
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
    app.exec_()
