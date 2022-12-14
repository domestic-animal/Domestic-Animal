import sys
import pygame
import os
sys.path.insert(0, './Entities')

from player import player
from weapon import weapon
from powerup import DamagePowerUP
from powerup import HealthPowerUP
from powerup import FireRatePowerUP
from powerup import ScorePowerUP

sys.path.insert(0, './assets_handler')
from spritesheet import SpriteSheet

enemy_sheet = pygame.image.load(os.path.join("Assets", "Enemies_26x26_[6,2].png"))
png = SpriteSheet(enemy_sheet,26,26,1,2,6).skin[0]
PLAYER_CONTROLS=[]

## test health power up
## test health power up
def test_health():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=HealthPowerUP(300,600,png,500,1)
	
	# action
    testobj.health-=500
    power.add_powerup(testobj)
	
    assert testobj.health==1000

## test damage power up
def test_damage():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=DamagePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
	
    assert testobj.weapon.damage==60

	
def test_damage_2():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=DamagePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
	
    assert testobj.weapon.damage==70


def test_damage_threashhold():
	#assumtion
    we = weapon(png, -1, damage=260, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=DamagePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)

    assert testobj.weapon.damage==260

def test_damage_threashhold2():
	#assumtion
    we = weapon(png, -1, damage=130, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=DamagePowerUP(300,600,png,500,2)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)

    assert testobj.weapon.damage==130

## test score power up
def test_score():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=ScorePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
	
    assert testobj.ScoreMultiplayer==2


def test_score_2():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=ScorePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
	
    assert testobj.ScoreMultiplayer==3


def test_score_threashhold():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=ScorePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)

	
    assert testobj.ScoreMultiplayer==10

def test_score_threashhold2():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=ScorePowerUP(300,600,png,500,2)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)

	
    assert testobj.ScoreMultiplayer==5


## test fire rate of the powerups	
def test_rate():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=FireRatePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
	
    assert testobj.weapon.fire_rate==9


def test_rate_2():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=FireRatePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
	
    assert testobj.weapon.fire_rate==8

def test_rate_threashhold():
	#assumtion
    we = weapon(png, -1, damage=50, fire_rate=10)
    testobj=player(300,600,we,png,PLAYER_CONTROLS,1000,7)
    power=FireRatePowerUP(300,600,png,500,1)
	
	# action
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
    power.add_powerup(testobj)
	
    assert testobj.weapon.fire_rate==1