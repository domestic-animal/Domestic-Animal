import copy
import pygame
from bullet import bullet, explosion,zapper,penetrate
import random
class weapon:

    cool_down_counter = 0

    def __init__(self,bullet,enemyWeapon,ishorizontal,isvertical,fire_rate = 30,damage = 30, velocity = 10,vs = 0,bullettype=1):
        self.bullet_img = bullet
        self.enemyWeapon = enemyWeapon
        self.fire_rate = fire_rate
        self.damage = damage
        self.velocity = velocity
        self.bullettype = bullettype
        self.ishorizontal = ishorizontal
        self.isvertical =isvertical
        self.vs = vs
        if(self.bullettype == 1):
            self.fire_rate = 100
    def shoot(self,x,y):
        if(self.enemyWeapon > 0) and self.vs == 0:
            if random.randrange(0, 2*self.fire_rate) == 1:
                    b = bullet(x+13, y, self.bullet_img,self.damage, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                    return b
        else:
            if self.cool_down_counter >= self.fire_rate:
                self.cool_down_counter = 0
            elif self.cool_down_counter > 0:
                self.cool_down_counter += 1

            if self.cool_down_counter == 0:
                self.bullet_img.playSound()
                if(self.bullettype ==0 ):
                    b = bullet(x+14, y, self.bullet_img,self.damage, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                elif (self.bullettype == 1):
                    b = explosion(x+14, y, self.bullet_img,self.damage/20, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                elif(self.bullettype == 2):
                    b = zapper(x+14, y, self.bullet_img,self.damage/7, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                elif (self.bullettype == 3):
                    b = penetrate(x+14, y, self.bullet_img,self.damage/15, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                self.cool_down_counter = 1
                return b
        return None
