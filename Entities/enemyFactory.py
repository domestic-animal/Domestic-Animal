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
    enemySheet = pygame.image.load(os.path.join(".","assets", "Enemies_26x26_[6,2].png"))
    bulletSheet = pygame.image.load(os.path.join(".", "assets", "Bullets_10x16_[4,2].png"))
    ENEMY_SKINS = SpriteSheet(enemySheet,26,26,2,2,6).skin
    BULLET_SKINS = SpriteSheet(bulletSheet,10,16,1,2,4).skin
    DOG = ENEMY_SKINS[2]

    CAT = ENEMY_SKINS[1]

    CAT_LASER = BULLET_SKINS[2]

    DOG_LASER = BULLET_SKINS[1]
        
    def create(self,type,diff,x,y,threshold):
        if type=="d":
            w = weapon(self.DOG_LASER, 1, int(700/diff),20*diff,3*diff)
            return enemy.dog(x,5*diff,y,w,self.DOG,100*diff,3*diff,threshold)
        elif  type=="c":
            w = weapon(self.CAT_LASER, 1, int(500/diff),20*diff,2*diff)
            return enemy.cat(x,7*diff,y,w,self.CAT,50*diff,5*diff,threshold)
       # elif  type=="r":
        #    w = weapon(self.YELLOW_LASER, 1, int(230/diff),20*diff,2*diff)
     
        else: 
            return None

