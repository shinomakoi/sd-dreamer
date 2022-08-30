# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_frame.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_sd_dreamer_main(object):
    def setupUi(self, sd_dreamer_main):
        if not sd_dreamer_main.objectName():
            sd_dreamer_main.setObjectName(u"sd_dreamer_main")
        sd_dreamer_main.setWindowModality(Qt.NonModal)
        sd_dreamer_main.resize(1479, 1027)
        sd_dreamer_main.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        sd_dreamer_main.setWindowIcon(icon)
        self.gridLayout = QGridLayout(sd_dreamer_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.processOutput = QPlainTextEdit(sd_dreamer_main)
        self.processOutput.setObjectName(u"processOutput")
        self.processOutput.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processOutput.sizePolicy().hasHeightForWidth())
        self.processOutput.setSizePolicy(sizePolicy)
        self.processOutput.setMaximumSize(QSize(16777215, 100))
        self.processOutput.setAutoFillBackground(True)
        self.processOutput.setFrameShape(QFrame.StyledPanel)
        self.processOutput.setUndoRedoEnabled(False)
        self.processOutput.setReadOnly(True)
        self.processOutput.setOverwriteMode(False)
        self.processOutput.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.processOutput, 8, 0, 1, 2)

        self.errorMessages = QLabel(sd_dreamer_main)
        self.errorMessages.setObjectName(u"errorMessages")

        self.gridLayout.addWidget(self.errorMessages, 9, 0, 1, 1)

        self.tabby = QTabWidget(sd_dreamer_main)
        self.tabby.setObjectName(u"tabby")
        self.tabby.setAutoFillBackground(True)
        self.tabby.setUsesScrollButtons(True)
        self.tabby.setDocumentMode(False)
        self.tabby.setTabsClosable(False)
        self.tabby.setMovable(False)
        self.tabby.setTabBarAutoHide(False)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setAutoFillBackground(True)
        self.gridLayout_15 = QGridLayout(self.tab_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.scrollArea_2 = QScrollArea(self.tab_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 686, 796))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scale_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.scale_4.setObjectName(u"scale_4")

        self.gridLayout_2.addWidget(self.scale_4, 7, 0, 1, 1)

        self.stepsVal = QSlider(self.scrollAreaWidgetContents_3)
        self.stepsVal.setObjectName(u"stepsVal")
        self.stepsVal.setMinimum(1)
        self.stepsVal.setMaximum(300)
        self.stepsVal.setValue(50)
        self.stepsVal.setOrientation(Qt.Horizontal)
        self.stepsVal.setTickInterval(20)

        self.gridLayout_2.addWidget(self.stepsVal, 4, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 2, 1, 2)

        self.scale_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.scale_3.setObjectName(u"scale_3")

        self.gridLayout_2.addWidget(self.scale_3, 6, 0, 1, 1)

        self.batchVal = QSlider(self.scrollAreaWidgetContents_3)
        self.batchVal.setObjectName(u"batchVal")
        self.batchVal.setMinimum(1)
        self.batchVal.setMaximum(30)
        self.batchVal.setOrientation(Qt.Horizontal)
        self.batchVal.setTickPosition(QSlider.NoTicks)
        self.batchVal.setTickInterval(10)

        self.gridLayout_2.addWidget(self.batchVal, 7, 1, 1, 1)

        self.scaleVal = QSlider(self.scrollAreaWidgetContents_3)
        self.scaleVal.setObjectName(u"scaleVal")
        self.scaleVal.setMinimum(-20)
        self.scaleVal.setMaximum(40)
        self.scaleVal.setSingleStep(1)
        self.scaleVal.setValue(8)
        self.scaleVal.setSliderPosition(8)
        self.scaleVal.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.scaleVal, 5, 1, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 5, 2, 1, 2)

        self.heightThing = QComboBox(self.scrollAreaWidgetContents_3)
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.setObjectName(u"heightThing")
        self.heightThing.setInsertPolicy(QComboBox.InsertAtTop)

        self.gridLayout_2.addWidget(self.heightThing, 3, 1, 1, 1)

        self.precisionToggle = QComboBox(self.scrollAreaWidgetContents_3)
        self.precisionToggle.addItem("")
        self.precisionToggle.addItem("")
        self.precisionToggle.setObjectName(u"precisionToggle")

        self.gridLayout_2.addWidget(self.precisionToggle, 9, 1, 1, 2)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 9, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 2, 1, 2)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 8, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.scale_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.scale_2.setObjectName(u"scale_2")

        self.gridLayout_2.addWidget(self.scale_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 7, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.seedVal = QLineEdit(self.scrollAreaWidgetContents_3)
        self.seedVal.setObjectName(u"seedVal")

        self.gridLayout_2.addWidget(self.seedVal, 1, 1, 1, 1)

        self.scale = QLabel(self.scrollAreaWidgetContents_3)
        self.scale.setObjectName(u"scale")

        self.gridLayout_2.addWidget(self.scale, 5, 0, 1, 1)

        self.Steps = QLabel(self.scrollAreaWidgetContents_3)
        self.Steps.setObjectName(u"Steps")

        self.gridLayout_2.addWidget(self.Steps, 4, 0, 1, 1)

        self.promptVal = QComboBox(self.scrollAreaWidgetContents_3)
        self.promptVal.setObjectName(u"promptVal")
        self.promptVal.setAutoFillBackground(True)
        self.promptVal.setEditable(True)
        self.promptVal.setMaxVisibleItems(35)
        self.promptVal.setMaxCount(100)
        self.promptVal.setInsertPolicy(QComboBox.InsertAtBottom)
        self.promptVal.setFrame(True)

        self.gridLayout_2.addWidget(self.promptVal, 0, 1, 1, 3)

        self.samplerToggle = QComboBox(self.scrollAreaWidgetContents_3)
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.setObjectName(u"samplerToggle")

        self.gridLayout_2.addWidget(self.samplerToggle, 8, 1, 1, 2)

        self.widthThing = QComboBox(self.scrollAreaWidgetContents_3)
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.setObjectName(u"widthThing")

        self.gridLayout_2.addWidget(self.widthThing, 2, 1, 1, 1)

        self.itsVal = QSlider(self.scrollAreaWidgetContents_3)
        self.itsVal.setObjectName(u"itsVal")
        self.itsVal.setMinimum(1)
        self.itsVal.setMaximum(100)
        self.itsVal.setValue(4)
        self.itsVal.setSliderPosition(4)
        self.itsVal.setOrientation(Qt.Horizontal)
        self.itsVal.setTickPosition(QSlider.NoTicks)
        self.itsVal.setTickInterval(10)

        self.gridLayout_2.addWidget(self.itsVal, 6, 1, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.gridLayout_14 = QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.img2imgCheck = QCheckBox(self.groupBox)
        self.img2imgCheck.setObjectName(u"img2imgCheck")

        self.gridLayout_14.addWidget(self.img2imgCheck, 0, 0, 1, 1)

        self.img2imgFile = QLineEdit(self.groupBox)
        self.img2imgFile.setObjectName(u"img2imgFile")
        self.img2imgFile.setAutoFillBackground(False)
        self.img2imgFile.setFrame(True)
        self.img2imgFile.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.img2imgFile, 0, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_14.addWidget(self.label_26, 1, 2, 1, 1)

        self.artButton = QPushButton(self.groupBox)
        self.artButton.setObjectName(u"artButton")
        self.artButton.setEnabled(True)

        self.gridLayout_14.addWidget(self.artButton, 2, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_14.addWidget(self.label_27, 1, 0, 1, 1)

        self.img2imgStrength = QLineEdit(self.groupBox)
        self.img2imgStrength.setObjectName(u"img2imgStrength")

        self.gridLayout_14.addWidget(self.img2imgStrength, 1, 1, 1, 1)

        self.imgFileSelect = QPushButton(self.groupBox)
        self.imgFileSelect.setObjectName(u"imgFileSelect")

        self.gridLayout_14.addWidget(self.imgFileSelect, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 10, 1, 1, 2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.fixedCodeCheck = QCheckBox(self.groupBox_3)
        self.fixedCodeCheck.setObjectName(u"fixedCodeCheck")

        self.gridLayout_13.addWidget(self.fixedCodeCheck, 5, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 8, 0, 1, 1)

        self.outputFolderLine = QLineEdit(self.groupBox_3)
        self.outputFolderLine.setObjectName(u"outputFolderLine")

        self.gridLayout_13.addWidget(self.outputFolderLine, 8, 1, 1, 1)

        self.outputFolderSelect = QPushButton(self.groupBox_3)
        self.outputFolderSelect.setObjectName(u"outputFolderSelect")

        self.gridLayout_13.addWidget(self.outputFolderSelect, 8, 2, 1, 1)

        self.optimizedCheck = QCheckBox(self.groupBox_3)
        self.optimizedCheck.setObjectName(u"optimizedCheck")

        self.gridLayout_13.addWidget(self.optimizedCheck, 6, 1, 1, 1)

        self.seedCheck = QCheckBox(self.groupBox_3)
        self.seedCheck.setObjectName(u"seedCheck")
        self.seedCheck.setChecked(True)

        self.gridLayout_13.addWidget(self.seedCheck, 1, 1, 1, 1)

        self.small_batchCheck = QCheckBox(self.groupBox_3)
        self.small_batchCheck.setObjectName(u"small_batchCheck")
        self.small_batchCheck.setEnabled(False)

        self.gridLayout_13.addWidget(self.small_batchCheck, 4, 1, 1, 1)

        self.gridCheck = QCheckBox(self.groupBox_3)
        self.gridCheck.setObjectName(u"gridCheck")
        self.gridCheck.setEnabled(True)
        self.gridCheck.setChecked(False)

        self.gridLayout_13.addWidget(self.gridCheck, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 11, 1, 1, 2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_15.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabby.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inpaint_img_select = QPushButton(self.tab_4)
        self.inpaint_img_select.setObjectName(u"inpaint_img_select")

        self.gridLayout_4.addWidget(self.inpaint_img_select, 0, 2, 1, 1)

        self.inpaint_img = QLineEdit(self.tab_4)
        self.inpaint_img.setObjectName(u"inpaint_img")
        self.inpaint_img.setReadOnly(False)

        self.gridLayout_4.addWidget(self.inpaint_img, 0, 1, 1, 1)

        self.inpaintButton = QPushButton(self.tab_4)
        self.inpaintButton.setObjectName(u"inpaintButton")

        self.gridLayout_4.addWidget(self.inpaintButton, 2, 1, 1, 1)

        self.label_19 = QLabel(self.tab_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.inpaintSteps = QLineEdit(self.tab_4)
        self.inpaintSteps.setObjectName(u"inpaintSteps")

        self.gridLayout_4.addWidget(self.inpaintSteps, 1, 1, 1, 1)

        self.label_17 = QLabel(self.tab_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.tabby.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setAutoFillBackground(True)
        self.gridLayout_10 = QGridLayout(self.tab_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_32 = QLabel(self.tab_5)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_10.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_10.addWidget(self.label_29, 5, 0, 1, 1)

        self.rnvModelSelect = QComboBox(self.tab_5)
        self.rnvModelSelect.setObjectName(u"rnvModelSelect")

        self.gridLayout_10.addWidget(self.rnvModelSelect, 2, 2, 1, 1)

        self.upImageInputFolderSelect = QPushButton(self.tab_5)
        self.upImageInputFolderSelect.setObjectName(u"upImageInputFolderSelect")

        self.gridLayout_10.addWidget(self.upImageInputFolderSelect, 5, 4, 1, 1)

        self.modelScale = QComboBox(self.tab_5)
        self.modelScale.addItem("")
        self.modelScale.addItem("")
        self.modelScale.addItem("")
        self.modelScale.addItem("")
        self.modelScale.setObjectName(u"modelScale")

        self.gridLayout_10.addWidget(self.modelScale, 2, 4, 1, 1)

        self.upImageOutputFolder = QLineEdit(self.tab_5)
        self.upImageOutputFolder.setObjectName(u"upImageOutputFolder")
        self.upImageOutputFolder.setReadOnly(True)

        self.gridLayout_10.addWidget(self.upImageOutputFolder, 6, 2, 1, 1)

        self.upImageOutputFolderSelect = QPushButton(self.tab_5)
        self.upImageOutputFolderSelect.setObjectName(u"upImageOutputFolderSelect")

        self.gridLayout_10.addWidget(self.upImageOutputFolderSelect, 6, 4, 1, 1)

        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_10.addWidget(self.label_30, 6, 0, 1, 1)

        self.upscaleButton = QPushButton(self.tab_5)
        self.upscaleButton.setObjectName(u"upscaleButton")

        self.gridLayout_10.addWidget(self.upscaleButton, 7, 2, 1, 1)

        self.upImageInputFolder = QLineEdit(self.tab_5)
        self.upImageInputFolder.setObjectName(u"upImageInputFolder")
        self.upImageInputFolder.setReadOnly(True)

        self.gridLayout_10.addWidget(self.upImageInputFolder, 5, 2, 1, 1)

        self.label_16 = QLabel(self.tab_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_10.addWidget(self.label_16, 2, 3, 1, 1)

        self.tabby.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.tab_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.tab_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)

        self.rnvBinPath = QLineEdit(self.groupBox_2)
        self.rnvBinPath.setObjectName(u"rnvBinPath")
        self.rnvBinPath.setReadOnly(True)

        self.gridLayout_6.addWidget(self.rnvBinPath, 1, 2, 1, 1)

        self.pyBinPath = QLineEdit(self.groupBox_2)
        self.pyBinPath.setObjectName(u"pyBinPath")
        self.pyBinPath.setReadOnly(False)

        self.gridLayout_6.addWidget(self.pyBinPath, 0, 2, 1, 1)

        self.pyBinSelect = QPushButton(self.groupBox_2)
        self.pyBinSelect.setObjectName(u"pyBinSelect")

        self.gridLayout_6.addWidget(self.pyBinSelect, 0, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)

        self.rnvModelPath = QLineEdit(self.groupBox_2)
        self.rnvModelPath.setObjectName(u"rnvModelPath")
        self.rnvModelPath.setReadOnly(True)

        self.gridLayout_6.addWidget(self.rnvModelPath, 2, 2, 1, 1)

        self.rnvBinPathSelect = QPushButton(self.groupBox_2)
        self.rnvBinPathSelect.setObjectName(u"rnvBinPathSelect")

        self.gridLayout_6.addWidget(self.rnvBinPathSelect, 1, 3, 1, 1)

        self.rnvModelPathSelect = QPushButton(self.groupBox_2)
        self.rnvModelPathSelect.setObjectName(u"rnvModelPathSelect")

        self.gridLayout_6.addWidget(self.rnvModelPathSelect, 2, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 4)

        self.tabby.addTab(self.tab_6, "")

        self.gridLayout.addWidget(self.tabby, 0, 0, 4, 1)

        self.previousImgButton = QPushButton(sd_dreamer_main)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 4, 1, 1, 1)

        self.generateButton = QPushButton(sd_dreamer_main)
        self.generateButton.setObjectName(u"generateButton")

        self.gridLayout.addWidget(self.generateButton, 6, 0, 1, 2)

        self.cancelButton = QPushButton(sd_dreamer_main)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)

        self.gridLayout.addWidget(self.cancelButton, 4, 0, 1, 1)

        self.nextImageButton = QPushButton(sd_dreamer_main)
        self.nextImageButton.setObjectName(u"nextImageButton")

        self.gridLayout.addWidget(self.nextImageButton, 3, 1, 1, 1)

        self.scrollArea = QScrollArea(sd_dreamer_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 726, 717))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageView = QLabel(self.scrollAreaWidgetContents)
        self.imageView.setObjectName(u"imageView")
        self.imageView.setPixmap(QPixmap(u"view_default.png"))
        self.imageView.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imageView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.imgIndex = QLabel(sd_dreamer_main)
        self.imgIndex.setObjectName(u"imgIndex")
        self.imgIndex.setEnabled(True)
        self.imgIndex.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.imgIndex, 2, 1, 1, 1)


        self.retranslateUi(sd_dreamer_main)
        self.stepsVal.valueChanged.connect(self.label_6.setNum)
        self.scaleVal.valueChanged.connect(self.label_25.setNum)
        self.itsVal.valueChanged.connect(self.label_8.setNum)
        self.batchVal.valueChanged.connect(self.label_22.setNum)

        self.tabby.setCurrentIndex(0)
        self.heightThing.setCurrentIndex(4)
        self.promptVal.setCurrentIndex(-1)
        self.widthThing.setCurrentIndex(4)
        self.modelScale.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(sd_dreamer_main)
    # setupUi

    def retranslateUi(self, sd_dreamer_main):
        sd_dreamer_main.setWindowTitle(QCoreApplication.translate("sd_dreamer_main", u"SD Dreamer", None))
#if QT_CONFIG(tooltip)
        self.processOutput.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Stable diffusion output", None))
#endif // QT_CONFIG(tooltip)
        self.errorMessages.setText(QCoreApplication.translate("sd_dreamer_main", u"Ready", None))
        self.scale_4.setText(QCoreApplication.translate("sd_dreamer_main", u"Batch size", None))
#if QT_CONFIG(tooltip)
        self.stepsVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of steps. Max recommended 150", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("sd_dreamer_main", u"50", None))
        self.scale_3.setText(QCoreApplication.translate("sd_dreamer_main", u"Iterations", None))
#if QT_CONFIG(tooltip)
        self.batchVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of batches", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.scaleVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Classifier free guidance scale. Tries to match prompt more, may cause artifacts at high/low numbers", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("sd_dreamer_main", u"8", None))
        self.heightThing.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"256", None))
        self.heightThing.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"320", None))
        self.heightThing.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"384", None))
        self.heightThing.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"448", None))
        self.heightThing.setItemText(4, QCoreApplication.translate("sd_dreamer_main", u"512", None))
        self.heightThing.setItemText(5, QCoreApplication.translate("sd_dreamer_main", u"576", None))
        self.heightThing.setItemText(6, QCoreApplication.translate("sd_dreamer_main", u"640", None))
        self.heightThing.setItemText(7, QCoreApplication.translate("sd_dreamer_main", u"704", None))
        self.heightThing.setItemText(8, QCoreApplication.translate("sd_dreamer_main", u"768", None))
        self.heightThing.setItemText(9, QCoreApplication.translate("sd_dreamer_main", u"832", None))
        self.heightThing.setItemText(10, QCoreApplication.translate("sd_dreamer_main", u"896", None))
        self.heightThing.setItemText(11, QCoreApplication.translate("sd_dreamer_main", u"960", None))
        self.heightThing.setItemText(12, QCoreApplication.translate("sd_dreamer_main", u"1024", None))

