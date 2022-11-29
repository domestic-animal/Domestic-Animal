from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.profile import Profile
import os

class Customization(QMainWindow):
    control_signal = pyqtSignal(dict)

    def __init__(self, pager : QStackedWidget):
        super(Customization,self).__init__()
        
        uic.loadUi(os.path.join("launcher","ui","customization.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager

        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-1))
        
        self.findChild(QPushButton, "bt_save").clicked.connect(self.saveControls)
        self.feed_label = self.findChild(QLabel, "lb_feed")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)

    def saveControls(self):
        controls = {}
        controls["up"] = self.findChild(QComboBox, "combo_up").currentText()
        controls["down"] = self.findChild(QComboBox, "combo_down").currentText()
        controls["left"] = self.findChild(QComboBox, "combo_left").currentText()
        controls["right"] = self.findChild(QComboBox, "combo_right").currentText()
        controls["fire"]=self.findChild(QComboBox, "combo_fire").currentText()
        
        if(self.validateControls(controls)):
            self.feed_label.setText("Saved Sucessfully !")
            self.control_signal.emit(controls)
        else:
            self.feed_label.setText("Invalid. Controls must be unique.")


    def getProfile(self, p : Profile):
        controls = p.get_controls()
        if controls["up"] == "":
            self.findChild(QComboBox, "combo_up").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_down").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_left").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_right").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_fire").setCurrentIndex(0)
        else:
            self.findChild(QComboBox, "combo_up").setCurrentText(controls["up"])
            self.findChild(QComboBox, "combo_down").setCurrentText(controls["down"])
            self.findChild(QComboBox, "combo_left").setCurrentText(controls["left"])
            self.findChild(QComboBox, "combo_right").setCurrentText(controls["right"])
            self.findChild(QComboBox, "combo_fire").setCurrentText(controls["fire"])

        

    @staticmethod
    def validateControls(l : dict)->bool:
        s = set(l.get(elem) for elem in l)
        if len(l) == len(s):
            return True
        else:
            return False
    