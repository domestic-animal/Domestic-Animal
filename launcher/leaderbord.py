from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from file.file_manager import FileManager
import os

ASC = False
DESC = True
SCORE = 0
TIME = 1

class Leaderboard(QMainWindow):
    def __init__(self, pager : QStackedWidget, manager : FileManager):
        super(Leaderboard,self).__init__()
        # intialize ui
        uic.loadUi(os.path.join("launcher","ui","leaderboard.ui"),baseinstance=self, resource_suffix='_rc')
        self.pager = pager
        self.manager = manager
        self.back_button = self.findChild(QToolButton, "bt_back")
        self.back_button.clicked.connect(lambda: self.pager.setCurrentIndex(self.pager.currentIndex()-3))
        # back button icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join("launcher","assets","back.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon)
        

        self.bt_sort = self.findChild(QToolButton, "bt_order")
        self.bt_sort.clicked.connect(self.handle_sort_button)
        self.combo = self.findChild(QComboBox, "combo")
        self.combo.currentIndexChanged.connect(self.change_criteria)


        self.order = ASC
        self.criteria = SCORE

        
        self.area = self.findChild(QScrollArea, 'scrollArea')
        self.layout = self.area.widget().layout()
        
    def setup_ui(self):
        temp = self.manager.get_profiles()
        if temp is False:
            return

        profiles = []

        for p in temp:
            profiles.append(self.manager.load_profile(p))
        
        if(self.bt_sort.text() == "↑"):
            self.order = ASC
        else:
            self.order = DESC

        if(self.criteria == SCORE):
            # sort by score
            profiles.sort(key = lambda p : p.get_endless_score(), reverse = self.order)
            
        else:
            # sort by time
            profiles.sort(key = lambda p : p.get_endless_survival_time(), reverse = self.order)
            

        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
        for i,p in enumerate(profiles):
            name = QLabel(str(p.get_name()))
            # name.setMinimumHeight(200)
            name.setAlignment(QtCore.Qt.AlignCenter)
            score = QLabel(str(p.get_endless_score()))
            # score.setMinimumHeight(200)
            score.setAlignment(QtCore.Qt.AlignCenter)
            time = QLabel(str(p.get_endless_survival_time()))
            # time.setMinimumHeight(200)
            time.setAlignment(QtCore.Qt.AlignCenter)
            self.layout.addWidget(name, i,0,i+1,1)
            self.layout.addWidget(score, i,1,i+1,2)
            self.layout.addWidget(time, i,2,i+1,3)

    def change_criteria(self):
        if self.combo.currentIndex() == 0:
            self.criteria = SCORE
        else:
            self.criteria = TIME
        self.setup_ui()

    def handle_sort_button(self):
        if(self.bt_sort.text() == "↑"):
            self.bt_sort.setText("↓")
        else:
            self.bt_sort.setText("↑")
        self.setup_ui()
