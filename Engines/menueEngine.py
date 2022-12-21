import pygame

from menue_components.pause import pauseMenue
from menue_components.start_menue import startMenue
from menue_components.market import market
from menue_components.button import Button
from menue_components.inventory import inventory
from assets_handler import spritesheet
from Assets import *

class menu:

<<<<<<< HEAD
    def __init__(self, screen, WIDTH, HEIGHT, profile):
        self.buttons:Button = []
=======
    def __init__(self, screen, WIDTH, HEIGHT, profile,background):
        self.buttons = []
>>>>>>> 2f80677de4cf35b18d318ff64c6b81a1c8d6e4a6
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
<<<<<<< HEAD
                # print(b.price)
                if not b.price == 0:
                    b.draw(self.screen)

=======
                if b.price !=0 :
                    b.draw(self.screen)
>>>>>>> 2f80677de4cf35b18d318ff64c6b81a1c8d6e4a6
            pygame.display.update()

            
        return [selection]

    def getGameState(self):
        return None
