from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pytest
from main import GUI


@pytest.fixture
def app(qtbot):
    test = GUI()
    qtbot.addWidget(test)

    return test


def test_continue_button_after_click(app, qtbot):
    qtbot.mouseClick(app.p.findChild(QPushButton, "bt_continue"), QtCore.Qt.LeftButton)
    assert app.p.lb_feed.text() == "Choose a profile first"
    
    
def test_profile_creation(app, qtbot):
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    qtbot.keyPress(app.p.create_edit[0], QtCore.Qt.Key.Key_W)
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    flag = False
    for b in app.p.radio_buttons:
        if b.text() == "w":
            flag = True
    assert flag
    
def test_empty_profile_name(app, qtbot):
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    assert app.p.lb_feed.text() == "Empty names not allowed"
    
def test_duplicate_profile(app, qtbot):
    # create first profile
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    qtbot.keyPress(app.p.create_edit[0], QtCore.Qt.Key.Key_Z)
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    
    #try to create second prfoile
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    qtbot.keyPress(app.p.create_edit[0], QtCore.Qt.Key.Key_Z)
    qtbot.mouseClick(app.p.create_buttons[0], QtCore.Qt.LeftButton)
    
    assert app.p.lb_feed.text() == "profile already exists"