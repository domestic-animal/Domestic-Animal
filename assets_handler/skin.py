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
        return state

    def __setstate__(self, state):
        state["frames"] = self.convert_to_surface_list(state.pop("frames_string"))
        self.__dict__.update(state)

    def convert_to_string_list(self, surface_list):
        surface_string = []
        for surface in surface_list:
            s = (pygame.image.tostring(surface, "RGB"), surface.get_size())
            surface_string.append(s)
        return surface_string

    def convert_to_surface_list(self, surface_strings):
        surfaces = []
        for surface in surface_strings:
            s = pygame.image.fromstring(surface[0], surface[1], "RGB")
            surfaces.append(s)
        return surfaces
