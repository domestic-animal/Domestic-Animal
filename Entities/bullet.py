import pygame
from entity import entity
class bullet(entity):

    def __init__(self,x,y,image, damage, velocity, ishorizontal,is_friendly):
        super().__init__(x,y,image,velocity)
        self.damage = damage
        self.ishorizontal = ishorizontal
        self.is_friendly = is_friendly
    

    def move(self):
        if self.ishorizontal == 0:
            self.y += self.is_friendly*self.velocity
        else:
            self.x += self.velocity*self.ishorizontal

    def off_screen(self,width,height):
        return not(self.y <= height and self.y >= 0) or not (self.x <= width and self.x >= 0)

    def damage(self,entity):
        entity.health-=self.damage
        self.y=-40

        