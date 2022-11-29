import pygame
class entity:
    def __init__(self,x,y,skin, velocity):
        self.x =x
        self.y = y
        self.skin = skin
        self.velocity = velocity
        self.mask= pygame.mask.from_surface(self.skin.frames[0])
        self.width = self.skin.frames[0].get_width()
        self.height = self.skin.frames[0].get_height()

    def move():
        pass
    
    def draw(self, window):
        window.blit(self.skin.updateAnimation(), (self.x, self.y))
        