# importing libraries
import configparser
import os
import random
import sys
from pathlib import Path

import png
from PIL import Image
from PySide2.QtCore import *
from PySide2.QtCore import QProcess
from PySide2.QtGui import *
from PySide2.QtWidgets import *


################### ALPHA 0.1 ###################

# print('working dir=',os.getcwd())
home_dir_path = os.path.dirname(os.path.realpath(__file__))
print('SD Dreamer home directory: ',home_dir_path)

# load settings.ini file
config = configparser.ConfigParser()
settings_file=(Path(home_dir_path)/'settings.ini')

# define directories
config.read(Path(home_dir_path)/'settings.ini')
# sd_folder_path = config.get('Settings', 'sd_folder')

inpainting_dir=Path(home_dir_path)/'inpainting'
print('Inpaint directory: ',inpainting_dir)

sd_folder_path=Path(home_dir_path)
sd_folder_path=str(sd_folder_path.parent)

txt2img_default=Path(home_dir_path)/'scripts'/'txt2img_sdd.py'
txt2img_k=Path(home_dir_path)/'scripts'/'txt2img_k_sdd.py'
txt2img_opti=Path(home_dir_path)/'scripts'/'optimized_txt2img_sdd.py'
txt2img_opti_k=Path(home_dir_path)/'scripts'/'optimized_txt2img_k_sdd.py'

img2img_default=Path(home_dir_path)/'scripts'/'img2img_sdd.py'
img2img_k=Path(home_dir_path)/'scripts'/'img2img_k_sdd.py'
img2img_opti=Path(home_dir_path)/'scripts'/'optimized_img2img_sdd.py'
img2img_opti_k=Path(home_dir_path)/'scripts'/'optimized_img2img_k_sdd.py'

class inpainter_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.inpainter_process = None

        print('Inpaint image: ',inpaint_source)

        r=png.Reader(inpaint_source)
        png_w=(r.read()[0])
        png_h=(r.read()[1])
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

        if inpainted==True:
            im_rgb = Image.open(Path(str(inpainting_dir))/'masking'/'out'/'image.png')
        else:
            
            im_rgb = Image.open(inpaint_source)
            im_rgb.save(Path(str(inpainting_dir))/'masking'/'image.png')
            im_rgb.save(Path(str(inpainting_dir))/'masking'/'out'/'image.png')

            im_rgba = im_rgb.copy()
            im_rgba.putalpha(200)
            im_rgba.save(Path(str(inpainting_dir))/'inpaint_view.png')

        # print('view=Path(str(inpainting_dir)+'/inpaint_view.png')
        label = QLabel(self)
        pixy=Path(inpainting_dir)/'inpaint_view.png'
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
        img_mask_s=(str(Path(inpainting_dir)/'masking'/'image_mask.png'))
        self.image.save(img_mask_s)
        self.inpaint_process()

    def inpaint_process(self):
        # inpaint_py='/home/pigeondave/gits/stable-diffusion-ret/scripts/inpaint.py'

        # print('inpaint script=', inpaint_py)
        # print('inpaint dir=', inpainting_dir)

        inpaint_py=Path(home_dir_path)/'scripts'/'inpaint.py'

        masky=Path(str(inpainting_dir))/'masking'/'out'
        masky=str(masky / "_")[:-1]

        print('Working directory: ',os.getcwd())
        self.inpainter_process = QProcess()  # Keep a reference to the QProcess
        self.inpainter_process.stateChanged.connect(self.handle_state)
        self.inpainter_process.finished.connect(self.process_finished)  # Clean up once done
        inpaint_args=[str(inpaint_py), '--indir', str(Path(inpainting_dir)/'masking'), '--outdir', masky, '--steps', sd_dreamer_main(self).inpaintSteps.text()]
        print('Inpaint args - ', sd_dreamer_main(self).pyBinPath.text(),inpaint_args)
        print(sd_dreamer_main(self).pyBinPath.text())
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
        im_rgb = Image.open(Path(str(inpainting_dir))/'masking'/'out'/'image.png')
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
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "","PNG(*.png);;All Files(*.*) ")
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

from PySide2 import QtWidgets
from PySide2.QtCore import QUrl  # , QPropertyAnimation
from PySide2.QtCore import QProcess
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFileDialog

from painter import paintWindow
from ui import Ui_sd_dreamer_main

# load settings from settings.ini

esrgan_bin_ini = config.get('Settings', 'esrgan_bin')
esrbin_models_ini = config.get('Settings', 'esrbin_models')
up_input_folder_ini = config.get('Settings', 'up_input_folder')
up_output_folder_ini = config.get('Settings', 'up_output_folder')
py_bin_path_ini = config.get('Settings', 'py_bin_path')
first_run_ini = config.get('Settings', 'first_run')

