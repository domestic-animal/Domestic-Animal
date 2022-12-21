import random
import pygame
import copy
from entity import entity
class bullet(entity):

    def __init__(self,x,y,image, damage, velocity, ishorizontal,isvertical,is_friendly):
        super().__init__(x,y,image,velocity)
        self.damage = damage
        self.ishorizontal = ishorizontal
        self.isvertical = isvertical
        self.is_friendly = is_friendly
        self.collisions = 1
    

    def move(self):
        if self.ishorizontal == 0:
            self.y += self.isvertical*self.velocity
        else:
            self.x += self.velocity*self.ishorizontal

    def off_screen(self,width,height):
        return not(self.y <= height and self.y >= 0) or not (self.x <= width and self.x >= 0)

    def Objectdamage(self,entity):
        entity.health-=self.damage
        self.y=-40

class zapper(bullet):

    def __init__(self,x,y,image, damage, velocity, ishorizontal,isvertical,is_friendly):
        super().__init__(x,y,image, damage, velocity, ishorizontal,isvertical,is_friendly)
        self.collisions = 6

    def Objectdamage(self, entity):
        entity.health-=self.damage
        self.collisions-=1
        
        if self.collisions==0:
            self.y=-40
        if  self.ishorizontal==0:
            go=random.choice([1,-1])
            self.ishorizontal=go
            #self.skin.rotate(1)
        else:
            #self.skin.rotate(-1)
            self.ishorizontal=0

class penetrate(bullet):
    
    def __init__(self,x,y,image, damage, velocity, ishorizontal,isvertical,is_friendly):
        super().__init__(x,y,image, damage, velocity, ishorizontal,isvertical,is_friendly)
        self.collisions = 10


    def Objectdamage(self, entity):
        entity.health-=self.damage
        self.collisions-= 1
        
        if(self.collisions) <= 0:
            self.y=-40

