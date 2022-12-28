# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Domestic-Animal\Domestic-Animal\launcher\ui\launcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:310.1, stop:0 rgba(136, 164, 124, 255))\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame{\n"
"background-color: transparent;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.frame.setStyleSheet("QWidget{\n"
"background-color: transparent;\n"
"}\n"
"QPushButton{\n"
"color: rgb(28, 49, 94);\n"
"border: 2px solid rgb(28, 49, 94);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(230, 226, 195);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(28, 49, 94);\n"
"}\n"
"QToolButton{\n"
"background-color: rgb(136, 164, 124);\n"
"border: 1px solid;\n"
"border-radius: 5px;\n"
"}\n"
"QToolButton::hover{\n"
"background-color: rgb(230, 226, 195);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_play = QtWidgets.QPushButton(self.frame)
        self.bt_play.setGeometry(QtCore.QRect(200, 160, 400, 75))
        self.bt_play.setObjectName("bt_play")
        self.bt_vs = QtWidgets.QRadioButton(self.frame)
        self.bt_vs.setGeometry(QtCore.QRect(520, 250, 81, 31))
        self.bt_vs.setObjectName("bt_vs")
        self.bt_endless = QtWidgets.QRadioButton(self.frame)
        self.bt_endless.setGeometry(QtCore.QRect(350, 250, 151, 31))
        self.bt_endless.setObjectName("bt_endless")
        self.bt_story = QtWidgets.QRadioButton(self.frame)
        self.bt_story.setGeometry(QtCore.QRect(200, 250, 141, 31))
        self.bt_story.setObjectName("bt_story")
        self.bt_custom = QtWidgets.QPushButton(self.frame)
        self.bt_custom.setGeometry(QtCore.QRect(200, 420, 400, 75))
        self.bt_custom.setObjectName("bt_custom")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 20, 811, 51))
        self.label.setStyleSheet("font-size: 30px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bt_back = QtWidgets.QToolButton(self.frame)
        self.bt_back.setGeometry(QtCore.QRect(0, 0, 71, 42))
        self.bt_back.setStyleSheet("")
        self.bt_back.setObjectName("bt_back")
        self.bt_saves = QtWidgets.QPushButton(self.frame)
        self.bt_saves.setGeometry(QtCore.QRect(200, 310, 400, 75))
        self.bt_saves.setObjectName("bt_saves")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_play.setText(_translate("MainWindow", "New Game"))
        self.bt_vs.setText(_translate("MainWindow", "VS"))
        self.bt_endless.setText(_translate("MainWindow", "Endless"))
        self.bt_story.setText(_translate("MainWindow", "Story"))
        self.bt_custom.setText(_translate("MainWindow", "Customize Controls"))
        self.label.setText(_translate("MainWindow", "Welcome to Domestic Animal"))
        self.bt_back.setText(_translate("MainWindow", "..."))
        self.bt_saves.setText(_translate("MainWindow", "Saved Games"))
