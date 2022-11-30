from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.profile import Profile
from file.file_manager import FileManager
from Engines.engineController import engineController
import os
import sys


class Game_Thread(QThread):
    deadSignal = pyqtSignal()
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.controller = None
        
    
    def setController(self, e : engineController)->None:
        self.controller = e		
  
    def run(self):
        print("game thread running")
        self.controller.run()
        self.stop()

    def stop(self):
        print("thread killed")
        self.deadSignal.emit()
        self.quit()


   


class Launcher(QMainWindow):
	def __init__(self, pager : QStackedWidget, manager: FileManager):
		super(Launcher,self).__init__()
		uic.loadUi(os.path.join("launcher","ui","launcher.ui"),baseinstance=self, resource_suffix='_rc')
		self.pager = pager
		self.controller = None
		self.game_thread = Game_Thread()
		self.game_thread.deadSignal.connect(lambda : sys.exit())
		self.storyButton = self.findChild(QRadioButton, "bt_story")
		self.endlessButton = self.findChild(QRadioButton, "bt_endless")
		self.vsButton = self.findChild(QRadioButton, "bt_vs")
		self.storyButton.setChecked(True)
		self.manager = manager
		# customization button setup
		self.customButton = self.findChild(QPushButton, "bt_custom")
		self.customButton.clicked.connect(lambda : self.pager.setCurrentIndex(self.pager.currentIndex()+1))

		#back button setup
		self.back_button = self.findChild(QToolButton, "bt_back")
		self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-1))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.back_button.setIcon(icon)

		self.playButton = self.findChild(QPushButton, "bt_play")
		self.playButton.clicked.connect(self.handlePlayButton)

		self.controls = None
		self.profile = None

	def handlePlayButton(self):
		self.pager.hide()
		assets, backgrounds = self.manager.load_assets()
		print(self.profile.get_controls())
		self.controller = engineController(settings=self.controls, profile= self.profile, assets = assets, backgrounds = backgrounds)
		self.game_thread.setController(self.controller)
		if self.storyButton.isChecked():
			#start vs mode
			
			print("story")
		elif self.endlessButton.isChecked():
			#start endless mode
			self.game_thread.start()
			print("endless")
		else:
			#start story mode
			print("vs")

	def catchProfile(self, s : Profile):
		self.profile = 	s

	def catchControls(self, c : dict):
		self.controls = c
		self.profile.set_controls(c)
		
		


