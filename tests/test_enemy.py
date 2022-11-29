import sys
sys.path.insert(0, './Entities')
from enemy import dog
import pygame
import os

img= pygame.image.load(os.path.join("Assets","Enemies_26x26_[6,2].png"))

def test_bullet():
	#assumtion
	temp=dog(10,50,20,None,img,50,20,(500,500))
	
	# action
	temp.move()
	
	assert temp.y==40
