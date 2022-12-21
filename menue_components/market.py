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
        self.created_buttons = []
        self.skin_image = SpriteSheet(pygame.image.load("Assets\Ships_16x16_[8,2].png"),16, 16, 5, 1, 8 ).skin
        self.weapon_image = SpriteSheet(pygame.image.load("Assets\Bullets_10x16_[4,2].png"), 10, 16, 5, 1, 4).skin
        self.button_image = SpriteSheet(pygame.image.load("Assets\Buttons_64x22_[13,1].png"),64, 22, 2, 1, 13 ).skin

        self.skin1 =  Button( self.WIDTH / 6 - 50, self.HEIGHT -700, 80, 80, price=1000, image = self.skin_image[0], number=0)
        self.skin2 = Button(self.WIDTH / 6 - 50, self.HEIGHT -600, 80, 80, price=1500, image = self.skin_image[2], number=1)
        self.skin3 = Button(self.WIDTH / 6 - 50, self.HEIGHT -500, 80, 80, price=2000, image = self.skin_image[4], number=2)
        self.skin4= Button(self.WIDTH / 6 - 50, self.HEIGHT -400, 80, 80, price=3000, image = self.skin_image[6], number=3)

        self.skins= [self.skin1,self.skin2,self.skin3,self.skin4]

        self.weapon1= Button(self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 700, 50, 80, price=1000, image=self.weapon_image[0], number=4)
        self.weapon2=Button(self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 600, 50, 80, price=2000, image=self.weapon_image[1], number=5)
        self.weapon3=Button(self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 500, 50, 80, price=3000, image=self.weapon_image[2], number=6)

        self.weapons= [self.weapon1, self.weapon2,self.weapon3]

    def create_pause_buttons(self):
<<<<<<< HEAD
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
=======
        
        skinsarr =self.profile.get_skins()
        for i in range(4):
            if not ((i*2) in skinsarr):
                self.created_buttons.append(self.skins[i])

        weaparr =self.profile.get_unlocked_weapons()
        for i in range(3):
            if not (i in weaparr):
                self.created_buttons.append(self.weapons[i])
                
        self.created_buttons.append(Button( self.WIDTH / 2 - 50, self.HEIGHT - 240, 128, 44, price=1, image = self.button_image[8], number = 7))
        return self.created_buttons
>>>>>>> 2f80677de4cf35b18d318ff64c6b81a1c8d6e4a6

    # skins , weapon , upgrades
    def handle_button(self, b):
        if self.profile.get_coins() >= b.price and b.number != 7:
            rem = self.profile.get_coins()- b.price
            self.profile.set_coins(rem)
            b.price = 0
            self.created_buttons.pop(b.number)
            if b.number <= 3:
                skins = self.profile.get_skins()
                skins.append(b.number*2)
                self.profile.set_skins(skins)
            else: 
                weapons = self.profile.get_unlocked_weapons()
                weapons.append(b.number-4)
                self.profile.set_unlocked_weapons(weapons)
<<<<<<< HEAD

        else:
            print("no coins")
=======
                # self.profile.set_current_weapon(b.number-4)
>>>>>>> 2f80677de4cf35b18d318ff64c6b81a1c8d6e4a6
        

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    if b.isOver(pos):
                        self.handle_button(b)

                if b.number ==7 and b.isOver(pos):
                    # TODO : handle quit function to quit game or return to start menue
                    runM = False
                    selection = "menu"

        return runM ,selection
