import pygame
import pygame_menu
import os
from levelSelector import levelSelector
from normalGameEngine import normalGameEngine
class engineController:

    def __init__(self,diff= 1,mode = -1,settings = None,fileManager = None,profile = None,gameState = "game"):
        self.profile = profile
        self.lvlSelector = levelSelector()
        self.states = []
        self.fileManager = fileManager
        self.settings = settings
        self.mode = mode
        self.diff = self.diff
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
          #to be loaded from file manager
                YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(".","assets", "pixel_ship_yellow.png"))
                BG = pygame.transform.scale(pygame.image.load(os.path.join(".","assets","background-black.png")), (600, 800))
                YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
            ##################
                level = self.lvlSelector.getLevel(self.mode,self.diff)
                self.currEngine = normalGameEngine(self.WIN,level,self.diff,profile = 0,
                playerAssets= [YELLOW_SPACE_SHIP, YELLOW_LASER],gameAssets=[BG])
            elif self.gameState == "menu":
                self.currEngine = self.Engines[1]
            else:
                self.currEngine = self.Engine[2]

e = engineController()
e.run()