# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSlider,
    QSpinBox, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_sd_dreamer_main(object):
    def setupUi(self, sd_dreamer_main):
        if not sd_dreamer_main.objectName():
            sd_dreamer_main.setObjectName(u"sd_dreamer_main")
        sd_dreamer_main.resize(1345, 1078)
        sd_dreamer_main.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(247, 247, 247, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(76, 81, 88, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(45, 47, 49, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(247, 250, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(35, 36, 40, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush4)
        brush5 = QBrush(QColor(54, 57, 63, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(20, 20, 20, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(40, 115, 152, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush3)
        sd_dreamer_main.setPalette(palette)
        font = QFont()
        font.setBold(False)
        sd_dreamer_main.setFont(font)
        self.gridLayout = QGridLayout(sd_dreamer_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.errorMessages = QLabel(sd_dreamer_main)
        self.errorMessages.setObjectName(u"errorMessages")

        self.gridLayout.addWidget(self.errorMessages, 9, 0, 1, 1)

        self.scrollArea = QScrollArea(sd_dreamer_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 819, 726))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageView = QLabel(self.scrollAreaWidgetContents)
        self.imageView.setObjectName(u"imageView")
        self.imageView.setMaximumSize(QSize(1440, 1440))
        palette1 = QPalette()
        brush8 = QBrush(QColor(21, 22, 23, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush8)
        brush9 = QBrush(QColor(251, 253, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        brush10 = QBrush(QColor(170, 171, 172, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.imageView.setPalette(palette1)
        self.imageView.setContextMenuPolicy(Qt.CustomContextMenu)
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

        self.gridLayout.addWidget(self.scrollArea, 3, 1, 3, 5)

        self.previousImgButton = QPushButton(sd_dreamer_main)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 6, 1, 1, 1, Qt.AlignLeft)

        self.generateButton = QPushButton(sd_dreamer_main)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(True)
        self.generateButton.setMaximumSize(QSize(265, 16777215))
        self.generateButton.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.generateButton.setFont(font1)
        self.generateButton.setStyleSheet(u"background-color: rgb(147, 217, 255);")
        icon = QIcon()
        icon.addFile(u"appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.generateButton.setIcon(icon)
        self.generateButton.setIconSize(QSize(24, 24))
        self.generateButton.setCheckable(False)
        self.generateButton.setAutoDefault(True)
        self.generateButton.setFlat(False)

        self.gridLayout.addWidget(self.generateButton, 0, 4, 1, 1)

        self.frame = QFrame(sd_dreamer_main)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(1160, 16777215))
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.promptVal = QComboBox(self.frame)
        self.promptVal.setObjectName(u"promptVal")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.promptVal.setFont(font2)
        self.promptVal.setEditable(True)
        self.promptVal.setMaxVisibleItems(35)
        self.promptVal.setMaxCount(100)
        self.promptVal.setInsertPolicy(QComboBox.InsertAtTop)
        self.promptVal.setFrame(True)

        self.verticalLayout.addWidget(self.promptVal)

        self.negPromptVal = QLineEdit(self.frame)
        self.negPromptVal.setObjectName(u"negPromptVal")
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.negPromptVal.setFont(font3)

        self.verticalLayout.addWidget(self.negPromptVal)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 4)

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

        self.gridLayout.addWidget(self.processOutput, 8, 0, 1, 6)

        self.nextImageButton = QPushButton(sd_dreamer_main)
        self.nextImageButton.setObjectName(u"nextImageButton")

        self.gridLayout.addWidget(self.nextImageButton, 6, 5, 1, 1, Qt.AlignRight)

        self.cancelButton = QPushButton(sd_dreamer_main)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(True)
        self.cancelButton.setMaximumSize(QSize(198, 16777215))

        self.gridLayout.addWidget(self.cancelButton, 0, 5, 1, 1)

        self.groupBox_4 = QGroupBox(sd_dreamer_main)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.gridLayout_12 = QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.imageLoadButton = QPushButton(self.groupBox_4)
        self.imageLoadButton.setObjectName(u"imageLoadButton")

        self.gridLayout_12.addWidget(self.imageLoadButton, 1, 4, 1, 1)

        self.imgFilename = QLineEdit(self.groupBox_4)
        self.imgFilename.setObjectName(u"imgFilename")
        self.imgFilename.setAcceptDrops(False)
        self.imgFilename.setAutoFillBackground(False)
        self.imgFilename.setFrame(False)
        self.imgFilename.setReadOnly(True)
        self.imgFilename.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.imgFilename, 0, 0, 1, 7)

        self.operationFolderSelect = QToolButton(self.groupBox_4)
        self.operationFolderSelect.setObjectName(u"operationFolderSelect")

        self.gridLayout_12.addWidget(self.operationFolderSelect, 1, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setBold(True)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.label_9.setFont(font4)

        self.gridLayout_12.addWidget(self.label_9, 2, 1, 1, 1)

        self.operationsGoButton = QPushButton(self.groupBox_4)
        self.operationsGoButton.setObjectName(u"operationsGoButton")
        self.operationsGoButton.setFont(font4)

        self.gridLayout_12.addWidget(self.operationsGoButton, 2, 3, 1, 2)

        self.operationBox = QComboBox(self.groupBox_4)
        self.operationBox.addItem("")
        self.operationBox.addItem("")
        self.operationBox.setObjectName(u"operationBox")

        self.gridLayout_12.addWidget(self.operationBox, 2, 2, 1, 1)

        self.operationFolder = QLineEdit(self.groupBox_4)
        self.operationFolder.setObjectName(u"operationFolder")

        self.gridLayout_12.addWidget(self.operationFolder, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 7, 1, 1, 5)

        self.label_12 = QLabel(sd_dreamer_main)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 6, 2, 1, 1)

        self.scrollArea_2 = QScrollArea(sd_dreamer_main)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(500, 16777215))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.scrollArea_2.setFont(font5)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 475, 610))
        self.gridLayout_17 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.embeddingCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.embeddingCheck.setObjectName(u"embeddingCheck")

        self.gridLayout_17.addWidget(self.embeddingCheck, 17, 1, 1, 1)

        self.builtUpscaleStrength = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.builtUpscaleStrength.setObjectName(u"builtUpscaleStrength")
        self.builtUpscaleStrength.setMinimum(0.010000000000000)
        self.builtUpscaleStrength.setMaximum(0.990000000000000)
        self.builtUpscaleStrength.setSingleStep(0.020000000000000)
        self.builtUpscaleStrength.setValue(0.750000000000000)

        self.gridLayout_17.addWidget(self.builtUpscaleStrength, 2, 3, 1, 1)

        self.seamlessCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.seamlessCheck.setObjectName(u"seamlessCheck")

        self.gridLayout_17.addWidget(self.seamlessCheck, 11, 1, 1, 1)

        self.variantAmountValue = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.variantAmountValue.setObjectName(u"variantAmountValue")
        self.variantAmountValue.setMinimum(0.010000000000000)
        self.variantAmountValue.setMaximum(0.990000000000000)
        self.variantAmountValue.setSingleStep(0.020000000000000)
        self.variantAmountValue.setValue(0.300000000000000)

        self.gridLayout_17.addWidget(self.variantAmountValue, 3, 3, 1, 1)

        self.faceRestoreBox = QGroupBox(self.scrollAreaWidgetContents_3)
        self.faceRestoreBox.setObjectName(u"faceRestoreBox")
        self.faceRestoreBox.setFlat(False)
        self.faceRestoreBox.setCheckable(False)
        self.gridLayout_8 = QGridLayout(self.faceRestoreBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.codeformerCheck = QRadioButton(self.faceRestoreBox)
        self.codeformerCheck.setObjectName(u"codeformerCheck")

        self.gridLayout_8.addWidget(self.codeformerCheck, 2, 0, 1, 1)

        self.radioButton = QRadioButton(self.faceRestoreBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_8.addWidget(self.radioButton, 0, 0, 1, 1)

        self.gfpganCheck = QRadioButton(self.faceRestoreBox)
        self.gfpganCheck.setObjectName(u"gfpganCheck")

        self.gridLayout_8.addWidget(self.gfpganCheck, 1, 0, 1, 1)

        self.codeformerValue = QDoubleSpinBox(self.faceRestoreBox)
        self.codeformerValue.setObjectName(u"codeformerValue")
        self.codeformerValue.setMinimum(0.100000000000000)
        self.codeformerValue.setMaximum(0.990000000000000)
        self.codeformerValue.setSingleStep(0.020000000000000)
        self.codeformerValue.setValue(0.750000000000000)

        self.gridLayout_8.addWidget(self.codeformerValue, 2, 2, 1, 1)

        self.faceStrength = QDoubleSpinBox(self.faceRestoreBox)
        self.faceStrength.setObjectName(u"faceStrength")
        self.faceStrength.setMinimum(0.100000000000000)
        self.faceStrength.setMaximum(0.990000000000000)
        self.faceStrength.setSingleStep(0.020000000000000)
        self.faceStrength.setValue(0.750000000000000)

        self.gridLayout_8.addWidget(self.faceStrength, 0, 2, 1, 1)

        self.label_4 = QLabel(self.faceRestoreBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_14 = QLabel(self.faceRestoreBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_8.addWidget(self.label_14, 2, 1, 1, 1)


        self.gridLayout_17.addWidget(self.faceRestoreBox, 10, 1, 1, 3)

        self.builtUpscaleCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.builtUpscaleCheck.setObjectName(u"builtUpscaleCheck")

        self.gridLayout_17.addWidget(self.builtUpscaleCheck, 2, 1, 1, 1)

        self.thresholdValue = QSpinBox(self.scrollAreaWidgetContents_3)
        self.thresholdValue.setObjectName(u"thresholdValue")
        self.thresholdValue.setMinimum(1)
        self.thresholdValue.setMaximum(100)
        self.thresholdValue.setValue(5)

        self.gridLayout_17.addWidget(self.thresholdValue, 12, 3, 1, 1)

        self.precisionToggle = QCheckBox(self.scrollAreaWidgetContents_3)
        self.precisionToggle.setObjectName(u"precisionToggle")

        self.gridLayout_17.addWidget(self.precisionToggle, 16, 1, 1, 1)

        self.perlinValue = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.perlinValue.setObjectName(u"perlinValue")
        self.perlinValue.setMinimum(0.010000000000000)
        self.perlinValue.setMaximum(1.000000000000000)
        self.perlinValue.setSingleStep(0.020000000000000)
        self.perlinValue.setValue(0.200000000000000)

        self.gridLayout_17.addWidget(self.perlinValue, 13, 3, 1, 1)

        self.builtUpscaleScale = QComboBox(self.scrollAreaWidgetContents_3)
        self.builtUpscaleScale.addItem("")
        self.builtUpscaleScale.addItem("")
        self.builtUpscaleScale.setObjectName(u"builtUpscaleScale")

        self.gridLayout_17.addWidget(self.builtUpscaleScale, 2, 2, 1, 1)

        self.hiresfixCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.hiresfixCheck.setObjectName(u"hiresfixCheck")

        self.gridLayout_17.addWidget(self.hiresfixCheck, 14, 1, 1, 1)

        self.perlinCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.perlinCheck.setObjectName(u"perlinCheck")

        self.gridLayout_17.addWidget(self.perlinCheck, 13, 1, 1, 1)

        self.memFreeCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.memFreeCheck.setObjectName(u"memFreeCheck")

        self.gridLayout_17.addWidget(self.memFreeCheck, 15, 1, 1, 1)

        self.embeddingInputFile = QLineEdit(self.scrollAreaWidgetContents_3)
        self.embeddingInputFile.setObjectName(u"embeddingInputFile")

        self.gridLayout_17.addWidget(self.embeddingInputFile, 18, 1, 1, 2)

        self.variantAmountCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.variantAmountCheck.setObjectName(u"variantAmountCheck")

        self.gridLayout_17.addWidget(self.variantAmountCheck, 3, 1, 1, 1)

        self.thresholdCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.thresholdCheck.setObjectName(u"thresholdCheck")

        self.gridLayout_17.addWidget(self.thresholdCheck, 12, 1, 1, 1)

        self.gridCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.gridCheck.setObjectName(u"gridCheck")

        self.gridLayout_17.addWidget(self.gridCheck, 4, 1, 1, 1)

        self.seedCheck = QCheckBox(self.scrollAreaWidgetContents_3)
        self.seedCheck.setObjectName(u"seedCheck")
        self.seedCheck.setChecked(True)

        self.gridLayout_17.addWidget(self.seedCheck, 1, 1, 1, 1)

        self.embeddingSelect = QToolButton(self.scrollAreaWidgetContents_3)
        self.embeddingSelect.setObjectName(u"embeddingSelect")

        self.gridLayout_17.addWidget(self.embeddingSelect, 18, 3, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.scrollArea_2, 4, 0, 4, 1)

        self.mainTab = QTabWidget(sd_dreamer_main)
        self.mainTab.setObjectName(u"mainTab")
        self.mainTab.setMaximumSize(QSize(500, 16777215))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.heightThing = QSpinBox(self.tab_3)
        self.heightThing.setObjectName(u"heightThing")
        self.heightThing.setMinimum(256)
        self.heightThing.setMaximum(2048)
        self.heightThing.setSingleStep(64)
        self.heightThing.setValue(512)

        self.gridLayout_2.addWidget(self.heightThing, 3, 2, 1, 1)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.promptTagAdd = QPushButton(self.tab_3)
        self.promptTagAdd.setObjectName(u"promptTagAdd")

        self.gridLayout_2.addWidget(self.promptTagAdd, 0, 3, 1, 1)

        self.scale = QLabel(self.tab_3)
        self.scale.setObjectName(u"scale")
        self.scale.setFont(font4)

        self.gridLayout_2.addWidget(self.scale, 5, 0, 1, 1)

        self.widthThing = QSpinBox(self.tab_3)
        self.widthThing.setObjectName(u"widthThing")
        self.widthThing.setMinimum(256)
        self.widthThing.setMaximum(2048)
        self.widthThing.setSingleStep(64)
        self.widthThing.setValue(512)

        self.gridLayout_2.addWidget(self.widthThing, 2, 2, 1, 1)

        self.seedVal = QLineEdit(self.tab_3)
        self.seedVal.setObjectName(u"seedVal")

        self.gridLayout_2.addWidget(self.seedVal, 1, 2, 1, 1)

        self.itsVal = QSlider(self.tab_3)
        self.itsVal.setObjectName(u"itsVal")
        self.itsVal.setMinimum(1)
        self.itsVal.setMaximum(60)
        self.itsVal.setValue(2)
        self.itsVal.setSliderPosition(2)
        self.itsVal.setOrientation(Qt.Horizontal)
        self.itsVal.setTickPosition(QSlider.NoTicks)
        self.itsVal.setTickInterval(6)

        self.gridLayout_2.addWidget(self.itsVal, 6, 2, 1, 1)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)

        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)

        self.stepsVal = QSlider(self.tab_3)
        self.stepsVal.setObjectName(u"stepsVal")
        self.stepsVal.setMinimum(1)
        self.stepsVal.setMaximum(200)
        self.stepsVal.setValue(30)
        self.stepsVal.setSliderPosition(30)
        self.stepsVal.setOrientation(Qt.Horizontal)
        self.stepsVal.setTickPosition(QSlider.NoTicks)
        self.stepsVal.setTickInterval(20)

        self.gridLayout_2.addWidget(self.stepsVal, 4, 2, 1, 1)

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

        self.gridLayout_2.addWidget(self.samplerToggle, 7, 2, 1, 1)

        self.promptTag = QComboBox(self.tab_3)
        self.promptTag.setObjectName(u"promptTag")
        self.promptTag.setEditable(True)
        self.promptTag.setMaxCount(100)
        self.promptTag.setInsertPolicy(QComboBox.InsertAtTop)

        self.gridLayout_2.addWidget(self.promptTag, 0, 2, 1, 1)

        self.scale_3 = QLabel(self.tab_3)
        self.scale_3.setObjectName(u"scale_3")
        self.scale_3.setFont(font4)

        self.gridLayout_2.addWidget(self.scale_3, 6, 0, 1, 1)

        self.scaleVal = QSlider(self.tab_3)
        self.scaleVal.setObjectName(u"scaleVal")
        self.scaleVal.setMinimum(1)
        self.scaleVal.setMaximum(30)
        self.scaleVal.setSingleStep(1)
        self.scaleVal.setValue(8)
        self.scaleVal.setSliderPosition(8)
        self.scaleVal.setOrientation(Qt.Horizontal)
        self.scaleVal.setTickPosition(QSlider.NoTicks)
        self.scaleVal.setTickInterval(3)

        self.gridLayout_2.addWidget(self.scaleVal, 5, 2, 1, 1)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 5, 3, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 3, 1, 1)

        self.scale_2 = QLabel(self.tab_3)
        self.scale_2.setObjectName(u"scale_2")
        self.scale_2.setFont(font4)

        self.gridLayout_2.addWidget(self.scale_2, 1, 0, 1, 1)

        self.Steps = QLabel(self.tab_3)
        self.Steps.setObjectName(u"Steps")
        self.Steps.setFont(font4)

        self.gridLayout_2.addWidget(self.Steps, 4, 0, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 3, 1, 1)

        self.mainTab.addTab(self.tab_3, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setAutoFillBackground(True)
        self.gridLayout_14 = QGridLayout(self.tab_9)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.img2imgUpscaleCheck = QCheckBox(self.tab_9)
        self.img2imgUpscaleCheck.setObjectName(u"img2imgUpscaleCheck")

        self.gridLayout_14.addWidget(self.img2imgUpscaleCheck, 1, 0, 1, 1)

        self.artButton = QPushButton(self.tab_9)
        self.artButton.setObjectName(u"artButton")

        self.gridLayout_14.addWidget(self.artButton, 4, 0, 1, 2)

        self.groupBox_6 = QGroupBox(self.tab_9)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.img2imgFile = QLineEdit(self.groupBox_6)
        self.img2imgFile.setObjectName(u"img2imgFile")
        self.img2imgFile.setAutoFillBackground(False)
        self.img2imgFile.setFrame(True)
        self.img2imgFile.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.img2imgFile, 2, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_6)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 0, 0, 1, 1)

        self.img2imgStrength = QDoubleSpinBox(self.groupBox_6)
        self.img2imgStrength.setObjectName(u"img2imgStrength")
        self.img2imgStrength.setMaximum(0.990000000000000)
        self.img2imgStrength.setSingleStep(0.010000000000000)
        self.img2imgStrength.setValue(0.750000000000000)

        self.gridLayout_7.addWidget(self.img2imgStrength, 0, 2, 1, 1)

        self.imgFileSelect = QToolButton(self.groupBox_6)
        self.imgFileSelect.setObjectName(u"imgFileSelect")

        self.gridLayout_7.addWidget(self.imgFileSelect, 2, 2, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_6, 2, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_15 = QGridLayout(self.groupBox_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_15.addWidget(self.label_15, 3, 0, 1, 1)

        self.embiggenScale = QSpinBox(self.groupBox_3)
        self.embiggenScale.setObjectName(u"embiggenScale")
        self.embiggenScale.setMinimum(2)
        self.embiggenScale.setMaximum(4)
        self.embiggenScale.setSingleStep(2)

        self.gridLayout_15.addWidget(self.embiggenScale, 3, 1, 1, 1)

        self.embiggenCheck = QCheckBox(self.groupBox_3)
        self.embiggenCheck.setObjectName(u"embiggenCheck")

        self.gridLayout_15.addWidget(self.embiggenCheck, 0, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_15.addWidget(self.label_16, 4, 0, 1, 1)

        self.embiggenStrength = QDoubleSpinBox(self.groupBox_3)
        self.embiggenStrength.setObjectName(u"embiggenStrength")
        self.embiggenStrength.setMinimum(0.100000000000000)
        self.embiggenStrength.setMaximum(0.990000000000000)
        self.embiggenStrength.setSingleStep(0.020000000000000)
        self.embiggenStrength.setValue(0.750000000000000)

        self.gridLayout_15.addWidget(self.embiggenStrength, 4, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_15.addWidget(self.label_17, 5, 0, 1, 1)

        self.embiggenOverlap = QDoubleSpinBox(self.groupBox_3)
        self.embiggenOverlap.setObjectName(u"embiggenOverlap")
        self.embiggenOverlap.setMinimum(0.100000000000000)
        self.embiggenOverlap.setMaximum(0.990000000000000)
        self.embiggenOverlap.setSingleStep(0.020000000000000)
        self.embiggenOverlap.setValue(0.300000000000000)

        self.gridLayout_15.addWidget(self.embiggenOverlap, 5, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_3, 3, 0, 1, 2)

        self.imgIndex = QLabel(self.tab_9)
        self.imgIndex.setObjectName(u"imgIndex")

        self.gridLayout_14.addWidget(self.imgIndex, 1, 1, 1, 1)

        self.mainTab.addTab(self.tab_9, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.invertMaskCheck = QCheckBox(self.tab_4)
        self.invertMaskCheck.setObjectName(u"invertMaskCheck")

        self.gridLayout_4.addWidget(self.invertMaskCheck, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.inpaint_img_select = QToolButton(self.groupBox_2)
        self.inpaint_img_select.setObjectName(u"inpaint_img_select")

        self.gridLayout_6.addWidget(self.inpaint_img_select, 1, 2, 1, 1)

        self.inpaintButton = QPushButton(self.groupBox_2)
        self.inpaintButton.setObjectName(u"inpaintButton")

        self.gridLayout_6.addWidget(self.inpaintButton, 2, 0, 1, 3)

        self.maskBlurVaue = QSpinBox(self.groupBox_2)
        self.maskBlurVaue.setObjectName(u"maskBlurVaue")
        self.maskBlurVaue.setMinimum(1)
        self.maskBlurVaue.setMaximum(16)
        self.maskBlurVaue.setValue(3)

        self.gridLayout_6.addWidget(self.maskBlurVaue, 0, 1, 1, 1)

        self.inpaint_img = QLineEdit(self.groupBox_2)
        self.inpaint_img.setObjectName(u"inpaint_img")
        self.inpaint_img.setReadOnly(False)

        self.gridLayout_6.addWidget(self.inpaint_img, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_2, 3, 0, 1, 2)

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
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_9.addWidget(self.label_32, 0, 0, 1, 1)

        self.rnvModelSelect = QComboBox(self.groupBox)
        self.rnvModelSelect.setObjectName(u"rnvModelSelect")

        self.gridLayout_9.addWidget(self.rnvModelSelect, 0, 1, 1, 2)


        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)

        self.mainTab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.tab_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line = QFrame(self.tab_6)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 1)

        self.pyBinPath = QLineEdit(self.tab_6)
        self.pyBinPath.setObjectName(u"pyBinPath")
        self.pyBinPath.setReadOnly(False)

        self.gridLayout_3.addWidget(self.pyBinPath, 7, 0, 1, 1)

        self.line_3 = QFrame(self.tab_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 9, 0, 1, 1)

        self.restoreModelsCheck = QCheckBox(self.tab_6)
        self.restoreModelsCheck.setObjectName(u"restoreModelsCheck")
        font6 = QFont()
        font6.setBold(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.restoreModelsCheck.setFont(font6)
        self.restoreModelsCheck.setAcceptDrops(False)
        self.restoreModelsCheck.setChecked(True)

        self.gridLayout_3.addWidget(self.restoreModelsCheck, 8, 0, 1, 1)

        self.outputFolderSelect = QToolButton(self.tab_6)
        self.outputFolderSelect.setObjectName(u"outputFolderSelect")

        self.gridLayout_3.addWidget(self.outputFolderSelect, 4, 1, 1, 1)

        self.label_13 = QLabel(self.tab_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.custCheckpointSelect = QToolButton(self.tab_6)
        self.custCheckpointSelect.setObjectName(u"custCheckpointSelect")

        self.gridLayout_3.addWidget(self.custCheckpointSelect, 1, 1, 1, 1)

        self.pyBinSelect = QToolButton(self.tab_6)
        self.pyBinSelect.setObjectName(u"pyBinSelect")

        self.gridLayout_3.addWidget(self.pyBinSelect, 7, 1, 1, 1)

        self.outputFolderLine = QLineEdit(self.tab_6)
        self.outputFolderLine.setObjectName(u"outputFolderLine")

        self.gridLayout_3.addWidget(self.outputFolderLine, 4, 0, 1, 1)

        self.custCheckpointLine = QLineEdit(self.tab_6)
        self.custCheckpointLine.setObjectName(u"custCheckpointLine")

        self.gridLayout_3.addWidget(self.custCheckpointLine, 1, 0, 1, 1)

        self.line_2 = QFrame(self.tab_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 5, 0, 1, 1)

        self.label_10 = QLabel(self.tab_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_18 = QLabel(self.tab_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 6, 0, 1, 1)

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

        self.gridLayout.addWidget(self.mainTab, 3, 0, 1, 1)


        self.retranslateUi(sd_dreamer_main)
        self.stepsVal.valueChanged.connect(self.label_6.setNum)
        self.itsVal.valueChanged.connect(self.label_8.setNum)
        self.scaleVal.valueChanged.connect(self.label_25.setNum)

        self.generateButton.setDefault(False)
        self.promptVal.setCurrentIndex(-1)
        self.operationBox.setCurrentIndex(0)
        self.mainTab.setCurrentIndex(0)
        self.samplerToggle.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(sd_dreamer_main)
    # setupUi

    def retranslateUi(self, sd_dreamer_main):
        sd_dreamer_main.setWindowTitle(QCoreApplication.translate("sd_dreamer_main", u"SD Dreamer", None))
        self.errorMessages.setText(QCoreApplication.translate("sd_dreamer_main", u"Ready", None))
        self.imageView.setText("")
#if QT_CONFIG(tooltip)
        self.previousImgButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Previous image", None))
#endif // QT_CONFIG(tooltip)
        self.previousImgButton.setText(QCoreApplication.translate("sd_dreamer_main", u"< Previous", None))
#if QT_CONFIG(shortcut)
        self.previousImgButton.setShortcut(QCoreApplication.translate("sd_dreamer_main", u"Left", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Generate images", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Dream (txt2img)", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("sd_dreamer_main", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.promptVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"The prompt to generate images with. No quotations", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.negPromptVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Negative prompt to use", None))
#endif // QT_CONFIG(tooltip)
        self.negPromptVal.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Negative prompt", None))
#if QT_CONFIG(tooltip)
        self.processOutput.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Stable diffusion output", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.nextImageButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Next image", None))
#endif // QT_CONFIG(tooltip)
        self.nextImageButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Next >", None))
#if QT_CONFIG(shortcut)
        self.nextImageButton.setShortcut(QCoreApplication.translate("sd_dreamer_main", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.cancelButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Cancel", None))
        self.groupBox_4.setTitle("")
#if QT_CONFIG(tooltip)
        self.imageLoadButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Refresh the viewer with images from custom folder", None))
#endif // QT_CONFIG(tooltip)
        self.imageLoadButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.imgFilename.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Image filename", None))
#endif // QT_CONFIG(tooltip)
        self.imgFilename.setText(QCoreApplication.translate("sd_dreamer_main", u"Filename:", None))
#if QT_CONFIG(tooltip)
        self.operationFolderSelect.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select a folder", None))
#endif // QT_CONFIG(tooltip)
        self.operationFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_9.setText(QCoreApplication.translate("sd_dreamer_main", u"Operation:", None))
#if QT_CONFIG(tooltip)
        self.operationsGoButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Perform operation", None))
#endif // QT_CONFIG(tooltip)
        self.operationsGoButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Go", None))
        self.operationBox.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"Upscale folder: ESRGAN", None))
        self.operationBox.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"Upscale folder: LDSR", None))

#if QT_CONFIG(tooltip)
        self.operationBox.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Operations to perform", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.operationFolder.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Load a custom folder of images", None))
#endif // QT_CONFIG(tooltip)
        self.operationFolder.setText("")
        self.operationFolder.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Load custom images folder", None))
        self.label_12.setText(QCoreApplication.translate("sd_dreamer_main", u"Right click image for actions", None))
#if QT_CONFIG(tooltip)
        self.embeddingCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Use an embedding made with textual inversion", None))
#endif // QT_CONFIG(tooltip)
        self.embeddingCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Embedding (select before loading model)", None))
#if QT_CONFIG(tooltip)
        self.builtUpscaleStrength.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of upscale effect", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.seamlessCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Generates seamless tiling tetures", None))
#endif // QT_CONFIG(tooltip)
        self.seamlessCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Seamless textures", None))
        self.faceRestoreBox.setTitle(QCoreApplication.translate("sd_dreamer_main", u"Face restore", None))
        self.codeformerCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"CodeFormer", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Don't apply face restoration model", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("sd_dreamer_main", u"None", None))
#if QT_CONFIG(tooltip)
        self.gfpganCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Enable GFPGAN face restoration. Higher value, stronger effect", None))
#endif // QT_CONFIG(tooltip)
        self.gfpganCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"GFPGAN", None))
#if QT_CONFIG(tooltip)
        self.codeformerValue.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of CodeFormer face restoration", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.faceStrength.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of GFPGAN face restoration", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("sd_dreamer_main", u"Strength", None))
        self.label_14.setText(QCoreApplication.translate("sd_dreamer_main", u"Fidelity", None))
#if QT_CONFIG(tooltip)
        self.builtUpscaleCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Upscale each image with Real-ESRGAN", None))
#endif // QT_CONFIG(tooltip)
        self.builtUpscaleCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Upscale", None))
#if QT_CONFIG(tooltip)
        self.precisionToggle.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Full precision (float32) mode. Slower, more VRAM", None))
#endif // QT_CONFIG(tooltip)
        self.precisionToggle.setText(QCoreApplication.translate("sd_dreamer_main", u"Full precision (select before loading model)", None))
        self.builtUpscaleScale.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"2", None))
        self.builtUpscaleScale.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"4", None))

#if QT_CONFIG(tooltip)
        self.hiresfixCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Reduces tiling in higher res images at cost of some speed", None))
#endif // QT_CONFIG(tooltip)
        self.hiresfixCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"High-res fix", None))
