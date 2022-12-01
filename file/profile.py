
class Profile:

    __name = ""
    __controls = {"left": "", "right": "", "up": "", "down": "", "fire": ""}
    __achievements = []
    __story_progress = 0
    __unlocked_weapons = []
    __current_weapon = ""
    __skins = []
    __current_skin = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_controls(self, controls):
        self.__controls = controls

    def get_controls(self):
        return self.__controls

    def set_achievements(self, achievements):
        self.__achievements = achievements

    def get_achievements(self):
        return self.__achievements

    def set_story_progress(self, progress):
        self.__story_progress = progress

    def get_story_progress(self):
        return self.__story_progress

    def set_unlocked_weapons(self, unlocked_weapons):
        self.__unlocked_weapons = unlocked_weapons

    def get_unlocked_weapons(self):
        return self.__unlocked_weapons

    def set_current_weapon(self, current_weapon):
        self.__current_weapon = current_weapon

    def get_current_weapon(self):
        return self.__current_weapon

    def set_skins(self, skins):
        self.__skins = skins

    def get_skins(self):
        return self.__skins

    def set_current_skin(self, current_skin):
        self.__current_skin = current_skin

    def get_current_skin(self):
        return self.__current_skin

    def get_profile(self):
        return {
            "name": self.__name,
            "achievements": self.__achievements,
            "controls": self.__controls,
            "story_progress": self.__story_progress,
            "unlocked_weapons": self.__unlocked_weapons,
            "current_weapon": self.__current_weapon,
            "skins": self.__skins,
            "current_skin": self.__current_skin
        }

    def set_profile(self, json_object):
        self.__name = json_object["name"]
        self.__controls = json_object["controls"]
        self.__achievements = json_object["achievements"]
        self.__current_weapon = json_object["current_weapon"]
        self.__unlocked_weapons = json_object["unlocked_weapons"]
        self.__story_progress = json_object["story_progress"]
        self.__current_skin = json_object["current_skin"]
        self.__skins = json_object["skins"]


