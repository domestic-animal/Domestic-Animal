from assets_handler.spritesheet import SpriteSheet
from file.profile import Profile
import filepath
import os
import json
import pygame
from cryptography.fernet import Fernet


class FileManager:
    def __init__(self):
        pass

    __p_dir = os.path.join(filepath.ROOT_DIR, "projects")
    __fernet = Fernet(b'lBW8DUQf7LkNAuDhTGeBCPHfytQ6dJP7TjVTM5_KlwE=')

    def create_profile(self, name):
        """
        Creates new profile
        :param name: username
        :return: object of class Profile if the profile is created successfully
                 False otherwise
        """
        u_path = os.path.join(self.__p_dir, name + ".txt")
        profile = Profile()
        profile.set_name(name)
        file = self.__create_new_file(name)
        if not os.path.exists(self.__p_dir):
            os.mkdir(self.__p_dir)
        if self.__write_file(file, u_path):
            return profile
        else:
            return False

    def save_profile(self, profile: Profile):
        """
        Saves the profile progress
        :param profile (Profile): a profile to save
        :return: True if profile is saved successfully
                 False otherwise
        """
        u_path = os.path.join(self.__p_dir, profile.get_name() + ".txt")
        if not os.path.exists(u_path):
            return False
        new_profile = {
            "name": profile.get_name(),
            "achievements": profile.get_achievements(),
            "controls": profile.get_controls(),
            "story_progress": profile.get_story_progress(),
            "unlocked_weapons": profile.get_unlocked_weapons(),
            "current_weapon": profile.get_current_weapon(),
            "skins": profile.get_skins(),
            "current_skin": profile.get_current_skin()
        }
        return self.__write_file(new_profile, u_path)

    def get_profiles(self):
        """
        Gets a list of current users
        :return: string list of the usernames
        """
        if os.path.exists(self.__p_dir):
            profile_list = os.listdir(self.__p_dir)
            profile_list = [p.split('.')[0] for p in profile_list]
            return profile_list
        return False

    def delete_profile(self, name):
        """
        deletes a profile from available user profiles
        :param name(str): username of the required profile
        :return: True if profile is deleted successfully
                 False otherwise
        """
        path = os.path.join(self.__p_dir, name + ".txt")
        if os.path.exists(path):
            try:
                os.remove(path)
                return True
            except OSError:
                return False
        return False

    def load_profile(self, name):
        """
        loads a profile from available user profiles
        :param name(str): username of the required file
        :return: True if profile is loaded successfully
                 False otherwise
        """
        try:
            with open(os.path.join(self.__p_dir, name + ".txt"), 'rb') as openfile:
                file = self.__fernet.decrypt(openfile.read())
                json_object = json.loads(file.decode())
                print(json_object)
        except OSError:
            return False
        profile = Profile()
        profile.set_name(json_object["name"])
        profile.set_controls(json_object["controls"])
        profile.set_achievements(json_object["achievements"])
        profile.set_current_weapon(json_object["current_weapon"])
        profile.set_unlocked_weapons(json_object["unlocked_weapons"])
        profile.set_story_progress(json_object["story_progress"])
        profile.set_current_skin(json_object["current_skin"])
        profile.set_skins(json_object["skins"])
        return profile

    def load_assets(self):
        """
        loads assests images
        :return: assets(list of Skin), backgrounds(list of Surface) if loaded successfully
                 False otherwise
        """
        try:
            path = os.path.join(filepath.ROOT_DIR, "Assets")
            player_sheet = pygame.image.load(os.path.join(path, "Ships_16x16_[8,2].png"))
            bullet_sheet = pygame.image.load(os.path.join(path, "Bullets_10x16_[4,2].png"))
            enemy_sheet = pygame.image.load(os.path.join(path,  "Enemies_26x26_[6,2].png"))
            PLAYER_SHIP_SKINS = SpriteSheet(player_sheet, 16, 16, 3, 2).skin
            BULLET_SHIP_SKINS = SpriteSheet(bullet_sheet, 10, 16, 1.2, 2).skin
            ENEMY_SKINS = SpriteSheet(enemy_sheet, 26, 26, 1.75, 2, 6).skin
            assets = [PLAYER_SHIP_SKINS, BULLET_SHIP_SKINS, ENEMY_SKINS]
            background_imgs = ['allBGstars_1024x1913.png', 'fajrBG_1024x768.png',
                               'landscapeBG_384x224.png', 'nightBGwithmoon_1024x768.png',
                               'riverBG_256x320.png', 'spaceBG_256x224.png']
            backgrounds = []
            for img in background_imgs:
                b_path = os.path.join(path,"Backgrounds", img)
                BG = pygame.image.load(b_path)
                backgrounds.append(BG)
            return assets, backgrounds
        except OSError:
            return False

    def __create_new_file(self, name):
        """
        helper function to create new profile
        :param name(str): username
        :return: dict of with profile attributes
        """
        return {
            "name": name,
            "achievements": [],
            "controls": {"left": "", "right": "", "up": "", "down": "", "fire": ""},
            "story_progress": 0,
            "unlocked_weapons": [],
            "current_weapon": "",
            "skins": [],
            "current_skin": ""
        }

    def __write_file(self, file, path):
        try:
            with open(path, "wb") as outfile:
                json_object = json.dumps(file, indent=4)
                encrypted_file = self.__fernet.encrypt(json_object.encode())
                outfile.write(encrypted_file)
                return True
        except OSError:
            return False
