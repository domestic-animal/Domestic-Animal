import pygame
from menue_components.pause import pauseMenue
from menue_components.gameover import gameoverMenu
from menue_components.start_menue import startMenue
from menue_components.market import market
from menue_components.button import Button
from menue_components.inventory import inventory
from menue_components.text_button import Text_Button
from menue_components.levels import level
from file.profile import Profile
from Assets import *

class menu:


    def __init__(self, screen, WIDTH, HEIGHT, profile,background,game_mode):
        self.image_buttons : Button = []
        self.text_buttons : Text_Button = []
        self.menue = None
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.profile = profile
        self.background = background
        self.game_mode = game_mode

    # 1: pause menue
    # 2: start menue
    # 3 : market menue
    # 4 : inventory
    def create_menue(self, type=1, profile : Profile= None):
        if type == 1:
            self.menue = pauseMenue(self.screen, self.WIDTH, self.HEIGHT,self.game_mode)
        elif type == 2:
            self.menue = startMenue(self.screen, self.WIDTH, self.HEIGHT,self.game_mode)
        elif type == 3:
            self.menue = market(self.screen, self.WIDTH, self.HEIGHT, profile,self.game_mode)
        elif type ==4:
            self.menue = inventory(self.screen, self.WIDTH, self.HEIGHT, profile,self.game_mode)
        elif type ==5:
            self.menue = level(self.screen, self.WIDTH, self.HEIGHT, profile,self.game_mode)
        elif type == 6:
            self.menue = gameoverMenu((self.screen, self.WIDTH, self.HEIGHT, profile,self.game_mode))
        self.image_buttons, self.text_buttons = self.menue.create_pause_buttons()

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
            runMenue,selection = self.menue.handle_events(event, pos, self.image_buttons)
            self.image_buttons, self.text_buttons = self.menue.create_pause_buttons()
            # draw buttons on the screen
            for b in self.image_buttons:
                b.draw(self.screen)
            for b in self.text_buttons:
                b.draw(self.screen)
            pygame.display.update()

            
        return [selection]

    def getGameState(self):
        return None