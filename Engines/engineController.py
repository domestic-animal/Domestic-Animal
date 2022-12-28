import random
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
        self.loadedLvl=profile.get_story_progress()
        self.diff = 1
        if(self.gameStateLOADED != None):
            self.controllerState = "game"
            self.loadedLvl=gameState.level
            self.diff==gameState.difficulty
        self.gameState = None
        self.BGM = self.assets[6]
        self.states = []
        #difficulity
        self.diff = 1
        #window to draw objects on
        self.WIDTH, self.HEIGHT = 600, 700
        self.CO_OP=1
        self.WIN = pygame.display.set_mode(( self.WIDTH, self.HEIGHT))
        for i in range(len(self.Background)):
           self.Background[i] = pygame.transform.scale(self.Background[i],self.WIN.get_size())
           self.Background[i].convert_alpha()
        pygame.init()
        

    def run(self):
        """
            run function to run the engine controller to start the game
        """    

           
        ### Main logic loop ###
        while True:
            #draw a background
            BG = random.choice(self.Background)
            self.WIN.blit(BG, (0, 0))
            #switch between engines
            self.switch()
            #start the selected engine
            self.states = self.currEngine.start()
            self.WIN = pygame.display.set_mode(( self.WIDTH, self.HEIGHT))
            self.filemanager.save_profile(self.profile)
            #get the new state
            if len(self.states) >1:
                self.gameState = self.states[1]

            if self.states[0] == "start":
                self.loadedLvl=self.profile.get_story_progress()
                self.controllerState = "game"
                self.CO_OP=1

            elif self.states[0] == "start2":
                self.loadedLvl=self.profile.get_story_progress()
                self.controllerState = "game"
                self.CO_OP=2

            elif self.states[0] == "runAway" :
                self.BGM.stop()
                pygame.display.quit()
                break
            elif self.states[0] == "menu":
                self.controllerState = "menu"
            elif self.states[0] == "market":
                self.controllerState = "market"
            elif self.states[0] == "inventory":
                self.controllerState = "inventory"
            elif self.states[0] == "level":
                self.controllerState = "level"
            elif self.states[0] == "diff":
                self.controllerState = "diff"
            elif self.controllerState == "diff":
                if isinstance(self.states[0],int):
                    self.diff=int(self.states[0])
                self.controllerState = "menu"
            else:
                self.loadedLvl=int(self.states[0])
                self.controllerState = "game"
        
                
            

    def switch(self):
            """switching function to switch between game engines
            
            """
            self.BGM.loadTrack(2)
            self.BGM.play()
            ## if the controller state is game 
            if self.controllerState == "game":
                self.BGM.stop()
                PLAYER_SHIP_SKINS = self.assets[0]
                BULLET_SHIP_SKINS = self.assets[1]
                ENEMY_SKINS = self.assets[2]
                POWER_UPS = self.assets[3]
                BOSSES = self.assets[4]
                ENEMY_BULLET_SKINS = self.assets[5]
                BACKGROUND_MUSIC = self.BGM

                self.convert(PLAYER_SHIP_SKINS,BULLET_SHIP_SKINS,ENEMY_SKINS,POWER_UPS,BOSSES,ENEMY_BULLET_SKINS)
                #to be changed according to inventory menu
                PLAYER_ASSETS =[PLAYER_SHIP_SKINS[self.profile.get_current_skin()] , BULLET_SHIP_SKINS[self.profile.get_current_weapon()],
                PLAYER_SHIP_SKINS[self.profile.get_current_skin()+1], BULLET_SHIP_SKINS[self.profile.get_current_weapon()]]

                BG = random.choice(self.Background)
                ENEMY_ASSETS = [ENEMY_SKINS,BOSSES,ENEMY_BULLET_SKINS]
                GAME_ASSETS = [BG,POWER_UPS,BACKGROUND_MUSIC]
                #Endless mode
                if self.mode == -1:
                    # get the chosen level from the level selector
                    level = self.lvlSelector.getLevel(self.mode,self.diff,ENEMY_SKINS,ENEMY_BULLET_SKINS,BOSSES,self.WIDTH,self.HEIGHT)
                    # assign the current Engine to be the normal game engine
                    self.currEngine = normalGameEngine(window =self.WIN,level =level,
                    diff = self.diff,profile = self.profile,settings1 = self.settings1,settings2= self.settings2,
                    playerAssets= PLAYER_ASSETS,enemyAssets=ENEMY_ASSETS,gameAssets= GAME_ASSETS,
                     gameState=self.gameStateLOADED,fileManager=self.filemanager,is_coop=self.CO_OP )
                    self.gameStateLOADED = None
                #Versus mode
                elif self.mode == 0:
                    self.currEngine = vsGameEngine(window =self.WIN,profile = self.profile,settings1 = self.settings1,
                    settings2 = self.settings2,playerAssets= PLAYER_ASSETS,gameAssets=[BG])

                elif self.mode > 0:
                    # get the chosen level from the level selector
                    level = self.lvlSelector.getLevel(self.loadedLvl,self.diff,ENEMY_SKINS,ENEMY_BULLET_SKINS,BOSSES,self.WIDTH,self.HEIGHT)
                    # assign the current Engine to be the normal game engine
                    self.currEngine = normalGameEngine(window =self.WIN,level =level,
                    diff = self.diff,profile = self.profile,settings1 = self.settings1,settings2= self.settings2,
                    playerAssets= PLAYER_ASSETS,enemyAssets=ENEMY_ASSETS,gameAssets= GAME_ASSETS,
                     gameState=self.gameStateLOADED ,fileManager=self.filemanager, is_coop=self.CO_OP)
                    self.gameStateLOADED = None

            
            #if the controller state is opening a menu
            elif self.controllerState == "menu":
                #assign the current engine to be the menu engine
                self.currEngine = menu(self.WIN, self.WIDTH, self.HEIGHT,self.profile,self.Background[1],self.mode)
                #create the main menu
                self.currEngine.create_menue(2, self.profile)
            
            elif self.controllerState =="market":
                market = menu(self.WIN, self.WIDTH, self.HEIGHT,self.profile,self.Background[0],self.mode)
                market.create_menue(3, self.profile)
                self.currEngine = market
            
            elif self.controllerState == "inventory":
                inventory = menu(self.WIN, self.WIDTH, self.HEIGHT,self.profile,self.Background[0],self.mode)
                inventory.create_menue(4,self.profile)
                self.currEngine = inventory

            elif self.controllerState == "level":
                lvl = menu(self.WIN, self.WIDTH, self.HEIGHT,self.profile,self.Background[0],self.mode)
                lvl.create_menue(5,self.profile)
                self.currEngine = lvl
            elif self.controllerState == "diff":
                diffic = menu(self.WIN, self.WIDTH, self.HEIGHT,self.profile,self.Background[0],self.mode)
                diffic.create_menue(7)
                self.currEngine = diffic

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