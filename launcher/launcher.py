from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.profile import Profile
from file.file_manager import FileManager
from Engines.engineController import engineController
from launcher.customization import Customization
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
		self.game_thread.deadSignal.connect(lambda : sys.exit())
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
		# load assets
		assets, backgrounds = self.manager.load_assets()
		
		if self.storyButton.isChecked():
			#start vs mode
			
			print("story")
		elif self.endlessButton.isChecked():
			#start endless mode
			# for now the intialization is done here don't forget to move it up after loading the assets
			self.controller = engineController(settings = Customization.mapControls(self.profile.get_controls()),
                                     profile= self.profile, assets = assets, backgrounds = backgrounds)
			self.game_thread.setController(self.controller)
			self.game_thread.start()
			print("endless")
		else:
			#start story mode
			print("vs")

	def catchProfile(self, s : Profile):
		self.profile = 	s

	def catchControls(self, c : dict):
		self.profile.set_controls(c)
		self.manager.save_profile(self.profile)
		
		