#if QT_CONFIG(tooltip)
        self.heightThing.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Height of output image", None))
#endif // QT_CONFIG(tooltip)
        self.heightThing.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"512", None))
        self.precisionToggle.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"autocast", None))
        self.precisionToggle.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"full", None))

#if QT_CONFIG(tooltip)
        self.precisionToggle.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Precision", None))
#endif // QT_CONFIG(tooltip)
        self.precisionToggle.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"autocast", None))
        self.label_21.setText(QCoreApplication.translate("sd_dreamer_main", u"Precision", None))
        self.label_8.setText(QCoreApplication.translate("sd_dreamer_main", u"4", None))
        self.label_20.setText(QCoreApplication.translate("sd_dreamer_main", u"Sampler", None))
        self.label_2.setText(QCoreApplication.translate("sd_dreamer_main", u"Height", None))
        self.scale_2.setText(QCoreApplication.translate("sd_dreamer_main", u"Seed", None))
        self.label_4.setText(QCoreApplication.translate("sd_dreamer_main", u"Prompt", None))
        self.label_22.setText(QCoreApplication.translate("sd_dreamer_main", u"1", None))
        self.label.setText(QCoreApplication.translate("sd_dreamer_main", u"Width", None))
#if QT_CONFIG(tooltip)
        self.seedVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"The random noise seed to initialise. Same prompt, settings and seed = same image", None))