#if QT_CONFIG(tooltip)
        self.perlinCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Amount of perlin noise mixed into the initial noise", None))
#endif // QT_CONFIG(tooltip)
        self.perlinCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Perlin noise", None))
#if QT_CONFIG(tooltip)
        self.memFreeCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Free GPU memory after image generation", None))
#endif // QT_CONFIG(tooltip)
        self.memFreeCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Free GPU mem", None))
#if QT_CONFIG(tooltip)
        self.embeddingInputFile.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select textual inversion embedding file (.bin or .pt)", None))
#endif // QT_CONFIG(tooltip)
        self.embeddingInputFile.setText("")
        self.embeddingInputFile.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Path to embedding file", None))
#if QT_CONFIG(tooltip)
        self.variantAmountCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Generates variations of a seed. Used with iterations", None))
#endif // QT_CONFIG(tooltip)
        self.variantAmountCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Variant amount", None))
#if QT_CONFIG(tooltip)
        self.thresholdCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Thresholding amount. Helps combat oversaturation with higher CFG scale values", None))
#endif // QT_CONFIG(tooltip)
        self.thresholdCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Threshold", None))
#if QT_CONFIG(tooltip)
        self.gridCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Don't make a grid", None))
#endif // QT_CONFIG(tooltip)
        self.gridCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Grid", None))
