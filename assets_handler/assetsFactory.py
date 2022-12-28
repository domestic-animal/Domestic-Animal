import sys
sys.path.insert(0, './assets_handler')
from assets_handler.spritesheet import SpriteSheet
from assets_handler.music import Music
import filepath
import pygame
from pygame import mixer
import os
pygame.init()
mixer.init()

class assetsFactory:
    """
    The factory class for loading the assets - images and sounds
    """

    def __init__(self):
        self.path = os.path.abspath("Assets")   # The assets absolutePath
        print("path:", self.path)
        self.soundsPath = os.path.join(self.path, "Sounds")         # The sounds absolutePath

    def create_skins(self, asset, scale = 1, cooldown = 100):
        """
        This function creates the SpriteSheet object and
        >> Returns the 'skin' array (animation for game-engine)
        :param asset: String describing the assets wanted
        :param scale (optional): Scale to be adjusted
        :param cooldown (optional): Refresh rate for the animation in milliseconds
        """
        ss: SpriteSheet = None 
        if asset == "ships":
            SHIPS_IMAGE = pygame.image.load(os.path.join(self.path, "Ships_16x16_[8,2].png"))
            ss = SpriteSheet(SHIPS_IMAGE, 16, 16, scale, 2, 8, cooldown)

        elif asset == "bullets": # 4 sounds
            sounds = [  pygame.mixer.Sound(os.path.join(self.soundsPath, "pistonBullet.wav")),
                        pygame.mixer.Sound(os.path.join(self.soundsPath, "fireballBullet.wav")),
                        pygame.mixer.Sound(os.path.join(self.soundsPath, "electricBullet.wav")),
                        pygame.mixer.Sound(os.path.join(self.soundsPath, "rocketBullet.wav"))  ]
            BULLETS_IMAGE = pygame.image.load(os.path.join(self.path, "Bullets_10x16_[4,2].png"))
            ss = SpriteSheet(BULLETS_IMAGE, 10, 16, scale, 2, 4, cooldown, sounds)

        elif asset == "enemies": # 3 * 2 sounds
            sound1 = [pygame.mixer.Sound(os.path.join(self.soundsPath, "catDefeated.wav"))] * 2
            sound2 = [pygame.mixer.Sound(os.path.join(self.soundsPath, "dogDefeated.wav"))] * 2
            sound3 = [pygame.mixer.Sound(os.path.join(self.soundsPath, "mouseIndicator.wav"))] * 2
            sounds = sound1 + sound2 + sound3
            ENEMIES_IMAGE = pygame.image.load(os.path.join(self.path, "Enemies_26x26_[6,2].png"))
            ss = SpriteSheet(ENEMIES_IMAGE, 26, 26, scale, 2, 6, cooldown, sounds)

        elif asset == "powerups": # 1 * 5 sounds
            sounds = [pygame.mixer.Sound(os.path.join(self.soundsPath, "pickPowerup.wav"))] * 5
            POWERUPS_IMAGE = pygame.image.load(os.path.join(self.path, "Powerups_31x31_[5,2].png"))
            ss = SpriteSheet(POWERUPS_IMAGE, 31, 31, scale, 2, 5, cooldown, sounds)

        elif asset == "bosses":
            BOSSES_IMAGE = pygame.image.load(os.path.join(self.path, "Bosses_138x192_[2,6].png"))
            ss = SpriteSheet(BOSSES_IMAGE, 138, 192, scale, 6, 2, cooldown)

        elif asset == "enemies_bullets":
            ENEMIES_BULLETS_IMAGE = pygame.image.load(os.path.join(self.path, "EnemiesBullets_15x24_[4,3].png"))
            ss = SpriteSheet(ENEMIES_BULLETS_IMAGE, 15, 24, scale, 3, 4, cooldown)

        return ss.skin if ss != None else None


    def create_backgrounds(self):
        """
        Function to load & return the in-game backgrounds as array of pygame.image(s)
        """
        backgrounds = []
        path_of_backgrounds = os.path.join(self.path, "Backgrounds")

        for image in os.listdir(path_of_backgrounds):
            image_path = os.path.join(path_of_backgrounds, image)
            backgrounds.append(pygame.image.load(image_path)) # Loading the image & appending
        return backgrounds


    def create_images(self, asset, scale = 1):
        """
        This function creates the SpriteSheet object and
        >> Returns the 'skin' array (NO animation for menues & market)
        :param asset: String describing the assets wanted
        :param scale: Scale to be adjusted 
        """
        ss: SpriteSheet = None
        if asset == "buttons":
            BUTTONS_IMAGE = pygame.image.load(os.path.join(self.path, "Buttons_45x11_[24,1].png"))
            ss = SpriteSheet(BUTTONS_IMAGE, 45, 11, scale, 1, 24)

        elif asset == "ships":
            SHIPS_IMAGE = pygame.image.load(os.path.join(self.path, "Ships_16x16_[8,2].png"))
            ss = SpriteSheet(SHIPS_IMAGE, 16, 16, scale, 1, 8)

        elif asset == "bullets":
            BULLETS_IMAGE = pygame.image.load(os.path.join(self.path, "Bullets_10x16_[4,2].png"))
            ss = SpriteSheet(BULLETS_IMAGE, 10, 16, scale, 1, 4)

        elif asset == "powerups":
            POWERUPS_IMAGE = pygame.image.load(os.path.join(self.path, "Powerups_31x31_[5,2].png"))
            ss = SpriteSheet(POWERUPS_IMAGE, 31, 31, scale, 1, 5)

        elif asset == "logo":
            GAME_LOGO = pygame.image.load(os.path.join(self.path, "Domestic_Animals_logo_64x32.png"))
            ss = SpriteSheet(GAME_LOGO, 64, 32, scale, 1, 1)

        return ss.skin if ss != None else None

    def create_button_sound(self):
        return pygame.mixer.Sound(os.path.join(self.soundsPath, "buttonClick.wav"))

    def create_music(self):
        """
        Function to get the absolutePaths of music files
        and returns (the Music object) that holds the handling logic for playing music
        """
        music = []
        musicPath = os.path.join(self.path, "Music")
        for piece in os.listdir(musicPath):
            music.append(os.path.join(musicPath, piece))
        return Music(music)