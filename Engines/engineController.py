import pygame
import os
import sys
from Engines.levelSelector import levelSelector
from Engines.normalGameEngine import normalGameEngine
sys.path.insert(0, './assets_handler')

class engineController:

    def __init__(self,assets,profile,backgrounds, mode= -1,gameState = "game"):
        self.profile = profile
        self.lvlSelector = levelSelector()
        self.settings = profile.get_controls()
        self.states = []
        self.assets = assets
        self.mode = mode
        self.diff = 1
        self.gameState = gameState
        self.Background = backgrounds
        
    
    WIDTH, HEIGHT = 600, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
  
    def run(self):

        while True:
            
            self.switch()
            self.currEngine.start()
            break
            self.states = self.currEngine.getStates()




    def switch(self):
            if self.gameState == "game":
           #to be loaded from file manager
                PLAYER_SHIP_SKINS = self.assets[0]
                for i in PLAYER_SHIP_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                BULLET_SHIP_SKINS = self.assets[1]
                for i in BULLET_SHIP_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                ENEMY_SKINS = self.assets[2]
                for i in ENEMY_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                BG = self.Background[0]
                
            ##################
                print(self.settings)
                level = self.lvlSelector.getLevel(self.mode,self.diff,ENEMY_SKINS,BULLET_SHIP_SKINS)
                self.currEngine = normalGameEngine(self.WIN,level,self.diff,profile = self.profile,settings = self.settings,
                playerAssets= [PLAYER_SHIP_SKINS[0], BULLET_SHIP_SKINS[0]],enemyAssets=[ENEMY_SKINS[5]],gameAssets=[BG])
            elif self.gameState == "menu":
                self.currEngine = self.Engines[1]
            else:
                self.currEngine = self.Engine[2]

#e = engineController()
#e.run()