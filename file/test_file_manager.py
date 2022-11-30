import pytest
import os
import filepath
from file_manager import FileManager

def test_file_creation():
    file_manager = FileManager()
    name = "name"
    file_manager.create_profile(name)
    path = os.path.join(os.path.dirname(os.getcwd()), "profiles", name + '.txt')
    assert os.path.exists(path)
    os.remove(path)


def test_file_creation_profiles_dir_removed():
    os.remove(os.path.join(os.path.dirname(os.getcwd()), "profiles"))
    file_manager = FileManager()
    name = "name"
    file_manager.create_profile(name)
    path = os.path.join(os.path.dirname(os.getcwd()), "profiles", name + '.json')
    assert os.path.exists(path)
    os.remove(path)

def
