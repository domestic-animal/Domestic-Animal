import pygame

from menue_components.pause import pauseMenue
from menue_components.start_menue import startMenue
from menue_components.market import market
from menue_components.inventory import inventory


class menu:

    def __init__(self, screen, WIDTH, HEIGHT, profile):
        self.buttons = []
        self.menue = None
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile

    # 1: pause menue
    # 2: start menue
    # 3 : market menue
    def create_menue(self, type=1, profile = None):
        if type == 1:
            self.menue = pauseMenue(self.screen, self.WIDTH, self.HEIGHT)
        elif type == 2:
            self.menue = startMenue(self.screen, self.WIDTH, self.HEIGHT)
        elif type == 3:
            self.menue = market(self.screen, self.WIDTH, self.HEIGHT, profile)
        elif type ==4:
            self.menue = inventory(self.screen, self.WIDTH, self.HEIGHT, profile)
        self.buttons = self.menue.create_pause_buttons()

    def start(self):
        pygame.init()

        # rum menue engine
        runMenue = True
        selection = ""
        clock = pygame.time.Clock()
        FPS = 60
        while runMenue:
            clock.tick(FPS)
            pos = pygame.mouse.get_pos()
            event = pygame.event.get()

            # handle events with current position
            runMenue,selection = self.menue.handle_events(event, pos, self.buttons)
            
            # draw buttons on the screen
            for b in self.buttons:
                b.draw(self.screen,True)

            pygame.display.update()
        return [selection]

    def getGameState(self):
        return None
