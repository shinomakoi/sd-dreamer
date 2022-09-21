# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_frame.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
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
        sd_dreamer_main.resize(1257, 1002)
        sd_dreamer_main.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        sd_dreamer_main.setWindowIcon(icon)
        sd_dreamer_main.setStyleSheet(u"")
        self.gridLayout = QGridLayout(sd_dreamer_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(sd_dreamer_main)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.gridLayout_12 = QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.operationOne = QRadioButton(self.groupBox_4)
        self.operationOne.setObjectName(u"operationOne")
        self.operationOne.setEnabled(True)
        self.operationOne.setChecked(True)

        self.gridLayout_12.addWidget(self.operationOne, 1, 5, 1, 1)

        self.operationFolderSelect = QToolButton(self.groupBox_4)
        self.operationFolderSelect.setObjectName(u"operationFolderSelect")

        self.gridLayout_12.addWidget(self.operationFolderSelect, 2, 3, 1, 1)

        self.imageLoadButton = QPushButton(self.groupBox_4)
        self.imageLoadButton.setObjectName(u"imageLoadButton")

        self.gridLayout_12.addWidget(self.imageLoadButton, 2, 4, 1, 1)

        self.operationalAll = QRadioButton(self.groupBox_4)
        self.operationalAll.setObjectName(u"operationalAll")
        self.operationalAll.setChecked(False)

        self.gridLayout_12.addWidget(self.operationalAll, 1, 4, 1, 1)

        self.operationBox = QComboBox(self.groupBox_4)
        self.operationBox.addItem("")
        self.operationBox.addItem("")
        self.operationBox.addItem("")
        self.operationBox.addItem("")
        self.operationBox.setObjectName(u"operationBox")

        self.gridLayout_12.addWidget(self.operationBox, 1, 1, 1, 2)

        self.operationFolder = QLineEdit(self.groupBox_4)
        self.operationFolder.setObjectName(u"operationFolder")

        self.gridLayout_12.addWidget(self.operationFolder, 2, 1, 1, 2)

        self.customFolderCheck = QCheckBox(self.groupBox_4)
        self.customFolderCheck.setObjectName(u"customFolderCheck")
        self.customFolderCheck.setEnabled(True)

        self.gridLayout_12.addWidget(self.customFolderCheck, 2, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_12.addWidget(self.label_9, 1, 0, 1, 1)

        self.operationsGoButton = QPushButton(self.groupBox_4)
        self.operationsGoButton.setObjectName(u"operationsGoButton")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.operationsGoButton.setFont(font)

        self.gridLayout_12.addWidget(self.operationsGoButton, 2, 5, 1, 1)

        self.imgFilename = QLineEdit(self.groupBox_4)
        self.imgFilename.setObjectName(u"imgFilename")
        self.imgFilename.setAcceptDrops(False)
        self.imgFilename.setAutoFillBackground(False)
        self.imgFilename.setFrame(False)
        self.imgFilename.setReadOnly(True)
        self.imgFilename.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.imgFilename, 0, 0, 1, 6)


        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 1, 4)

        self.processOutput = QPlainTextEdit(sd_dreamer_main)
        self.processOutput.setObjectName(u"processOutput")
        self.processOutput.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processOutput.sizePolicy().hasHeightForWidth())
        self.processOutput.setSizePolicy(sizePolicy)
        self.processOutput.setMaximumSize(QSize(16777215, 100))
        self.processOutput.setAcceptDrops(False)
        self.processOutput.setAutoFillBackground(False)
        self.processOutput.setFrameShape(QFrame.StyledPanel)
        self.processOutput.setUndoRedoEnabled(False)
        self.processOutput.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.processOutput.setReadOnly(True)
        self.processOutput.setOverwriteMode(False)
        self.processOutput.setBackgroundVisible(False)
        self.processOutput.setCenterOnScroll(False)

        self.gridLayout.addWidget(self.processOutput, 5, 0, 1, 5)

        self.errorMessages = QLabel(sd_dreamer_main)
        self.errorMessages.setObjectName(u"errorMessages")

        self.gridLayout.addWidget(self.errorMessages, 6, 0, 1, 1)

        self.previousImgButton = QPushButton(sd_dreamer_main)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 3, 1, 1, 1, Qt.AlignLeft)

        self.promptVal = QComboBox(sd_dreamer_main)
        self.promptVal.setObjectName(u"promptVal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.promptVal.sizePolicy().hasHeightForWidth())
        self.promptVal.setSizePolicy(sizePolicy1)
        self.promptVal.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.promptVal.setFont(font1)
        self.promptVal.setAutoFillBackground(True)
        self.promptVal.setEditable(True)
        self.promptVal.setMaxVisibleItems(35)
        self.promptVal.setMaxCount(100)
        self.promptVal.setInsertPolicy(QComboBox.InsertAtTop)
        self.promptVal.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        self.promptVal.setFrame(True)

        self.gridLayout.addWidget(self.promptVal, 0, 0, 1, 3)

        self.cancelButton = QPushButton(sd_dreamer_main)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)
        self.cancelButton.setMaximumSize(QSize(198, 16777215))

        self.gridLayout.addWidget(self.cancelButton, 0, 4, 1, 1)

        self.scrollArea = QScrollArea(sd_dreamer_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 714, 652))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageView = QLabel(self.scrollAreaWidgetContents)
        self.imageView.setObjectName(u"imageView")
        self.imageView.setMaximumSize(QSize(1440, 1440))
        palette = QPalette()
        brush = QBrush(QColor(21, 22, 23, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(251, 253, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush2 = QBrush(QColor(251, 253, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush3 = QBrush(QColor(251, 253, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush4 = QBrush(QColor(170, 171, 172, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush5 = QBrush(QColor(251, 253, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.imageView.setPalette(palette)
        self.imageView.setAcceptDrops(True)
        self.imageView.setAutoFillBackground(False)
        self.imageView.setStyleSheet(u"background-color: rgb(21, 22, 23);")
        self.imageView.setFrameShape(QFrame.NoFrame)
        self.imageView.setFrameShadow(QFrame.Plain)
        self.imageView.setPixmap(QPixmap(u"view_default.png"))
        self.imageView.setScaledContents(False)
        self.imageView.setAlignment(Qt.AlignCenter)
        self.imageView.setWordWrap(False)

        self.horizontalLayout.addWidget(self.imageView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 1, 2, 4)

        self.groupBox_3 = QGroupBox(sd_dreamer_main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gfpganStrength = QDoubleSpinBox(self.groupBox_3)
        self.gfpganStrength.setObjectName(u"gfpganStrength")
        self.gfpganStrength.setMinimum(0.100000000000000)
        self.gfpganStrength.setMaximum(0.990000000000000)
        self.gfpganStrength.setSingleStep(0.020000000000000)
        self.gfpganStrength.setValue(0.600000000000000)

        self.gridLayout_5.addWidget(self.gfpganStrength, 6, 3, 1, 1)

        self.precisionToggle = QCheckBox(self.groupBox_3)
        self.precisionToggle.setObjectName(u"precisionToggle")

        self.gridLayout_5.addWidget(self.precisionToggle, 9, 0, 1, 4)

        self.builtUpscaleScale = QComboBox(self.groupBox_3)
        self.builtUpscaleScale.addItem("")
        self.builtUpscaleScale.addItem("")
        self.builtUpscaleScale.setObjectName(u"builtUpscaleScale")

        self.gridLayout_5.addWidget(self.builtUpscaleScale, 3, 1, 1, 1)

        self.seamlessCheck = QCheckBox(self.groupBox_3)
        self.seamlessCheck.setObjectName(u"seamlessCheck")

        self.gridLayout_5.addWidget(self.seamlessCheck, 8, 0, 1, 2)

        self.builtUpscaleCheck = QCheckBox(self.groupBox_3)
        self.builtUpscaleCheck.setObjectName(u"builtUpscaleCheck")

        self.gridLayout_5.addWidget(self.builtUpscaleCheck, 3, 0, 1, 1)

        self.builtUpscaleStrength = QDoubleSpinBox(self.groupBox_3)
        self.builtUpscaleStrength.setObjectName(u"builtUpscaleStrength")
        self.builtUpscaleStrength.setMinimum(0.010000000000000)
        self.builtUpscaleStrength.setMaximum(0.990000000000000)
        self.builtUpscaleStrength.setSingleStep(0.020000000000000)
        self.builtUpscaleStrength.setValue(0.600000000000000)

        self.gridLayout_5.addWidget(self.builtUpscaleStrength, 3, 3, 1, 1)

        self.seedCheck = QCheckBox(self.groupBox_3)
        self.seedCheck.setObjectName(u"seedCheck")
        self.seedCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.seedCheck, 1, 0, 2, 2)

        self.gridCheck = QCheckBox(self.groupBox_3)
        self.gridCheck.setObjectName(u"gridCheck")

        self.gridLayout_5.addWidget(self.gridCheck, 5, 0, 1, 2)

        self.gfpganCheck = QCheckBox(self.groupBox_3)
        self.gfpganCheck.setObjectName(u"gfpganCheck")

        self.gridLayout_5.addWidget(self.gfpganCheck, 6, 0, 1, 2)

        self.embeddingCheck = QCheckBox(self.groupBox_3)
        self.embeddingCheck.setObjectName(u"embeddingCheck")

        self.gridLayout_5.addWidget(self.embeddingCheck, 10, 0, 1, 4)

        self.embeddingInputFile = QLineEdit(self.groupBox_3)
        self.embeddingInputFile.setObjectName(u"embeddingInputFile")

        self.gridLayout_5.addWidget(self.embeddingInputFile, 11, 0, 1, 4)

        self.variantAmountCheck = QCheckBox(self.groupBox_3)
        self.variantAmountCheck.setObjectName(u"variantAmountCheck")

        self.gridLayout_5.addWidget(self.variantAmountCheck, 4, 0, 1, 1)

        self.variantAmountValue = QDoubleSpinBox(self.groupBox_3)
        self.variantAmountValue.setObjectName(u"variantAmountValue")
        self.variantAmountValue.setMinimum(0.010000000000000)
        self.variantAmountValue.setMaximum(0.990000000000000)
        self.variantAmountValue.setSingleStep(0.020000000000000)
        self.variantAmountValue.setValue(0.500000000000000)

        self.gridLayout_5.addWidget(self.variantAmountValue, 4, 3, 1, 1)

        self.embeddingSelect = QToolButton(self.groupBox_3)
        self.embeddingSelect.setObjectName(u"embeddingSelect")

        self.gridLayout_5.addWidget(self.embeddingSelect, 11, 4, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 3, 1)

        self.generateButton = QPushButton(sd_dreamer_main)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(True)
        self.generateButton.setMaximumSize(QSize(265, 16777215))
        self.generateButton.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        self.generateButton.setFont(font2)
        self.generateButton.setStyleSheet(u"background-color: rgb(147, 217, 255);")
        self.generateButton.setIcon(icon)
        self.generateButton.setIconSize(QSize(24, 24))
        self.generateButton.setCheckable(False)
        self.generateButton.setAutoDefault(True)
        self.generateButton.setFlat(False)

        self.gridLayout.addWidget(self.generateButton, 0, 3, 1, 1)

        self.nextImageButton = QPushButton(sd_dreamer_main)
        self.nextImageButton.setObjectName(u"nextImageButton")

        self.gridLayout.addWidget(self.nextImageButton, 3, 4, 1, 1, Qt.AlignRight)

        self.mainTab = QTabWidget(sd_dreamer_main)
        self.mainTab.setObjectName(u"mainTab")
        self.mainTab.setMaximumSize(QSize(500, 16777215))
        self.mainTab.setAutoFillBackground(False)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scaleVal = QSlider(self.tab_3)
        self.scaleVal.setObjectName(u"scaleVal")
        self.scaleVal.setMinimum(-15)
        self.scaleVal.setMaximum(30)
        self.scaleVal.setSingleStep(1)
        self.scaleVal.setValue(8)
        self.scaleVal.setSliderPosition(8)
        self.scaleVal.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.scaleVal, 4, 2, 1, 1)

        self.scale_3 = QLabel(self.tab_3)
        self.scale_3.setObjectName(u"scale_3")

        self.gridLayout_2.addWidget(self.scale_3, 5, 0, 1, 1)

        self.widthThing = QComboBox(self.tab_3)
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
        self.widthThing.addItem("")
        self.widthThing.addItem("")
        self.widthThing.setObjectName(u"widthThing")
        self.widthThing.setEditable(True)

        self.gridLayout_2.addWidget(self.widthThing, 1, 2, 1, 1)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 4, 3, 1, 1)

        self.Steps = QLabel(self.tab_3)
        self.Steps.setObjectName(u"Steps")

        self.gridLayout_2.addWidget(self.Steps, 3, 0, 1, 1)

        self.heightThing = QComboBox(self.tab_3)
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
        self.heightThing.addItem("")
        self.heightThing.addItem("")
        self.heightThing.setObjectName(u"heightThing")
        self.heightThing.setEditable(True)
        self.heightThing.setInsertPolicy(QComboBox.InsertAtTop)

        self.gridLayout_2.addWidget(self.heightThing, 2, 2, 1, 1)

        self.scale_2 = QLabel(self.tab_3)
        self.scale_2.setObjectName(u"scale_2")

        self.gridLayout_2.addWidget(self.scale_2, 0, 0, 1, 1)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 6, 0, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.samplerToggle = QComboBox(self.tab_3)
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.addItem("")
        self.samplerToggle.setObjectName(u"samplerToggle")

        self.gridLayout_2.addWidget(self.samplerToggle, 6, 2, 1, 2)

        self.itsVal = QSlider(self.tab_3)
        self.itsVal.setObjectName(u"itsVal")
        self.itsVal.setMinimum(1)
        self.itsVal.setMaximum(60)
        self.itsVal.setValue(1)
        self.itsVal.setSliderPosition(1)
        self.itsVal.setOrientation(Qt.Horizontal)
        self.itsVal.setTickPosition(QSlider.NoTicks)
        self.itsVal.setTickInterval(10)

        self.gridLayout_2.addWidget(self.itsVal, 5, 2, 1, 1)

        self.seedVal = QLineEdit(self.tab_3)
        self.seedVal.setObjectName(u"seedVal")

        self.gridLayout_2.addWidget(self.seedVal, 0, 2, 1, 1)

        self.stepsVal = QSlider(self.tab_3)
        self.stepsVal.setObjectName(u"stepsVal")
        self.stepsVal.setMinimum(1)
        self.stepsVal.setMaximum(200)
        self.stepsVal.setValue(30)
        self.stepsVal.setSliderPosition(30)
        self.stepsVal.setOrientation(Qt.Horizontal)
        self.stepsVal.setTickInterval(20)

        self.gridLayout_2.addWidget(self.stepsVal, 3, 2, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 5, 3, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 3, 1, 1)

        self.scale = QLabel(self.tab_3)
        self.scale.setObjectName(u"scale")

        self.gridLayout_2.addWidget(self.scale, 4, 0, 1, 1)

        self.mainTab.addTab(self.tab_3, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setAutoFillBackground(True)
        self.gridLayout_14 = QGridLayout(self.tab_9)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_27 = QLabel(self.tab_9)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_14.addWidget(self.label_27, 2, 0, 1, 1)

        self.imgIndex = QLabel(self.tab_9)
        self.imgIndex.setObjectName(u"imgIndex")

        self.gridLayout_14.addWidget(self.imgIndex, 0, 3, 1, 1)

        self.imgFileSelect = QToolButton(self.tab_9)
        self.imgFileSelect.setObjectName(u"imgFileSelect")

        self.gridLayout_14.addWidget(self.imgFileSelect, 1, 3, 1, 1)

        self.img2imgStrength = QDoubleSpinBox(self.tab_9)
        self.img2imgStrength.setObjectName(u"img2imgStrength")
        self.img2imgStrength.setMaximum(0.990000000000000)
        self.img2imgStrength.setSingleStep(0.010000000000000)
        self.img2imgStrength.setValue(0.750000000000000)

        self.gridLayout_14.addWidget(self.img2imgStrength, 2, 1, 1, 2)

        self.artButton = QPushButton(self.tab_9)
        self.artButton.setObjectName(u"artButton")

        self.gridLayout_14.addWidget(self.artButton, 4, 0, 1, 4)

        self.img2imgFile = QLineEdit(self.tab_9)
        self.img2imgFile.setObjectName(u"img2imgFile")
        self.img2imgFile.setAutoFillBackground(False)
        self.img2imgFile.setFrame(True)
        self.img2imgFile.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.img2imgFile, 1, 0, 1, 3)

        self.img2imgDisplayed = QCheckBox(self.tab_9)
        self.img2imgDisplayed.setObjectName(u"img2imgDisplayed")

        self.gridLayout_14.addWidget(self.img2imgDisplayed, 0, 0, 1, 2)

        self.img2imgUpscaleCheck = QCheckBox(self.tab_9)
        self.img2imgUpscaleCheck.setObjectName(u"img2imgUpscaleCheck")

        self.gridLayout_14.addWidget(self.img2imgUpscaleCheck, 3, 0, 1, 1)

        self.mainTab.addTab(self.tab_9, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inpaintingDisplayedCheck = QCheckBox(self.tab_4)
        self.inpaintingDisplayedCheck.setObjectName(u"inpaintingDisplayedCheck")

        self.gridLayout_4.addWidget(self.inpaintingDisplayedCheck, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.invertMaskCheck = QCheckBox(self.tab_4)
        self.invertMaskCheck.setObjectName(u"invertMaskCheck")

        self.gridLayout_4.addWidget(self.invertMaskCheck, 2, 1, 1, 1)

        self.inpaintButton = QPushButton(self.tab_4)
        self.inpaintButton.setObjectName(u"inpaintButton")

        self.gridLayout_4.addWidget(self.inpaintButton, 6, 1, 1, 1)

        self.inpaint_img_select = QToolButton(self.tab_4)
        self.inpaint_img_select.setObjectName(u"inpaint_img_select")

        self.gridLayout_4.addWidget(self.inpaint_img_select, 4, 2, 1, 1)

        self.inpaint_img = QLineEdit(self.tab_4)
        self.inpaint_img.setObjectName(u"inpaint_img")
        self.inpaint_img.setReadOnly(False)

        self.gridLayout_4.addWidget(self.inpaint_img, 4, 1, 1, 1)

        self.maskBlurVaue = QSpinBox(self.tab_4)
        self.maskBlurVaue.setObjectName(u"maskBlurVaue")
        self.maskBlurVaue.setMinimum(1)
        self.maskBlurVaue.setMaximum(16)
        self.maskBlurVaue.setValue(4)

        self.gridLayout_4.addWidget(self.maskBlurVaue, 3, 1, 1, 1)

        self.mainTab.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setAutoFillBackground(True)
        self.gridLayout_10 = QGridLayout(self.tab_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_5 = QGroupBox(self.tab_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_13 = QGridLayout(self.groupBox_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.latentSRSteps = QSpinBox(self.groupBox_5)
        self.latentSRSteps.setObjectName(u"latentSRSteps")
        self.latentSRSteps.setMinimum(1)
        self.latentSRSteps.setMaximum(200)
        self.latentSRSteps.setValue(40)

        self.gridLayout_13.addWidget(self.latentSRSteps, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_13.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_13.addWidget(self.label_11, 0, 2, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.rnvModelSelect = QComboBox(self.groupBox)
        self.rnvModelSelect.setObjectName(u"rnvModelSelect")

        self.gridLayout_9.addWidget(self.rnvModelSelect, 0, 1, 1, 2)

        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_9.addWidget(self.label_32, 0, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_9.addWidget(self.label_16, 1, 0, 1, 1)

        self.modelScale = QComboBox(self.groupBox)
        self.modelScale.addItem("")
        self.modelScale.addItem("")
        self.modelScale.addItem("")
        self.modelScale.addItem("")
        self.modelScale.setObjectName(u"modelScale")

        self.gridLayout_9.addWidget(self.modelScale, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)

        self.mainTab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.tab_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.tab_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.custCheckpointLine = QLineEdit(self.groupBox_2)
        self.custCheckpointLine.setObjectName(u"custCheckpointLine")

        self.gridLayout_6.addWidget(self.custCheckpointLine, 1, 0, 1, 2)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 6, 0, 1, 2)

        self.custCheckpointSelect = QToolButton(self.groupBox_2)
        self.custCheckpointSelect.setObjectName(u"custCheckpointSelect")

        self.gridLayout_6.addWidget(self.custCheckpointSelect, 1, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 3, 0, 1, 1)

        self.outputFolderLine = QLineEdit(self.groupBox_2)
        self.outputFolderLine.setObjectName(u"outputFolderLine")

        self.gridLayout_6.addWidget(self.outputFolderLine, 4, 0, 1, 2)

        self.pyBinPath = QLineEdit(self.groupBox_2)
        self.pyBinPath.setObjectName(u"pyBinPath")
        self.pyBinPath.setReadOnly(False)

        self.gridLayout_6.addWidget(self.pyBinPath, 7, 0, 1, 2)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 5, 0, 1, 3)

        self.pyBinSelect = QToolButton(self.groupBox_2)
        self.pyBinSelect.setObjectName(u"pyBinSelect")

        self.gridLayout_6.addWidget(self.pyBinSelect, 7, 2, 1, 1)

        self.outputFolderSelect = QToolButton(self.groupBox_2)
        self.outputFolderSelect.setObjectName(u"outputFolderSelect")

        self.gridLayout_6.addWidget(self.outputFolderSelect, 4, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 4)

        self.mainTab.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_11 = QGridLayout(self.tab_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.tab_8)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.mainTab.addTab(self.tab_8, "")

        self.gridLayout.addWidget(self.mainTab, 1, 0, 1, 1)


        self.retranslateUi(sd_dreamer_main)
        self.stepsVal.valueChanged.connect(self.label_6.setNum)
        self.scaleVal.valueChanged.connect(self.label_25.setNum)
        self.itsVal.valueChanged.connect(self.label_8.setNum)

        self.operationBox.setCurrentIndex(0)
        self.promptVal.setCurrentIndex(-1)
        self.generateButton.setDefault(False)
        self.mainTab.setCurrentIndex(0)
        self.widthThing.setCurrentIndex(4)
        self.heightThing.setCurrentIndex(4)
        self.samplerToggle.setCurrentIndex(3)
        self.modelScale.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(sd_dreamer_main)
    # setupUi

    def retranslateUi(self, sd_dreamer_main):
        sd_dreamer_main.setWindowTitle(QCoreApplication.translate("sd_dreamer_main", u"SD Dreamer", None))
        self.groupBox_4.setTitle("")
        self.operationOne.setText(QCoreApplication.translate("sd_dreamer_main", u"Selected image", None))
        self.operationFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.imageLoadButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Refresh", None))
        self.operationalAll.setText(QCoreApplication.translate("sd_dreamer_main", u"All images", None))
        self.operationBox.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"Upscale: ESRGAN", None))
        self.operationBox.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"Upscale: Latent-SR", None))
        self.operationBox.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"Art", None))
        self.operationBox.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"Get metadata", None))

        self.operationFolder.setText("")
        self.operationFolder.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Load custom folder", None))
        self.customFolderCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Custom folder", None))
        self.label_9.setText(QCoreApplication.translate("sd_dreamer_main", u"Operation", None))
        self.operationsGoButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Go", None))
        self.imgFilename.setText(QCoreApplication.translate("sd_dreamer_main", u"Filename:", None))
#if QT_CONFIG(tooltip)
        self.processOutput.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Stable diffusion output", None))
#endif // QT_CONFIG(tooltip)
        self.errorMessages.setText(QCoreApplication.translate("sd_dreamer_main", u"Ready", None))
        self.previousImgButton.setText(QCoreApplication.translate("sd_dreamer_main", u"< Previous", None))
#if QT_CONFIG(shortcut)
        self.previousImgButton.setShortcut(QCoreApplication.translate("sd_dreamer_main", u"Left", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.promptVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"The prompt to generate images with. No quotations", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.promptVal.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.cancelButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Cancel", None))
        self.imageView.setText("")
        self.groupBox_3.setTitle("")
#if QT_CONFIG(tooltip)
        self.precisionToggle.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Full precision mode. Slower, more VRAM", None))
#endif // QT_CONFIG(tooltip)
        self.precisionToggle.setText(QCoreApplication.translate("sd_dreamer_main", u"Full precision (select before loading model)", None))
        self.builtUpscaleScale.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"2", None))
        self.builtUpscaleScale.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"4", None))

#if QT_CONFIG(tooltip)
        self.seamlessCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Generates seamless tiling tetures", None))
#endif // QT_CONFIG(tooltip)
        self.seamlessCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Seamless textures", None))
        self.builtUpscaleCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Upscale", None))
#if QT_CONFIG(tooltip)
        self.seedCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Enable random seeding", None))
#endif // QT_CONFIG(tooltip)
        self.seedCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Random seed", None))
        self.gridCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"No grid", None))
#if QT_CONFIG(tooltip)
        self.gfpganCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Enable GFPGAN face restoration. Higher value, stronger effect", None))
#endif // QT_CONFIG(tooltip)
        self.gfpganCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"GFPGAN strength", None))
#if QT_CONFIG(tooltip)
        self.embeddingCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Enable an embedding made with textual inversion", None))
#endif // QT_CONFIG(tooltip)
        self.embeddingCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Embedding (select before loading model)", None))
#if QT_CONFIG(tooltip)
        self.embeddingInputFile.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select textual inversion embedding file (.bin or .pt)", None))
#endif // QT_CONFIG(tooltip)
        self.embeddingInputFile.setText("")
        self.embeddingInputFile.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Path to embedding file", None))
#if QT_CONFIG(tooltip)
        self.variantAmountCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Generates variations of a seed", None))
#endif // QT_CONFIG(tooltip)
        self.variantAmountCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Variant amount", None))
        self.embeddingSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_4.setText(QCoreApplication.translate("sd_dreamer_main", u"Strength", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Generate images", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Dream (txt2img)", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("sd_dreamer_main", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.nextImageButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Next >", None))
#if QT_CONFIG(shortcut)
        self.nextImageButton.setShortcut(QCoreApplication.translate("sd_dreamer_main", u"Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.scaleVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Classifier free guidance scale. Tries to match prompt more, may cause artifacts at high/low numbers", None))
#endif // QT_CONFIG(tooltip)
        self.scale_3.setText(QCoreApplication.translate("sd_dreamer_main", u"Iterations", None))
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
        self.widthThing.setItemText(13, QCoreApplication.translate("sd_dreamer_main", u"1152", None))
        self.widthThing.setItemText(14, QCoreApplication.translate("sd_dreamer_main", u"1408", None))

#if QT_CONFIG(tooltip)
        self.widthThing.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Width of output image", None))
#endif // QT_CONFIG(tooltip)
        self.widthThing.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"512", None))
        self.label.setText(QCoreApplication.translate("sd_dreamer_main", u"Width", None))
        self.label_25.setText(QCoreApplication.translate("sd_dreamer_main", u"8", None))
        self.Steps.setText(QCoreApplication.translate("sd_dreamer_main", u"Steps", None))
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
        self.heightThing.setItemText(13, QCoreApplication.translate("sd_dreamer_main", u"1152", None))
        self.heightThing.setItemText(14, QCoreApplication.translate("sd_dreamer_main", u"1408", None))

#if QT_CONFIG(tooltip)
        self.heightThing.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Height of output image", None))
#endif // QT_CONFIG(tooltip)
        self.heightThing.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"512", None))
        self.scale_2.setText(QCoreApplication.translate("sd_dreamer_main", u"Seed", None))
        self.label_20.setText(QCoreApplication.translate("sd_dreamer_main", u"Sampler", None))
        self.label_2.setText(QCoreApplication.translate("sd_dreamer_main", u"Height", None))
        self.samplerToggle.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"ddim", None))
        self.samplerToggle.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"plms", None))
        self.samplerToggle.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"k_lms", None))
        self.samplerToggle.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"k_euler", None))
        self.samplerToggle.setItemText(4, QCoreApplication.translate("sd_dreamer_main", u"k_euler_a", None))
        self.samplerToggle.setItemText(5, QCoreApplication.translate("sd_dreamer_main", u"k_dpm_2", None))
        self.samplerToggle.setItemText(6, QCoreApplication.translate("sd_dreamer_main", u"k_dpm_2_a", None))
        self.samplerToggle.setItemText(7, QCoreApplication.translate("sd_dreamer_main", u"k_heun", None))

