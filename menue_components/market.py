import os
import pygame
from Assets import *
from assets_handler.assetsFactory import assetsFactory
from menue_components.button import Button
from menue_components.text_button import Text_Button
from file.profile import Profile

class market():
    def __init__(self ,screen, WIDTH, HEIGHT, profile : Profile,mode):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile

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


        coins : str = "Coins: " + str(self.profile.get_coins())
        created_buttons.append(Button(self.WIDTH / 2 - 90, self.HEIGHT -680, 180, 44, price=0, image = self.button_image[3], number=-1))
        text_buttons.append(Text_Button(self.WIDTH / 7+20 , self.HEIGHT -640, 60, 60, coins, 35))
        skins = self.profile.get_skins()
        unlocked_weapons = self.profile.get_unlocked_weapons()
        if not self.search(skins, 0):
            created_buttons.append(Button( self.WIDTH / 4 - 32, self.HEIGHT -550, 64, 64, price=100000, image = self.skin_image[0], number=0))
            text_buttons.append(Text_Button(self.WIDTH / 4 - 50, self.HEIGHT -481, 60, 30,"100000"))

        if not self.search(skins, 1):
            created_buttons.append(Button(self.WIDTH / 4 - 32, self.HEIGHT -441, 64, 64, price=150000, image = self.skin_image[2], number=1))
            text_buttons.append(Text_Button(self.WIDTH / 4 - 50, self.HEIGHT -372, 60, 30,"150000"))

        if not self.search(skins, 2):
            created_buttons.append(Button(self.WIDTH / 4 - 32, self.HEIGHT -332, 64, 64, price=200000, image = self.skin_image[4], number=2))
            text_buttons.append(Text_Button(self.WIDTH / 4 - 50, self.HEIGHT -263, 60, 30,"200000"))

        if not self.search(skins, 3):
            created_buttons.append(Button(self.WIDTH / 4 - 32, self.HEIGHT -223, 64, 64, price=300000, image = self.skin_image[6], number=3))
            text_buttons.append(Text_Button(self.WIDTH / 4 - 50, self.HEIGHT -154, 60, 30,"300000"))


        if not self.search(unlocked_weapons, 0):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 550, 50, 80, price=100000, image = self.weapon_image[0], number=4))
            text_buttons.append(Text_Button(self.WIDTH / (4/3) - 50, self.HEIGHT -481, 60, 30,"100000"))

        if not self.search(unlocked_weapons, 1):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 441, 50, 80, price=200000, image = self.weapon_image[1], number=5))
            text_buttons.append(Text_Button(self.WIDTH / (4/3) - 50, self.HEIGHT -372, 60, 30,"200000"))

        if not self.search(unlocked_weapons, 2):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 332, 50, 80, price=300000, image = self.weapon_image[2], number=6))
            text_buttons.append(Text_Button(self.WIDTH / (4/3) - 50, self.HEIGHT -263, 60, 30,"300000"))

        if not self.search(unlocked_weapons, 3):
            created_buttons.append(Button(self.WIDTH / (4/3) - 25, self.HEIGHT - 223, 50, 80 ,price=400000, image = self.weapon_image[3], number=7))
            text_buttons.append(Text_Button(self.WIDTH / (4/3) - 50, self.HEIGHT -154, 60, 30,"400000"))

        created_buttons.append(Button( self.WIDTH / 2 - 90, self.HEIGHT - 80, 180, 44, price=0, image = self.button_image[9], number = -1))
        
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