#endif // QT_CONFIG(tooltip)
        self.seedVal.setText(QCoreApplication.translate("sd_dreamer_main", u"42", None))
        self.scale.setText(QCoreApplication.translate("sd_dreamer_main", u"CFG scale", None))
        self.Steps.setText(QCoreApplication.translate("sd_dreamer_main", u"Steps", None))
#if QT_CONFIG(tooltip)
        self.promptVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"The prompt to generate images with. No quotations", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.promptVal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.samplerToggle.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"ddim", None))
        self.samplerToggle.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"plms", None))
        self.samplerToggle.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"k_lms", None))
        self.samplerToggle.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"k_euler_a", None))
        self.samplerToggle.setItemText(4, QCoreApplication.translate("sd_dreamer_main", u"k_dpm_2_a", None))

#if QT_CONFIG(tooltip)
        self.samplerToggle.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Sampler", None))
#endif // QT_CONFIG(tooltip)
        self.widthThing.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"256", None))
        self.widthThing.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"320", None))
        self.widthThing.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"384", None))
        self.widthThing.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"448", None))
        self.widthThing.setItemText(4, QCoreApplication.translate("sd_dreamer_main", u"512", None))
        self.widthThing.setItemText(5, QCoreApplication.translate("sd_dreamer_main", u"576", None))
        self.widthThing.setItemText(6, QCoreApplication.translate("sd_dreamer_main", u"640", None))
        self.widthThing.setItemText(7, QCoreApplication.translate("sd_dreamer_main", u"704", None))
        self.widthThing.setItemText(8, QCoreApplication.translate("sd_dreamer_main", u"768", None))
        self.widthThing.setItemText(9, QCoreApplication.translate("sd_dreamer_main", u"832", None))
        self.widthThing.setItemText(10, QCoreApplication.translate("sd_dreamer_main", u"896", None))
        self.widthThing.setItemText(11, QCoreApplication.translate("sd_dreamer_main", u"960", None))
        self.widthThing.setItemText(12, QCoreApplication.translate("sd_dreamer_main", u"1024", None))

