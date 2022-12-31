import sys

sys.path.insert(0, './Entities')
sys.path.insert(0, './Engines')
sys.path.insert(0, './assets_handler')
from enemy import dog
from enemy import cat
from enemy import bossDog
from enemy import bossCat
from player import player
from bullet import bullet
from observer import gameobserver
from powerfactory import PowerUpFactory
from enemyFactory import enemyFactory
from spritesheet import SpriteSheet
import pygame
import os
enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
ENEMY_SKINS = SpriteSheet(enemy_sheet,26,26,1,2,6).skin

bullet_sheet = pygame.image.load(os.path.join("Assets", "Bullets_10x16_[4,2].png"))
BULLET_SHIP_SKINS = SpriteSheet(bullet_sheet,10,16,1,2).skin

def test_collisions_enemy_friendly_bullet():
    factor=enemyFactory(ENEMY_SKINS,ENEMY_SKINS,ENEMY_SKINS)
    gameObserver = gameobserver(800,800)
    tempenemy=[factor.create("d",1,300,400,(600,600))]
    tempbull = [bullet(300, 400, BULLET_SHIP_SKINS[0],50,4, 0,1,0),bullet(200, 600, BULLET_SHIP_SKINS[0],100,4, 0,1,1)]
    tempplayr = [player(200,600,1,(ENEMY_SKINS[0],BULLET_SHIP_SKINS[1]),[],1000,7)]
    gameObserver.collision(tempbull,tempenemy,tempplayr)

    assert tempenemy[0].health != 100

def test_collisions_player_non_friendly_bullet():
    factor=enemyFactory(ENEMY_SKINS,ENEMY_SKINS,ENEMY_SKINS)
    gameObserver = gameobserver(800,800)
    tempenemy=[factor.create("d",1,300,400,(600,600))]
    tempbull = [bullet(300, 400, BULLET_SHIP_SKINS[0],50,4, 0,1,0),bullet(200, 600, BULLET_SHIP_SKINS[0],100,4, 0,1,1)]
    tempplayr = [player(200,600,1,(ENEMY_SKINS[0],BULLET_SHIP_SKINS[1]),[],1000,7)]
    gameObserver.collision(tempbull,tempenemy,tempplayr)

    assert tempplayr[0].health != 1000

def test_collisions_player_enemy():
    factor=enemyFactory(ENEMY_SKINS,ENEMY_SKINS,ENEMY_SKINS)
    gameObserver = gameobserver(800,800)
    tempenemy=[factor.create("d",1,300,400,(600,600))]
    tempbull = [bullet(200, 600, BULLET_SHIP_SKINS[0],100,4, 0,1,1)]
    tempplayr = [player(300,400,1,(ENEMY_SKINS[0],BULLET_SHIP_SKINS[1]),[],1000,7)]
    gameObserver.collision(tempbull,tempenemy,tempplayr)

    assert tempplayr[0].health != 1000 and tempenemy[0].health != 100

def test_collisions_player_powerup():
    factor=PowerUpFactory(ENEMY_SKINS[0],ENEMY_SKINS[0],ENEMY_SKINS[0],ENEMY_SKINS[0],ENEMY_SKINS[0])
    gameObserver = gameobserver(800,800)
    temppower = [factor.create("h", 200,600,600)]
    tempbull = [bullet(300, 400, BULLET_SHIP_SKINS[0],50,4, 0,1,0),bullet(200, 600, BULLET_SHIP_SKINS[0],100,4, 0,1,1)]
    tempplayr = [player(200,600,1,(ENEMY_SKINS[0],BULLET_SHIP_SKINS[1]),[],1000,7)]
    gameObserver.collision(tempbull,[],tempplayr)
    gameObserver.powerUpdate(temppower,tempplayr)

    assert tempplayr[0].health == 1000 

def test_bullet_removal():
    factor=enemyFactory(ENEMY_SKINS,ENEMY_SKINS,ENEMY_SKINS)
    gameObserver = gameobserver(800,800)
    tempenemy=[factor.create("d",1,300,400,(600,600))]
    tempbull = [bullet(300, 400, BULLET_SHIP_SKINS[0],50,4, 0,1,0),bullet(200, 600, BULLET_SHIP_SKINS[0],100,4, 0,1,1)]
    tempplayr = [player(200,600,1,(ENEMY_SKINS[0],BULLET_SHIP_SKINS[1]),[],1000,7)]
    gameObserver.collision(tempbull,tempenemy,tempplayr)
    gameObserver.off_screen(tempbull)

    assert len(tempbull) == 0
