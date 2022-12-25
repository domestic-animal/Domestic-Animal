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
        button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22 , 2, 1, 13 ).skin
    
        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 500, 128, 44, price=0, image = button_image[0], number = 0)) #start
        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 420, 128, 44, price=0, image = button_image[9], number = 0)) #level
        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 340, 128, 44, price=0, image = button_image[3], number = 0)) #market
        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 260, 128, 44, price=0, image = button_image[12], number = 0)) #inventry
        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 180, 128, 44, price=0, image = button_image[5], number = 0)) # exit
        
        return created_buttons , []

    def handle_events(self, events, pos, buttons):
        runM = True
        selection = ""
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    # start game
                    runM = False
                    selection = "start"
                
                if buttons[1].isOver(pos):
                    # start game
                    runM = False
                    selection = "level"

                if buttons[2].isOver(pos):
                    # display market
                    runM = False
                    selection = "market"

                if buttons[3].isOver(pos):
                    # display inventory
                    runM = False
                    selection = "inventory"

                if buttons[4].isOver(pos):
                    # close menu
                    runM = False
                    selection = "runAway"
        return runM , selection

