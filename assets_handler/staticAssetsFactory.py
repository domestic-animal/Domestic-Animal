from assets_handler.spritesheet import SpriteSheet
import pygame

class staticAssetsFactory:
    """
    The factory class for the *silent* assets
    """

    def __init__(self):
        """
        Constructor: loads all the silent assets
        """
        # Loading the static spritesheet images
        self.BUTTONS_IMAGE = pygame.image.load("Assets\Buttons_64x22_[13,1].png")
        self.BULLETS_IMAGE = pygame.image.load("Assets\Bullets_10x16_[4,2].png")
        self.POWERUPS_IMAGE = pygame.image.load("Assets\Powerups_31x31_[5,2].png")
        self.SHIPS_IMAGE = pygame.image.load("Assets\Ships_16x16_[8,2].png")

    def create_images(self, asset, scale = 1):
        """
        This function creates the SpriteSheet object and returns its 'skin' array

        :param asset: String describing the assets wanted
        :param cooldown: Refresh rate for the animation in milliseconds
        """
        ss: SpriteSheet = None 
        if asset == "buttons":
            ss = SpriteSheet(self.BUTTONS_IMAGE, 64, 22, scale, 1, 13)

        elif asset == "bullets":
            ss = SpriteSheet(self.BULLETS_IMAGE, 10, 16, scale, 1, 4)

        elif asset == "powerups":
            ss = SpriteSheet(self.POWERUPS_IMAGE, 31, 31, scale, 1, 5)

        elif asset == "ships":
            ss = SpriteSheet(self.SHIPS_IMAGE, 16, 16, scale, 1, 8)

        return ss.skin
