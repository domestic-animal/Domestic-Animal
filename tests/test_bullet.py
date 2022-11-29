import sys

from Entities.bullet import bullet
from Entities.entity import entity

import pygame
import os

img=YELLOW_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))

def test_bullet():
	#assumtion
	temp=bullet(10,20,img,50,5,1)
	
	# action
	temp.move()
	
	assert temp.y==25