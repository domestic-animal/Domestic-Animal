from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from launcher.customization import Customization
from launcher.profiles import Profiles
from launcher.launcher import Launcher
from launcher.saveUI import SaveUI
from file.file_manager import FileManager
from launcher.leaderbord import Leaderboard
import os

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    id = QtGui.QFontDatabase.addApplicationFont(os.path.join("launcher","assets","game.ttf"))
    families = QtGui.QFontDatabase.applicationFontFamilies(id)
    font = QtGui.QFont(families[0], 16)
    app.setFont(font)
    widget = QtWidgets.QStackedWidget()
    manager = FileManager()
    # widget.setWindowFlag(Qt.FramelessWindowHint); #for borderless window  
    ui = Launcher(widget, manager)
    c = Customization(widget)
    p = Profiles(widget, manager)
    save_ui = SaveUI(widget)
    Leaderboard = Leaderboard(widget, manager)
    c.control_signal.connect(ui.catchControls)
    p.profile_signal.connect(ui.catchProfile)
    p.profile_signal.connect(c.getProfile)
    p.profile_signal.connect(save_ui.getProfile)
    ui.auto_save.deadSignal.connect(save_ui.setup_view)
    save_ui.load_signal.connect(ui.catchSave)
    widget.addWidget(p)
    widget.addWidget(ui)
    widget.addWidget(c)
    widget.addWidget(save_ui)
    widget.addWidget(Leaderboard)
    widget.setFixedSize(800,600)
    widget.show()
    
    app.exec_()