#if QT_CONFIG(tooltip)
        self.samplerToggle.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Sampler. Different samplers produce different images and have different speeds", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.itsVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of images in a batch", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.seedVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"The random noise seed to initialise. Same prompt, settings and seed = same image", None))
#endif // QT_CONFIG(tooltip)
        self.seedVal.setText(QCoreApplication.translate("sd_dreamer_main", u"42", None))
#if QT_CONFIG(tooltip)
        self.stepsVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of steps. Max recommended 150", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("sd_dreamer_main", u"1", None))
        self.label_6.setText(QCoreApplication.translate("sd_dreamer_main", u"30", None))
        self.scale.setText(QCoreApplication.translate("sd_dreamer_main", u"CFG scale", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_3), QCoreApplication.translate("sd_dreamer_main", u"Standard", None))
        self.label_27.setText(QCoreApplication.translate("sd_dreamer_main", u"Strength", None))
        self.imgIndex.setText(QCoreApplication.translate("sd_dreamer_main", u"0", None))
#if QT_CONFIG(tooltip)
        self.imgFileSelect.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select file", None))
#endif // QT_CONFIG(tooltip)
        self.imgFileSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
#if QT_CONFIG(tooltip)
        self.img2imgStrength.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of denoising. Lower the value, closer to original image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.artButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Paint an image", None))
