import pygame

class Skin():
    """
    Shape class: stores the frames of a shape & applies its animation
    """
    def __init__(self, images, cooldown):
        """
        Constructor: sets the class attributes

        :param images: Array of the frames
        :param cooldown: Refresh rate for the animation
        """
        self.frames = images                        # Array of the frames
        self.last_update = pygame.time.get_ticks()  # The last time a refresh has done
        self.animation_cooldown = cooldown          # Refresh rate between frames
        self.currframe = 0                          # Current frame displayed
        self.sound: pygame.mixer.Sound = None                           # Sound to be played in game

    def setSound(self, sound): #used by the SpriteSheet
        self.sound = sound

    def playSound(self):
        if self.sound != None:
            self.sound.play()
    
    def setCooldown(self, cooldown):
        self.animation_cooldown = cooldown
    
    def rotate(self, r):
        """
        Function to rotate all the frames of the specific skin

        :param r: number of (90-degree)s to rotate the images (anti-clockwise -> +ve, clockwise -> -ve)
        """
        n = len(self.frames)
        frames = [0] * n
        for i in range(n):
            frames[i] = pygame.transform.rotate(self.frames[i], 90 * r)
        self.frames = frames


    def scale(self, r):
        """
        Function to rotate all the frames of the specific skin

        :param r: number of (90-degree)s to rotate the images (anti-clockwise -> +ve, clockwise -> -ve)
        """
        n = len(self.frames)
        frames = [0] * n
        for i in range(n):
            frames[i] = pygame.transform.scale(self.frames[i], r)
        self.frames = frames

    def updateAnimation(self):
        """
        Function to apply the animation using the skin's frames.
        
        Returns the next frame image to display after a specified cooldown
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.currframe += 1
            self.last_update = current_time
            if self.currframe >= len(self.frames):
                self.currframe = 0
        return self.frames[self.currframe]


    def __getstate__(self):
        state = self.__dict__.copy()
        state["frames_string"] = self.convert_to_string_list(state.pop("frames"))
        s = state.pop("sound")
        if s is not None:
            state["sound_raw"] = s.get_raw()
        else:
            state["sound_raw"] = None
        return state

    def __setstate__(self, state):
        state["frames"] = self.convert_to_surface_list(state.pop("frames_string"))
        s = state.pop("sound_raw")
        if s is not None:
            state["sound"] = pygame.mixer.Sound(s)
        else:
            state["sound"] = None
        self.__dict__.update(state)

    def convert_to_string_list(self, surface_list):
        surface_string = []
        for surface in surface_list:
            s = (pygame.image.tostring(surface, "RGBA"), surface.get_size())
            surface_string.append(s)
        return surface_string

    def convert_to_surface_list(self, surface_strings):
        surfaces = []
        for surface in surface_strings:
            s = pygame.image.fromstring(surface[0], surface[1], "RGBA")
            surfaces.append(s)
        return surfaces