#if QT_CONFIG(tooltip)
        self.seedCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Enable random seeding", None))
#endif // QT_CONFIG(tooltip)
        self.seedCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Random seed", None))
        self.embeddingSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_5.setText(QCoreApplication.translate("sd_dreamer_main", u"Prompt tag", None))
#if QT_CONFIG(tooltip)
        self.promptTagAdd.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Add tag to prompt", None))
#endif // QT_CONFIG(tooltip)
        self.promptTagAdd.setText(QCoreApplication.translate("sd_dreamer_main", u"Add", None))
        self.scale.setText(QCoreApplication.translate("sd_dreamer_main", u"CFG scale", None))
#if QT_CONFIG(tooltip)
        self.seedVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"The random noise seed to initialise. Same prompt, settings and seed = same image", None))
#endif // QT_CONFIG(tooltip)
        self.seedVal.setText(QCoreApplication.translate("sd_dreamer_main", u"42", None))
#if QT_CONFIG(tooltip)
        self.itsVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of images to generate", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("sd_dreamer_main", u"Sampler", None))
#if QT_CONFIG(tooltip)
        self.stepsVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Number of steps. Max recommended 150", None))
#endif // QT_CONFIG(tooltip)
        self.samplerToggle.setItemText(0, QCoreApplication.translate("sd_dreamer_main", u"k_euler", None))
        self.samplerToggle.setItemText(1, QCoreApplication.translate("sd_dreamer_main", u"k_euler_a", None))
        self.samplerToggle.setItemText(2, QCoreApplication.translate("sd_dreamer_main", u"k_lms", None))
        self.samplerToggle.setItemText(3, QCoreApplication.translate("sd_dreamer_main", u"k_dpm_2", None))
        self.samplerToggle.setItemText(4, QCoreApplication.translate("sd_dreamer_main", u"k_dpm_2_a", None))
        self.samplerToggle.setItemText(5, QCoreApplication.translate("sd_dreamer_main", u"k_heun", None))
        self.samplerToggle.setItemText(6, QCoreApplication.translate("sd_dreamer_main", u"ddim", None))
        self.samplerToggle.setItemText(7, QCoreApplication.translate("sd_dreamer_main", u"plms", None))