#endif // QT_CONFIG(tooltip)
        self.artButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Paint an image", None))
#if QT_CONFIG(tooltip)
        self.img2imgFile.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Path of source image for img2img", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.img2imgFile.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.img2imgFile.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Input image for img2img", None))
#if QT_CONFIG(tooltip)
        self.img2imgDisplayed.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Use the image in the image viewer", None))
#endif // QT_CONFIG(tooltip)
        self.img2imgDisplayed.setText(QCoreApplication.translate("sd_dreamer_main", u"Use image displayed in viewer", None))
#if QT_CONFIG(tooltip)
        self.img2imgUpscaleCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Upscale image to the dimensions specified in standard tab", None))
#endif // QT_CONFIG(tooltip)
        self.img2imgUpscaleCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"img2img upscale", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_9), QCoreApplication.translate("sd_dreamer_main", u"img2img", None))
#if QT_CONFIG(tooltip)
        self.inpaintingDisplayedCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Use the image in the image viewer", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintingDisplayedCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Use image displayed in viewer", None))
        self.label_3.setText(QCoreApplication.translate("sd_dreamer_main", u"Mask blur", None))
#if QT_CONFIG(tooltip)
        self.invertMaskCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Inpaint the opposite area", None))
#endif // QT_CONFIG(tooltip)
        self.invertMaskCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Invert mask", None))
        self.inpaintButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Create", None))
        self.inpaint_img_select.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
