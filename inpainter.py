import os
from pathlib import Path

from PIL import Image
from PySide6.QtCore import *
from PySide6.QtCore import QUrl  # , QPropertyAnimation
from PySide6.QtGui import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QFileDialog

# constants
HOME_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SD_FOLDER_PATH = Path(HOME_DIR_PATH).parent
INPAINTING_DIR = Path(HOME_DIR_PATH)/'inpainting'


class inpainter_window(QMainWindow):

    def __init__(self, inpaint_source):
        super().__init__()
        self.inpainter_process = None
        SD_FOLDER_PATH = Path(HOME_DIR_PATH).parent
        self.inpaint_source = inpaint_source

        icon = QIcon()
        icon.addFile(str(Path(HOME_DIR_PATH)/"appicon.png"),
                     QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        print('Inpaint image: ', inpaint_source)

        im = Image.open(inpaint_source)
        inpaint_width, inpaint_height = im.size

        os.chdir(SD_FOLDER_PATH)

        self.setWindowTitle("SD Dreamer - Inpaint")

        self.setMaximumHeight(inpaint_height)
        self.setMaximumWidth(inpaint_width)
        self.setMinimumHeight(inpaint_height)
        self.setMinimumWidth(inpaint_width)

        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)

        # making image color to black
        self.image.fill(Qt.white)

        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 32
        # default color
        self.brushColor = Qt.black

        # QPoint object to track the point
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()

        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")

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
        clearAction.triggered.connect(lambda: self.clear(inpaint_source))

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

        pix_72= QAction("72px", self)
        b_size.addAction(pix_72)
        pix_72.triggered.connect(self.Pixel_72)
    
        pix_96 = QAction("96px", self)
        b_size.addAction(pix_96)
        pix_96.triggered.connect(self.Pixel_96)

        # similarly repeating above steps for different color
        white = QAction("White", self)
        white.triggered.connect(self.whiteColor)

        self.load_img(inpaint_source)

    def load_img(self, inpaint_source):

        im_rgb = Image.open(inpaint_source)
        im_rgb.save(Path(str(INPAINTING_DIR))/'masking'/'image.png')

        im_rgba = im_rgb.copy()
        im_rgba.putalpha(215)
        im_rgba.save(Path(str(INPAINTING_DIR))/'inpaint_view.png')

        label = QLabel(self)
        pixy = Path(INPAINTING_DIR)/'inpaint_view.png'
        pixmap = QPixmap(str(pixy))
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

    # method for checking mouse cicks
    def mousePressEvent(self, event):

        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.scenePosition()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):

        if (event.buttons() and Qt.LeftButton) and self.drawing:

            # creating painter object
            painter = QPainter(self.image)

            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.lastPoint, event.scenePosition())

            # change the last point
            self.lastPoint = event.scenePosition()
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
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def inpy(self):
        img_mask_s = (str(Path(INPAINTING_DIR)/'masking'/'image_mask.png'))
        self.image.save(img_mask_s)
        self.setWindowTitle("Saved. Press 'Dream (inpaint)' to inpaint")

    def clear(self, inpaint_source):
        # make the whole canvas white
        self.image.fill(Qt.white)
        self.load_img(inpaint_source)
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

    def Pixel_72(self):
        self.brushSize = 72

    def Pixel_96(self):
        self.brushSize = 96

    def whiteColor(self):
        self.brushColor = QColor(255, 255, 255, 100)

    def blackColor(self):
        self.brushColor = QColor(0, 0, 0, 100)