#if QT_CONFIG(tooltip)
        self.samplerToggle.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Sampler. Different samplers produce different images and have different speeds", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.promptTag.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Sets a preset prompt or prompt part and adds to current prompt", None))
#endif // QT_CONFIG(tooltip)
        self.scale_3.setText(QCoreApplication.translate("sd_dreamer_main", u"Iterations", None))
#if QT_CONFIG(tooltip)
        self.scaleVal.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Prompt following strictness. Negative values give opposite of prompt", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("sd_dreamer_main", u"Width", None))
        self.label_25.setText(QCoreApplication.translate("sd_dreamer_main", u"8", None))
        self.label_8.setText(QCoreApplication.translate("sd_dreamer_main", u"2", None))
        self.scale_2.setText(QCoreApplication.translate("sd_dreamer_main", u"Seed", None))
        self.Steps.setText(QCoreApplication.translate("sd_dreamer_main", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("sd_dreamer_main", u"Height", None))
        self.label_6.setText(QCoreApplication.translate("sd_dreamer_main", u"30", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_3), QCoreApplication.translate("sd_dreamer_main", u"Standard", None))
#if QT_CONFIG(tooltip)
        self.img2imgUpscaleCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Upscale image to the dimensions specified in standard tab", None))
#endif // QT_CONFIG(tooltip)
        self.img2imgUpscaleCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"img2img upscale", None))