#if QT_CONFIG(tooltip)
        self.widthThing.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Width of output image", None))
#endif // QT_CONFIG(tooltip)
        self.widthThing.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"512", None))
#if QT_CONFIG(tooltip)
        self.itsVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of images in a batch", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("sd_dreamer_main", u"Img2img", None))
#if QT_CONFIG(tooltip)
        self.img2imgCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Uses image instead of seed to initialise", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.img2imgCheck.setStatusTip(QCoreApplication.translate("sd_dreamer_main", u"Transfer prompt to an image and vice versa", None))
#endif // QT_CONFIG(statustip)
        self.img2imgCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Enabled", None))
#if QT_CONFIG(tooltip)
        self.img2imgFile.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Path of source image for img2img", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.img2imgFile.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.img2imgFile.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Input image for img2img", None))
        self.label_26.setText(QCoreApplication.translate("sd_dreamer_main", u"0.1 - 1.0", None))
#if QT_CONFIG(tooltip)
        self.artButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Paint a thing", None))
#endif // QT_CONFIG(tooltip)
        self.artButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Paint an image", None))
        self.label_27.setText(QCoreApplication.translate("sd_dreamer_main", u"Strength", None))
#if QT_CONFIG(tooltip)
        self.img2imgStrength.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of the blend - 0.1 - 1.0", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.img2imgStrength.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.img2imgStrength.setText(QCoreApplication.translate("sd_dreamer_main", u"0.8", None))
        self.imgFileSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("sd_dreamer_main", u"Options", None))
