import pygame

from menue_components.button import Button
import os

class inventory():
    def __init__(self ,screen, WIDTH, HEIGHT, profile):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.profile = profile

# __name = ""
#     __player_controls = {"left": "LEFT", "right": "RIGHT", "up": "UP", "down": "DOWN", "fire": "SPACE"}
#     __co_player_controls = {"left": "a", "right": "d", "up": "w", "down": "s", "fire": "LCTRL"}
#     __achievements = []
#     __story_progress = 0
#     __unlocked_weapons = []
#     __current_weapon = ""
#     __co_player_weapon = ""
#     __skins = []
#     __current_skin = ""
#     __coins = 0

    def create_pause_buttons(self):
        created_buttons = []
        achievments = Button((20, 20, 100), self.WIDTH / 6 - 50, self.HEIGHT - 400, 100, 40, "skin",20)
        unlocked_weapons = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 400, 100, 40, "weapon",12)
        skins = Button((20, 20, 100), self.WIDTH - self.WIDTH / 6 - 50, self.HEIGHT - 400, 100, 40, "return", price=0)
        created_buttons.append(achievments)
        created_buttons.append(unlocked_weapons)
        created_buttons.append(skins)
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
