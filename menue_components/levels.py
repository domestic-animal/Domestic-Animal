import pygame
from Assets import *
from assets_handler.assetsFactory import assetsFactory
from menue_components.button import Button
from file.profile import Profile

class level():
    def __init__(self ,screen, WIDTH, HEIGHT, profile : Profile,mode):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile

    
    def create_pause_buttons(self):
        created_buttons : Button = []
        factory= assetsFactory()
        button_image = factory.create_images("buttons", 4)

        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -680, 180, 44, price=0, image = button_image[15], number=-1))
        max_level = self.profile.get_story_progress() 
        if max_level >= 0:
            created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT -600, 180, 44, price=0, image = button_image[16], number=0))

        if max_level >= 1:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -540, 180, 44, price=0, image = button_image[17], number=1))

        if max_level >= 2:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -480, 180, 44, price=0, image = button_image[18], number=2))

        if max_level >= 3:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -420, 180, 44, price=0, image = button_image[19], number=3))

        if max_level >= 4:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 360, 180, 44, price=0, image = button_image[20], number=4))

        if max_level >= 5:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 300, 180, 44, price=0, image = button_image[21], number=5))

        if max_level >= 6:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 240, 180, 44, price=0, image = button_image[22], number=6))

        if max_level >= 7:
            created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT - 180,180, 44, price=0, image = button_image[23], number=7))

        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 80, 180, 44, price=0, image = button_image[9], number = -1))
        
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
