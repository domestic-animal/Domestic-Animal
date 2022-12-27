from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from launcher.customization import Customization
from launcher.profiles import Profiles
from launcher.launcher import Launcher
from launcher.saveUI import SaveUI
from file.file_manager import FileManager
from launcher.leaderbord import Leaderboard
import os


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.widget = QtWidgets.QStackedWidget()
        self.manager = FileManager()
        # widget.setWindowFlag(Qt.FramelessWindowHint); #for borderless window  
        self.ui = Launcher(self.widget, self.manager)
        self.c = Customization(self.widget)
        self.p = Profiles(self.widget, self.manager)
        self.save_ui = SaveUI(self.widget)
        self.l = Leaderboard(self.widget, self.manager)
        self.c.control_signal.connect(self.ui.catchControls)
        self.p.profile_signal.connect(self.ui.catchProfile)
        self.p.profile_signal.connect(self.c.getProfile)
        self.p.profile_signal.connect(self.save_ui.getProfile)
        self.ui.auto_save.deadSignal.connect(self.save_ui.setup_view)
        self.save_ui.load_signal.connect(self.ui.catchSave)
        self.ui.findChild(QPushButton, "bt_leaderboard").clicked.connect(self.l.setup_ui)
        self.widget.addWidget(self.p)
        self.widget.addWidget(self.ui)
        self.widget.addWidget(self.c)
        self.widget.addWidget(self.save_ui)
        self.widget.addWidget(self.l)
        self.widget.setFixedSize(800,600)
        self.widget.show()
    
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    id = QtGui.QFontDatabase.addApplicationFont(os.path.join("launcher","assets","game.ttf"))
    families = QtGui.QFontDatabase.applicationFontFamilies(id)
    font = QtGui.QFont(families[0], 16)
    app.setFont(font)
    gui = GUI()
    app.exec_()