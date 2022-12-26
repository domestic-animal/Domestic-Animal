import pygame
import random
from weapon import weapon
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
         return self.weapon.shoot(self.x,self.y)

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
        self.max_health = health

    
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x, self.y + self.skin.frames[0].get_height() + 10, self.skin.frames[0].get_width(), 8))
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.skin.frames[0].get_height() + 10, self.skin.frames[0].get_width() * (self.health/self.max_health), 8))

    def move(self):
        if self.y<self.threshold[1]:
            self.y=self.y+self.velocity


    def shoot(self):
        if random.random()<0.7:
            return self.weapon.shoot( self.x+(self.skin.frames[0].get_width()/2), self.y+self.skin.frames[0].get_height())
        else:
            if random.random()<0.5:
                 return self.weapon2.shoot( self.x, self.y+self.skin.frames[0].get_height())
            else:
                return self.weapon3.shoot( self.x+self.skin.frames[0].get_width(), self.y+self.skin.frames[0].get_height() )



       
class bossCat(enemy):

    def __init__(self, x, damage, y, weapon, img, health, velocity, threshold,score):
        super().__init__(x, damage, y, weapon, img, health, velocity, threshold,score)
        self.max_health = health

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x, self.y + self.skin.frames[0].get_height() + 10, self.skin.frames[0].get_width(), 8))
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.skin.frames[0].get_height() + 10, self.skin.frames[0].get_width() * (self.health/self.max_health), 8))
    
    def move(self):
    
        if(self.x+self.skin.frames[0].get_width() >= self.threshold[0] and self.y+self.skin.frames[0].get_height() < self.threshold[1]):
            self.y+= self.velocity
        if(self.x <=0 and self.y+self.skin.frames[0].get_height() >0):
            self.y -= self.velocity
        if(self.y+self.skin.frames[0].get_height() >= self.threshold[1] and self.x+self.skin.frames[0].get_width() > 0):
            self.x -= self.velocity
        if(self.y <=0  and self.x+self.skin.frames[0].get_width() < self.threshold[0]):
            self.x += self.velocity
    

    def shoot(self):
        if(self.x+self.skin.frames[0].get_width() >= self.threshold[0] and self.y+self.skin.frames[0].get_height() < self.threshold[1]):
            self.weapon.ishorizontal = -1
        if(self.x <=0 and self.y+self.skin.frames[0].get_height() >0):
            self.weapon.ishorizontal = 1
        if(self.y+self.skin.frames[0].get_height() >= self.threshold[1] and self.x+self.skin.frames[0].get_width() > 0):
            self.weapon.ishorizontal = 0
            self.weapon.isvertical = -1
        if(self.y <=0  and self.x+self.skin.frames[0].get_width() < self.threshold[0]):
            self.weapon.ishorizontal = 0
            self.weapon.isvertical = 1
        return self.weapon.shoot(self.x,self.y)
        

        

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