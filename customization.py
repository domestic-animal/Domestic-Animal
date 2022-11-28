from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

class Customization(QMainWindow):
    #control_signal = pyqtSignal(list)

    def __init__(self, pager : QStackedWidget):
        super(Customization,self).__init__()
        uic.loadUi("customization.ui",baseinstance=self, resource_suffix='_rc')
        self.pager = pager

        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-1))
        
        self.findChild(QPushButton, "bt_save").clicked.connect(self.saveControls)
        self.feed_label = self.findChild(QLabel, "lb_feed")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)

    def saveControls(self):
        controls = []
        controls.append(self.findChild(QComboBox, "combo_up").currentText())
        controls.append(self.findChild(QComboBox, "combo_down").currentText())
        controls.append(self.findChild(QComboBox, "combo_left").currentText())
        controls.append(self.findChild(QComboBox, "combo_right").currentText())
        controls.append(self.findChild(QComboBox, "combo_fire").currentText())
        
        if(self.validateControls(controls)):
            self.feed_label.setText("Saved Sucessfully !")
        else:
            self.feed_label.setText("Invalid. Controls must be unique.")

    @staticmethod
    def validateControls(l : list)->bool:
        if len(l) == len(set(l)):
            return True
        else:
            return False
    