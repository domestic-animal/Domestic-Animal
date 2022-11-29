import sys
sys.path.insert(0, './Entities')
from bullet import bullet

import pygame
import os

img= pygame.image.load(os.path.join("Assets","Enemies_26x26_[6,2].png"))

def test_bullet():
	#assumtion
	temp=bullet(10,20,img,50,5,0,1)
	
	# action
	temp.move()
	
	assert temp.y==25