#if QT_CONFIG(tooltip)
        self.fixedCodeCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"If enabled, uses the same starting code across samples", None))
#endif // QT_CONFIG(tooltip)
        self.fixedCodeCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Fixed code", None))
        self.label_10.setText(QCoreApplication.translate("sd_dreamer_main", u"Output folder", None))
#if QT_CONFIG(tooltip)
        self.outputFolderLine.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Where images will get output to", None))
#endif // QT_CONFIG(tooltip)
        self.outputFolderLine.setText("")
        self.outputFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
#if QT_CONFIG(tooltip)
        self.optimizedCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Slower but less VRAM usage. Use more batches", None))
#endif // QT_CONFIG(tooltip)
        self.optimizedCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Optimized mode", None))
#if QT_CONFIG(tooltip)
        self.seedCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Enable random seeding", None))
#endif // QT_CONFIG(tooltip)
        self.seedCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Random seed", None))
#if QT_CONFIG(tooltip)
        self.small_batchCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"For 6 or less outputs. Only for 'optimized' scripts", None))
#endif // QT_CONFIG(tooltip)
        self.small_batchCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Turbo", None))
#if QT_CONFIG(tooltip)
        self.gridCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Don't produce a grid", None))
#endif // QT_CONFIG(tooltip)
        self.gridCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"No grid", None))
        self.tabby.setTabText(self.tabby.indexOf(self.tab_3), QCoreApplication.translate("sd_dreamer_main", u"Generate", None))
        self.inpaint_img_select.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
