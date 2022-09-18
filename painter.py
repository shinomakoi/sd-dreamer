import os
import random
from pathlib import Path
from random import choice

import png
from PySide2.QtCore import *
from PySide2.QtCore import QUrl  # , QPropertyAnimation
from PySide2.QtCore import QProcess
from PySide2.QtGui import *
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QFileDialog

SPRAY_PARTICLES = 40
SPRAY_DIAMETER = 9

class paintWindow(QMainWindow,):
    def __init__(self, sd_folder_path, art_source, paint_w, paint_h):
        super().__init__()

        print('Art image: ', art_source)
        self.setWindowTitle("SD Art studio")

        if art_source != False:
            r = png.Reader(art_source)
            png_w = (r.read()[0])
            png_h = (r.read()[1])
            os.chdir(sd_folder_path)

            print(png_w, png_h)

            # setting geometry to main window
            self.setMaximumHeight(png_h)
            self.setMaximumWidth(png_w)
            self.setMinimumHeight(png_h)
            self.setMinimumWidth(png_w)

            self.image = QImage(art_source)
        else:
            print(paint_w, paint_h)

            self.setWindowTitle("SD Art studio")

            self.setGeometry(100, 100, paint_w, paint_h)
            self.setMaximumHeight(paint_h)
            self.setMaximumWidth(paint_w)
            self.setMinimumHeight(paint_h)
            self.setMinimumWidth(paint_w)

            self.image = QImage(self.size(), QImage.Format_RGB32)

            self.image.fill(Qt.white)

        self.drawing = False
        # default brush size
        self.brushSize = 24
        # default color
        self.brushColor = QColor(0, 0, 0, 20)

        # QPoint object to tract the point
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()

        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")

        # adding brush size to main menu
        b_size = mainMenu.addMenu("Brush Size")

        # adding brush color to ain menu
        b_color = mainMenu.addMenu("Brush Color")

        noise_toggle = mainMenu.addMenu("Noise/color")

        # creating save action
        saveAction = QAction("Save", self)
        # adding short cut for save action
        saveAction.setShortcut("Ctrl + S")
        # adding save to the file menu
        fileMenu.addAction(saveAction)
        # adding action to the save
        saveAction.triggered.connect(self.save)

        # creating clear action
        clearAction = QAction("Clear", self)
        # adding short cut to the clear action
        clearAction.setShortcut("Ctrl + Z")
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(lambda: self.clear(art_source))

        noiseOnAction = QAction("Noise mode", self)
        noise_toggle.addAction(noiseOnAction)
        noiseOnAction.triggered.connect(lambda: self.noiseOn())

        noiseOffAction = QAction("Paint brush mode", self)
        noise_toggle.addAction(noiseOffAction)
        noiseOffAction.triggered.connect(lambda: self.noiseOff())

        # creating options for brush sizes
        pix_6 = QAction("6px", self)
        b_size.addAction(pix_6)
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

        # creating options for brush color
        # creating action for black color
        black = QAction("Black", self)
        # adding this action to the brush colors
        b_color.addAction(black)
        # adding methods to the black
        black.triggered.connect(self.blackColor)

        # similarly repeating above steps for different color
        white = QAction("White", self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)

        green = QAction("Green", self)
        b_color.addAction(green)
        green.triggered.connect(self.greenColor)

        yellow = QAction("Yellow", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)

        red = QAction("Red", self)
        b_color.addAction(red)
        red.triggered.connect(self.redColor)

        brown = QAction("Brown", self)
        b_color.addAction(brown)
        brown.triggered.connect(self.brownColor)

        blue = QAction("Blue", self)
        b_color.addAction(blue)
        blue.triggered.connect(self.blueColor)

        cyan = QAction("Cyan", self)
        b_color.addAction(cyan)
        cyan.triggered.connect(self.cyanColor)

        gray = QAction("Gray", self)
        b_color.addAction(gray)
        gray.triggered.connect(self.grayColor)

        magenta = QAction("Magenta", self)
        b_color.addAction(magenta)
        magenta.triggered.connect(self.magentaColor)

        darkblue = QAction("Dark blue", self)
        b_color.addAction(darkblue)
        darkblue.triggered.connect(self.darkblueColor)

        darkgreen = QAction("Dark green", self)
        b_color.addAction(darkgreen)
        darkgreen.triggered.connect(self.darkgreenColor)

        darkred = QAction("Dark red", self)
        b_color.addAction(darkred)
        darkred.triggered.connect(self.darkredColor)

        darkgray = QAction("Dark gray", self)
        b_color.addAction(darkgray)
        darkgray.triggered.connect(self.darkgrayColor)

        lightskin = QAction("Light skin", self)
        b_color.addAction(lightskin)
        lightskin.triggered.connect(self.lightskinColor)

    def mousePressEvent(self, event):

        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            # make drawing flag true
            self.drawing = True
            # make last point to the point of cursor
            self.lastPoint = event.pos()

    # method for tracking mouse activity

    global noise
    noise = False

    def mouseMoveEvent(self, event):

        # checking if left button is pressed and drawing flag is true
        if (event.buttons() & Qt.LeftButton) & self.drawing and noise == False:

            # creating painter object
            painter = QPainter(self.image)

            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            pen2 = QPen()
            pen2.setWidth(3)

            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()
        else:
            colors = [QColor(255, 0, 0, 10), QColor(
                0, 255, 0, 10), QColor(0, 0, 255, 10)]

            painter = QPainter(self.image)
            pen = QPen()
            pen.setWidth(2)
            painter.setPen(QPen(self.brushSize))
            for n in range(SPRAY_PARTICLES):
                pen.setColor((choice(colors)))
                xo = random.gauss(0, SPRAY_DIAMETER)
                yo = random.gauss(0, SPRAY_DIAMETER)
                painter.setPen(pen)
                painter.drawPoint(event.x() + xo, event.y() + yo)

                self.update()
            painter.end()

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

    # method for saving canvas
    def save(self):
        img_paint_s = (str(Path('outputs')/'sd_dreamer'/'art.png'))
        self.image.save(img_paint_s)
        print('saved to : ', img_paint_s)
        self.setWindowTitle("Saved - click 'Dream (img2img)' to generate")

    # method for clearing every thing on canvas

    def clear(self, art_source):
        # make the whole canvas white

        if art_source == False:
            self.image.fill(Qt.white)
        else:
            self.image = QImage(art_source)

        # update
        self.update()

    def noiseOn(self):
        global noise
        noise = True

    def noiseOff(self):
        global noise
        noise = False

        self.update()

    # methods for changing pixel sizes
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

    # methods for changing brush color

    def whiteColor(self):
        self.brushColor = QColor(255, 255, 255, 20)

    def blackColor(self):
        self.brushColor = QColor(0, 0, 0, 20)

    def greenColor(self):
        self.brushColor = QColor(85, 170, 0, 20)

    def yellowColor(self):
        self.brushColor = QColor(255, 255, 0, 20)

    def redColor(self):
        self.brushColor = QColor(255, 0, 0, 20)

    def brownColor(self):
        self.brushColor = QColor(85, 0, 0, 20)

    def blueColor(self):
        self.brushColor = QColor(0, 85, 255, 20)

    def cyanColor(self):
        self.brushColor = QColor(85, 255, 255, 20)

    def grayColor(self):
        self.brushColor = QColor(180, 180, 180, 20)

    def magentaColor(self):
        self.brushColor = QColor(211, 70, 211, 20)

    def darkblueColor(self):
        self.brushColor = QColor(0, 0, 127, 20)

    def darkgreenColor(self):
        self.brushColor = QColor(0, 85, 0, 20)

    def darkyellowColor(self):
        self.brushColor = QColor(118, 110, 0, 20)

    def darkredColor(self):
        self.brushColor = QColor(170, 0, 0, 20)

    def darkgrayColor(self):
        self.brushColor = QColor(52, 52, 52, 20)

    def lightskinColor(self):
        self.brushColor = QColor(249, 228, 221, 20)