print('First run: ',first_run_ini)

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
                image_count=len(image_list)
            except: 
                print('image list is empty')
                image_count=0
            image_index=int(int(self.imgIndex.text()))

            if button == 'next' and int(image_index) < image_count-1:
                image_index=int(int(self.imgIndex.text())) + 1
                image_to_display=image_list[image_index]
                pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
                self.imageView.setPixmap(pixmap)
                print('next to',image_to_display)
                self.imgIndex.setText(str(image_index))

            if button == 'previous'and int(image_index) > 0:
                image_index=int(int(self.imgIndex.text()))-1
                image_to_display=image_list[image_index]
                pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
                self.imageView.setPixmap(pixmap)
                print('next to',image_to_display)
                self.imgIndex.setText(str(image_index))

        self.nextImageButton.clicked.connect(lambda: cycle_images('next'))
        self.previousImgButton.clicked.connect(lambda: cycle_images('previous'))

# check for the base SD install
        check_install = os.path.exists(Path(sd_folder_path) / 'environment.yaml') 
        if check_install == False:
            self.errorMessages.setText("WARNING: SD install folder seems incorrect. SD Dreamer folder must be in SD install folder")
            print ("WARNING: SD install folder seems incorrect. SD Dreamer folder must be in SD install folder")

        try:
            os.chdir(sd_folder_path)
        except:
            print("SD FOLDER NOT FOUND")
            self.errorMessages.setText("The SD folder not found")
      
        print('SD install working directory: ',sd_folder_path)

        def upscale_process():
            self.start_process(True)

        def dream_process():
            self.start_process(False)

        self.generateButton.pressed.connect(dream_process)
        self.cancelButton.pressed.connect(self.stop_process)
        self.upscaleButton.pressed.connect(upscale_process)

        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(0,1632714927)))

        self.rnvBinPath.setText(esrgan_bin_ini)
        self.rnvModelPath.setText(esrbin_models_ini)
        self.upImageInputFolder.setText(up_input_folder_ini)
        self.upImageOutputFolder.setText(up_output_folder_ini)
        self.pyBinPath.setText(py_bin_path_ini)

        if first_run_ini == '0':

            config.set('Settings', 'first_run', '1')
            with open(settings_file, 'w') as configfile:
                config.write(configfile)

        self.outputFolderLine.setText(str(Path(sd_folder_path)/'outputs'/'sd_dreamer'))

        try:
            for x in os.listdir(esrbin_models_ini): # generate ESGRAN model list
                if x.endswith(".bin"):
                    self.rnvModelSelect.addItem(x.strip('.bin'))
        except:
            print('Real-ESGRAN models not found')

