import pygame
from Assets import *
from menue_components.button import Button
from menue_components.text_button import Text_Button
from file.profile import Profile
from assets_handler.assetsFactory import assetsFactory


class inventory():
    def __init__(self ,screen, WIDTH, HEIGHT, profile : Profile,mode):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile
        self.created_buttons = []

    def load_imagae(self):
        factory= assetsFactory()
        self.skin_image = factory.create_images("ships", 4) #16*16
        self.weapon_image = factory.create_images("bullets", 5) #10*16
        self.button_image = factory.create_images("buttons", 4) #45*11

    def search (self, myList : list, number):
        for x in myList:
            if x == number:
                return True
        return False
    
    def create_pause_buttons(self):
        self.load_imagae()
        created_buttons : Button = []
        text_buttons : Text_Button = []
        cur_weapon_number = self.profile.get_current_weapon()
        cur_skin_number = self.profile.get_current_skin()


        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -680, 100, 40, price=0, image = self.button_image[13], number=-1))
        skins = self.profile.get_skins()
        unlocked_weapons = self.profile.get_unlocked_weapons()
        if  self.search(skins, 0):
            created_buttons.append(Button( self.WIDTH / 4 - 32, self.HEIGHT -550, 64, 64, price=1000, image = self.skin_image[0], number=0))
            if cur_skin_number == 0:
                text_buttons.append(Text_Button(self.WIDTH / 4 - 32-40, self.HEIGHT -550-64, 64, 64, ".", 200, (0,0,0)))

        if self.search(skins, 1):
            created_buttons.append(Button(self.WIDTH / 4 - 32, self.HEIGHT -441, 64, 64, price=1500, image = self.skin_image[2], number=1))
            if cur_skin_number == 2:
                text_buttons.append(Text_Button(self.WIDTH / 4 - 32-40, self.HEIGHT -441-64, 64, 64, ".", 200, (0,0,0)))

        if self.search(skins, 2):
            created_buttons.append(Button(self.WIDTH / 4 - 32, self.HEIGHT -332, 64, 64, price=2000, image = self.skin_image[4], number=2))
            if cur_skin_number == 4:
                text_buttons.append(Text_Button(self.WIDTH / 4 - 32-40, self.HEIGHT -332-64, 64, 64, ".", 200, (0,0,0)))

        if self.search(skins, 3):
            created_buttons.append(Button(self.WIDTH / 4 - 32, self.HEIGHT -223, 64, 64, price=3000, image = self.skin_image[6], number=3))
            if cur_skin_number == 6:
                text_buttons.append(Text_Button(self.WIDTH / 4 - 32-40, self.HEIGHT -223-64, 64, 64, ".", 200, (0,0,0)))

        if self.search(unlocked_weapons, 0):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 550, 50, 80, price=1000, image = self.weapon_image[0], number=4))
            if cur_weapon_number == 0:
                text_buttons.append(Text_Button(self.WIDTH / (4/3) - 25-40, self.HEIGHT -550-64, 50, 80, ".", 200, (0,0,0)))

        if self.search(unlocked_weapons, 1):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 441, 50, 80, price=2000, image = self.weapon_image[1], number=5))
            if cur_weapon_number == 1:
                text_buttons.append(Text_Button(self.WIDTH / (4/3) - 25-40, self.HEIGHT -441-64, 50, 80, ".", 200, (0,0,0)))

        if self.search(unlocked_weapons, 2):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 332, 50, 80, price=3000, image = self.weapon_image[2], number=6))
            if cur_weapon_number == 2:
                text_buttons.append(Text_Button(self.WIDTH / (4/3) - 25-40, self.HEIGHT -332-64, 50, 80, ".", 200, (0,0,0)))

        if self.search(unlocked_weapons, 3):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 223, 50, 80 ,price=4000, image = self.weapon_image[3], number=7))
            if cur_weapon_number == 3:
                text_buttons.append(Text_Button(self.WIDTH / (4/3) - 25-40, self.HEIGHT -223-64, 50, 80, ".", 200, (0,0,0)))

        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 120, 128, 44, price=0, image = self.button_image[8], number = -1))
        
        return created_buttons , text_buttons

        # skins , weapon , upgrades
    def handle_button(self, b : Button):
        if b.number <= 3:
            self.profile.set_current_skin(b.number*2)
            print("select skin number : ",b.number*2)
        else: 
            self.profile.set_current_weapon(b.number-4)
            print("select weapon number : ",b.number-4)
        

        

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range (len(buttons)-1):
                    if buttons[i].isOver(pos):
                        self.handle_button(buttons[i])

                if buttons[len(buttons)-1].isOver(pos):
                    # TODO : handle quit function to quit game or return to start menue
                    runM = False
                    selection = "menu"

        return runM ,selection
