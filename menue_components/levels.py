import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button
from file.profile import Profile

class level():
    def __init__(self ,screen, WIDTH, HEIGHT, profile : Profile):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile

    def load_imagae(self):
        self.button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22, 2, 1, 13 ).skin

    
    def create_pause_buttons(self):
        self.load_imagae()
        created_buttons : Button = []

        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT -780, 128, 44, price=0, image = self.button_image[9], number=-1))
        max_level = self.profile.get_story_progress() 
        if max_level >= 1:
            created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT -670, 128, 44, price=0, image = self.button_image[0], number=1))

        if max_level >= 2:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT -595, 128, 44, price=0, image = self.button_image[1], number=2))

        if max_level >= 3:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT -520, 128, 44, price=0, image = self.button_image[2], number=3))

        if max_level >= 4:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT -445, 128, 44, price=0, image = self.button_image[3], number=4))

        if max_level >= 5:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 370, 128, 44, price=0, image = self.button_image[4], number=5))

        if max_level >= 6:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 295, 128, 44, price=0, image = self.button_image[5], number=6))

        if max_level >= 7:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 220, 128, 44, price=0, image = self.button_image[6], number=7))

        if max_level >= 8:
            created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 145,128, 44, price=0, image = self.button_image[7], number=8))

        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 60, 128, 44, price=0, image = self.button_image[8], number = -1))
        
        return created_buttons , []
      

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                # handle only buttons of weapons and
                for i in range (1,len(buttons)-1):  
                    if buttons[i].isOver(pos):
                        selection = str(buttons[i].number)
                        print("select lvl : ", buttons[i].number)
                        runM = False

                if buttons[len(buttons)-1].isOver(pos):
                    # handle quit function to quit game or return to start menue
                    runM = False
                    selection = "menu"

        return runM , selection