# saving the paths to the ini file

        def rnvBinPathSelect_select():
                rnvBin=(QFileDialog.getOpenFileName(self, 'Open file', '',"All files (*.*)")[0])
                if len(rnvBin) > 0:
                    self.rnvBinPath.setText(rnvBin)
                    config.set('Settings', 'esrgan_bin', rnvBin)
                with open(settings_file, 'w') as configfile:
                    config.write(configfile)
                config.set('Settings', 'esrgan_bin', rnvBin)

        self.rnvBinPathSelect.clicked.connect(rnvBinPathSelect_select)

        def rnvModelPathSelect_select():
                rnvModels=(QFileDialog.getExistingDirectory(self, ("Select model folder")))
                if len(rnvModels) > 0:
                    self.rnvModelPath.setText(rnvModels)
                    config.set('Settings', 'esrbin_models', rnvModels)
                with open(settings_file, 'w') as configfile:
                    config.write(configfile)

                for x in os.listdir(rnvModels):
                    if x.endswith(".bin"):
                        self.rnvModelSelect.addItem(x.strip('.bin'))

        self.rnvModelPathSelect.clicked.connect(rnvModelPathSelect_select)

        def upImageInputFolderSelect_select():
                up_input_img_folder=(QFileDialog.getExistingDirectory(self, ("Select input folder")))
                if len(up_input_img_folder) > 0:
                    self.upImageInputFolder.setText(up_input_img_folder)
                    config.set('Settings', 'up_input_folder', up_input_img_folder)
                with open(settings_file, 'w') as configfile:
                    config.write(configfile)
        self.upImageInputFolderSelect.clicked.connect(upImageInputFolderSelect_select)

        def upImageOutputFolderSelect_select():
                up_output_img_folder=(QFileDialog.getExistingDirectory(self, ("Select output folder")))
                if len(up_output_img_folder) > 0:
                    self.upImageOutputFolder.setText(up_output_img_folder)
                    config.set('Settings', 'up_output_folder', up_output_img_folder)
                with open(settings_file, 'w') as configfile:
                    config.write(configfile)
        self.upImageOutputFolderSelect.clicked.connect(upImageOutputFolderSelect_select)

        def py_binSelect_select():
                py_bin_path=(QFileDialog.getOpenFileName(self, 'Open file', '',"All files (*.*)")[0])
                if len(py_bin_path) > 0:
                    self.pyBinPath.setText(py_bin_path)
                    config.set('Settings', 'py_bin_path', py_bin_path)
                with open(settings_file, 'w') as configfile:
                    config.write(configfile)
        self.pyBinSelect.clicked.connect(py_binSelect_select)

 # add prompts and remove duplicates       
        prompt_list=[]
        try:
            for old_prompt in reversed(list(open(Path(home_dir_path)/"sdd_prompt_archive.txt"))):
                prompt_list.append(old_prompt.strip())
                prompt_list = list(dict.fromkeys(prompt_list))
        except:
            print("SD prompt archive not found")

        for old_prompt in prompt_list:
            self.promptVal.addItem(old_prompt)

        def select_img2imgimg():
            file_x=(QFileDialog.getOpenFileName(self, 'Open file', '',"Images (*.png *.jpg *.bmp *.webp)")[0])
            if len(file_x) > 0:
                self.img2imgFile.setText(file_x)
        self.imgFileSelect.clicked.connect(select_img2imgimg)

        def select_outputFolder():
            file_y=(QFileDialog.getExistingDirectory(self, ("Select output folder")))
            if len(file_y) > 0:
                self.outputFolderLine.setText(file_y)
        self.outputFolderSelect.clicked.connect(select_outputFolder)

        def select_inpaint_image():
            global inpaint_source
            inpaint_source=(QFileDialog.getOpenFileName(self, 'Open file', '',"Images (*.png)")[0])
            if len(inpaint_source) > 0:
                self.inpaint_img.setText(inpaint_source)
                print('Inpaint source: ',inpaint_source)
        self.inpaint_img_select.clicked.connect(select_inpaint_image)

        def inpaint():
            self.w = inpainter_window()
            self.w.show()
        self.inpaintButton.pressed.connect(inpaint)

        def art():
            self.img2imgFile.setText(str(Path(sd_folder_path)/'outputs'/'sd_dreamer/paint.png'))
            self.img2imgCheck.setChecked(True)
            self.art_win = paintWindow(int(self.widthThing.currentText()), int(self.heightThing.currentText()))
            self.art_win.show()
        self.artButton.pressed.connect(art)
 
    def start_process(self, upscale_go):
        self.processOutput.appendPlainText("Starting up process")
        self.generator_process = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.generator_process.stateChanged.connect(self.handle_state)
        self.generator_process.finished.connect(self.process_finished)  # Clean up once complete.
        self.generator_process.readyReadStandardOutput.connect(self.handle_stdout)
        self.generator_process.readyReadStandardError.connect(self.handle_stderr)

        # forbiddenChars = (">", "<", "/", ":" '"', "\\", "|", "?", "*")
        # forbiddenChars=str(forbiddenChars)

        prompt=self.promptVal.currentText()
    
        # print('folder to make=',out_folder_create)

        if upscale_go == True:
            print('Upscaling, folder in: ', self.upImageInputFolder.text())
            print('Upscaling, folder out ', self.upImageOutputFolder.text())

            self.generator_process.start(esrgan_bin_ini, ['-n',self.rnvModelSelect.currentText(),'-s',self.modelScale.currentText(), '-i', self.upImageInputFolder.text(), '-o', self.upImageOutputFolder.text()])
            self.cancelButton.setEnabled(True)
            self.generateButton.setEnabled(False)

        for r in ((">", ""), ("<", ""),("/", ""),("<", ""),("?", ""),("*", ""),("\\", ""),('"', ""),(',', ""),('.', ""),('\n', "")):
            prompt = prompt.replace(*r).strip()
        global out_folder_create
        out_folder_create=Path(self.outputFolderLine.text())/prompt.replace(' ', '_')[:150]
        out_folder_create=str(out_folder_create)+'_'+self.seedVal.text()

        for r in ((">", ""), ("<", ""),("<", ""),("|", ""),("?", ""),("*", ""),('"', ""),(' ', "_"),(',', ""),('.', ""),('\n', "")):
            out_folder_create = out_folder_create.replace(*r).strip()

        else:
            if self.samplerToggle.currentText() == 'ddim' or self.samplerToggle.currentText() == 'plms':
                txt2img_file=txt2img_default
                img2img_file=img2img_default
                if self.optimizedCheck.isChecked():
                    txt2img_file=txt2img_opti
                    img2img_file=img2img_opti
            else:
                txt2img_file=txt2img_k
                img2img_file=img2img_k
                if self.optimizedCheck.isChecked():
                    txt2img_file=txt2img_opti_k
                    img2img_file=img2img_opti_k
                
            sd_args=[f'{txt2img_file}', '--prompt', r'"'+prompt+r'"','--precision',self.precisionToggle.currentText(), '--W', self.widthThing.currentText(),'--H', self.heightThing.currentText(), '--scale', str(self.scaleVal.value()), '--n_iter', str(self.itsVal.value()), '--n_samples', str(self.batchVal.value()), '--ddim_steps', str(self.stepsVal.value()), '--seed', self.seedVal.text(), '--n_rows', '3','--outdir', str(Path(out_folder_create))]

            if self.small_batchCheck.isChecked():
                sd_args.insert(-4, "--turbo")

            if self.img2imgCheck.isChecked():
                sd_args[0] = str(Path(img2img_file))
                sd_args.pop(5),sd_args.pop(5),sd_args.pop(5),sd_args.pop(5),
                sd_args.insert(-4, "--init-img")
                sd_args.insert(-4, self.img2imgFile.text())
                sd_args.insert(-4, "--strength")
                sd_args.insert(-4, self.img2imgStrength.text())
                # if img2img_file==img2img_k:
                #     sd_args.insert(3, "--klms")
                #     print("Inserted KLMS into img2img")
                    
            if self.gridCheck.isChecked():
                    sd_args.insert(3, "--skip_grid")

            if self.fixedCodeCheck.isChecked():
                    sd_args.insert(3, "--fixed_code")

            if self.samplerToggle.currentText() == 'ddim' or 'plms' and self.img2imgCheck.isChecked() == False:
                if self.samplerToggle.currentText() == 'plms':
                    sd_args.insert(3, "--plms")

            if txt2img_file==txt2img_k or txt2img_file==txt2img_opti_k or txt2img_file==img2img_opti_k or txt2img_file==img2img_k:
                print('k file detected')
                if self.samplerToggle.currentText() == 'k_lms':
                    sd_args.insert(3, "lms")
                if self.samplerToggle.currentText() == 'k_euler_a':
                    sd_args.insert(3, "euler")
                if self.samplerToggle.currentText() == 'k_dpm_2_a':
                    sd_args.insert(3, "dpm")
                sd_args.insert(3, "--sampler")
            else:
                print('kfile not detected')
            print('txt2img file: ',txt2img_file)
            print('img2img file: ',img2img_file)

            self.promptVal.addItem(self.promptVal.currentText())
            f = open(Path(home_dir_path)/"sdd_prompt_archive.txt", "a")
            f.write('\n'+self.promptVal.currentText())
            f.close()

            self.generator_process.start(py_bin_path_ini, sd_args)
            print(sd_args)
            self.cancelButton.setEnabled(True)
            self.generateButton.setEnabled(False)
            self.upscaleButton.setEnabled(False)

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

    def process_finished(self):
        
        def load_images(img_path=out_folder_create):
            global images_path
            images_path=str(Path(img_path)/('samples'))
            global image_list
            image_list = os.listdir(images_path)
            image_count=len(image_list)
            image_index=image_count-image_count

            print(image_count,'images in folder:', image_list)
            print('image_index=',image_index)
            
            image_to_display=image_list[image_index]
            pixmap = QPixmap(str(Path(images_path)/(image_to_display)))
            self.imageView.setPixmap(pixmap)
            self.imgIndex.setText(str(image_index))
        load_images()
    
        self.processOutput.appendPlainText("Generation finished.")
        self.generator_process = None
        if self.seedCheck.isChecked():
            self.seedVal.setText(str(random.randint(0,1632714927)))
        # self.cancelButton.setEnabled(False)
        self.generateButton.setEnabled(True)
        self.upscaleButton.setEnabled(True)


    def stop_process(self):
        if self.generator_process != None:
            self.generator_process.terminate()
            self.generator_process.terminate()
            self.processOutput.appendPlainText("Procesing has been ended.")
            # self.cancelButton.setEnabled(False)
            self.generateButton.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
window = sd_dreamer_main()
window.show()
app.exec_()

### to do
# inpaint fix clear
# fint inpainter save, only saves mask?
# add GFPGAN
# add txt2imgHD, upsample
# expand img2img
# image viewer, redo output
# prompt tags
# moar stuff
# keep in memory
# clean up code
# moar comments
# img2img view direct, upscale/upsample direct
# vram, ram
# appicon fix