import sys
sys.path.insert(0, './Entities')
sys.path.insert(0, './assets_handler')
from bullet import bullet
from spritesheet import SpriteSheet
import pygame
import os


bullet_sheet = pygame.image.load(os.path.join("Assets", "Bullets_10x16_[4,2].png"))
BULLET_SHIP_SKINS = SpriteSheet(bullet_sheet,10,16,1,2).skin
def test_bullet_vertical():
	#assumtion
	temp=bullet(10,20,BULLET_SHIP_SKINS[0],50,5,0,1)
	
	# action
	temp.move()
	
	assert (temp.y==25 and temp.x==10)
	
def test_bullet_vertical():
	#assumtion
	temp=bullet(10,20,BULLET_SHIP_SKINS[0],50,5,1,1)
	
	# action
	temp.move()
	
	assert (temp.y==20 and temp.x==15)
	
def test_off_screen():
        #assumtion
        temp = bullet(10,20,BULLET_SHIP_SKINS[0],50,5,0,1)
        temp2 = bullet(800,1000,BULLET_SHIP_SKINS[0],50,5,1,1)
        temp3 = bullet(10,1000,BULLET_SHIP_SKINS[0],50,5,1,1)
        temp4 = bullet(800,20,BULLET_SHIP_SKINS[0],50,5,1,1)

        # action
        test1=temp.off_screen(600,800)
        test2=temp2.off_screen(600,800)
        test3=temp3.off_screen(600,800)
        test4=temp4.off_screen(600,800)
                 


        assert test1==False and test2==True and test3==True and test4==True
