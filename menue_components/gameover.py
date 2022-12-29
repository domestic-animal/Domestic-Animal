import pygame
from Assets import *
from assets_handler.spritesheet import SpriteSheet
from menue_components.button import Button
from menue_components.text_button import Text_Button

from assets_handler.assetsFactory import assetsFactory

class gameoverMenu():
    def __init__(self ,screen, WIDTH, HEIGHT,mode):
         self.WIDTH = WIDTH
         self.HEIGHT = HEIGHT
         self.screen = screen
         self.mode = mode
        
    def create_pause_buttons(self):
        created_buttons = []
        text = Text_Button( self.WIDTH/2- 90,self.HEIGHT-480,180,44, text="Game Over!", font_size = 50,font_color = (255,255,255)) 
        text1 = Text_Button( self.WIDTH/2- 90,self.HEIGHT-400,180,44, text="Click anywhere to continue", font_size = 30,font_color = (255,255,255))       
        return created_buttons, [text,text1]

    def handle_events(self, events, pos, buttons):
        selection = ""
        runM = True
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                runM = False
                selection = "runAway"

        return runM ,selection