import os
import random
import string
from stat import S_IREAD, S_IWUSR
import filepath
from file_manager import FileManager
from profile import Profile

file_manager = FileManager()


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def remove_profiles():
    p_path = os.path.join(filepath.ROOT_DIR, "profiles", 'profiles.txt')
    os.chmod(p_path, S_IWUSR | S_IREAD)
    os.remove(p_path)


def test_file_creation():
    name = "name"
    file_manager.create_profile(name)
    path = os.path.join(filepath.ROOT_DIR, "profiles", name + '.txt')
    assert os.path.exists(path) and file_manager.get_profiles() == ["name"]
    file_manager.delete_profile("name")
    remove_profiles()


def test_file_creation_with_corrupted_profiles():
    p_path = os.path.join(filepath.ROOT_DIR, "profiles", "profiles.txt")
    with open(p_path, "w") as file:
        file.write("corrupted data")
    name = "name"
    file_manager.create_profile(name)
    path = os.path.join(filepath.ROOT_DIR, "profiles", name + '.txt')
    assert os.path.exists(path) and file_manager.get_profiles() == ["name"]
    file_manager.delete_profile("name")
    remove_profiles()


def test_profile_deletion():
    file_manager.create_profile("test")
    assert file_manager.delete_profile("test")
    remove_profiles()


def test_deletion_non_existed_profile():
    assert not file_manager.delete_profile("not_exist")


def test_profile_deletion_corrupted_profiles_index():
    file_manager.create_profile("delete")
    path = os.path.join(filepath.ROOT_DIR, "profiles", "profiles.txt")
    os.chmod(path, S_IWUSR | S_IREAD)
    with open(path, "w") as file:
        file.write("corrupted profiles")
    assert file_manager.delete_profile("delete")


def test_load_corrupted_profile():
    path = os.path.join(filepath.ROOT_DIR, "profiles", "corrupted.txt")
    with open(path, "w") as file:
        file.write("corrupted data")
    assert not file_manager.load_profile("corrupted")
    os.remove(path)


def test_load_corrupted_profiles_index():
    path = os.path.join(filepath.ROOT_DIR, "profiles", "profiles.txt")
    with open(path, "w") as file:
        file.write("corrupted profiles")
    assert not file_manager.get_profiles()
    os.remove(path)


def test_save_profile():
    p = file_manager.create_profile("testSave")
    p.set_story_progress(10)
    file_manager.save_profile(p)
    p1 = file_manager.load_profile("testSave")
    assert p1.get_story_progress() == 10
    file_manager.delete_profile("testSave")
    remove_profiles()


def test_save_non_existed_profile():
    p = Profile()
    p.set_name("testNotExist")
    p.set_story_progress(10)
    assert not file_manager.save_profile(p)


def test_editing_file():
    file_manager.create_profile("testEdit")
    path = os.path.join(filepath.ROOT_DIR, "profiles", "testEdit" + '.txt')
    try:
        with open(path, "w") as openfile:
            openfile.write("test edit file")
    except PermissionError:
        assert True
    file_manager.delete_profile("testEdit")
    remove_profiles()


def test_get_profiles():
    profiles = []
    for i in range(0, 5):
        p = random_string(5)
        profiles.append(p)
        file_manager.create_profile(p)
        assert file_manager.get_profiles().sort() == profiles.sort()
    for i in range(0, 5):
        p = profiles.pop()
        file_manager.delete_profile(p)
        assert file_manager.get_profiles().sort() == profiles.sort()
    remove_profiles()
