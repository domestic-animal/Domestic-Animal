import pygame
from assets_handler.assetsFactory import assetsFactory
from menue_components.button import Button


class startMenue():
    def __init__(self, screen, WIDTH, HEIGHT,mode):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.mode = mode

    def create_pause_buttons(self):
        created_buttons:Button = []
        factory= assetsFactory()
        button_image = factory.create_images("buttons", 4)

        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 500, 180, 44, price=0, image = button_image[0], number = 0)) #start single
        if self.mode != 0:#not VS mode
            created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 420, 180, 44, price=0, image = button_image[1], number = 5)) #start multi
        if self.mode > 0 :#story game
            created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 580, 180, 44, price=0, image = button_image[24], number = 6)) #diffculty
            created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 340, 180, 44, price=0, image = button_image[15], number = 1)) #level
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 260, 180, 44, price=0, image = button_image[4], number = 2)) #market
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 180, 180, 44, price=0, image = button_image[14], number = 3)) #inventry
        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 100, 180, 44, price=0, image = button_image[6], number = 4)) # exit
        
        return created_buttons , []

    def handle_events(self, events, pos, buttons):
        runM = True
        selection = ""
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    if b.isOver(pos):
                        runM = False
                        if b.number == 0:
                            selection = "start" 
                        elif b.number == 1 :
                            selection = "level"
                        elif b.number == 2 :
                            selection = "market"
                        elif b.number == 3 :
                            selection = "inventory"
                        elif b.number == 4 :
                            selection = "runAway"
                        elif b.number == 5:
                            selection = "start2"
                        elif b.number == 6:
                            selection = "diff"
                

        return runM , selection

