# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\study\third year\first term\software engineering\Domestic-Animal\customization.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_custom(object):
    def setupUi(self, custom):
        custom.setObjectName("custom")
        custom.setEnabled(True)
        custom.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(14)
        custom.setFont(font)
        custom.setStyleSheet("QPushButton{\n"
"    border: 5px solid;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(79, 255, 53);\n"
"    font: 16pt \"Purisa\";\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: red;\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: red;\n"
"    border: 10px solid green;\n"
"}\n"
"QLabel{\n"
"font: 16pt \"Purisa\";\n"
"}\n"
"QComboBox{\n"
"font: 16pt \"Purisa\";\n"
"}\n"
"QToolButton{\n"
"    background-color: black;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(custom)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 190, 671, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_7.setStyleSheet("border: 2px solid green;\n"
"border-radius: 3px;")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout.addWidget(self.comboBox_7, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.combo_down = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_down.setStyleSheet("border: 2px solid green;\n"
"border-radius: 3px;")
        self.combo_down.setObjectName("combo_down")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.combo_down.addItem("")
        self.gridLayout.addWidget(self.combo_down, 2, 2, 1, 1)
        self.combo_up = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_up.setStyleSheet("border: 2px solid green;\n"
"border-radius: 3px;")
        self.combo_up.setObjectName("combo_up")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.combo_up.addItem("")
        self.gridLayout.addWidget(self.combo_up, 1, 2, 1, 1)
        self.combo_left = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_left.setStyleSheet("border: 2px solid green;\n"
"border-radius: 3px;")
        self.combo_left.setObjectName("combo_left")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.combo_left.addItem("")
        self.gridLayout.addWidget(self.combo_left, 3, 2, 1, 1)
        self.combo_right = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_right.setStyleSheet("border: 2px solid green;\n"
"border-radius: 3px;")
        self.combo_right.setObjectName("combo_right")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.combo_right.addItem("")
        self.gridLayout.addWidget(self.combo_right, 4, 2, 1, 1)
        self.combo_fire = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_fire.setStyleSheet("border: 2px solid green;\n"
"border-radius: 3px;")
        self.combo_fire.setObjectName("combo_fire")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.combo_fire.addItem("")
        self.gridLayout.addWidget(self.combo_fire, 6, 2, 1, 1)
        self.bt_back = QtWidgets.QToolButton(custom)
        self.bt_back.setGeometry(QtCore.QRect(0, 0, 71, 42))
        self.bt_back.setObjectName("bt_back")
        self.lb_feed = QtWidgets.QLabel(custom)
        self.lb_feed.setGeometry(QtCore.QRect(150, 10, 421, 31))
        self.lb_feed.setText("")
        self.lb_feed.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_feed.setObjectName("lb_feed")
        self.bt_save = QtWidgets.QPushButton(custom)
        self.bt_save.setGeometry(QtCore.QRect(650, 10, 141, 41))
        self.bt_save.setStyleSheet("")
        self.bt_save.setObjectName("bt_save")

        self.retranslateUi(custom)
        QtCore.QMetaObject.connectSlotsByName(custom)

    def retranslateUi(self, custom):
        _translate = QtCore.QCoreApplication.translate
        custom.setWindowTitle(_translate("custom", "Form"))
        self.label_4.setText(_translate("custom", "Right"))
        self.label_2.setText(_translate("custom", "Fire"))
        self.label_3.setText(_translate("custom", "Up"))
        self.comboBox_7.setItemText(0, _translate("custom", "Player 1"))
        self.comboBox_7.setItemText(1, _translate("custom", "Player 2"))
        self.label_6.setText(_translate("custom", "Left"))
        self.label_5.setText(_translate("custom", "Down"))
        self.combo_down.setItemText(0, _translate("custom", "Arrow up"))
        self.combo_down.setItemText(1, _translate("custom", "Arrow down"))
        self.combo_down.setItemText(2, _translate("custom", "Arrow left"))
        self.combo_down.setItemText(3, _translate("custom", "Arrow right"))
        self.combo_down.setItemText(4, _translate("custom", "Q"))
        self.combo_down.setItemText(5, _translate("custom", "W"))
        self.combo_down.setItemText(6, _translate("custom", "E"))
        self.combo_down.setItemText(7, _translate("custom", "R"))
        self.combo_down.setItemText(8, _translate("custom", "T"))
        self.combo_down.setItemText(9, _translate("custom", "Y"))
        self.combo_down.setItemText(10, _translate("custom", "U"))
        self.combo_down.setItemText(11, _translate("custom", "I"))
        self.combo_down.setItemText(12, _translate("custom", "O"))
        self.combo_down.setItemText(13, _translate("custom", "P"))
        self.combo_down.setItemText(14, _translate("custom", "A"))
        self.combo_down.setItemText(15, _translate("custom", "S"))
        self.combo_down.setItemText(16, _translate("custom", "D"))
        self.combo_down.setItemText(17, _translate("custom", "F"))
        self.combo_down.setItemText(18, _translate("custom", "G"))
        self.combo_down.setItemText(19, _translate("custom", "H"))
        self.combo_down.setItemText(20, _translate("custom", "J"))
        self.combo_down.setItemText(21, _translate("custom", "K"))
        self.combo_down.setItemText(22, _translate("custom", "L"))
        self.combo_down.setItemText(23, _translate("custom", "M"))
        self.combo_down.setItemText(24, _translate("custom", "N"))
        self.combo_down.setItemText(25, _translate("custom", "B"))
        self.combo_down.setItemText(26, _translate("custom", "V"))
        self.combo_down.setItemText(27, _translate("custom", "C"))
        self.combo_down.setItemText(28, _translate("custom", "X"))
        self.combo_down.setItemText(29, _translate("custom", "Z"))
        self.combo_down.setItemText(30, _translate("custom", "Space"))
        self.combo_down.setItemText(31, _translate("custom", "LCTRL"))
        self.combo_down.setItemText(32, _translate("custom", "LALT"))
        self.combo_down.setItemText(33, _translate("custom", "RCTRL"))
        self.combo_down.setItemText(34, _translate("custom", "RALT"))
        self.combo_down.setItemText(35, _translate("custom", "LSHIFT"))
        self.combo_up.setItemText(0, _translate("custom", "Arrow up"))
        self.combo_up.setItemText(1, _translate("custom", "Arrow down"))
        self.combo_up.setItemText(2, _translate("custom", "Arrow left"))
        self.combo_up.setItemText(3, _translate("custom", "Arrow right"))
        self.combo_up.setItemText(4, _translate("custom", "Q"))
        self.combo_up.setItemText(5, _translate("custom", "W"))
        self.combo_up.setItemText(6, _translate("custom", "E"))
        self.combo_up.setItemText(7, _translate("custom", "R"))
        self.combo_up.setItemText(8, _translate("custom", "T"))
        self.combo_up.setItemText(9, _translate("custom", "Y"))
        self.combo_up.setItemText(10, _translate("custom", "U"))
        self.combo_up.setItemText(11, _translate("custom", "I"))
        self.combo_up.setItemText(12, _translate("custom", "O"))
        self.combo_up.setItemText(13, _translate("custom", "P"))
        self.combo_up.setItemText(14, _translate("custom", "A"))
        self.combo_up.setItemText(15, _translate("custom", "S"))
        self.combo_up.setItemText(16, _translate("custom", "D"))
        self.combo_up.setItemText(17, _translate("custom", "F"))
        self.combo_up.setItemText(18, _translate("custom", "G"))
        self.combo_up.setItemText(19, _translate("custom", "H"))
        self.combo_up.setItemText(20, _translate("custom", "J"))
        self.combo_up.setItemText(21, _translate("custom", "K"))
        self.combo_up.setItemText(22, _translate("custom", "L"))
        self.combo_up.setItemText(23, _translate("custom", "M"))
        self.combo_up.setItemText(24, _translate("custom", "N"))
        self.combo_up.setItemText(25, _translate("custom", "B"))
        self.combo_up.setItemText(26, _translate("custom", "V"))
        self.combo_up.setItemText(27, _translate("custom", "C"))
        self.combo_up.setItemText(28, _translate("custom", "X"))
        self.combo_up.setItemText(29, _translate("custom", "Z"))
        self.combo_up.setItemText(30, _translate("custom", "Space"))
        self.combo_up.setItemText(31, _translate("custom", "LCTRL"))
        self.combo_up.setItemText(32, _translate("custom", "LALT"))
        self.combo_up.setItemText(33, _translate("custom", "RCTRL"))
        self.combo_up.setItemText(34, _translate("custom", "RALT"))
        self.combo_up.setItemText(35, _translate("custom", "LSHIFT"))
        self.combo_left.setItemText(0, _translate("custom", "Arrow up"))
        self.combo_left.setItemText(1, _translate("custom", "Arrow down"))
        self.combo_left.setItemText(2, _translate("custom", "Arrow left"))
        self.combo_left.setItemText(3, _translate("custom", "Arrow right"))
        self.combo_left.setItemText(4, _translate("custom", "Q"))
        self.combo_left.setItemText(5, _translate("custom", "W"))
        self.combo_left.setItemText(6, _translate("custom", "E"))
        self.combo_left.setItemText(7, _translate("custom", "R"))
        self.combo_left.setItemText(8, _translate("custom", "T"))
        self.combo_left.setItemText(9, _translate("custom", "Y"))
        self.combo_left.setItemText(10, _translate("custom", "U"))
        self.combo_left.setItemText(11, _translate("custom", "I"))
        self.combo_left.setItemText(12, _translate("custom", "O"))
        self.combo_left.setItemText(13, _translate("custom", "P"))
        self.combo_left.setItemText(14, _translate("custom", "A"))
        self.combo_left.setItemText(15, _translate("custom", "S"))
        self.combo_left.setItemText(16, _translate("custom", "D"))
        self.combo_left.setItemText(17, _translate("custom", "F"))
        self.combo_left.setItemText(18, _translate("custom", "G"))
        self.combo_left.setItemText(19, _translate("custom", "H"))
        self.combo_left.setItemText(20, _translate("custom", "J"))
        self.combo_left.setItemText(21, _translate("custom", "K"))
        self.combo_left.setItemText(22, _translate("custom", "L"))
        self.combo_left.setItemText(23, _translate("custom", "M"))
        self.combo_left.setItemText(24, _translate("custom", "N"))
        self.combo_left.setItemText(25, _translate("custom", "B"))
        self.combo_left.setItemText(26, _translate("custom", "V"))
        self.combo_left.setItemText(27, _translate("custom", "C"))
        self.combo_left.setItemText(28, _translate("custom", "X"))
        self.combo_left.setItemText(29, _translate("custom", "Z"))
        self.combo_left.setItemText(30, _translate("custom", "Space"))
        self.combo_left.setItemText(31, _translate("custom", "LCTRL"))
        self.combo_left.setItemText(32, _translate("custom", "LALT"))
        self.combo_left.setItemText(33, _translate("custom", "RCTRL"))
        self.combo_left.setItemText(34, _translate("custom", "RALT"))
        self.combo_left.setItemText(35, _translate("custom", "LSHIFT"))
        self.combo_right.setItemText(0, _translate("custom", "Arrow up"))
        self.combo_right.setItemText(1, _translate("custom", "Arrow down"))
        self.combo_right.setItemText(2, _translate("custom", "Arrow left"))
        self.combo_right.setItemText(3, _translate("custom", "Arrow right"))
        self.combo_right.setItemText(4, _translate("custom", "Q"))
        self.combo_right.setItemText(5, _translate("custom", "W"))
        self.combo_right.setItemText(6, _translate("custom", "E"))
        self.combo_right.setItemText(7, _translate("custom", "R"))
        self.combo_right.setItemText(8, _translate("custom", "T"))
        self.combo_right.setItemText(9, _translate("custom", "Y"))
        self.combo_right.setItemText(10, _translate("custom", "U"))
        self.combo_right.setItemText(11, _translate("custom", "I"))
        self.combo_right.setItemText(12, _translate("custom", "O"))
        self.combo_right.setItemText(13, _translate("custom", "P"))
        self.combo_right.setItemText(14, _translate("custom", "A"))
        self.combo_right.setItemText(15, _translate("custom", "S"))
        self.combo_right.setItemText(16, _translate("custom", "D"))
        self.combo_right.setItemText(17, _translate("custom", "F"))
        self.combo_right.setItemText(18, _translate("custom", "G"))
        self.combo_right.setItemText(19, _translate("custom", "H"))
        self.combo_right.setItemText(20, _translate("custom", "J"))
        self.combo_right.setItemText(21, _translate("custom", "K"))
        self.combo_right.setItemText(22, _translate("custom", "L"))
        self.combo_right.setItemText(23, _translate("custom", "M"))
        self.combo_right.setItemText(24, _translate("custom", "N"))
        self.combo_right.setItemText(25, _translate("custom", "B"))
        self.combo_right.setItemText(26, _translate("custom", "V"))
        self.combo_right.setItemText(27, _translate("custom", "C"))
        self.combo_right.setItemText(28, _translate("custom", "X"))
        self.combo_right.setItemText(29, _translate("custom", "Z"))
        self.combo_right.setItemText(30, _translate("custom", "Space"))
        self.combo_right.setItemText(31, _translate("custom", "LCTRL"))
        self.combo_right.setItemText(32, _translate("custom", "LALT"))
        self.combo_right.setItemText(33, _translate("custom", "RCTRL"))
        self.combo_right.setItemText(34, _translate("custom", "RALT"))
        self.combo_right.setItemText(35, _translate("custom", "LSHIFT"))
        self.combo_fire.setItemText(0, _translate("custom", "Arrow up"))
        self.combo_fire.setItemText(1, _translate("custom", "Arrow down"))
        self.combo_fire.setItemText(2, _translate("custom", "Arrow left"))
        self.combo_fire.setItemText(3, _translate("custom", "Arrow right"))
        self.combo_fire.setItemText(4, _translate("custom", "Q"))
        self.combo_fire.setItemText(5, _translate("custom", "W"))
        self.combo_fire.setItemText(6, _translate("custom", "E"))
        self.combo_fire.setItemText(7, _translate("custom", "R"))
        self.combo_fire.setItemText(8, _translate("custom", "T"))
        self.combo_fire.setItemText(9, _translate("custom", "Y"))
        self.combo_fire.setItemText(10, _translate("custom", "U"))
        self.combo_fire.setItemText(11, _translate("custom", "I"))
        self.combo_fire.setItemText(12, _translate("custom", "O"))
        self.combo_fire.setItemText(13, _translate("custom", "P"))
        self.combo_fire.setItemText(14, _translate("custom", "A"))
        self.combo_fire.setItemText(15, _translate("custom", "S"))
        self.combo_fire.setItemText(16, _translate("custom", "D"))
        self.combo_fire.setItemText(17, _translate("custom", "F"))
        self.combo_fire.setItemText(18, _translate("custom", "G"))
        self.combo_fire.setItemText(19, _translate("custom", "H"))
        self.combo_fire.setItemText(20, _translate("custom", "J"))
        self.combo_fire.setItemText(21, _translate("custom", "K"))
        self.combo_fire.setItemText(22, _translate("custom", "L"))
        self.combo_fire.setItemText(23, _translate("custom", "M"))
        self.combo_fire.setItemText(24, _translate("custom", "N"))
        self.combo_fire.setItemText(25, _translate("custom", "B"))
        self.combo_fire.setItemText(26, _translate("custom", "V"))
        self.combo_fire.setItemText(27, _translate("custom", "C"))
        self.combo_fire.setItemText(28, _translate("custom", "X"))
        self.combo_fire.setItemText(29, _translate("custom", "Z"))
        self.combo_fire.setItemText(30, _translate("custom", "Space"))
        self.combo_fire.setItemText(31, _translate("custom", "LCTRL"))
        self.combo_fire.setItemText(32, _translate("custom", "LALT"))
        self.combo_fire.setItemText(33, _translate("custom", "RCTRL"))
        self.combo_fire.setItemText(34, _translate("custom", "RALT"))
        self.combo_fire.setItemText(35, _translate("custom", "LSHIFT"))
        self.bt_back.setText(_translate("custom", "..."))
        self.bt_save.setText(_translate("custom", "Save"))