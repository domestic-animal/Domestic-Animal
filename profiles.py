from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from functools import partial

class Profiles(QMainWindow):
    
    profile_signal = pyqtSignal(str)
    
    def __init__(self, pager : QStackedWidget):
        super(Profiles,self).__init__()
        uic.loadUi("profiles.ui",baseinstance=self, resource_suffix='_rc')
        self.pager = pager
        
        self.findChild(QPushButton, "bt_continue").clicked.connect(self.handleContinue)
        
        self.layout = self.findChild(QGridLayout, "gridLayout")
        self.label = self.findChild(QLabel, "lb_feed")
        
        
        ##read the profiles
        self.profiles = ["ab","bc","f"]
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
            icon.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
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
        del self.profiles[i]
        self.setup_profiles()
        
    def handleCreate(self, i : int):
        self.create_buttons[i].setText("save")
        self.create_buttons[i].clicked.connect(partial(self.preformCreation, i))
        self.create_edit[i].show()
        
    def preformCreation(self, i: int):
        self.profiles.append(self.create_edit[i].text())
        '''
        save new profile here
        '''
        del self.create_buttons[i]
        del self.create_edit[i]
        self.setup_profiles()

    def handleContinue(self):
        flag = False
        for bt in self.radio_buttons:
            if bt.isChecked():
                self.pager.setCurrentIndex(self.pager.currentIndex()+1)
                self.profile_signal.emit(bt.text())
                flag = True
        if not flag:
            self.label.setText("Choose a profile first")
                    
	