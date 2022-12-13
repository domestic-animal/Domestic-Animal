import sys
import pygame
import os
sys.path.insert(0, './Entities')
from player import player
from weapon import weapon

from powerup import DamagePowerUP
from powerup import HealthPowerUP
from powerup import ImmunityPowerUP
from powerup import FireRatePowerUP
from powerup import ScorePowerUP
from powerupFactory import PowerUpFactory

sys.path.insert(0, './assets_handler')
from spritesheet import SpriteSheet

enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
png = SpriteSheet(enemy_sheet,26,26,1,2,6).skin[0]
PLAYER_CONTROLS=[]

def test_power_factor():
    #assumtion
    factor=PowerUpFactory(png,png,png,png,png)

    #action
    health=factor.create("h",100,100,100,1000)
    damage=factor.create("d",100,100,100,1000)
    Score=factor.create("s",100,100,100,1000)
    rate=factor.create("r",100,100,100,1000)
    immue=factor.create("i",100,100,100,1000)
    none=factor.create("k",100,100,100,1000)
  
    assert  isinstance(health, HealthPowerUP) and isinstance(damage, DamagePowerUP) and isinstance(Score, ScorePowerUP) and isinstance(rate, FireRatePowerUP) and isinstance(immue, ImmunityPowerUP) and none==None

	