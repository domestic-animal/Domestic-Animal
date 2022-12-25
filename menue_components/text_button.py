import os
import pygame

class Text_Button:
    def __init__(self, color, x,y,width,height, text="", font_size = 30):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.type = type

    def draw(self, win):
        # Call this method to draw the button on the screen
        # pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
    
        if self.text != '':
            font = pygame.font.Font(os.path.join(".","launcher","assets","game.ttf"), self.font_size)
            text = font.render(self.text, 1,(200,10,10))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
