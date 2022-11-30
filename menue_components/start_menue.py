import pygame

from menue_components.button import Button


class startMenue():
    def __init__(self, screen, WIDTH, HEIGHT):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen

    def create_pause_buttons(self):
        created_buttons = []
        start = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 500, 100, 40, "start")
        load = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 420, 100, 40, "load")
        market = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 360, 100, 40, "market")
        runAway = Button((20, 20, 100), self.WIDTH / 2 - 50, self.HEIGHT - 300, 100, 40, "exit")
        created_buttons.append(start)
        created_buttons.append(load)
        created_buttons.append(market)
        created_buttons.append(runAway)
        return created_buttons

    def handle_events(self, events, pos, buttons):
        runM = True
        selection = ""
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].isOver(pos):
                    # TODO : start game
                    runM = False
                    selection = "start"
                    pass
                if buttons[1].isOver(pos):
                    # TODO : handle load function
                    pass
                if buttons[2].isOver(pos):
                    # TODO : go market
                    pass
                if buttons[3].isOver(pos):
                    # TODO : close program
                    pass
            if e.type == pygame.MOUSEMOTION:
                for b in buttons:
                    if b.isOver(pos):
                        b.color = (0, 255, 0)
                    else:
                        b.color = (20, 20, 100)
        return runM ,selection

