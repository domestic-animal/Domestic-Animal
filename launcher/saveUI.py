from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.file_manager import FileManager
from Engines.gameState import gameState
import os

class SaveUI(QMainWindow):
    load_signal = pyqtSignal(gameState)
    def __init__(self, pager : QStackedWidget, manager: FileManager):
        super(SaveUI,self).__init__()
        # intialize ui
        uic.loadUi(os.path.join("launcher","ui","saves.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager
        self.manager = manager
        #back button setup
        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-2))
		# back button icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)
        
        
  
  