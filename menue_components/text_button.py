import pygame

class Text_Button:
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
