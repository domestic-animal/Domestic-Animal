import pygame
from assets_handler.skin import Skin

class SpriteSheet():
	"""
	SpriteSheet class: handles the operations with the spritesheets png images
	that exist in the Assets folder.
		(spritesheet: A png image that holds the skins & their frames of a game entity
		ordered by shapes as rows & shape's frames as columns)
	"""
	
	def __init__(self, sheet, width, height, scale, frames_number, skins_number = 1, cooldown = 100, rotation = 0):
		"""
		Constructor: extracts the frames & sets the class attributes

		:param sheet: The image containing the spritesheet (after converting)
		:param width: The width of a single frame
		:param height: The height of a single frame
		:param scale: Scale to be adjusted
		:param frames_number: Number of frames in the spritesheet (the column images)
		:param skins_number: Number of skins in the spritesheet (the row images)
		:param cooldown: Refresh rate for the animation
		:param rotation: number of (90-degree)s to rotate the images (anti-clockwise -> +ve, clockwise -> -ve)
		"""
		self.sheet = sheet 						# The sheet to extract the frames from
		self.skin = [0] * skins_number			# Array of the skins found in the spritesheet
		# extracting the frames
		for s in range(skins_number):
			frame = [0] * frames_number
			for f in range(frames_number):
				frame[f] = self.get_image(width, height, scale, f, s, rotation)
			# if there is no animation (single frame) store the image directly,
			# otherwise store it as Skin object 
			self.skin[s] = frame[0] if frames_number == 1 else Skin(frame, cooldown)
		self.width = width * scale   			# The width after scaling (for coordination purposes)
		self.height = height * scale 			# The height after scaling (for coordination purposes)
		# Swapping dimenstion if it rotates 90 degrees
		if rotation % 2 == 1:
			self.width, self.height = self.height, self.width

	def get_image(self, width, height, scale, f, s, r):
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
					((f * width), (s * height),
					 (f * width + width), (s * height + height)))
		image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling
		image = pygame.transform.rotate(image, 90 * r) # rotating
		image.set_colorkey((0, 0, 0)) #Transparency - removes black color
		return image
