import pygame
import os
import sys

from Engines.levelSelector import levelSelector
from Engines.normalGameEngine import normalGameEngine
from Engines.menueEngine import menu
sys.path.insert(0, './assets_handler')

"""Engine controller controls the flow of the game and 
chooses which engine to run either the menu Engine or the
game engine
    
"""
class engineController:

    def __init__(self,assets,profile,settings,backgrounds, mode= -1,gameState = "menu"):
        """Constructor

        Args:
            assets 2D skin list: all possible assets that can be loaded into the game
            profile (proflie object): user's profile
            settings (dictionary): player's controls
            backgrounds (pygame.image): backgrounds to be drawn
            mode (int, optional): game mode Defaults to -1 for endless.
            gameState (str, optional): controls whether we are in a menu or in a game Defaults to "menu".
        """
        self.profile = profile
        self.settings = settings
        self.assets = assets
        self.mode = mode
        self.gameState = gameState
        self.Background = backgrounds
        #level selector to select a certain level to load
        self.lvlSelector = levelSelector()
        # returned states from the engines
        self.states = ""
        #difficulity
        self.diff = 1
        #window to draw objects on
        self.WIDTH, self.HEIGHT = 600, 800
        self.WIN = pygame.display.set_mode(( self.WIDTH, self.HEIGHT))
        

    def run(self):
        """
            run function to run the engine controller to start the game
        """    
        ### Main logic loop ###
        while True:
            #draw a background
            self.WIN.blit(self.Background[1], (0, 0))
            #switch between engines
            self.switch()
            #start the selected engine
            self.states = self.currEngine.start()
            #get the new state
            self.gameState = self.states
            if self.states == "start":
                self.gameState = "game"
            if self.states == "runAway" :
                break
            

    def switch(self):
            """switching function to switch between game engines
            
            """
            ## if the game state is game 
            if self.gameState == "game":
                PLAYER_SHIP_SKINS = self.assets[0]
                BULLET_SHIP_SKINS = self.assets[1]
                ENEMY_SKINS = self.assets[2]
                self.convert(PLAYER_SHIP_SKINS,BULLET_SHIP_SKINS,ENEMY_SKINS)
                BG = self.Background[0]
                
            # get the chosen level from the level selector
                level = self.lvlSelector.getLevel(self.mode,self.diff,ENEMY_SKINS,BULLET_SHIP_SKINS)
            # assign the current Engine to be the normal game engine
                self.currEngine = normalGameEngine(window =self.WIN,level =level,
                diff = self.diff,profile = self.profile,settings1 = self.settings,
                playerAssets= [PLAYER_SHIP_SKINS[0], BULLET_SHIP_SKINS[0],PLAYER_SHIP_SKINS[3], BULLET_SHIP_SKINS[3]],
                enemyAssets=[ENEMY_SKINS[5]],gameAssets=[BG])
            
            #if the game state is opening a menu
            elif self.gameState == "menu":
                #assign the current engine to be the menu engine
                self.currEngine = menu(self.WIN, self.WIDTH, self.HEIGHT)
                #create the main menu
                self.currEngine.create_menue(2)

    def convert(self, PLAYER_SHIP_SKINS, BULLET_SHIP_SKINS,ENEMY_SKINS):
   ## convert all assets for optimizations
                for i in PLAYER_SHIP_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                for i in BULLET_SHIP_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                for i in ENEMY_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()


    def getGameState(self):
        if self.gameState == "game":
            return self.currEngine.getGameState()
        else:
            None