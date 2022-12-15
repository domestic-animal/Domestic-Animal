from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.profile import Profile
from file.file_manager import FileManager
from Engines.engineController import engineController
from Engines.gameState import gameState
from launcher.customization import Customization
from launcher.Auto_saver import Auto_Save_Thread
import os
import sys

'''
A thread to run the game on
'''
class Game_Thread(QThread):
    deadSignal = pyqtSignal()
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.controller = None
        
    '''
    a function that sets the engine controller
    paramter(e) : engineController instance
    '''
    def setController(self, e : engineController)->None:
        self.controller = e		
  
    def run(self):
        # thread's main function
        print("game thread running")
        self.controller.run()
        self.stop()

    def stop(self):
        # stop the thread on finish
        print("thread killed")
        self.deadSignal.emit()
        self.quit()


   


class Launcher(QMainWindow):
	def __init__(self, pager : QStackedWidget, manager: FileManager):
		super(Launcher,self).__init__()
		# intialize ui
		uic.loadUi(os.path.join("launcher","ui","launcher.ui"),baseinstance=self, resource_suffix='_rc')
		# pager to navigate between views
		self.pager = pager
		self.controller = None # controller
		self.manager = manager # file manager
		self.game_thread = Game_Thread() # game thread
		self.auto_save = Auto_Save_Thread()# auto save thread
		self.game_thread.deadSignal.connect(self.pager.show)
		self.game_thread.deadSignal.connect(self.auto_save.stop)
		self.storyButton = self.findChild(QRadioButton, "bt_story")
		self.endlessButton = self.findChild(QRadioButton, "bt_endless")
		self.vsButton = self.findChild(QRadioButton, "bt_vs")
		self.storyButton.setChecked(True)
		
		# customization button setup
		self.customButton = self.findChild(QPushButton, "bt_custom")
		self.customButton.clicked.connect(lambda : self.pager.setCurrentIndex(self.pager.currentIndex()+1))

		#back button setup
		self.back_button = self.findChild(QToolButton, "bt_back")
		self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-1))
		# back button icon
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.back_button.setIcon(icon)

		self.playButton = self.findChild(QPushButton, "bt_play")
		self.playButton.clicked.connect(self.handlePlayButton)

		# the chosen profile
		self.profile = None

	'''
	a function that handles the event of click on 'play' button
 	'''
	def handlePlayButton(self):
		self.pager.hide()
		mode  = 0;
		if self.storyButton.isChecked():
			#start vs mode
			mode = 1
			print("story")
		elif self.endlessButton.isChecked():
			#start endless mode
			mode = -1
			print("endless")
		else:
			#start story mode
			mode = 0
			print("vs")

		# load assets
		assets, backgrounds = self.manager.load_assets()
  
		self.controller = engineController(settings1 = Customization.mapControls(self.profile.get_controls()),
                                     profile= self.profile, assets = assets, backgrounds = backgrounds, mode=mode,
                                    filemanager= self.manager, settings2=Customization.mapControls(self.profile.get_controls()))

		self.game_thread.setController(self.controller)
		self.game_thread.start()
		self.auto_save.setController(self.controller)
		self.auto_save.start()

	def catchProfile(self, s : Profile):
		self.profile = 	s

	def catchControls(self, c : dict, index: int):
		if index == 0:
			self.profile.set_controls(c)
		else:
			self.profile.set_co_player_controls(c)
		self.manager.save_profile(self.profile)
  
	def catchSave(self, state: gameState): 
		pass
		
		


