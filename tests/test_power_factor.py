import sys
import pygame
import os
sys.path.insert(0, './Entities')
from powerup import DamagePowerUP
from powerup import HealthPowerUP
from powerup import ImmunityPowerUP
from powerup import FireRatePowerUP
from powerup import ScorePowerUP
from powerfactory import PowerUpFactory

sys.path.insert(0, './assets_handler')
from spritesheet import SpriteSheet

enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
png = SpriteSheet(enemy_sheet,26,26,1,2,6).skin[0]
PLAYER_CONTROLS=[]

def test_power_factor_health():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    health=factor.create("h",100,100,1)
  
    assert  isinstance(health, HealthPowerUP)

def test_power_factor_damage():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    damage=factor.create("d",100,100,1)

  
    assert isinstance(damage, DamagePowerUP)

def test_power_factor_score():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    Score=factor.create("s",100,100,1)

  
    assert isinstance(Score, ScorePowerUP)


def test_power_factor_rate():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    rate=factor.create("r",100,100,1)

    assert isinstance(rate, FireRatePowerUP)

def test_power_factor_immue():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    immue=factor.create("i",100,100,1)

  
    assert isinstance(immue, ImmunityPowerUP)

def test_power_factor_wrong():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    none=factor.create("k",100,100,1)
  
    assert none==None
	