from assets_handler.spritesheet import SpriteSheet
import pygame

class dynamicAssetsFactory:
    """
    The factory class for the *animated* assets that contains frames
    """

    def __init__(self, cooldown = 100):
        """
        Constructor: loads all the animated assets
        """
        self.cooldown = cooldown
        # Loading the animated spritesheet images
        self.BOSSES_IMAGE = pygame.image.load("Assets\Bosses_138x192_[2,6].png")
        self.BULLETS_IMAGE = pygame.image.load("Assets\Bullets_10x16_[4,2].png")
        self.ENEMIES_IMAGE = pygame.image.load("Assets\Enemies_26x26_[6,2].png")
        self.ENEMIES_BULLETS_IMAGE = pygame.image.load("Assets\EnemiesBullets_15x24_[4,3].png")
        self.POWERUPS_IMAGE = pygame.image.load("Assets\Powerups_31x31_[5,2].png")
        self.SHIPS_IMAGE = pygame.image.load("Assets\Ships_16x16_[8,2].png")

    def create_skins(self, asset, scale = 1, cooldown = 100):
        """
        This function creates the SpriteSheet object and returns its 'skin' array

        :param asset: String describing the assets wanted
        :param cooldown: Refresh rate for the animation in milliseconds
        """
        ss: SpriteSheet = None 
        if asset == "bosses":
            ss = SpriteSheet(self.BOSSES_IMAGE, 138, 192, scale, 6, 2)

        elif asset == "bullets":
            ss = SpriteSheet(self.BULLETS_IMAGE, 10, 16, scale, 2, 4)

        elif asset == "enemies":
            ss = SpriteSheet(self.ENEMIES_IMAGE, 26, 26, scale, 2, 6)

        elif asset == "enemies_bullets":
            ss = SpriteSheet(self.ENEMIES_BULLETS_IMAGE, 15, 24, scale, 3, 4)

        elif asset == "powerups":
            ss = SpriteSheet(self.POWERUPS_IMAGE, 31, 31, scale, 2, 5)

        elif asset == "ships":
            ss = SpriteSheet(self.SHIPS_IMAGE, 16, 16, scale, 2, 8)

        return ss.skin
