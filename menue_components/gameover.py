import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button
from menue_components.text_button import Text_Button

from assets_handler.assetsFactory import assetsFactory

class gameoverMenu():
    def __init__(self ,screen, WIDTH, HEIGHT,mode):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.mode = mode
        
    def create_pause_buttons(self):
        created_buttons = []
        factory= assetsFactory()
        button_image = factory.create_images("buttons", 8)
        text = Text_Button( self.WIDTH/2- 90,self.HEIGHT-440,180,44, text="Game Over!", font_size = 30,font_color = (255,255,255))
        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 400, 180, 44, price=1, image = button_image[6], number = 0))
        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 340, 180, 44, price=0, image = button_image[7], number = 1))
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 280, 180, 44, price=1, image = button_image[5], number = 2))
        
        return created_buttons, [text]

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    if b.isOver(pos):
                        runM = False
                        if b.number == 0:
                            selection = "continue" 
                        elif b.number == 1 :
                            selection = "save"
                        elif b.number == 2 :
                            selection = "runAway"

        return runM ,selection