import os
import pygame
import enemy
from weapon import weapon
from bullet import bullet
import random
class enemyFactory:
   
    dog = pygame.image.load(os.path.join(".","assets", "pixel_ship_blue_small.png"))
    cats = pygame.image.load(os.path.join(".","assets", "pixel_ship_red_small.png"))
    RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))

    GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

    BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
    
    YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

        
    def create(self,type,diff,x,y,threshold):
        if type=="d":
            w = weapon(self.YELLOW_LASER, 1, int(700/diff),20*diff,3*diff)
            return enemy.dog(x,5*diff,y,w,self.dog,100*diff,3*diff,threshold)
        elif  type=="c":
            w = weapon(self.BLUE_LASER, 1, int(500/diff),20*diff,2*diff)
            return enemy.cat(x,7*diff,y,w,self.cats,50*diff,5*diff,threshold)
        elif  type=="r":
            w = weapon(self.YELLOW_LASER, 1, int(230/diff),20*diff,2*diff)
     
        else: 
            return None

