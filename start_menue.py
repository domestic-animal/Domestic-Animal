import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button


class startMenue():
    def __init__(self, screen, WIDTH, HEIGHT):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen

    def create_pause_buttons(self):
        created_buttons = []
        button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22, 2, 1, 13 ).skin
        start = Button( self.WIDTH / 2 - 50, self.HEIGHT - 500, 128, 44, price=1, image = button_image[0], number = 0)
        load = Button( self.WIDTH / 2 - 50, self.HEIGHT - 420, 128, 44, price=1, image = button_image[1], number = 0)
        market = Button( self.WIDTH / 2 - 50, self.HEIGHT - 360, 128, 44, price=1, image = button_image[3], number = 0)
        inventory = Button( self.WIDTH / 2 - 50, self.HEIGHT - 300, 128, 44, price=1, image = button_image[12], number = 0) # assigned random
        runAway = Button( self.WIDTH / 2 - 50, self.HEIGHT - 240, 128, 44, price=1, image = button_image[5], number = 0)
        created_buttons.append(start)
        created_buttons.append(load)
        created_buttons.append(market)
        created_buttons.append(inventory)
        created_buttons.append(runAway)
        return created_buttons

    def handle_events(self, events, pos, buttons):
        runM = True
        selection = ""
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    # TODO : start game
                    runM = False
                    selection = "start"

                if buttons[1].isOver(pos):
                    # TODO : handle load function
                    selection = "load"
                    
                if buttons[2].isOver(pos):
                    runM = False
                    selection = "market"

                if buttons[3].isOver(pos):
                    # TODO : display inventory
                    runM = False
                    selection = "inventory"

                if buttons[4].isOver(pos):
                    # TODO : close program
                    runM = False
                    selection = "runAway"
        return runM ,selection

