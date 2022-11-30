import pygame
from skin import Skin

class SpriteSheet():
	"""
	SpriteSheet class: handles the operations with the spritesheets png images
	that exist in the Assets folder.
		(spritesheet: A png image that holds the skins & their frames of a game entity
		ordered by shapes as rows & shape's frames as columns)
	"""
	
	def __init__(self, sheet, width, height, scale, frames_number, skins_number = 1, cooldown = 100):
		"""
		Constructor: sets the class attributes
		"""
		self.sheet = sheet
		self.skin = [0] * skins_number
		for s in range(skins_number):
			frame = [0, 0]
			for f in range(frames_number):
				frame[f] = self.get_image(width, height, scale, f, s)
			self.skin[s] = Skin(frame, cooldown)
		self.width = width * scale   #for coordination purposes
		self.height = height * scale #for coordination purposes

	def get_image(self, width, height, scale, f, s = 0):
		"""
		function to extract the image (width x height) from the stored
		spritesheet as it's the (f)^th frame in the (s)^th skin.
		
		retunes a pygame.Surface that holds the extracted image
		"""
		image = pygame.Surface((width, height))#.convert_alpha()
		image.blit(self.sheet, (0, 0),
					((f * width), (s * height),
					 (f * width + width), (s * height + height)))
		image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling
		image.set_colorkey((0, 0, 0)) #Transparency - removes black color
		return image
