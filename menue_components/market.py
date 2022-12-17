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
        skin = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 400, 100, 40, "skin",20)
        weapon = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 340, 100, 40, "weapon",12)
        runAway = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 280, 100, 40, "return", price=0)
        created_buttons.append(skin)
        created_buttons.append(weapon)
        created_buttons.append(runAway)
        return created_buttons

    # skins , weapon , upgrades

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    if self.profile.get_coins() > buttons[0].price :
                        print("your coins is : ", self.profile.get_coins())
                        print("buy skin")
                        rem = self.profile.get_coins()-buttons[0].price
                        print("your coins is : ", rem)
                        self.profile.set_coins(rem)
                    else:
                        print("no coins")

                if buttons[1].isOver(pos):
                    print(" buy weapon")

                if buttons[2].isOver(pos):
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
