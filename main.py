from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from launcher.customization import Customization
from launcher.profiles import Profiles
from launcher.launcher import Launcher
from file.file_manager import FileManager

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()
    manager = FileManager()
    # widget.setWindowFlag(Qt.FramelessWindowHint); #for borderless window  
    ui = Launcher(widget, manager)
    c = Customization(widget)
    p = Profiles(widget, manager)
    c.control_signal.connect(ui.catchControls)
    p.profile_signal.connect(ui.catchProfile)
    p.profile_signal.connect(c.getProfile)
    widget.addWidget(p)
    widget.addWidget(ui)
    widget.addWidget(c)
    widget.setFixedSize(800,600)
    widget.show()
    
    app.exec_()