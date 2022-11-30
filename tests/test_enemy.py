import sys
sys.path.insert(0, './Entities')
sys.path.insert(0, './assets_handler')
from enemy import dog
from spritesheet import SpriteSheet
import pygame
import os

enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
ENEMY_SKINS = SpriteSheet(enemy_sheet,26,26,1,2,6).skin
def test_bullet():
	#assumtion
	temp=dog(10,50,20,None,ENEMY_SKINS[0],50,20,(500,500))
	
	# action
	temp.move()
	
	assert temp.y==40
