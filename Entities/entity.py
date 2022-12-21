import pygame
class entity:
    def __init__(self,x,y,skin, velocity):
        self.x =x
        self.y = y
        self.skin = skin
        self.velocity = velocity
        self.mask = pygame.mask.from_surface(self.skin.frames[0])
        self.width = self.skin.frames[0].get_width()
        self.height = self.skin.frames[0].get_height()

    def move():
        pass
    
    def draw(self, window):
        window.blit(self.skin.updateAnimation(), (self.x, self.y))

    def __getstate__(self):
        state = self.__dict__.copy()
        mask = state.pop("mask")
        surface = mask.to_surface(unsetcolor="blue", unsetsurface=None)
        state["mask_string"] = (pygame.image.tostring(surface, "RGBA"), surface.get_size())
        return state

    def __setstate__(self, state):
        surface = state.pop("mask_string")
        s = pygame.image.fromstring(surface[0], surface[1], "RGBA")
        state["mask"] = pygame.mask.from_surface(s)
        self.__dict__.update(state)
