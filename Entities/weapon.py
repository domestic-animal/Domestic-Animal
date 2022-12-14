import pygame
from bullet import bullet
import random
class weapon:

    cool_down_counter = 0

    def __init__(self,bullet,enemyWeapon,fire_rate = 30,damage = 30, velocity = 10):
        self.bullet_img = bullet
        self.enemyWeapon = enemyWeapon
        self.fire_rate = fire_rate
        self.damage = damage
        self.velocity = velocity

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
                b = bullet(x+15, y, self.bullet_img,self.damage, self.velocity, ishorizontal,self.enemyWeapon)
                self.cool_down_counter = 1
                return b
        return None