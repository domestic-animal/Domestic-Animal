from PyQt5 import QtCore, QtGui, QtWidgets
from customization import Customization
from profiles import Profiles
from launcher import Launcher
from file.file_manager import FileManager

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()
    manager = FileManager()
    
    ui = Launcher(widget)
    c = Customization(widget)
    p = Profiles(widget, manager)
    c.control_signal.connect(ui.catchControls)
    p.profile_signal.connect(ui.catchProfile)
    widget.addWidget(p)
    widget.addWidget(ui)
    widget.addWidget(c)
    widget.setFixedSize(800,600)
    widget.show()
    
    app.exec_()