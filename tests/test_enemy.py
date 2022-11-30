import sys
sys.path.insert(0, './Entities')
sys.path.insert(0, './assets_handler')
from enemy import dog
from enemy import cat
from spritesheet import SpriteSheet
import pygame
import os

enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
ENEMY_SKINS = SpriteSheet(enemy_sheet,26,26,1,2,6).skin

def test_dog_noraml():
	#assumtion
	temp=dog(10,50,20,None,ENEMY_SKINS[0],50,20,(500,500))
	
	# action
	temp.move()
	
	assert temp.y==40 and temp.x==10

def test_dog_threash():
	#assumtion
	temp = dog(10,50,500,None,ENEMY_SKINS[0],50,20,(500,500))

	# action
	temp.move()
	
	assert temp.y==500

def test_cat_noraml():
	#assumtion
	temp=cat(10,50,20,None,ENEMY_SKINS[0],50,20,(500,500))
	
	# action
	temp.move()
	
	assert temp.y==40 and temp.x==10
	
def test_cat_threash():
	#assumtion
	temp=cat(100,50,510,None,ENEMY_SKINS[0],50,40,(500,510))
	
	# action
	temp.move()
	
	assert temp.y==510 and temp.x==140
	
def test_cat_threash_2():
	#assumtion
	temp=cat(470,50,510,None,ENEMY_SKINS[0],50,40,(500,510))
	
	# action
	temp.move()
	
	assert temp.y==510 and temp.x==430
