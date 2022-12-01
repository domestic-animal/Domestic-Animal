import pygame

from menue_components.button import Button
import os

class pauseMenue():
    def __init__(self ,screen, WIDTH, HEIGHT):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen

    def create_pause_buttons(self):
        created_buttons = []
        cont = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 400, 100, 40, "continue")
        save = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 340, 100, 40, "save")
        runAway = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 280, 100, 40, "quit")
        created_buttons.append(cont)
        created_buttons.append(save)
        created_buttons.append(runAway)
        return created_buttons

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    runM = False
                    selection = "continue"
                if buttons[1].isOver(pos):
                    # TODO : handle save function
                    selection = "save"
                if buttons[2].isOver(pos):
                    # TODO : handle quit function to quit game or return to start menue
                    runM = False
                    selection = "runAway"
            if e.type == pygame.MOUSEMOTION:
                for b in buttons:
                    if b.isOver(pos):
                        b.color = (0, 255, 0)
                    else:
                        b.color = (20, 20, 100)

        return runM ,selection
