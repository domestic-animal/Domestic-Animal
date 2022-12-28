# https://stackoverflow.com/questions/63435298/how-to-create-a-button-class-in-pygame
import pygame
from Assets import *

class Button:
    def __init__(self, x, y, width, height,price, image,number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.price = price
        self.image = image
        self.number = number

    def draw(self, win):
        # Call this method to draw the button on the screen
        win.blit(self.image, (self.x, self.y))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
