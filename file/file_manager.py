from assets_handler.assetsFactory import assetsFactory
from file.profile import Profile
import filepath
import os
import json
import pygame
from cryptography.fernet import Fernet, InvalidToken
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import shutil


class FileManager:
    def __init__(self):
        pass

    __p_dir = os.path.join(filepath.ROOT_DIR, "profiles")
    __fernet = Fernet(b'lBW8DUQf7LkNAuDhTGeBCPHfytQ6dJP7TjVTM5_KlwE=')

    def create_profile(self, name):
        """
        Creates new profile
        :param name: (str) username
        :return: object of class Profile if the profile is created successfully
        False otherwise
        """
        profile = Profile()
        profile.set_name(name)
        if not os.path.exists(self.__p_dir):
            os.mkdir(self.__p_dir)
        try:
            os.mkdir(os.path.join(self.__p_dir, name))
        except OSError:
            return False
        u_path = os.path.join(self.__p_dir,name , name + ".txt")
        if self.__write_file(profile.get_profile(), u_path):
            p_path = os.path.join(self.__p_dir, "profiles.txt")
            profiles = [name]
            if os.path.exists(p_path):
                p = self.__read_file("profiles")
                if p is not None and p != "C":
                    profiles = p["profiles"]
                    profiles.append(name)
            if profiles is None or not self.__write_file({"profiles": profiles}, p_path):
                self.delete_profile(name)
                return False
            return profile
        else:
            return False

    def save_profile(self, profile: Profile):
        """
        Saves the profile progress
        :param profile:  Profile object to save
        :return: True if profile is saved successfully
        False otherwise
        """
        u_path = os.path.join(self.__p_dir, profile.get_name(), profile.get_name() + ".txt")
        if not os.path.exists(u_path):
            return False
        new_profile = profile.get_profile()
        return self.__write_file(new_profile, u_path)

    def get_profiles(self):
        """
        Gets a list of current users
        :return: string list of the usernames
        """
        p_path = os.path.join(self.__p_dir, "profiles" + ".txt")
        if os.path.exists(p_path):
            profiles = self.__read_file("profiles")
            if profiles is None or profiles == "C":
                return False
            else:
                return profiles["profiles"]

    def delete_profile(self, name):
        """
        deletes a profile from available user profiles
        :param name: (str) username of the required profile
        :return: True if profile is deleted successfully
                 False otherwise
        """
        path = os.path.join(self.__p_dir, name, name + ".txt")
        if os.path.exists(path):
            try:
                os.chmod(path, S_IWUSR | S_IREAD)
                shutil.rmtree(os.path.join(self.__p_dir, name), ignore_errors=True)
            except OSError:
                return False
        p_path = os.path.join(self.__p_dir, "profiles" + ".txt")
        if os.path.exists(p_path):
            profiles = self.get_profiles()
            if profiles and name in profiles:
                profiles.remove(name)
                self.__write_file({"profiles": profiles}, p_path)
            return True
        return False

    def load_profile(self, name):
        """
        loads a profile from available user profiles
        :param name: (str) username of the required file
        :return: True if profile is loaded successfully
                 False otherwise
        """
        json_object = self.__read_file(os.path.join(name, name))
        if json_object is None or json_object == "C":
            return False
        profile = Profile()
        profile.set_profile(json_object)
        return profile

    def load_assets(self):
        """
        loads assests images
        :return: assets(list of Skin), backgrounds(list of Surface) 
        """
        factory=assetsFactory()
        PLAYER_SHIP_SKINS = factory.create_skins("ships",2.5)
        BULLET_SHIP_SKINS = factory.create_skins("bullets",1.2)
        ENEMY_SKINS = factory.create_skins("enemies",1.5)
        POWER_UP_SKINS = factory.create_skins("powerups",1.5)
        BOSSES_SKINS =  factory.create_skins("bosses")
        ENEMY_BULLET_SKINS = factory.create_skins("enemies_bullets")
        MUSIC = factory.create_music()
        assets = [PLAYER_SHIP_SKINS, BULLET_SHIP_SKINS, ENEMY_SKINS, POWER_UP_SKINS,BOSSES_SKINS,ENEMY_BULLET_SKINS,MUSIC]
        backgrounds = factory.create_backgrounds()
        return assets, backgrounds

    def __write_file(self, file, path):
        try:
            if os.path.exists(path):
                os.chmod(path, S_IWUSR | S_IREAD)
            with open(path, "wb") as outfile:
                json_object = json.dumps(file, indent=4)
                encrypted_file = self.__fernet.encrypt(json_object.encode())
                outfile.write(encrypted_file)
                os.chmod(path, S_IREAD | S_IRGRP | S_IROTH)
                return True
        except OSError:
            return False

    def __read_file(self, filename):
        try:
            with open(os.path.join(self.__p_dir, filename + ".txt"), 'rb') as openfile:
                file = self.__fernet.decrypt(openfile.read())
                json_object = json.loads(file.decode())
                return json_object
        except (InvalidToken, TypeError):
            return "C"
        except OSError:
            return None



