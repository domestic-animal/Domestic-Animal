import sys
sys.path.insert(0, './Entities')
sys.path.insert(0, './assets_handler')
from enemy import dog
from enemy import cat
from enemy import bossDog
from enemy import bossCat
from enemyFactory import enemyFactory
from spritesheet import SpriteSheet
import pygame
import os

enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
ENEMY_SKINS = SpriteSheet(enemy_sheet,26,26,1,2,6).skin

bullet_sheet = pygame.image.load(os.path.join("Assets", "Bullets_10x16_[4,2].png"))
BULLET_SHIP_SKINS = SpriteSheet(bullet_sheet,10,16,1,2).skin

def test_right_instance():
    
    factor=enemyFactory(ENEMY_SKINS,ENEMY_SKINS,ENEMY_SKINS)
    
    temp1=factor.create("d",1,50,50,(600,600))
    
    temp2=factor.create("c",1,50,50,(600,600))

    temp3=factor.create("bd",1,50,50,(600,600))

    temp4=factor.create("bc",1,50,50,(600,600))

    temp5=factor.create("lk",1,50,50,(600,600))

    assert isinstance(temp1, dog) and isinstance(temp2, cat) and  isinstance(temp3, bossDog) and isinstance(temp4, bossCat) and temp5==None
