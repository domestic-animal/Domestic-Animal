import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button
from assets_handler.assetsFactory import assetsFactory


class pauseMenue():
    def __init__(self ,screen, WIDTH, HEIGHT,mode):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.mode = mode
        
    def create_pause_buttons(self):
        created_buttons = []
        factory= assetsFactory()
        button_image = factory.create_images("buttons", 4)
        
        decrease_amount = 400
        step = 60
        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -  decrease_amount, 180, 44, price=1, image = button_image[12], number = 0))
        decrease_amount -= step
        if self.mode >= 0 :
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -  decrease_amount, 180, 44, price=0, image = button_image[3], number = 1))
            decrease_amount -= step
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - decrease_amount, 180, 44, price=1, image = button_image[6], number = 2))
        
        return created_buttons, []

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
