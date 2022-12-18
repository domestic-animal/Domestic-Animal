import pygame

from menue_components.button import Button
import os

class market():
    def __init__(self ,screen, WIDTH, HEIGHT, profile):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.profile = profile

    def create_pause_buttons(self):
        created_buttons = []
        
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 6 - 50, self.HEIGHT -700, 100, 40, "skin1",20))
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 6 - 50, self.HEIGHT -640, 100, 40, "skin1",20))
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 6 - 50, self.HEIGHT -580, 100, 40, "skin1",20))
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 700, 100, 40, "weapon1",12))
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 640, 100, 40, "weapon2",12))
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 580, 100, 40, "weapon3",12))
        created_buttons.append(Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 700, 100, 40, "upgrade1", price=30))
        created_buttons.append(Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 640, 100, 40, "upgrade2", price=35))
        created_buttons.append(Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 580, 100, 40, "upgrade3", price=40))
        created_buttons.append(Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 220, 100, 40, "return", price=0))
        return created_buttons

    # skins , weapon , upgrades
    def handle_button(self, b):
        if self.profile.get_coins() >= b.price :
            print("your coins is : ", self.profile.get_coins())
            print("buy")
            rem = self.profile.get_coins()- b.price
            print("your coins is : ", rem)
            self.profile.set_coins(rem)
        else:
            print("no coins")
        

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range (len(buttons)):
                    if buttons[i].isOver(pos):
                        self.handle_button(buttons[i])

                if buttons[len(buttons)-1].isOver(pos):
                    # TODO : handle quit function to quit game or return to start menue
                    runM = False
                    selection = "menu"
            if e.type == pygame.MOUSEMOTION:
                for b in buttons:
                    if b.isOver(pos):
                        b.color = (0, 255, 0)
                    else:
                        b.color = (20, 20, 100)

        return runM ,selection
