from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Engines.engineController import engineController

class Auto_Save_Thread(QThread):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.controller = None
        self.ThreadActive = True
        
    '''
    a function that sets the engine controller
    paramter(e) : engineController instance
    '''
    def setController(self, e : engineController)->None:
        self.controller = e		
  
    def run(self):
        # thread's main function
        print("auto save started")
        mutex = QMutex() #mutex lock for synchronization safety
        while self.ThreadActive:
            self.msleep(2500)
            mutex.lock()
            state = self.controller.getGameState()
            mutex.unlock()
            if state is not None:
                print(state.Score)

    def stop(self):
        # stop the thread on finish
        self.ThreadActive = False
        print("auto save thread finished")
        self.quit()