################### BETA 0.2 ###################
################### Work in progress ###################

########## to do ##########
# inpaint fix clear
# fint inpainter save, only saves mask?
# add GFPGAN
# expand img2img
# image viewer, redo output
# prompt tags
# clean up code
# moar comments
# vram, ram view
# appicon fix
# prevent changing size after paint saved
# inpaint feedback, errors etc
# fix not cancelling?
# save more settings
# txt2imgHD using img2img even when unchecked? when paint?
# add drag and drop for images
# redo inpaint/clear?
# add img2img to op center
# filter out folders and other files from imageview
# add noise to paint
# add paint to img view
# add stdout to UI
# img2img upscale
# increase max res
# add noise to paint
# new inpainting
# ksamplers to txt2imgHD
# change seeding in scripts
# rename txt2imgbatch file

import configparser
import os
import random
import sys
import threading
from pathlib import Path

import png
from PIL import Image
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

txt2img_default = Path(home_dir_path)/'scripts'/'txt2img_sdd.py'
txt2img_k = Path(home_dir_path)/'scripts'/'txt2img_k_sdd.py'

img2img_default = Path(home_dir_path)/'scripts'/'img2img_sdd.py'
img2img_k = Path(home_dir_path)/'scripts'/'img2img_k_sdd.py'

txt2img_hd = Path(home_dir_path)/'scripts'/'txt2imghd.py'
anon_upscale = Path(home_dir_path)/'scripts'/'upsample.py'
latent_sr_path = Path(home_dir_path)/'scripts'/'predict_sr.py'


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
        self.image.fill(Qt.black)

        # variables
        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 24
        # default color
        self.brushColor = Qt.white

        # QPoint object to tract the point
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()

        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")

        # adding brush size to main menu
        b_size = mainMenu.addMenu("Brush Size")

        inpaintAction = QAction("Inpaint", self)
        saveAction = QAction("Save mask", self)

        # adding short cut for save action
        saveAction.setShortcut("Ctrl + S")
        # adding save to the file menu
        fileMenu.addAction(inpaintAction)

        fileMenu.addAction(saveAction)

        # adding action to the save
        inpaintAction.triggered.connect(self.inpy)
        saveAction.triggered.connect(self.save)

        # creating clear action
        clearAction = QAction("Clear", self)
        # adding short cut to the clear action
        clearAction.setShortcut("Ctrl + C")
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(self.clear)

        # creating options for brush sizes
        # creating action for selecting pixel of 4px
        pix_4 = QAction("4px", self)
        # adding this action to the brush size
        b_size.addAction(pix_4)
        # adding method to this
        pix_4.triggered.connect(self.Pixel_4)

        # similarly repeating above steps for different sizes
        pix_7 = QAction("7px", self)
        b_size.addAction(pix_7)
        pix_7.triggered.connect(self.Pixel_7)

        pix_9 = QAction("9px", self)
        b_size.addAction(pix_9)
        pix_9.triggered.connect(self.Pixel_9)

        pix_12 = QAction("12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        pix_24 = QAction("24px", self)
        b_size.addAction(pix_24)
        pix_24.triggered.connect(self.Pixel_24)

        pix_32 = QAction("32px", self)
        b_size.addAction(pix_32)
        pix_32.triggered.connect(self.Pixel_32)

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
            im_rgb.save(Path(str(inpainting_dir))/'masking'/'out'/'image.png')

            im_rgba = im_rgb.copy()
            im_rgba.putalpha(200)
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
        self.inpaint_process()

    def inpaint_process(self):
        inpaint_py = Path(home_dir_path)/'scripts'/'inpaint.py'
        masky = Path(str(inpainting_dir))/'masking'/'out'
        masky = str(masky / "_")[:-1]

        print('inpaint script=', inpaint_py)
        print('inpaint dir=', inpainting_dir)

        print('Working directory: ', os.getcwd())
        self.inpainter_process = QProcess()  # Keep a reference to the QProcess
        self.inpainter_process.stateChanged.connect(self.handle_state)
        self.inpainter_process.finished.connect(
            self.process_finished)  # Clean up once done
        inpaint_args = [str(inpaint_py), '--indir', str(Path(inpainting_dir)/'masking'),
                        '--outdir', masky, '--steps', sd_dreamer_main(self).inpaintSteps.text()]
        print('Inpaint args - ', sd_dreamer_main(self).pyBinPath.text(), inpaint_args)
        self.inpainter_process.start(py_bin_path_ini, inpaint_args)
        self.setWindowTitle("Inpainting...")

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Idle',
            QProcess.Starting: 'Initialising...',
            QProcess.Running: 'Inpainting...',
        }
        state_name = states[state]
        print(state_name)

    def process_finished(self):
        self.setWindowTitle("Inpainter")
        im_rgb = Image.open(Path(str(inpainting_dir)) /
                            'masking'/'out'/'image.png')
        im_rgb.save(Path(str(inpainting_dir))/'masking'/'image.png')
        im_rgba = im_rgb.copy()
        im_rgba.putalpha(200)
        im_rgba.save(Path(str(inpainting_dir))/'inpaint_view.png')
        self.clear(True)
        self.inpainter_process = None

    def stop_process(self):
        if self.generator_process != None:
            self.generator_process.terminate()

    # method for saving canvas
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG(*.png);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    # method for clearing everything on canvas
    def clear(self, inpainted=True):
        # make the whole canvas white
        self.image.fill(Qt.black)
        self.load_img(inpainted)
        # update
        self.update()

    # methods for changing pixel sizes
    def Pixel_4(self):
        self.brushSize = 4

    def Pixel_7(self):
        self.brushSize = 7

    def Pixel_9(self):
        self.brushSize = 9

    def Pixel_12(self):
        self.brushSize = 12

    def Pixel_24(self):
        self.brushSize = 24

    def Pixel_32(self):
        self.brushSize = 32

    # methods for changing brush color

    def whiteColor(self):
        self.brushColor = Qt.white


