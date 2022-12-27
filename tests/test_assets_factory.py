from assets_handler.assetsFactory import assetsFactory
from assets_handler.skin import Skin
import pygame

ASSETS_FACTORY = assetsFactory()

def test_animated_skins():
    
    ships = ASSETS_FACTORY.create_skins("ships")
    bullets = ASSETS_FACTORY.create_skins("bullets")
    enemies = ASSETS_FACTORY.create_skins("enemies")
    powerups = ASSETS_FACTORY.create_skins("powerups")
    bosses = ASSETS_FACTORY.create_skins("bosses")
    enemies_bullets = ASSETS_FACTORY.create_skins("enemies_bullets")

    Nothing = ASSETS_FACTORY.create_skins("HELP!")

    for ship in ships:
        assert isinstance(ship, Skin)
    for bullet in bullets:
        assert isinstance(bullet, Skin)
    for enemy in enemies:
        assert isinstance(enemy, Skin)
    for powerup in powerups:
        assert isinstance(powerup, Skin)
    for boss in bosses:
        assert isinstance(boss, Skin)
    for enemy_bullet in enemies_bullets:
        assert isinstance(enemy_bullet, Skin)
        
    assert Nothing == None

def test_silent_skins():

    buttons = ASSETS_FACTORY.create_images("buttons")
    ships = ASSETS_FACTORY.create_images("ships")
    bullets = ASSETS_FACTORY.create_images("bullets")
    powerups = ASSETS_FACTORY.create_images("powerups")
    logos = ASSETS_FACTORY.create_images("logo")

    Nothing = ASSETS_FACTORY.create_images("HELP me!!")

    for button in buttons:
        assert isinstance(button, pygame.Surface)
    for ship in ships:
        assert isinstance(ship, pygame.Surface)
    for bullet in bullets:
        assert isinstance(bullet, pygame.Surface)
    for powerup in powerups:
        assert isinstance(powerup, pygame.Surface)
    for logo in logos:
        assert isinstance(logo, pygame.Surface)
    
    assert Nothing == None

def test_backgrounds():

    BGs = ASSETS_FACTORY.create_backgrounds()
    for bg in BGs:
        assert isinstance(bg, pygame.Surface)