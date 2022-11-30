import pygame
import os
import sys
from levelSelector import levelSelector
from normalGameEngine import normalGameEngine
from menueEngine import menu

sys.path.insert(0, './assets_handler')

# from skin import skin
from spritesheet import SpriteSheet


class engineController:

    def __init__(self, mode=-1, settings=None, fileManager=None, profile=None, gameState="menu"):
        self.profile = profile
        self.lvlSelector = levelSelector()
        self.states = []
        self.fileManager = fileManager
        self.settings = settings
        self.mode = mode
        self.diff = 1
        self.gameState = gameState

    WIDTH, HEIGHT = 600, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        while True:
            self.switch()
            self.currEngine.start()
            self.states = self.currEngine.getStates()

    def switch(self):
        if self.gameState == "game":
            # to be loaded from file manager
            player_sheet = pygame.image.load(os.path.join(".", "assets", "Ships_16x16_[8,2].png"))
            bullet_sheet = pygame.image.load(os.path.join(".", "assets", "Bullets_10x16_[4,2].png"))
            enemy_sheet = pygame.image.load(os.path.join(".", "assets", "Enemies_26x26_[6,2].png"))
            BG = pygame.image.load(os.path.join(".", "assets", "Backgrounds", "allBGstars_1024x1913.png"))
            PLAYER_SHIP_SKINS = SpriteSheet(player_sheet, 16, 16, 3, 2).skin
            BULLET_SHIP_SKINS = SpriteSheet(bullet_sheet, 10, 16, 1, 2).skin
            ENEMY_SKINS = SpriteSheet(enemy_sheet, 26, 26, 1, 2, 6).skin
            ##################
            level = self.lvlSelector.getLevel(self.mode, self.diff)
            self.currEngine = normalGameEngine(self.WIN, level, self.diff, profile=0,
                                               playerAssets=[PLAYER_SHIP_SKINS[0], BULLET_SHIP_SKINS[0]],
                                               enemyAssets=[ENEMY_SKINS[5]], gameAssets=[BG])
        elif self.gameState == "menu":
            pygame.init()
            self.currEngine = menu(self.WIN, self.WIDTH, self.HEIGHT)
            self.currEngine.create_menue(2)


        else:
            self.currEngine = self.Engine[2]


e = engineController()
e.run()
