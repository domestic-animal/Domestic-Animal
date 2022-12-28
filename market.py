import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button
from file.profile import Profile

class market():
    def __init__(self ,screen, WIDTH, HEIGHT, profile:Profile):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.profile = profile

    def create_pause_buttons(self):
        created_buttons : Button = []
        skin_image = SpriteSheet(pygame.image.load("Assets\Ships_16x16_[8,2].png"),16, 16, 5, 1, 8 ).skin
        weapon_image = SpriteSheet(pygame.image.load("Assets\Bullets_10x16_[4,2].png"), 10, 16, 5, 1, 4).skin
        button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22, 2, 1, 13 ).skin

        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT -780, 100, 40, price=1, image = button_image[3], number=0))

        created_buttons.append(Button( self.WIDTH / 6 - 50, self.HEIGHT -700, 80, 80, price=1000, image = skin_image[0], number=0))
        created_buttons.append(Button(self.WIDTH / 6 - 50, self.HEIGHT -600, 80, 80, price=1500, image = skin_image[2], number=1))
        created_buttons.append(Button(self.WIDTH / 6 - 50, self.HEIGHT -500, 80, 80, price=2000, image = skin_image[4], number=2))
        created_buttons.append(Button(self.WIDTH / 6 - 50, self.HEIGHT -400, 80, 80, price=3000, image = skin_image[6], number=3))

        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 700, 50, 80, price=1000, image=weapon_image[0], number=4))
        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 600, 50, 80, price=2000, image=weapon_image[1], number=5))
        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 500, 50, 80, price=3000, image=weapon_image[2], number=6))
        created_buttons.append(Button(self.WIDTH / 2 - 50, self.HEIGHT - 400, 50, 80 ,price=4000, image=weapon_image[3], number=7))

        # created_buttons.append(Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 700, 100, 40, "upgrade1", price=30))
        # created_buttons.append(Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 640, 100, 40, "upgrade2", price=35))
        # created_buttons.append(Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 580, 100, 40, "upgrade3", price=40))
        created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 240, 128, 44, price=1, image = button_image[8], number = 0))
        return created_buttons

    # skins , weapon , upgrades
    def handle_button(self, b):
        if self.profile.get_coins() >= b.price :
            print("your coins is : ", self.profile.get_coins())
            print("buy")
            rem = self.profile.get_coins()- b.price
            print("your coins is : ", rem)
            self.profile.set_coins(rem)
            b.price = 0
            if b.number <= 3:
                skins = self.profile.get_skins()
                skins.append(b.number*2)
                print(b.number*2)
                self.profile.set_skins(skins)
            else: 
                weapons = self.profile.get_unlocked_weapons()
                weapons.append(b.number-4)
                print(b.number-4)
                self.profile.set_unlocked_weapons(weapons)

        else:
            print("no coins")
        

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range (1, len(buttons)-1):
                    if buttons[i].isOver(pos):
                        self.handle_button(buttons[i])

                if buttons[len(buttons)-1].isOver(pos):
                    # TODO : handle quit function to quit game or return to start menue
                    runM = False
                    selection = "menu"

        return runM ,selection