#if QT_CONFIG(tooltip)
        self.artButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Paint an image", None))
#endif // QT_CONFIG(tooltip)
        self.artButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Paint an image", None))
        self.groupBox_6.setTitle("")
#if QT_CONFIG(tooltip)
        self.img2imgFile.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Path of source image for img2img", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.img2imgFile.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.img2imgFile.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Input image for img2img", None))
        self.label_27.setText(QCoreApplication.translate("sd_dreamer_main", u"Strength", None))
#if QT_CONFIG(tooltip)
        self.img2imgStrength.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of denoising. Lower the value, closer to original image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.imgFileSelect.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select file", None))
#endif // QT_CONFIG(tooltip)
        self.imgFileSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("sd_dreamer_main", u"Embiggen", None))
        self.label_15.setText(QCoreApplication.translate("sd_dreamer_main", u"Scale", None))
#if QT_CONFIG(tooltip)
        self.embiggenScale.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Upscale 2x or 4x", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.embiggenCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Upscales generated image. Uses img2img 'Strength' value. Set to 0.2 - 0.4 for best results", None))
#endif // QT_CONFIG(tooltip)
        self.embiggenCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Enable", None))
        self.label_16.setText(QCoreApplication.translate("sd_dreamer_main", u"Upscale strength", None))
