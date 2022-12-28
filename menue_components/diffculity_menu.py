import pygame
from assets_handler.assetsFactory import assetsFactory
from menue_components.button import Button

class diffculityMenu():
    def __init__(self, screen, WIDTH, HEIGHT,mode):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.mode = mode

    def create_pause_buttons(self):
        created_buttons:Button = []
        factory= assetsFactory()
        button_image = factory.create_images("buttons", 4)

        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 200, 180, 44, price=0, image = button_image[3], number = 1)) #hard
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 350, 180, 44, price=0, image = button_image[14], number = 2)) #medium
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 450, 180, 44, price=0, image = button_image[3], number = 3)) #esay
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 600, 180, 44, price=0, image = button_image[0], number = -1)) #esay

        return created_buttons , []

    def handle_events(self, events, pos, buttons):
        runM = True
        selection = ""
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    if b.isOver(pos):
                        runM = False
                        if b.number == 1:
                            selection = "1"
                        elif b.number == 2 :
                            selection = "2"
                        elif b.number == 3 :
                            selection = "3"
                        else:
                            selection = "menu"

                

        return runM , selection