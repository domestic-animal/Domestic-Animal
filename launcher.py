from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from profile import Profile


class Launcher(QMainWindow):
	def __init__(self, pager : QStackedWidget):
		super(Launcher,self).__init__()
		uic.loadUi("launcher.ui",baseinstance=self, resource_suffix='_rc')
		self.pager = pager
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
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.back_button.setIcon(icon)

		self.playButton = self.findChild(QPushButton, "bt_play")
		self.playButton.clicked.connect(self.handlePlayButton)

		self.controls = None
		self.profile = None

	def handlePlayButton(self):
		if self.storyButton.isChecked():
			#start vs mode
			
			print("story")
		elif self.endlessButton.isChecked():
			#start endless mode
			print("endless")
		else:
			#start story mode
			print("vs")

	def catchProfile(self, s : Profile):
		self.profile = 	s
		print(self.profile.get_name())

	def catchControls(self, c : dict):
		self.controls = c
		print(self.controls)
		
		


