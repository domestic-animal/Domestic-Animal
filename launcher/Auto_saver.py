from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Engines.engineController import engineController
from file.gamestatesaver import GameStateSaver
import copy

class Auto_Save_Thread(QThread):
    
    deadSignal = pyqtSignal()

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.controller = None
        self.ThreadActive = True
        self.saver = GameStateSaver()
        
    '''
    a function that sets the engine controller
    paramter(e) : engineController instance
    '''
    def setController(self, e : engineController)->None:
        self.controller = e		
        self.name = self.controller.profile.get_name()
        self.mode = self.controller.mode
  
    def run(self):
        # thread's main function
        print("auto save started")
        self.mutex = QMutex() #mutex lock for synchronization safety
        while self.ThreadActive:
            self.msleep(2500)
            self.save()

        
    def save(self):
        self.mutex.lock()
        state = copy.deepcopy(self.controller.getGameState())
        self.mutex.unlock()
        if state is not None:
          if state.gameover == 0:
              self.saver.autosave_game_state(state, self.name, self.mode)
          else:
              self.saver.delete_autosaved_state(self.name, self.mode)



    def stop(self):
        # stop the thread on finish
        self.ThreadActive = False
        self.msleep(300)
        self.save()
        self.deadSignal.emit()
        print("auto save thread finished")
        self.quit()