#if QT_CONFIG(tooltip)
        self.embiggenStrength.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Strength of upscale effect", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("sd_dreamer_main", u"Overlap", None))
#if QT_CONFIG(tooltip)
        self.embiggenOverlap.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Tile overlap for embiggen", None))
#endif // QT_CONFIG(tooltip)
        self.imgIndex.setText(QCoreApplication.translate("sd_dreamer_main", u"0", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_9), QCoreApplication.translate("sd_dreamer_main", u"img2img", None))
#if QT_CONFIG(tooltip)
        self.invertMaskCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Inpaint the opposite area masked", None))
#endif // QT_CONFIG(tooltip)
        self.invertMaskCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Invert mask", None))
        self.groupBox_2.setTitle("")
        self.label_3.setText(QCoreApplication.translate("sd_dreamer_main", u"Mask blur", None))
#if QT_CONFIG(tooltip)
        self.inpaint_img_select.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select image to inpaint", None))
#endif // QT_CONFIG(tooltip)
        self.inpaint_img_select.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
#if QT_CONFIG(tooltip)
        self.inpaintButton.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Launch editor for inpainting", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintButton.setText(QCoreApplication.translate("sd_dreamer_main", u"Inpaint editor", None))
#if QT_CONFIG(tooltip)
        self.maskBlurVaue.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"How much to blur the mask edges", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inpaint_img.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Image to inpaint", None))
