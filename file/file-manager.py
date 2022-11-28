from profile import Profile
import os
import json


class FileManager:
    __p_dir = os.path.join(os.path.dirname(os.getcwd()), "profiles")

    def create_profile(self, name):
        u_path = os.path.join(self.__p_dir, name + ".json")
        if os.path.exists(u_path):
            print("user_exists")
            return False
        profile = Profile()
        profile.set_name(name)
        file = self.__create_new_file(name)
        if not os.path.exists(self.__p_dir):
            os.mkdir(self.__p_dir)
        with open(u_path, "w") as outfile:
            json.dump(file, outfile)
        return profile

    def save_profile(self, profile: Profile):
        u_path = os.path.join(self.__p_dir, profile.get_name())
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
        with open(u_path, "w") as outfile:
            json.dump(new_profile, outfile)
        return True

    def get_profiles(self):
        if os.path.exists(self.__p_dir):
            profile_list = os.listdir(self.__p_dir)
            profile_list = [p.split('.')[0] for p in profile_list]
            return profile_list
        return False

    def delete_profile(self, name):
        path = os.path.join(self.__p_dir, name + ".json")
        if os.path.exists(path):
            os.remove(path)

    def load_profile(self, name):
        with open(os.path.join(self.__p_dir, name + ".json"), 'r') as openfile:
            json_object = json.load(openfile)
        profile = Profile()
        profile.set_name(json_object["name"])
        profile.set_controls(json_object["controls"])
        profile.set_achievements(json_object["achievements"])
        profile.set_current_weapon(json_object["current_weapon"])
        profile.set_unlocked_weapons(json_object["unlocked_weapons"])
        profile.set_story_progress(json_object["story_progress"])
        profile.set_current_skin(json_object["current_skin"])
        profile.set_skins(json_object["skins"])
        print(json_object)
        return profile

    def __create_new_file(self, name):
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






x2 = FileManager()
x2.create_profile("test")
x2.create_profile("i")
pi = x2.load_profile("test")
print(x2.get_profiles())
print(os.path.join(os.path.dirname(os.getcwd()), "profiles"))
