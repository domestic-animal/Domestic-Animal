import unittest
import os
from file_manager import FileManager


class FileManagerTest(unittest.TestCase):

    def test_file_creation(self):
        file_manager = FileManager()
        name = "name"
        file_manager.create_profile(name)
        path = os.path.join(os.path.dirname(os.getcwd()), "profiles", name + '.json')
        self.assertTrue(os.path.exists(path), "creation Failed")
        os.remove(path)

    def test_file_creation_profiles_dir_removed(self):
        os.remove(os.path.join(os.path.dirname(os.getcwd()), "profiles"))
        file_manager = FileManager()
        name = "name"
        file_manager.create_profile(name)
        path = os.path.join(os.path.dirname(os.getcwd()), "profiles", name + '.json')
        self.assertTrue(os.path.exists(path), "creation Failed")
        os.remove(path)


if __name__ == '__main__':
    unittest.main()
