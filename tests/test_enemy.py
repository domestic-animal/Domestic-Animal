from Entities.enemy import dog
from Entities.entity import entity

import pygame
import os

img=YELLOW_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))

def test_bullet():
	#assumtion
	temp=dog(10,50,20,None,img,50,20,(500,500))
	
	# action
	temp.move()
	
	assert temp.y==40