import pygame
import random
from entity import entity
class enemy(entity):

     def __init__(self, x,damage, y,weapon,image,health,velocity,threshold,score):
        super().__init__(x,y,image,velocity)
        self.damage=damage
        self.health = health
        self.weapon=weapon
        self.threshold=threshold
        self.score=score
    
     def shoot(self):
         return self.weapon.shoot(self.x,self.y, 0)

     def move(self):
        pass


class dog(enemy):

    def __init__(self, x, damage, y, weapon, img, health, velocity, threshold,score):
        super().__init__(x, damage, y, weapon, img, health, velocity, threshold,score)
    def move(self):
        if self.y<self.threshold[1]:
            self.y=self.y+self.velocity

        
class cat(enemy):

    def __init__(self, x, damage, y, weapon, img, health, velocity, threshold,score):
        super().__init__(x, damage, y, weapon, img, health, velocity, threshold,score)
    def move(self):
    
        if(self.y >= self.threshold[1]):
            if(self.x+self.velocity < 0 or self.x+self.velocity > self.threshold[0]-self.skin.frames[0].get_width()):
                self.velocity *= -1
            self.x+= self.velocity
        else:
            self.y += self.velocity

        



class rat(enemy):

    def __init__(self, x, damage, y, weapon, img, health, velocity,threshold):
        super().__init__(x, damage, y, weapon, img, health, velocity,threshold)
    def move(self):
        t = random.choice([0, self.threshold[0]])
        if self.y <= self.threshold[1]:
            self.y= self.y+self.velocity
        elif self.x <= t:
            self.x += 1
        elif self.x > t:
            self.x -= 1 
    def shoot(self):
        return self.weapon.shoot(self.x, self.y,1 if self.x-1 == 0 else -1)