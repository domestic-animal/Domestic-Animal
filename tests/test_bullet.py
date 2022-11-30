import sys
sys.path.insert(0, './Entities')
sys.path.insert(0, './assets_handler')
from bullet import bullet
from spritesheet import SpriteSheet
import pygame
import os


bullet_sheet = pygame.image.load(os.path.join("Assets", "Bullets_10x16_[4,2].png"))
BULLET_SHIP_SKINS = SpriteSheet(bullet_sheet,10,16,1,2).skin
def test_bullet():
	#assumtion
	temp=bullet(10,20,BULLET_SHIP_SKINS[0],50,5,0,1)
	
	# action
	temp.move()
	
	assert temp.y==25
