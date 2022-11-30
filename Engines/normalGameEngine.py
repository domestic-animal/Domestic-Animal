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
from enemyFactory import enemyFactory
from Engines.level import endlesslevel
class normalGameEngine:
   
# Player player

    def __init__(self, window, level,diff,playerAssets,profile,enemyAssets = [],
     gameAssets = [],settings=[pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s],powerUps =0) -> None:
        self.WIN=window
        # for i in playerAssets:
        #     for j in i.frames:
        #         j.convert_alpha()
        # for i in enemyAssets:
        #     i.convert_alpha()
        # for i in gameAssets:
        #     i.convert_alpha()
        # Player
        self.playerAssets = playerAssets
        # enemy
        self.enemyAssets = enemyAssets
        #background
        self.gameAssets = gameAssets
        #controls
        self.settings = settings
        #self.PLAYER_CONTROLS = [settings.left,settings.right,settings.up,settings.down]
        self.PLAYER_CONTROLS = [settings[0], settings[1], settings[2], settings[3]]
        ###############################
        #self.PLAYER_CONTROLS = settings
        #################################
        #self.gameObserver = observe()
        self.level = level
        self.profile = profile
        self.rats = enemyAssets[0]

    def start(self):

        Enemies = []
        Bullets = []
        #Player = []
        FPS = 60
        clock = pygame.time.Clock()

        we=weapon(self.playerAssets[1],-1, damage = 250, fire_rate =10)

        gameObserver = observer()
        Enemies=self.level.getwave(0.5)
        pl1=player(300,600,we,self.playerAssets[0],self.settings,1000,7)
        def redraw_window():
            #background
            self.WIN.blit(self.gameAssets[0], (0,0))
            pl1.draw(self.WIN)
            for i in Enemies:
                i.draw(self.WIN)

            for i in Bullets:
                i.draw(self.WIN)

            pygame.display.update() 
            
        while True:
            
            clock.tick(FPS)
            redraw_window()
            if len(Enemies)==0:
                Enemies=self.level.getwave(0.5)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]: # shoot
                Bullet=pl1.shoot()
                if Bullet!= None:
                    Bullets.append(Bullet)

            pl1.move(keys, 600, 800)

            for i in Enemies:
                i.move()
                Bullet=i.shoot()
                if Bullet!= None:
                    Bullets.append(Bullet)

            for i in Bullets:
                i.move()
            if pl1.cool_down>0:
                pl1.cool_down-=1
            ##generate rat
            #to do : with difficulity
            if(random.randint(0, 2*60) == 1):
                rat = bullet(random.choice([0, 600]), pl1.y,self.rats,500,5,random.choice([1,-1]),1)
                Bullets.append(rat)
            gameObserver.collision(Bullets,Enemies,pl1)
            gameObserver.dead(Enemies)
            gameObserver.off_screen(Bullets)
            
            if pl1.health <= 0:
               break 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break



            
        