import os
import random
import pygame
import sys
"""
    Normal Game Engine that runs both the Story mode
    and the Endless mode using the level given
"""
from Engines.level import level
#from observer import observer as observe
sys.path.insert(0, './Entities')
from player import player
from weapon import weapon
from bullet import bullet
from Engines.observer import observer
from Engines.level import endlesslevel
from Engines.menueEngine import menu
class normalGameEngine:

    # Player player

    def __init__(self,window, level, diff, playerAssets, profile, enemyAssets=[],
                 gameAssets=[], settings=[pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], powerUps=0,
                 ):
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
            powerUps: how many powerups are allowed
        """
        self.WIN = window
        self.playerAssets = playerAssets
        self.enemyAssets = enemyAssets
        self.gameAssets = gameAssets
        self.settings = settings
        self.PLAYER_CONTROLS = [settings["left"],settings["right"],settings["up"],settings["down"]]
        self.level = level
        self.profile = profile

        #rat enemy for higher difficulty
        self.rats = enemyAssets[0]
        # pause menu
        self.menuengine = menu(self.WIN, 600,800)
        self.menuengine.create_menue(1)

    def start(self):
        """
            function used to start the game engine 
        """
        ####    Intitalization      ####
        #################################
        #storage lists
        Enemies = []
        Bullets = []
        # Player = []
        FPS = 60
        clock = pygame.time.Clock()
        gameObserver = observer()

        #player Entity
        we = weapon(self.playerAssets[1], -1, damage=200, fire_rate=10)
        pl1=player(300,600,we,self.playerAssets[0],self.PLAYER_CONTROLS,1000,7)

        #generate the wave
        Enemies=self.level.getwave(1)

        def redraw_window():
            """
                drawing function to redraw every frame
            """
            # drawing background
            self.WIN.blit(self.gameAssets[0], (0, 0))
            # drawing player
            pl1.draw(self.WIN)
            #drawing Enemies
            for i in Enemies:
                i.draw(self.WIN)
            #drawing bullets
            for i in Bullets:
                i.draw(self.WIN)
            #update the display
            pygame.display.update()


        ####    Main game loop      ####
        ################################
        while True:
            #drawing FPS
            clock.tick(FPS)
            #draw everything
            redraw_window()

            #generate a new wave when the wave is cleared
            if len(Enemies) == 0:
                Enemies = self.level.getwave(1)

            #detect the keys pressed
            keys = pygame.key.get_pressed()
            # detect shooting
            if keys[self.settings["fire"]]: 
                Bullet=pl1.shoot()
                if Bullet!= None:
                    Bullets.append(Bullet)

            #detect player movement
            pl1.move(keys, 600, 800)
            #move enemies and shoot
            for i in Enemies:
                i.move()
                Bullet = i.shoot()
                if Bullet != None:
                    Bullets.append(Bullet)
            #move bullets
            for i in Bullets:
                i.move()
            if pl1.cool_down > 0:
                pl1.cool_down -= 1

            ##generate rat
            # to do : with difficulity
            if (random.randint(0, 10* 60) == 1):
                rat_movement = random.choice([(0, 1), (600, -1)])
                rat = bullet(rat_movement[0], pl1.y, self.rats, 500, 5, rat_movement[1], 1)
                Bullets.append(rat)
            
            #observe game state and update it accordingly
            #observe collisions
            gameObserver.collision(Bullets, Enemies, pl1)
            #observe dead enemies
            gameObserver.dead(Enemies)
            #observe offscreen bullets
            gameObserver.off_screen(Bullets)


            #pasue menu
            if keys[pygame.K_ESCAPE]: # shoot
                selection = self.menuengine.start()
                if selection == "save":
                    pass
                if selection == "runAway":
                    return "menu"
                    

            #on death or quitting
            if pl1.health <= 0:
                return "menu"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "runAway"
                    



            
