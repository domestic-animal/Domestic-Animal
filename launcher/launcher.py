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
        print("game thread finished")
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
		self.storyButton = self.findChild(QRadioButton, "bt_story")
		self.endlessButton = self.findChild(QRadioButton, "bt_endless")
		self.vsButton = self.findChild(QRadioButton, "bt_vs")
		self.storyButton.setChecked(True)
		
		# customization button setup
		self.findChild(QPushButton, "bt_custom").clicked.connect(
      		lambda : self.pager.setCurrentIndex(self.pager.currentIndex()+1))
  
		self.findChild(QPushButton, "bt_saves").clicked.connect(
      		lambda : self.pager.setCurrentIndex(self.pager.currentIndex()+2))

		self.findChild(QPushButton, "bt_leaderboard").clicked.connect(
      		lambda : self.pager.setCurrentIndex(self.pager.currentIndex()+3))

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
		self.startGame(mode)


	def catchProfile(self, s : Profile):
		self.profile = 	s

	def catchControls(self, c : dict, index: int):
		if index == 0:
			self.profile.set_controls(c)
		else:
			self.profile.set_co_player_controls(c)
		self.manager.save_profile(self.profile)

	def setup_threads(self, mode : int) -> None:
		if(self.game_thread.isFinished()):
			print("threads re-created")
			self.game_thread = Game_Thread()
			self.game_thread.deadSignal.connect(self.pager.show)
			if mode != 0:
				while(not self.auto_save.isFinished()):
					pass
				self.auto_save = Auto_Save_Thread()
				self.auto_save.deadSignal.connect(self.pager.widget(3).setup_view)

	def startGame(self, mode : int, state = None) -> None:
		# load assets
		assets, backgrounds = self.manager.load_assets()

		self.setup_threads(mode)
  
		self.controller = engineController(settings1 = Customization.mapControls(self.profile.get_controls()),
                                     profile= self.profile, assets = assets, backgrounds = backgrounds, mode=mode,
                                    filemanager= self.manager, settings2=Customization.mapControls(self.profile.get_co_player_controls()),
									gameState= state)

		self.game_thread.setController(self.controller)
		self.game_thread.start()
		if mode != 0:
			self.game_thread.deadSignal.connect(self.auto_save.stop)
			self.auto_save.setController(self.controller)
			self.auto_save.start()


	def catchSave(self, state: gameState): 
		if(state.level == -1):#endless
			self.startGame(-1, state)
		else:#story
			self.startGame(1, state)
		
		
		