# load settings from settings.ini
esrgan_bin_ini = config.get('Settings', 'esrgan_bin')
esrbin_models_ini = config.get('Settings', 'esrbin_models')
py_bin_path_ini = config.get('Settings', 'py_bin_path')
first_run_ini = config.get('Settings', 'first_run')
chkpt_ini = config.get('Settings', 'ckpt_path')

print('First run: ', first_run_ini)

# from scripts.txt2img_k_sdd_batch import*


class sd_dreamer_main(QtWidgets.QFrame, Ui_sd_dreamer_main):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.generator_process = None
        self.w = None
        self.art_win = None
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
        # self.cancelButton.pressed.connect(self.stop_process)

        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(0, 1632714927)))

        self.rnvBinPath.setText(esrgan_bin_ini)
        self.rnvModelPath.setText(esrbin_models_ini)
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
            for x in os.listdir(esrbin_models_ini):  # generate ESGRAN model list
                if x.endswith(".bin"):
                    self.rnvModelSelect.addItem(x.strip('.bin'))
        except:
            print('Real-ESGRAN models not found')

# saving the paths to the ini file

        def operationFolderSelect_select():
            opf = (QFileDialog.getExistingDirectory(
                self, ("Select images folder")))
            if len(opf) > 0:
                self.operationFolder.setText(opf)
                self.load_images(opf, True)
        self.operationFolderSelect.clicked.connect(
            operationFolderSelect_select)

        def rnvBinPathSelect_select():
            rnvBin = (QFileDialog.getOpenFileName(
                self, 'Open file', '', "All files (*.*)")[0])
            if len(rnvBin) > 0:
                self.rnvBinPath.setText(rnvBin)
                config.set('Settings', 'esrgan_bin', rnvBin)
            with open(settings_file, 'w') as configfile:
                config.write(configfile)
            config.set('Settings', 'esrgan_bin', rnvBin)

        self.rnvBinPathSelect.clicked.connect(rnvBinPathSelect_select)

        def rnvModelPathSelect_select():
            rnvModels = (QFileDialog.getExistingDirectory(
                self, ("Select model folder")))
            if len(rnvModels) > 0:
                self.rnvModelPath.setText(rnvModels)
                config.set('Settings', 'esrbin_models', rnvModels)
            with open(settings_file, 'w') as configfile:
                config.write(configfile)

            for x in os.listdir(rnvModels):
                if x.endswith(".bin"):
                    self.rnvModelSelect.addItem(x.strip('.bin'))

        self.rnvModelPathSelect.clicked.connect(rnvModelPathSelect_select)

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
                print('Inpaint source: ', inpaint_source)
        self.inpaint_img_select.clicked.connect(select_inpaint_image)

        def inpaint():
            self.w = inpainter_window()
            self.w.show()
        self.inpaintButton.pressed.connect(inpaint)

        def art():
            self.img2imgFile.setText(
                str(Path(sd_folder_path)/'outputs'/'sd_dreamer/paint.png'))
            self.img2imgRadio.setChecked(True)
            self.art_win = paintWindow(
                int(self.widthThing.currentText()), int(self.heightThing.currentText()))
            self.art_win.show()
        self.artButton.pressed.connect(art)

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

            def anon_upscale_op():
                print("Anon op")
                # op_launcher('anon_upscale_op')

            def latent_sr():
                print("LatentSR op")
                op_launcher('latent_sr_op')

            def inpaint_op():
                global inpaint_source
                inpaint_source = Path(
                    images_path)/self.imgFilename.text().replace('Filename: ', '')
                inpaint_source = str(inpaint_source)
                print(inpaint_source)
                inpaint()
                print("Inpaint op")
                # op_launcher('inpaint_op')

            def art_op():
                print("img2img op")
                # op_launcher('img2img_op')

            if self.operationBox.currentIndex() == 0:
                esrgan_upscale_op()

            # if self.operationBox.currentIndex() == 1:
            #     anon_upscale_op()

            if self.operationBox.currentIndex() == 1:
                latent_sr()

            if self.operationBox.currentIndex() == 2:
                inpaint_op()

            if self.operationBox.currentIndex() == 3:
                art_op()

        self.operationsGoButton.pressed.connect(operations_hub)

        def dreamer_new():
            prompt = str(self.promptVal.currentText())
            steps = int(self.stepsVal.value())
            iterations = int(self.itsVal.value())
            batch = int(self.batchVal.value())
            seed = int(self.seedVal.text())
            precision = str(self.precisionToggle.currentText())
            rows = 3
            outpath = Path(self.outputFolderLine.text())
            width = int(self.widthThing.currentText())
            height = int(self.heightThing.currentText())
            scale = float(self.scaleVal.value())
            set_sampler = str(self.samplerToggle.currentText())
            init_img = self.img2imgFile.text()
            strength = float(self.img2imgStrength.value())
            detail_steps = int(self.txt2imgHD_steps.text())
            detail_scale = int(self.txt2imgHD_scale.text())
            realesrgan = esrgan_bin_ini
            img = init_img

            out_folder_create = Path(self.outputFolderLine.text())/prompt[:120]
            out_folder_create = str(out_folder_create)+'_'+self.seedVal.text()

            for r in ((">", ""), ("<", ""), ("<", ""), ("|", ""), ("?", ""), ("*", ""), ('"', ""), (' ', "_"), (',', ""), ('.', ""), ('\n', ""), (' ', '_')):
                out_folder_create = out_folder_create.replace(*r).strip()

            outpath = out_folder_create

            if self.txt2imgRadio.isChecked():
                txt2img_args = prompt, steps, iterations, batch, seed, precision, rows, outpath, scale, width, height, set_sampler
                print('txt2imgargs-', txt2img_args)

                def launch_txt2img(*txt2img_args):

                    self.errorMessages.setText(f"SD Dreamer: Loading model...")
                    from scripts.txt2img_k_sdd_batch import txt2img_main
                    self.errorMessages.setText(
                        f"SD Dreamer: Dreaming (txt2img)...")
                    txt2img_main(*txt2img_args)
                    self.errorMessages.setText(f"SD Dreamer: Finished")
                    self.load_images(outpath)
                t1 = threading.Thread(
                    target=launch_txt2img, args=(txt2img_args))

            if self.img2imgRadio.isChecked():
                if self.img2imgDisplayed.isChecked() and self.imgFilename.text() == 'Filename: ':
                    print('no image in viewer')
                    return
                elif self.img2imgDisplayed.isChecked() and self.imgFilename.text() != 'Filename: ':
                    init_img = Path(
                        images_path)/self.imgFilename.text().replace('Filename: ', '')
                img2img_args = prompt, steps, iterations, batch, seed, precision, rows, outpath, scale, width, height, set_sampler, str(
                    init_img), strength
                print('img2imgargs-', img2img_args)

                def launch_img2img(*img2img_args):
                    self.errorMessages.setText(f"SD Dreamer: Loading model...")
                    from scripts.txt2img_k_sdd_batch import img2img_main
                    self.errorMessages.setText(
                        f"SD Dreamer: Dreaming (img2img)...")
                    img2img_main(*img2img_args)
                    self.errorMessages.setText(f"SD Dreamer: Finished")
                    self.load_images(outpath)
                t1 = threading.Thread(
                    target=launch_img2img, args=(img2img_args))

            if self.txt2imgHDCheck.isChecked():
                txt2imghd_args = prompt, steps, iterations, seed, outpath, scale, width, height, detail_steps, detail_scale, realesrgan, strength
                if self.txt2imgHDImg.isChecked():
                    txt2imghd_args = prompt, steps, iterations, seed, outpath, scale, width, height, detail_steps, detail_scale, realesrgan, strength, img
                print('txt2imghdargs-', txt2imghd_args)

                def launch_txt2imghd(*txt2imghd_args):

                    self.errorMessages.setText(f"SD Dreamer: Loading model...")
                    from scripts.txt2img_k_sdd_batch import txt2imghd_main
                    self.errorMessages.setText(
                        f"SD Dreamer: Dreaming (txt2imgHD)...")
                    txt2imghd_main(*txt2imghd_args)
                    self.errorMessages.setText(f"SD Dreamer: Finished")
                    self.load_images(outpath)

                t1 = threading.Thread(
                    target=launch_txt2imghd, args=(txt2imghd_args))

            self.generateButton.setEnabled(False)
            t1.start()


            self.promptVal.addItem(self.promptVal.currentText())
            f = open(Path(home_dir_path)/"sdd_prompt_archive.txt", "a")
            f.write('\n'+self.promptVal.currentText())
            f.close()

            if self.seedCheck.isChecked():
                self.seedVal.setText(str(random.randint(0, 1632714927)))

        self.generateButton.clicked.connect(dreamer_new)

