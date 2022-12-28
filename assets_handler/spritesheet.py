import pygame
from assets_handler.skin import Skin

class SpriteSheet():
	"""
	SpriteSheet class: handles the operations with the spritesheets png images
	that exist in the Assets folder.
		(spritesheet: A png image that holds the skins & their frames of a game entity
		ordered by shapes as rows & shape's frames as columns)
	"""
	
	def __init__(self, sheet, width, height, scale, frames_number, skins_number = 1, cooldown = 100, sounds = []):
		"""
		Constructor: extracts the frames & sets the class attributes

		:param sheet: The image containing the spritesheet (after converting)
		:param width: The width of a single frame
		:param height: The height of a single frame
		:param scale: Scale to be adjusted
		:param frames_number: Number of frames in the spritesheet (the column images)
		:param skins_number: Number of skins in the spritesheet (the row images)
		:param cooldown: Refresh rate for the animation
		to be added -> :param Animated: A boolean to consider animation or not
		"""
		self.sheet = sheet 						# The sheet to extract the frames from
		skinsNumber = int(self.sheet.get_height() / height)
		self.skin = [0] * skinsNumber			# Array of the skins found in the spritesheet
		framesNumber = int(self.sheet.get_width() / width) if frames_number != 1 else 1
		hasSound = (len(sounds) != 0)
		# Extracting the frames for each skin
		for s in range(skinsNumber):
			frames = [0] * framesNumber
			for f in range(framesNumber):
				frames[f] = self.extract_frame(width, height, scale, f, s)
			self.skin[s] = Skin(frames, cooldown) if frames_number != 1 else frames[0]
			if hasSound:
				self.skin[s].setSound(sounds[s])

	def extract_frame(self, width, height, scale, f, s):
		"""
		Function to extract the image (width x height) from the stored
		spritesheet as it's the (f)^th frame in the (s)^th skin.
		
		:param width: The width of a single frame
		:param height: The height of a single frame
		:param scale: Scale to be adjusted
		:param f: The frame number to be extraced
		:param s: The skin number to extract its frame

		Retunes a pygame.Surface that holds the extracted image
		"""
		image = pygame.Surface((width, height))
		image.blit(self.sheet, (0, 0),
					(	 
					(f * width)		   , (s * height),
					(f * width + width), (s * height + height)
					))
		image = pygame.transform.scale(image, (width * scale, height * scale)) # scaling
		image.set_colorkey((0, 0, 0)) # Transparency - removes black color
		return image
