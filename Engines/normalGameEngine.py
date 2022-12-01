import os
import random
import pygame
import sys

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
        self.WIN = window
        self.playerAssets = playerAssets
        # enemy
        self.enemyAssets = enemyAssets
        # background
        self.gameAssets = gameAssets
        # controls
        self.settings = settings

        self.PLAYER_CONTROLS = [settings["left"],settings["right"],settings["up"],settings["down"]]
        #current level being played
        self.level = level
        #profile of the user
        self.profile = profile
        #rat enemy for higher difficulty
        self.rats = enemyAssets[0]
        # pause menu
        self.menuengine = menu(self.WIN, 600,800)
        self.menuengine.create_menue(1)

    def start(self):

        Enemies = []
        Bullets = []
        # Player = []
        FPS = 60
        clock = pygame.time.Clock()

        we = weapon(self.playerAssets[1], -1, damage=200, fire_rate=10)

        gameObserver = observer()

        Enemies=self.level.getwave(1)

        pl1=player(300,600,we,self.playerAssets[0],self.PLAYER_CONTROLS,1000,7)
        def redraw_window():
            # background
            self.WIN.blit(self.gameAssets[0], (0, 0))
            pl1.draw(self.WIN)
            for i in Enemies:
                i.draw(self.WIN)

            for i in Bullets:
                i.draw(self.WIN)

            pygame.display.update()

        while True:

            clock.tick(FPS)
            redraw_window()
            if len(Enemies) == 0:
                Enemies = self.level.getwave(1)
            keys = pygame.key.get_pressed()
            # detect shooting
            if keys[self.settings["fire"]]: 
                Bullet=pl1.shoot()
                if Bullet!= None:
                    Bullets.append(Bullet)

            pl1.move(keys, 600, 800)
            #move enemies and shoot
            for i in Enemies:
                i.move()
                Bullet = i.shoot()
                if Bullet != None:
                    Bullets.append(Bullet)

            for i in Bullets:
                i.move()
            if pl1.cool_down > 0:
                pl1.cool_down -= 1
            ##generate rat
            # to do : with difficulity
            if (random.randint(0, 10* 60) == 1):
                rat = bullet(random.choice([0, 600]), pl1.y, self.rats, 500, 5, random.choice([1, -1]), 1)
                Bullets.append(rat)
            gameObserver.collision(Bullets, Enemies, pl1)
            gameObserver.dead(Enemies)
            gameObserver.off_screen(Bullets)


            #pasue menu
            if keys[pygame.K_ESCAPE]: # shoot
                selection = self.menuengine.start()
                if selection == "save":
                    pass
                if selection == "runAway":
                    return "menu"
                    


            if pl1.health <= 0:
                return "menu"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "runAway"
                    



            
