from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.gamestatesaver import GameStateSaver
from file.profile import Profile
from Engines.gameState import gameState
import os

class SaveUI(QMainWindow):
    load_signal = pyqtSignal(gameState)
    def __init__(self, pager : QStackedWidget):
        super(SaveUI,self).__init__()
        # intialize ui
        uic.loadUi(os.path.join("launcher","ui","saves.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager
        #back button setup
        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-2))
		# back button icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","start.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.loader = GameStateSaver()
        
        for i in range(1,4):
            self.findChild(QToolButton, f'start{i}').setIcon(icon2)
            self.findChild(QToolButton, f'start{i}').setIconSize(QSize(120,60))
            self.findChild(QToolButton, f'start{i}').clicked.connect(partial(self.handle_choose_save,i))  
              
            
    def setup_view(self)->None:
        print("updating save ui")
        self.states = []
        self.states.append(self.loader.load_saved_story(self.profile.get_name()))
        self.states.append(self.loader.load_autosaved_story(self.profile.get_name()))
        self.states.append(self.loader.load_autosaved_endless(self.profile.get_name()))
        
        for i, state in enumerate(self.states):
            if state is None:
                self.findChild(QLabel, f'title{i+1}').hide()
                self.findChild(QWidget, f'line{i+1}').hide()
                self.findChild(QToolButton, f'start{i+1}').hide()
                self.findChild(QLabel, f'save{i+1}_crash').setText("")
                self.findChild(QLabel, f'save{i+1}_date').setText("")
                self.findChild(QLabel, f'save{i+1}_info').setText("")
            else:
                self.findChild(QLabel, f'title{i+1}').show()
                self.findChild(QWidget, f'line{i+1}').show()
                self.findChild(QToolButton, f'start{i+1}').show()
                self.findChild(QLabel, f'save{i+1}_date').setText(f"time: {state.time}")
                self.findChild(QLabel, f'save{i+1}_info').setText(f"score : {state.Score}")
                if state.isExit == 0:
                    self.findChild(QLabel, f'save{i+1}_crash').setText("crash")
                else:
                    self.findChild(QLabel, f'save{i+1}_crash').setText("")
                
                if state.level != -1:
                    self.findChild(QLabel, f'title{i+1}').setText(f'story   (level {state.level})')
        
  
    def handle_choose_save(self, i : int) -> None:
        self.pager.setCurrentIndex(1)
        self.pager.hide()
        self.load_signal.emit(self.states[i-1])
        
    def getProfile(self, p : Profile) -> None:
        self.profile = p
        self.setup_view()