import pygame
import os
import sys
from Engines.levelSelector import levelSelector
from Engines.normalGameEngine import normalGameEngine
from Engines.menueEngine import menu
sys.path.insert(0, './assets_handler')

class engineController:

    def __init__(self,assets,profile,settings,backgrounds, mode= -1,gameState = "menu"):
        self.profile = profile
        self.lvlSelector = levelSelector()
        self.settings = settings
        self.states = ""
        self.assets = assets
        self.mode = mode
        self.diff = 1
        self.gameState = gameState
        self.Background = backgrounds
        self.WIDTH, self.HEIGHT = 600, 800
        self.WIN = pygame.display.set_mode(( self.WIDTH, self.HEIGHT))
        
    
    def run(self):
        
        
        while True:
            self.WIN.blit(self.Background[1], (0, 0))
            self.switch()
            self.states = self.currEngine.start()
            self.gameState = self.states
            if self.states == "start":
                self.gameState = "game"
            if self.states == "runAway" :
                break
            

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
                self.currEngine = menu(self.WIN, self.WIDTH, self.HEIGHT)
                self.currEngine.create_menue(2)
            else:
                self.currEngine = self.Engine[2]

