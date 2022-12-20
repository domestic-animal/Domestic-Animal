import pygame
from weapon import weapon
from entity import entity
class player(entity):

     def __init__(self, x, y,we,image,input, health,velocity,vs=0):
        super().__init__(x,y,image[0],velocity)
        self.health = health
        self.weapon=weapon(image[1], vs= vs,enemyWeapon=vs, damage=45,ishorizontal=vs,isvertical=-1,fire_rate=20,bullettype=we)
        self.max_health=health
        self.input=input
        self.ScoreMultiplayer=1
        self.cool_down=0
        self.vs=vs

     def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    
     def shoot(self):
         return self.weapon.shoot(self.x,self.y)
    
     def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.skin.frames[0].get_height() + 10, self.skin.frames[0].get_width(), 8))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.skin.frames[0].get_height() + 10, self.skin.frames[0].get_width() * (self.health/self.max_health), 8))


     def move(self,keys,WIDTH,HEIGHT):
        if keys[self.input[0]] and self.x - self.velocity > 0: # left
            self.x -= self.velocity
        if keys[self.input[1]] and self.x + self.velocity + self.skin.frames[0].get_width() < WIDTH: # right
            self.x += self.velocity
        if keys[self.input[2]] and self.y - self.velocity > 0: # up
            self.y -= self.velocity
        if keys[self.input[3]] and self.y + self.velocity + self.skin.frames[0].get_height() + 15 < HEIGHT: # down
            self.y += self.velocity
      
    