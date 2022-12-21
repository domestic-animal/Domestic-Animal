import pygame

from menue_components.pause import pauseMenue
from menue_components.start_menue import startMenue
from menue_components.market import market
from menue_components.inventory import inventory
from assets_handler import spritesheet
from Assets import *

class menu:

    def __init__(self, screen, WIDTH, HEIGHT, profile,background):
        self.buttons = []
        self.menue = None
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile
        self.background = background

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
            self.screen.blit(self.background, (0, 0))

            clock.tick(FPS)
            pos = pygame.mouse.get_pos()
            event = pygame.event.get()
            # handle events with current position
            runMenue,selection = self.menue.handle_events(event, pos, self.buttons)
            self.buttons = self.menue.create_pause_buttons()
            # draw buttons on the screen
            for b in self.buttons:
                if b.price !=0 :
                    b.draw(self.screen)
            pygame.display.update()

            
        return [selection]

    def getGameState(self):
        return None
