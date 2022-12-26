import pygame
import sys
"""
    Normal Game Engine that runs both the Story mode
    and the Endless mode using the level given
"""
#from observer import observer as observe
sys.path.insert(0, './Entities')
from Entities.player import player
from Entities.weapon import weapon
from Engines.observer import vsobserver
from Engines.menueEngine import menu
from Engines.gameState import gameState
class vsGameEngine:

    # Player player

    def __init__(self,window,profile, playerAssets ,gameAssets, settings1,settings2):
        """
            Constructor

            parameters:
            window: pygame window to draw in
            level: the level to be played in the engine
            diff: the difficulity chosen
            playerAssets: player's Assets to be drawn on the window
            profile: currently logged in profile
            enemyAssets: enemy Assets to be drawn on the window
            gameAssets: any extra assets such as background
            settings: player's controls
        """

        self.WIN = window
        self.playerAssets = playerAssets
        self.gameAssets = gameAssets
        self.settings1 = settings1
        self.settings2 = settings2
        self.PLAYER1_CONTROLS = [settings1["left"],settings1["right"],settings1["up"],settings1["down"]]
        self.PLAYER2_CONTROLS =  [settings2["left"],settings2["right"],settings2["up"],settings2["down"]]
        self.profile = profile

        # pause menu
        self.menuengine = menu(self.WIN, self.WIN.get_width(),self.WIN.get_height())
        self.menuengine.create_menue(1)

        #constant attributes
        self.Bullets = []
        self.Players = []
        self.gameObserver = vsobserver(self.WIN.get_width(),self.WIN.get_height())


    def create_player(self):
        
        #player Entity
        self.playerAssets[1].rotate(-1)

        self.playerAssets[0].rotate(-1)
        pl1=player(200,295,1,(self.playerAssets[0],self.playerAssets[1]),self.PLAYER1_CONTROLS,250,7,1)
        self.Players.append(pl1)

        self.playerAssets[3].rotate(1)

        self.playerAssets[2].rotate(1)
        pl2=player(600,295,1,(self.playerAssets[2],self.playerAssets[3]),self.PLAYER2_CONTROLS,250,7,-1)
        self.Players.append(pl2)
    
    
    def move_entities(self,keys):
        #detect player movement
            for player in self.Players:
                player.move(keys, self.WIN.get_width(),self.WIN.get_height())

            #move bullets
            for bullet in self.Bullets:
                bullet.move()



    def shoot(self,keys):
            if keys[self.settings1["fire"]]: 
                Bullet=self.Players[0].shoot()
                if Bullet!= None:
                    self.Bullets.append(Bullet)
                    
            if  keys[self.settings2["fire"]]:
                Bullet=self.Players[1].shoot()
                if Bullet!= None:
                    self.Bullets.append(Bullet)

     # function to draw  the window
    def redraw_window(self):
            """
                drawing function to redraw every frame
            """
            # drawing background
            self.WIN.blit(self.gameAssets[0], (0, 0))
            # drawing player
            for i in self.Players:
                i.draw(self.WIN)
            #drawing bullets
            for i in self.Bullets:
                i.draw(self.WIN)

            #update the display
            pygame.display.update()

       
        

    def start(self):
        """
            function used to start the game engine 
        """
        ####    Intitalization      ####
        #################################
        self.create_player()
        #storage lists
        FPS = 60
        clock = pygame.time.Clock()
        #generate the wave


        ####    Main game loop      ####
        ################################
        while True:
            #drawing FPS
            clock.tick(FPS)
            #draw everything
            self.redraw_window()
            #generate a new wave when the wave is cleared

            #detect the keys pressed
            keys = pygame.key.get_pressed()
            # detect shooting
            self.shoot(keys)
            #move entities 
            self.move_entities(keys)
            
            #observe game state and update it accordingly
            #observe collisions
            self.gameObserver.collision(self.Bullets, self.Players)
            #observe offscreen bullets
            self.gameObserver.off_screen(self.Bullets)


            #pasue menu
            if keys[pygame.K_ESCAPE]: # shoot
                selection = self.menuengine.start()
                if selection[0] == "save":
                    pass
                if selection[0] == "runAway":
                    self.playerAssets[1].rotate(1)
                    self.playerAssets[0].rotate(1)
                    self.playerAssets[3].rotate(-1)
                    self.playerAssets[2].rotate(-1)
                    return ["menu"]
                    
            #on death or quitting
            if self.Players[0].health <= 0 or self.Players[1].health <= 0:
                    self.playerAssets[1].rotate(1)
                    self.playerAssets[0].rotate(1)
                    self.playerAssets[3].rotate(-1)
                    self.playerAssets[2].rotate(-1)
                    return ["menu"]


    def getGameState():
        return None
            
