from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from functools import partial
from file.profile import Profile
from file.file_manager import FileManager
import os

class Profiles(QMainWindow):
    
    profile_signal = pyqtSignal(Profile)
    
    def __init__(self, pager : QStackedWidget, manager : FileManager):
        super(Profiles,self).__init__()
        uic.loadUi(os.path.join("launcher","ui","profiles.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager
        self.fileManager = manager
        self.findChild(QPushButton, "bt_continue").clicked.connect(self.handleContinue)
        
        self.layout = self.findChild(QGridLayout, "gridLayout")
        self.label = self.findChild(QLabel, "lb_feed")
        
        
        ##read the profiles
        self.profiles = self.fileManager.get_profiles()
        if self.profiles is False or self.profiles is None:
            self.profiles = []
        self.setup_profiles()
        
    def setup_profiles(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
            
        self.create_buttons = []
        self.create_edit = []
        self.radio_buttons = []
            
            
        for i,elem in enumerate(self.profiles):
            bt = QRadioButton()
            bt.setText(elem)
            delete_bt = QToolButton()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
            delete_bt.setIcon(icon)
            delete_bt.clicked.connect(partial(self.handleDelete, i))
            self.radio_buttons.append(bt)
            self.layout.addWidget(bt, i,0,i+1,1)
            self.layout.addWidget(delete_bt, i,1,i+1,2)
            
        for i in range(len(self.profiles),5):
            bt = QPushButton()
            bt.setText("Create Profile")
            bt.setMinimumHeight(65)
            e = QLineEdit()
            e.setMinimumHeight(65)
            e.setMaxLength(10)
            e.setAlignment(Qt.AlignLeft)
            e.hide()
            bt.clicked.connect(partial(self.handleCreate, len(self.create_buttons)))
            self.create_buttons.append(bt)
            self.create_edit.append(e)
            self.layout.addWidget(bt, i,0,i+1,1)
            self.layout.addWidget(e, i,1,i+1,2)
            
    def handleDelete(self, i : int):
        self.fileManager.delete_profile(self.profiles[i])
        del self.profiles[i]
        self.setup_profiles()
        
    def handleCreate(self, i : int):
        self.create_buttons[i].setText("save")
        self.create_buttons[i].clicked.connect(partial(self.preformCreation, i))
        self.create_edit[i].show()
        
    def preformCreation(self, i: int):
        name = self.create_edit[i].text()
        
        
        
        if len(name) == 0:
            self.label.setText("Empty names not allowed")
            return
        if name  in self.profiles:
            self.label.setText("profile already exists")
            return
        
        p = self.fileManager.create_profile(name)
        if p is False:
            self.label.setText("error while creation")
            return
        if self.fileManager.save_profile(p) is False:
            self.label.setText("error while saving")
            return
        
        self.profiles.append(name)
        del self.create_buttons[i]
        del self.create_edit[i]
        self.setup_profiles()

    def handleContinue(self):
        flag = False
        for bt in self.radio_buttons:
            if bt.isChecked():
                self.pager.setCurrentIndex(self.pager.currentIndex()+1)
                p = self.fileManager.load_profile(bt.text())
                # handle errors
                if p is False:
                    self.label.setText("error while loading")
                    return
                self.profile_signal.emit(p)
                flag = True
        if not flag:
            self.label.setText("Choose a profile first")
                    
	