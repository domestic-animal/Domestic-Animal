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

        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 400, 180, 44, price=1, image = button_image[11], number = 0))
        if self.mode > 0 :
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 340, 180, 44, price=0, image = button_image[2], number = 1))
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 280, 180, 44, price=1, image = button_image[5], number = 2))
        
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