#endif // QT_CONFIG(tooltip)
        self.inpaint_img.setText("")
        self.inpaint_img.setPlaceholderText(QCoreApplication.translate("sd_dreamer_main", u"Image to inpaint", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_4), QCoreApplication.translate("sd_dreamer_main", u"Inpainting", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("sd_dreamer_main", u"LatentSR", None))
#if QT_CONFIG(tooltip)
        self.latentSRSteps.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Higher = slower, sharper details", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("sd_dreamer_main", u"Steps", None))
        self.label_11.setText(QCoreApplication.translate("sd_dreamer_main", u"1-200", None))
        self.groupBox.setTitle(QCoreApplication.translate("sd_dreamer_main", u"ESRGAN", None))
        self.label_32.setText(QCoreApplication.translate("sd_dreamer_main", u"Model select", None))
#if QT_CONFIG(tooltip)
        self.rnvModelSelect.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"ESRGAN model to use", None))
#endif // QT_CONFIG(tooltip)
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_5), QCoreApplication.translate("sd_dreamer_main", u"Upscaling", None))
#if QT_CONFIG(tooltip)
        self.pyBinPath.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Python binary", None))
#endif // QT_CONFIG(tooltip)
        self.pyBinPath.setText(QCoreApplication.translate("sd_dreamer_main", u"python", None))