#if QT_CONFIG(tooltip)
        self.inpaint_img.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Image to inpaint", None))
#endif // QT_CONFIG(tooltip)
        self.inpaint_img.setText("")
        self.inpaintButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Inpaint", None))
        self.label_19.setText(QCoreApplication.translate("sd_dreamer_main", u"Image", None))
#if QT_CONFIG(tooltip)
        self.inpaintSteps.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Steps. More = slower", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintSteps.setText(QCoreApplication.translate("sd_dreamer_main", u"30", None))
        self.label_17.setText(QCoreApplication.translate("sd_dreamer_main", u"Steps", None))
        self.tabby.setTabText(self.tabby.indexOf(self.tab_4), QCoreApplication.translate("sd_dreamer_main", u"Inpainting", None))
        self.label_32.setText(QCoreApplication.translate("sd_dreamer_main", u"Model select", None))
        self.label_29.setText(QCoreApplication.translate("sd_dreamer_main", u"Image input folder", None))
#if QT_CONFIG(tooltip)
        self.rnvModelSelect.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select Real-ESGRAN NCNN model", None))
#endif // QT_CONFIG(tooltip)
        self.upImageInputFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.modelScale.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"1", None))
        self.modelScale.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"2", None))
        self.modelScale.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"4", None))
        self.modelScale.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"8", None))

        self.modelScale.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"4", None))
