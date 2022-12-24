from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import os

class Leaderboard(QMainWindow):
    def __init__(self, pager : QStackedWidget):
        super(Leaderboard,self).__init__()
        # intialize ui
        uic.loadUi(os.path.join("launcher","ui","leaderboard.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager

        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-3))
        # back button icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)
        
        self.area = self.findChild(QScrollArea, 'scrollArea')
        
        
        self.area.widget().layout().addWidget(QLabel("new"), 2,0,3,1)