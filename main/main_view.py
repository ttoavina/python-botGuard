# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from main.main_controller import MainController


class Ui_MainWindow(object):
    
    def __init__(self):
        self.controller = MainController(self)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainCam = QtWidgets.QLabel(self.centralwidget)
        self.mainCam.setGeometry(QtCore.QRect(286, 12, 591, 501))
        self.mainCam.setObjectName("mainCam")
        self.config = QtWidgets.QGroupBox(self.centralwidget)
        self.config.setGeometry(QtCore.QRect(10, 10, 271, 131))
        self.config.setObjectName("config")
        self.splitter = QtWidgets.QSplitter(self.config)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 251, 101))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blurLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.blurLabel.setFont(font)
        self.blurLabel.setObjectName("blurLabel")
        self.horizontalLayout.addWidget(self.blurLabel)
        self.blurSpin = QtWidgets.QSpinBox(self.widget)
        self.blurSpin.setMaximum(1000)
        self.blurSpin.setProperty("value", 10)
        self.blurSpin.setObjectName("blurSpin")
        self.horizontalLayout.addWidget(self.blurSpin)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confMotionLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.confMotionLabel.setFont(font)
        self.confMotionLabel.setObjectName("confMotionLabel")
        self.horizontalLayout_2.addWidget(self.confMotionLabel)
        self.confMotionSpin = QtWidgets.QSpinBox(self.layoutWidget)
        self.confMotionSpin.setMaximum(100000)
        self.confMotionSpin.setProperty("value", 5000)
        self.confMotionSpin.setObjectName("confMotionSpin")
        self.horizontalLayout_2.addWidget(self.confMotionSpin)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modeLabel = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modeLabel.setFont(font)
        self.modeLabel.setObjectName("modeLabel")
        self.horizontalLayout_3.addWidget(self.modeLabel)
        self.radioButton = QtWidgets.QRadioButton(self.widget1)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.status = QtWidgets.QGroupBox(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 160, 271, 111))
        self.status.setObjectName("status")
        self.layoutWidget_2 = QtWidgets.QWidget(self.status)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 251, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fpsLabel = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setObjectName("fpsLabel")
        self.horizontalLayout_4.addWidget(self.fpsLabel)
        self.fpsNumber = QtWidgets.QLCDNumber(self.layoutWidget_2)
        self.fpsNumber.setObjectName("fpsNumber")
        self.horizontalLayout_4.addWidget(self.fpsNumber)
        self.layoutWidget_3 = QtWidgets.QWidget(self.status)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 60, 251, 30))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pixelLabel = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pixelLabel.setFont(font)
        self.pixelLabel.setObjectName("pixelLabel")
        self.horizontalLayout_5.addWidget(self.pixelLabel)
        self.intrusionNumber = QtWidgets.QLCDNumber(self.layoutWidget_3)
        self.intrusionNumber.setObjectName("intrusionNumber")
        self.horizontalLayout_5.addWidget(self.intrusionNumber)
        self.logList = QtWidgets.QListView(self.centralwidget)
        self.logList.setGeometry(QtCore.QRect(10, 280, 271, 241))
        self.logList.setObjectName("logList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.controller.load()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainCam.setText(_translate("MainWindow", "Chargement..."))
        self.config.setTitle(_translate("MainWindow", "Configuration"))
        self.blurLabel.setText(_translate("MainWindow", "Blur: "))
        self.confMotionLabel.setText(_translate("MainWindow", "Seuil: "))
        self.modeLabel.setText(_translate("MainWindow", "Mode : "))
        self.radioButton.setText(_translate("MainWindow", "Detection"))
        self.radioButton_2.setText(_translate("MainWindow", "Sourdine"))
        self.status.setTitle(_translate("MainWindow", "Status"))
        self.fpsLabel.setText(_translate("MainWindow", "FPS : "))
        self.pixelLabel.setText(_translate("MainWindow", "Pixel modifié: "))
