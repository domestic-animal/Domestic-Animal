import os
import pygame
import enemy
import sys
sys.path.insert(0, './assets_handler')


from spritesheet import SpriteSheet
from weapon import weapon
from bullet import bullet
import random
class enemyFactory:
    def __init__(self, BULLET_SKINS, ENEMY_SKINS):
        self.DOG = ENEMY_SKINS[2]

        self.CAT = ENEMY_SKINS[1]

        self.CAT_LASER = BULLET_SKINS[0]

        self.DOG_LASER = BULLET_SKINS[0]
        
    def create(self,type,diff,x,y,threshold):
        if type=="d":
            w = weapon(self.DOG_LASER, 1, int(650/diff),15*diff,2*diff)
            return enemy.dog(x,5*diff,y,w,self.DOG,100*diff,3*diff,threshold)
        elif  type=="c":
            w = weapon(self.CAT_LASER, 1, int(500/diff),20*diff,2*diff)
            return enemy.cat(x,7*diff,y,w,self.CAT,50*diff,5*diff,threshold)
       # elif  type=="r":
        #    w = weapon(self.YELLOW_LASER, 1, int(230/diff),20*diff,2*diff)
     
        else: 
            return None

