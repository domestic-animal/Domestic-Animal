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
     def dead(self):
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

class bossDog(enemy):

    def __init__(self, x, damage, y, weapon,weapon2,weapon3, img, health, velocity, threshold,score):
        super().__init__(x, damage, y, weapon, img, health, velocity, threshold,score)
        self.weapon2=weapon2
        self.weapon3=weapon3

    def move(self):
        if self.y<self.threshold[1]:
            self.y=self.y+self.velocity


    def shoot(self):
        if random.random()<0.7:
            return self.weapon.shoot( self.x+(self.skin.frames[0].get_width()/2), self.y+self.skin.frames[0].get_height(),0 )
        else:
            if random.random()<0.5:
                 return self.weapon2.shoot( self.x, self.y+self.skin.frames[0].get_height(),0 )
            else:
                return self.weapo3.shoot( self.x+self.skin.frames[0].get_width(), self.y+self.skin.frames[0].get_height(),0 )



       
class bossCat(enemy):

    def __init__(self, x, damage, y, weapon, img, health, velocity, threshold,score):
        super().__init__(x, damage, y, weapon, img, health, velocity, threshold,score)
    def move(self):
    
        if(self.y >= self.threshold[1] and self.x >= self.threshold[0]):
            self.x-= self.velocity
        elif(self.y <=0 and self.x <=0):
            self.x += self.velocity
        elif(self.x <= 0 and self.y >= self.threshold[1]):
            self.y -= self.velocity
        elif(self.x >= self.threshold[0] and self.y <=0):
            self.y += self.velocity
    

    def shoot(self):
        if(self.y <=0 and self.x <=0):
            self.weapon.shoot(self.x,self.y,0)
        elif(self.x <= 0 and self.y >= self.threshold[1]):
            self.weapon.shoot(self.x,self.y,-1)
        elif(self.x >= self.threshold[0] and self.y <=0):
            self.weapon.shoot(self.x,self.y, 1)
        

        

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