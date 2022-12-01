from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.profile import Profile
import os
import pygame

class Customization(QMainWindow):
    control_signal = pyqtSignal(dict)

    def __init__(self, pager : QStackedWidget):
        super(Customization,self).__init__()
        # load ui and set pager to navigate between views
        uic.loadUi(os.path.join("launcher","ui","customization.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager

        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(self.back)
        
        self.findChild(QPushButton, "bt_save").clicked.connect(self.saveControls)
        self.feed_label = self.findChild(QLabel, "lb_feed")
        # load teh icon of the back button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)

    '''
    a method that handles the event of clicking on 'save' button
    '''
    def saveControls(self):
        controls = {}
        controls["up"] = self.findChild(QComboBox, "combo_up").currentText()
        controls["down"] = self.findChild(QComboBox, "combo_down").currentText()
        controls["left"] = self.findChild(QComboBox, "combo_left").currentText()
        controls["right"] = self.findChild(QComboBox, "combo_right").currentText()
        controls["fire"]=self.findChild(QComboBox, "combo_fire").currentText()
        
        if(self.validateControls(controls)):
            self.feed_label.setText("Saved Sucessfully !")
            self.control_signal.emit(controls)
        else:
            self.feed_label.setText("Invalid. Controls must be unique.")

    '''
    a function that setups the view of the controls once the profile is selected
    it loads controls set by the user or default values
    paramter(p) : the selected profile
    '''
    def getProfile(self, p : Profile):
        #load controls
        controls = p.get_controls()
        if controls["up"] == "":
            self.findChild(QComboBox, "combo_up").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_down").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_left").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_right").setCurrentIndex(0)
            self.findChild(QComboBox, "combo_fire").setCurrentIndex(0)
        else:
            self.findChild(QComboBox, "combo_up").setCurrentText(controls["up"])
            self.findChild(QComboBox, "combo_down").setCurrentText(controls["down"])
            self.findChild(QComboBox, "combo_left").setCurrentText(controls["left"])
            self.findChild(QComboBox, "combo_right").setCurrentText(controls["right"])
            self.findChild(QComboBox, "combo_fire").setCurrentText(controls["fire"])
        
    '''
    a function that handles the click on 'back' button
    '''    
    def back(self):
        self.feed_label.setText("")
        self.pager.setCurrentIndex(self.pager.currentIndex()-1)
        
    '''
    a function that handles the mapping between selected controls and pygame controls
    parameter(d) : controls dictionary
    returns the new mapped dictionary or a default value if no controls are set
    '''
    @staticmethod
    def mapControls(d : dict) -> dict:
        new_d = {}
        default = {"up" : pygame.K_UP, "down" : pygame.K_DOWN, 
                   "left" : pygame.K_LEFT, "right" : pygame.K_RIGHT, "fire" : pygame.K_SPACE}
        for key in d:
            val = f'K_{d[key]}'
            if val == "K_":
                return default
            new_d[key] = getattr(pygame, val)
        return new_d        


    '''
    a function that checks for duplicates in controls
    parameter(l) : controls dictionary
    returns true if controls are unique false otherwise
    '''
    @staticmethod
    def validateControls(l : dict)->bool:
        s = set(l.get(elem) for elem in l)
        if len(l) == len(s):
            return True
        else:
            return False
    