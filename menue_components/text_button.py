import os
import pygame

class Text_Button:
    def __init__(self, x,y,width,height, text="", font_size = 30,font_color = (200,10,10)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_color = font_color

    def draw(self, win):
    
        if self.text != '':
            font = pygame.font.Font(os.path.join(".","launcher","assets","game.ttf"), self.font_size)
            text = font.render(self.text, 1,self.font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
