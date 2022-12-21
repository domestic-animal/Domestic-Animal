import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button


class pauseMenue():
    def __init__(self ,screen, WIDTH, HEIGHT):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen

    def create_pause_buttons(self):
        created_buttons = []
        button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22, 2, 1, 13 ).skin
        cont = Button(self.WIDTH / 2 - 50, self.HEIGHT - 400, 128, 44, price=1, image = button_image[11], number = 0)
        # save = Button(self.WIDTH / 2 - 50, self.HEIGHT - 340, 128, 44, price=0, image = button_image[2], number = 0)
        runAway = Button( self.WIDTH / 2 - 50, self.HEIGHT - 280, 128, 44, price=1, image = button_image[5], number = 0)
        created_buttons.append(cont)
        # created_buttons.append(save)
        created_buttons.append(runAway)
        return created_buttons

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    runM = False
                    selection = "continue"
                # if buttons[1].isOver(pos):
                #     # TODO : handle save function
                #     selection = "save"
                if buttons[1].isOver(pos):
                    # TODO : handle quit function to quit game or return to start menue
                    runM = False
                    selection = "runAway"

        return runM ,selection