#if QT_CONFIG(tooltip)
        self.upImageOutputFolder.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Path to output upscaled images to", None))
#endif // QT_CONFIG(tooltip)
        self.upImageOutputFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_30.setText(QCoreApplication.translate("sd_dreamer_main", u"Image output folder", None))
        self.upscaleButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Upscale", None))
#if QT_CONFIG(tooltip)
        self.upImageInputFolder.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Path of images to upscale", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("sd_dreamer_main", u"Scale: x", None))
        self.tabby.setTabText(self.tabby.indexOf(self.tab_5), QCoreApplication.translate("sd_dreamer_main", u"Upscaling", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("sd_dreamer_main", u"Paths", None))
        self.label_18.setText(QCoreApplication.translate("sd_dreamer_main", u"Python binary bath (don't change)", None))
        self.label_14.setText(QCoreApplication.translate("sd_dreamer_main", u"realesrgan-ncnn-vulkan binary path", None))
#if QT_CONFIG(tooltip)
        self.rnvBinPath.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Path to the binary", None))
#endif // QT_CONFIG(tooltip)
        self.rnvBinPath.setText(QCoreApplication.translate("sd_dreamer_main", u"/usr/bin/realesrgan-ncnn-vulkan", None))
        self.rnvBinPath.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Path to the base directory of stable diffusion", None))
#if QT_CONFIG(tooltip)
        self.pyBinPath.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Python binary", None))
#endif // QT_CONFIG(tooltip)
        self.pyBinPath.setText(QCoreApplication.translate("sd_dreamer_main", u"python", None))
        self.pyBinSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_15.setText(QCoreApplication.translate("sd_dreamer_main", u"Folder containing realesrgan-ncnn-vulkan models", None))
#if QT_CONFIG(tooltip)
        self.rnvModelPath.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Folder containting the models (.bin)", None))
#endif // QT_CONFIG(tooltip)
        self.rnvModelPath.setText(QCoreApplication.translate("sd_dreamer_main", u"/usr/share/realesrgan-ncnn-vulkan/models", None))
        self.rnvBinPathSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.rnvModelPathSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.tabby.setTabText(self.tabby.indexOf(self.tab_6), QCoreApplication.translate("sd_dreamer_main", u"Settings", None))
        self.previousImgButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Previous", None))
        self.generateButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Dream", None))
        self.cancelButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Cancel", None))
        self.nextImageButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Next", None))
        self.imageView.setText("")
        self.imgIndex.setText(QCoreApplication.translate("sd_dreamer_main", u"0", None))
    # retranslateUi