#if QT_CONFIG(tooltip)
        self.restoreModelsCheck.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Autoload face restore and esrgan models", None))
#endif // QT_CONFIG(tooltip)
        self.restoreModelsCheck.setText(QCoreApplication.translate("sd_dreamer_main", u"Load face restore/upscale models", None))
        self.outputFolderSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.label_13.setText(QCoreApplication.translate("sd_dreamer_main", u"Stable diffusion model to use:", None))
        self.custCheckpointSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
        self.pyBinSelect.setText(QCoreApplication.translate("sd_dreamer_main", u"...", None))
#if QT_CONFIG(tooltip)
        self.outputFolderLine.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Where images will get output to", None))
#endif // QT_CONFIG(tooltip)
        self.outputFolderLine.setText("")
#if QT_CONFIG(tooltip)
        self.custCheckpointLine.setToolTip(QCoreApplication.translate("sd_dreamer_main", u"Select a model/checkpoint (.ckpt file)", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("sd_dreamer_main", u"Image output folder:", None))
        self.label_18.setText(QCoreApplication.translate("sd_dreamer_main", u"Python path (don't change):", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_6), QCoreApplication.translate("sd_dreamer_main", u"Settings", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("sd_dreamer_main", u"Tip: you can cycle through images with left and right arrow keys and scroll up and down with up/down keys. Holding down button/key repeat cycles through images\n"
"\n"
"'Enter' key activates 'Dream' button\n"
"\n"
"If you run out of VRAM, you don't need to restart the app or reload the model - just try again\n"
"\n"
"LatentSR seems not to work with current invoke-ai environment\n"
"\n"
"Hover over an item to get a tooltip\n"
"\n"
"Width, height fields can be edited with custom value\n"
"\n"
"Right click image in viewer to perform operations", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_8), QCoreApplication.translate("sd_dreamer_main", u"Help", None))
    # retranslateUi

