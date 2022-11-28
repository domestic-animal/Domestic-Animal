from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from functools import partial
from customization import Customization

class Launcher(QMainWindow):
	def __init__(self, pager : QStackedWidget):
		super(Launcher,self).__init__()
		uic.loadUi("launcher.ui",baseinstance=self, resource_suffix='_rc')
		self.pager = pager
		self.storyButton = self.findChild(QPushButton, "bt_story")
		self.storyButton.clicked.connect(partial(self.handleStartButton, "story"))
		self.findChild(QPushButton, "bt_endless").clicked.connect(partial(self.handleStartButton, "endless"))
		self.findChild(QPushButton, "bt_vs").clicked.connect(partial(self.handleStartButton, "vs"))
		


	def handleStartButton(self, type : str):
		if type == "vs":
			#start vs mode
			self.pager.setCurrentIndex(self.pager.currentIndex()+1)
			print("vs")
		elif type == "endless":
			#start endless mode
			print("endless")
		else:
			#start story mode
			print("story")
		

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()
    ui = Launcher(widget)
    c = Customization(widget)
    #c.control_signal.connect(ui.getControls)
    widget.addWidget(ui)
    widget.addWidget(c)
    widget.setFixedSize(800,600)
    widget.show()
    
    app.exec_()
