import copy
import pygame
from bullet import bullet, laser,zapper,penetrate
import random
class weapon:

    cool_down_counter = 0

    def __init__(self,bullet,enemyWeapon,ishorizontal,isvertical,fire_rate = 30,damage = 30, velocity = 10):
        self.bullet_img = bullet
        self.enemyWeapon = enemyWeapon
        self.fire_rate = fire_rate
        self.damage = damage
        self.velocity = velocity
        self.ishorizontal = ishorizontal
        self.isvertical =isvertical
    def shoot(self,x,y):
        if random.randrange(0, 2*self.fire_rate) == 1:
                    b = bullet(x+13, y, self.bullet_img,self.damage, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                    return b
        


class playerWeapon(weapon):
    def __init__(self,bullet,enemyWeapon,ishorizontal,isvertical,fire_rate = 30,damage = 30, velocity = 10,bullettype=1):
        super().__init__(bullet,enemyWeapon,ishorizontal,isvertical,fire_rate ,damage, velocity)
        self.bullet_img = bullet
        self.enemyWeapon = enemyWeapon
        self.fire_rate = fire_rate
        self.damage = damage
        self.velocity = velocity
        self.bullettype = bullettype
        self.ishorizontal = ishorizontal
        self.isvertical =isvertical
    def shoot(self, x,y):
        
        if self.cool_down_counter <= 0:
                self.bullet_img.playSound()
                if(self.bullettype ==0 ):
                    b = bullet(x+14, y+13, self.bullet_img,self.damage, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                elif (self.bullettype == 1):
                    b = laser(x+14, y, self.bullet_img,self.damage/8, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                elif(self.bullettype == 2):
                    b = zapper(x+14, y, self.bullet_img,self.damage/7, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                elif (self.bullettype == 3):
                    b = penetrate(x+14, y, self.bullet_img,self.damage/12, self.velocity, self.ishorizontal,self.isvertical,self.enemyWeapon)
                self.cool_down_counter = 1
                return b
        else:
            if self.cool_down_counter >= self.fire_rate:
                self.cool_down_counter = 0
            elif self.cool_down_counter > 0:
                self.cool_down_counter += 1
        return None