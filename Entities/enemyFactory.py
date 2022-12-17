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
        #random cat skins and dog skins and bullet skins
        self.DOG = ENEMY_SKINS[3]
        self.DOG2 = ENEMY_SKINS[2]

        self.CAT = ENEMY_SKINS[0]
        self.CAT2 = ENEMY_SKINS[1]

        self.CAT_LASER = BULLET_SKINS[0]
        self.DOG_LASER = BULLET_SKINS[2]
        
    def create(self,type,diff,x,y,threshold):
        if type=="d":
            w = weapon(self.DOG_LASER, 1, int(650/diff),15*diff,2*diff)
            typeSkin=random.randint(1,2)
            if(typeSkin==1):
                return enemy.dog(x, 5*diff, y, w,  self.DOG,  100*diff,  5*diff,  threshold,  15*diff)
            return enemy.dog(x, 5*diff, y, w,  self.DOG2,  100*diff,  5*diff,  threshold,  15*diff)
        elif  type=="c":
            w = weapon(self.CAT_LASER, 1, int(550/diff),20*diff,2*diff)
            typeSkin=random.randint(1,2)
            if(typeSkin==1):
                return enemy.cat(x,  7*diff,  y,  w,  self.CAT,  50*diff,  5*diff,  threshold,  10*diff)
            return enemy.cat(x,  7*diff,  y,  w,  self.CAT2,  50*diff,  5*diff,  threshold,  10*diff)

        else: 
            return None