#if QT_CONFIG(tooltip)
        self.inpaint_img.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Image to inpaint", None))
#endif // QT_CONFIG(tooltip)
        self.inpaint_img.setText("")
        self.inpaint_img.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Image to do inpainting on", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_4), QCoreApplication.translate("sd_dreamer_main", u"Inpainting", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("sd_dreamer_main", u"LatentSR", None))
#if QT_CONFIG(tooltip)
        self.latentSRSteps.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Higher = slower, sharper details", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("sd_dreamer_main", u"Steps", None))
        self.label_11.setText(QCoreApplication.translate("sd_dreamer_main", u"1-200", None))
        self.groupBox.setTitle(QCoreApplication.translate("sd_dreamer_main", u"ESRGAN", None))
#if QT_CONFIG(tooltip)
        self.rnvModelSelect.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select Real-ESGRAN NCNN model", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("sd_dreamer_main", u"Model select", None))
        self.label_16.setText(QCoreApplication.translate("sd_dreamer_main", u"Scale", None))
        self.modelScale.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"1", None))
        self.modelScale.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"2", None))
        self.modelScale.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"4", None))
        self.modelScale.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"8", None))

#if QT_CONFIG(tooltip)
        self.modelScale.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select the right scale for the selected model", None))
#endif // QT_CONFIG(tooltip)
        self.modelScale.setCurrentText(QCoreApplication.translate("sd_dreamer_main", u"4", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_5), QCoreApplication.translate("sd_dreamer_main", u"Upscaling", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("sd_dreamer_main", u"Paths", None))
#if QT_CONFIG(tooltip)
        self.custCheckpointLine.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select a model/checkpoint (.ckpt file)", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("sd_dreamer_main", u"Python path (don't change):", None))
        self.custCheckpointSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_10.setText(QCoreApplication.translate("sd_dreamer_main", u"Output folder:", None))
#if QT_CONFIG(tooltip)
        self.outputFolderLine.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Where images will get output to", None))
#endif // QT_CONFIG(tooltip)
        self.outputFolderLine.setText("")
#if QT_CONFIG(tooltip)
        self.pyBinPath.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Python binary", None))
#endif // QT_CONFIG(tooltip)
        self.pyBinPath.setText(QCoreApplication.translate("sd_dreamer_main", u"python", None))
        self.pyBinSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.outputFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_13.setText(QCoreApplication.translate("sd_dreamer_main", u"Model/custom stable diffusion model:", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_6), QCoreApplication.translate("sd_dreamer_main", u"Settings", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("sd_dreamer_main", u"Tip: you can cycle through images with left and right arrow keys and scroll up and down with up/down keys. Holding down button/key repeat cycles through images\n"
"\n"
"'Enter' key activates 'Dream' button\n"
"\n"
"If you run out of VRAM, you don't need to restart the app or reload the model - just try again", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_8), QCoreApplication.translate("sd_dreamer_main", u"Help", None))
    # retranslateUi

