import pygame

from menue_components.pause import pauseMenue
from menue_components.start_menue import startMenue


class menu:

    def __init__(self, screen, WIDTH, HEIGHT):
        self.buttons = []
        self.menue = None
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen

    # 1: pause menue
    # 2: start menue
    def create_menue(self, type=1):

        if type == 1:
            self.menue = pauseMenue(self.screen, self.WIDTH, self.HEIGHT)
        elif type == 2:
            self.menue = startMenue(self.screen, self.WIDTH, self.HEIGHT)
        self.buttons = self.menue.create_pause_buttons()

    def start(self):
        pygame.init()

        # rum menue engine
        runMenue = True
        selection = ""
        while runMenue:
            pos = pygame.mouse.get_pos()
            event = pygame.event.get()

            # handle events with current position
            runMenue,selection = self.menue.handle_events(event, pos, self.buttons)
            
            # draw buttons on the screen
            for b in self.buttons:
                b.draw(self.screen)

            pygame.display.update()
        return selection
