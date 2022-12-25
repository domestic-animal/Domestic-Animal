import os
import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button
from menue_components.text_button import Text_Button
from file.profile import Profile

class market():
    def __init__(self ,screen, WIDTH, HEIGHT, profile : Profile):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile

    def load_imagae(self):
        self.skin_image = SpriteSheet(pygame.image.load("Assets\Ships_16x16_[8,2].png"),16, 16, 5, 1, 8 ).skin
        self.weapon_image = SpriteSheet(pygame.image.load("Assets\Bullets_10x16_[4,2].png"), 10, 16, 5, 1, 4).skin
        self.button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22, 2, 1, 13 ).skin

    def search (self, myList : list, number):
        for x in myList:
            if x == number:
                return True
        return False
    

    def create_pause_buttons(self):
        self.load_imagae()
        created_buttons : Button = []
        text_buttons : Text_Button = []


        coins : str = "Coins: " + str(self.profile.get_coins())
        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT -780, 100, 40, price=0, image = self.button_image[3], number=-1))
        text_buttons.append(Text_Button((200,200,200),self.WIDTH / 7+20 , self.HEIGHT -740, 60, 60, coins, 35))
        skins = self.profile.get_skins()
        unlocked_weapons = self.profile.get_unlocked_weapons()
        if not self.search(skins, 0):
            created_buttons.append(Button( self.WIDTH / 4 - 50, self.HEIGHT -670, 80, 80, price=1000, image = self.skin_image[0], number=0))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / 4 - 50, self.HEIGHT -585, 60, 30,"1000"))

        if not self.search(skins, 1):
            created_buttons.append(Button(self.WIDTH / 4 - 50, self.HEIGHT -535, 80, 80, price=1500, image = self.skin_image[2], number=1))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / 4 - 50, self.HEIGHT -450, 60, 30,"1500"))

        if not self.search(skins, 2):
            created_buttons.append(Button(self.WIDTH / 4 - 50, self.HEIGHT -400, 80, 80, price=2000, image = self.skin_image[4], number=2))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / 4 - 50, self.HEIGHT -315, 60, 30,"2000"))

        if not self.search(skins, 3):
            created_buttons.append(Button(self.WIDTH / 4 - 50, self.HEIGHT -265, 80, 80, price=3000, image = self.skin_image[6], number=3))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / 4 - 50, self.HEIGHT -180, 60, 30,"3000"))


        if not self.search(unlocked_weapons, 0):
            created_buttons.append(Button(self.WIDTH / (4/3) - 50, self.HEIGHT - 670, 50, 80, price=1000, image = self.weapon_image[0], number=4))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / (4/3) - 50, self.HEIGHT -585, 60, 30,"1000"))

        if not self.search(unlocked_weapons, 1):
            created_buttons.append(Button(self.WIDTH / (4/3) - 50, self.HEIGHT - 535, 50, 80, price=2000, image = self.weapon_image[1], number=5))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / (4/3) - 50, self.HEIGHT -450, 60, 30,"2000"))

        if not self.search(unlocked_weapons, 2):
            created_buttons.append(Button(self.WIDTH / (4/3) - 50, self.HEIGHT - 400, 50, 80, price=3000, image = self.weapon_image[2], number=6))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / (4/3) - 50, self.HEIGHT -315, 60, 30,"3000"))

        if not self.search(unlocked_weapons, 3):
            created_buttons.append(Button(self.WIDTH / (4/3) - 50, self.HEIGHT - 265, 50, 80 ,price=4000, image = self.weapon_image[3], number=7))
            text_buttons.append(Text_Button((150,100,100),self.WIDTH / (4/3) - 50, self.HEIGHT -180, 60, 30,"4000"))

        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 100, 128, 44, price=0, image = self.button_image[8], number = -1))
        
        return created_buttons , text_buttons


    # skins , weapon , upgrades
    def handle_button(self, b):
        if self.profile.get_coins() >= b.price :
            rem = self.profile.get_coins()- b.price
            print("current coins before : ",self.profile.get_coins())
            self.profile.set_coins(rem)
            print("current coins after : ",self.profile.get_coins())
            if b.number <= 3 and b.number >=0:
                skins = self.profile.get_skins()
                skins.append(b.number)
                print("select skin number : ",b.number)
                print(skins)
                self.profile.set_skins(skins)
            else: 
                weapons = self.profile.get_unlocked_weapons()
                weapons.append(b.number-4)
                print("select weapon number : ",b.number-4)
                print(weapons)
                self.profile.set_unlocked_weapons(weapons)
        

        else:
            print("no coins")

        

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                # handle only buttons of weapons and
                for i in range (1,len(buttons)-1):  
                    if buttons[i].isOver(pos):
                        self.handle_button(buttons[i])

                if buttons[len(buttons)-1].isOver(pos):
                    # handle quit function to quit game or return to start menue
                    runM = False
                    selection = "menu"

        return runM , selection
