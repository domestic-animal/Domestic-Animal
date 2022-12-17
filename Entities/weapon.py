import copy
import pygame
from bullet import bullet
from bullet import zapper
from bullet import penetrate
import random
class weapon:

    cool_down_counter = 0

    def __init__(self,bullet,enemyWeapon,fire_rate = 30,damage = 30, velocity = 10,bullettype=1):
        self.bullet_img = bullet
        self.enemyWeapon = enemyWeapon
        self.fire_rate = fire_rate
        self.damage = damage
        self.velocity = velocity
        self.bullettype = bullettype
    def shoot(self,x,y,ishorizontal):
        if(self.enemyWeapon > 0):
            if random.randrange(0, 2*self.fire_rate) == 1:
                    b = bullet(x+13, y, self.bullet_img,self.damage, self.velocity, ishorizontal,self.enemyWeapon)
                    return b
        else:
            if self.cool_down_counter >= self.fire_rate:
                self.cool_down_counter = 0
            elif self.cool_down_counter > 0:
                self.cool_down_counter += 1

            if self.cool_down_counter == 0:
                if(self.bullettype ==1 ):
                    b = bullet(x+14, y, self.bullet_img,self.damage, self.velocity, ishorizontal,self.enemyWeapon)
                elif(self.bullettype == 2):
                    b = zapper(x+14, y, self.bullet_img,self.damage/7, self.velocity, ishorizontal,self.enemyWeapon)
                else:
                    b = penetrate(x+14, y, self.bullet_img,self.damage/10, self.velocity, ishorizontal,self.enemyWeapon)
                self.cool_down_counter = 1
                return b
        return None
