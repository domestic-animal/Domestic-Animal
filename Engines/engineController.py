import pygame
import sys

from Engines.levelSelector import levelSelector
from Engines.normalGameEngine import normalGameEngine
from Engines.menueEngine import menu
from Engines.vsEngine import vsGameEngine
sys.path.insert(0, './assets_handler')

"""Engine controller controls the flow of the game and 
chooses which engine to run either the menu Engine or the
game engine
    
"""
class engineController:

    def __init__(self,assets,profile,filemanager,settings1,settings2,backgrounds, mode= 0,gameState=None):
        """Constructor

        Args:
            assets 2D skin list: all possible assets that can be loaded into the game
            profile (proflie object): user's profile
            settings (dictionary): player's controls
            backgrounds (pygame.image): backgrounds to be drawn
            mode (int, optional): game mode Defaults to -1 for endless.
            gameState (str, optional): controls whether we are in a menu or in a game Defaults to "menu".
        """
        self.filemanager = filemanager
        self.profile = profile
        self.settings1 = settings1
        self.settings2 = settings2
        self.assets = assets
        self.mode = mode
        self.controllerState = "menu"
        self.Background = backgrounds
        #level selector to select a certain level to load
        self.lvlSelector = levelSelector()
        # returned states from the engines
        self.gameStateLOADED=gameState
        if(self.gameStateLOADED != None):
            self.controllerState = "game"
        self.gameState = None
        self.states = []
        #difficulity
        self.diff = 1
        #window to draw objects on
        self.WIDTH, self.HEIGHT = 600, 800
        self.WIN = pygame.display.set_mode(( self.WIDTH, self.HEIGHT),pygame.RESIZABLE)
        pygame.init()
        

    def run(self):
        """
            run function to run the engine controller to start the game
        """    
        ### Main logic loop ###
        while True:
            #draw a background
            self.WIN.blit(self.Background[0], (0, 0))
            #switch between engines
            self.switch()
            #start the selected engine
            self.states = self.currEngine.start()
            self.WIN = pygame.display.set_mode(( self.WIDTH, self.HEIGHT),pygame.RESIZABLE)
            self.filemanager.save_profile(self.profile)
            #get the new state
            if len(self.states) >1:
                self.gameState = self.states[1]
            if self.states[0] == "start":
                self.controllerState = "game"
            if self.states[0] == "runAway" :
                pygame.display.quit()
                break
            if self.states[0] == "menu":
                self.controllerState = "menu"
            

    def switch(self):
            """switching function to switch between game engines
            
            """
            ## if the controller state is game 
            if self.controllerState == "game":
                PLAYER_SHIP_SKINS = self.assets[0]
                BULLET_SHIP_SKINS = self.assets[1]
                ENEMY_SKINS = self.assets[2]
                POWER_UPS = self.assets[3]
                BOSSES = self.assets[4]
                ENEMY_BULLET_SKINS = self.assets[5]

                self.convert(PLAYER_SHIP_SKINS,BULLET_SHIP_SKINS,ENEMY_SKINS,POWER_UPS,BOSSES,ENEMY_BULLET_SKINS)
                #to be changed according to inventory menu
                PLAYER_ASSETS =[PLAYER_SHIP_SKINS[2], BULLET_SHIP_SKINS[0],PLAYER_SHIP_SKINS[3], BULLET_SHIP_SKINS[2]]
                BG = self.Background[0]
                ENEMY_ASSETS = [ENEMY_SKINS,BOSSES,ENEMY_BULLET_SKINS]
                GAME_ASSETS = [BG,POWER_UPS]
                #Endless mode
                if self.mode == -1:
                    # get the chosen level from the level selector
                    level = self.lvlSelector.getLevel(self.mode,self.diff,ENEMY_SKINS,ENEMY_BULLET_SKINS,BOSSES)
                    # assign the current Engine to be the normal game engine
                    self.currEngine = normalGameEngine(window =self.WIN,level =level,
                    diff = self.diff,profile = self.profile,settings1 = self.settings1,settings2= self.settings2,
                    playerAssets= PLAYER_ASSETS,enemyAssets=ENEMY_ASSETS,gameAssets= GAME_ASSETS,
                     gameState=self.gameStateLOADED,powerUpsAssets = POWER_UPS,fileManager=self.filemanager )
                    self.gameStateLOADED = None
                #Versus mode
                elif self.mode == 0:
                    self.WIN = pygame.display.set_mode(( self.HEIGHT, self.WIDTH),pygame.RESIZABLE)
                    self.currEngine = vsGameEngine(window =self.WIN,profile = self.profile,settings1 = self.settings1,
                    settings2 = self.settings2,playerAssets= PLAYER_ASSETS,gameAssets=[BG])

                elif self.mode > 0:
                    # get the chosen level from the level selector
                    level = self.lvlSelector.getLevel(self.profile.get_story_progress(),self.diff,ENEMY_SKINS,ENEMY_BULLET_SKINS,BOSSES)
                    # assign the current Engine to be the normal game engine
                    self.currEngine = normalGameEngine(window =self.WIN,level =level,
                    diff = self.diff,profile = self.profile,settings1 = self.settings1,settings2= self.settings2,
                    playerAssets= PLAYER_ASSETS,enemyAssets=ENEMY_ASSETS,gameAssets= GAME_ASSETS,
                     gameState=self.gameStateLOADED,powerUpsAssets = POWER_UPS,fileManager=self.filemanager )
                    self.gameStateLOADED = None

            
            #if the controller state is opening a menu
            elif self.controllerState == "menu":
                #assign the current engine to be the menu engine
                self.currEngine = menu(self.WIN, self.WIDTH, self.HEIGHT)
                #create the main menu
                self.currEngine.create_menue(2)

    def convert(self, PLAYER_SHIP_SKINS, BULLET_SHIP_SKINS,ENEMY_SKINS, POWERUPS,BOSSES, ENEMY_BULLET_SKINS):
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
                
                for i in POWERUPS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                for i in ENEMY_BULLET_SKINS:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()

                for i in BOSSES:
                    i.frames[0].convert_alpha()
                    i.frames[1].convert_alpha()
                    i.frames[2].convert_alpha()
                    i.frames[3].convert_alpha()
                    i.frames[4].convert_alpha()
                    i.frames[5].convert_alpha()
               
                


    def getGameState(self):
        if self.controllerState == "game":
            return self.currEngine.getGameState()
        else:
            return self.gameState