# tests

    def start_process(self, process_type, op_enable=False):
        if self.customFolderCheck.isChecked() and op_enable is True:
            global images_path
            images_path = self.operationFolder.text()
            'Operation images input path:', images_path

        self.processOutput.appendPlainText("Starting process")
        # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.generator_process = QProcess()
        self.generator_process.stateChanged.connect(self.handle_state)
        # Clean up once complete.
        self.generator_process.finished.connect(
            lambda: self.process_finished(process_type))
        self.generator_process.readyReadStandardOutput.connect(
            self.handle_stdout)
        self.generator_process.readyReadStandardError.connect(
            self.handle_stderr)
        self.generateButton.setEnabled(False)

        # forbiddenChars = (">", "<", "/", ":" '"', "\\", "|", "?", "*")
        # forbiddenChars=str(forbiddenChars)

        if self.operationOne.isChecked():
            single_image = self.imgFilename.text().replace('Filename: ', '')
            op_input_path = Path(images_path)/(single_image)
        if self.operationalAll.isChecked():
            op_input_path = Path(images_path)

        if process_type == 'esrgan_upscale_op':
            esrgan_out_path = Path(
                self.outputFolderLine.text())/'upscales'/'real_esrgan_out'
            os.makedirs(esrgan_out_path, exist_ok=True)
            print('Upscaling, folder in: ', op_input_path)
            print('Upscaling, folder out ', esrgan_out_path)

            esrgan_args = ['-n', self.rnvModelSelect.currentText(
            ), '-s', self.modelScale.currentText(), '-i', str(op_input_path), '-o', str(esrgan_out_path)]

            if self.operationOne.isChecked():
                esrgan_args[-1] = str(Path(esrgan_out_path)/(single_image))
            print('ESGRAN args: ', esrgan_args)


            self.generator_process.start(self.rnvBinPath.text(), esrgan_args)
            self.cancelButton.setEnabled(True)




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
            self.cancelButton.setEnabled(True)
            return

        print('This part is after upscale and shouldnt be seen when upscaling')


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

    def load_images(self, img_path, cust_load=False):
        global images_path

        if cust_load == True:
            images_path = str(Path(img_path))
            print('custom folder load')
        else:
            print('not custom folder load')
            images_path = str(Path(img_path)/'samples')

        global image_list
        print("images_path - ", images_path)
        image_list = os.listdir(images_path)
        image_count = len(image_list)
        image_index = image_count-image_count

        print(image_count, 'images in folder:', image_list)
        print('image_index=', image_index)

        # global image_to_display
        image_to_display = image_list[-1]
        self.imgFilename.setText('Filename: '+image_to_display)

        pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
        self.imageView.setPixmap(pixmap)
        self.imgIndex.setText(str(image_index))
        self.generateButton.setEnabled(True)

    def process_finished(self, process_type):
        # add the generated images to the image view
        if process_type == 'dream':
            print('proc fin, dream')


        self.processOutput.appendPlainText("Generation finished.")
        self.generator_process = None
        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(0, 1632714927)))
        self.cancelButton.setEnabled(False)
        self.generateButton.setEnabled(True)

    def stop_process(self):
        if self.generator_process != None:
            self.generator_process.terminate()
            # self.generator_process.terminate()
            self.processOutput.appendPlainText("Procesing has been ended.")
            # self.cancelButton.setEnabled(False)
            self.generateButton.setEnabled(True)


app = QtWidgets.QApplication(sys.argv)
window = sd_dreamer_main()
window.show()
app.exec_()
