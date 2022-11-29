import pygame

class Skin():
    """
    Shape class: stores the frames of a shape & applies its animation
    """
    def __init__(self, images, cooldown):
        """
        Constructor: sets the class attributes
        """
        self.frames = images
        self.last_update = pygame.time.get_ticks()
        #self.mask = pygame.mask.from_surface(self.frames[0])
        self.animation_cooldown = cooldown
        self.currframe = 0
    
    def updateAnimation(self):
        """
        function to apply the animation using the skin's frames.
        
        returns the next frame image to display after a specified cooldown
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.currframe += 1
            self.last_update = current_time
            if self.currframe >= len(self.frames):
                self.currframe = 0
        return self.frames[self.currframe]
