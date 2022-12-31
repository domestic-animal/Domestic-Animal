import datetime
import os
import random

import pygame

import filepath
from Engines.gameState import gameState
from Engines.levelSelector import levelSelector
from Entities.player import player
from Entities.powerfactory import PowerUpFactory
from Entities.weapon import weapon
from spritesheet import SpriteSheet
from filepath import ROOT_DIR


def create_profiles_path():
    profiles_path = os.path.join(ROOT_DIR, "profiles")
    if not os.path.exists(profiles_path):
        os.mkdir(profiles_path)


def create_random_game_state():
    damage = random.randint(45, 200)
    fire_rate = random.randint(25, 200)
    path = os.path.join(filepath.ROOT_DIR, "Assets")
    dummy_sheet = pygame.image.load(os.path.join(path, "Enemies_26x26_[6,2].png"))
    dummy_skins = SpriteSheet(dummy_sheet, 26, 26, 1.75, 2, 6).skin
    player_postion = (random.randint(0, 600), random.randint(0, 400))
    plyer = player(player_postion[0], player_postion[1], 1, (dummy_skins[0],dummy_skins[0]), [1,2,3], 200, 7,1,130)
    bullet = plyer.shoot()
    lvlSelector = levelSelector()
    level = lvlSelector.getLevel(-1, 1, dummy_skins, dummy_skins,dummy_skins, 600, 800)
    enemies = level.getwave(1)

    powerFactory = PowerUpFactory(dummy_skins[0], dummy_skins[0], dummy_skins[0], dummy_skins[0], dummy_skins[0])
    powerups = []
    powers = ["h", "d", "s", "r", "i"]
    for i in range(0, 5):
        x = random.randint(50, 550)
        powerup = powerFactory.create(powers[i], x, -50, 0)
        powerups.append(powerup)
    game_state = gameState(powerups, random.randint(0, 1000),
                           [bullet], plyer, enemies, random.randint(0, 10), 0,
                           level, datetime.date, random.randint(0, 2), 0, 1)

    return game_state


def check_bullets(created_bullets, returned_bullets):
    if len(created_bullets) != len(returned_bullets):
        return False

    check = True
    for i in range(len(created_bullets)):
        check = check & (created_bullets[i].x == returned_bullets[i].x)
        check = check & (created_bullets[i].y == returned_bullets[i].y)
        check = check & (created_bullets[i].damage == returned_bullets[i].damage)
        check = check & (created_bullets[i].velocity == returned_bullets[i].velocity)
        check = check & (created_bullets[i].ishorizontal == returned_bullets[i].ishorizontal)
        check = check & (created_bullets[i].is_friendly == returned_bullets[i].is_friendly)
    return check


def check_enemies(created_enemies, returned_enemies):
    if len(created_enemies) != len(returned_enemies):
        return False

    check = True
    for i in range(len(created_enemies)):
        check = check & (created_enemies[i].x == created_enemies[i].x)
        check = check & (created_enemies[i].y == created_enemies[i].y)
        check = check & (created_enemies[i].damage == created_enemies[i].damage)
        check = check & (created_enemies[i].health == created_enemies[i].health)
        check = check & (created_enemies[i].threshold == created_enemies[i].threshold)
        check = check & (created_enemies[i].score == created_enemies[i].score)
    return check


def check_player(created_player, returned_player):
    check = True

    check = check & (created_player.x == returned_player.x)
    check = check & (created_player.y == returned_player.y)
    check = check & (created_player.health == returned_player.health)
    check = check & (created_player.vs == returned_player.vs)
    return check


def check_power_ups(created_powerups, returned_powerups):
    if len(created_powerups) != len(returned_powerups):
        return False

    check = True
    for i in range(len(created_powerups)):
        check = check & (created_powerups[i].x == returned_powerups[i].x)
        check = check & (created_powerups[i].y == returned_powerups[i].y)
        check = check & (created_powerups[i].threshold == returned_powerups[i].threshold)
        check = check & (created_powerups[i].velocity == returned_powerups[i].velocity)
    return check


def check_game_state(created_state: gameState, returned_state: gameState):
    check = check_player(created_state.players, returned_state.players)
    check = check & check_enemies(created_state.enemies, returned_state.enemies)
    check = check & check_bullets(created_state.bullets, returned_state.bullets)
    check = check & (created_state.time == returned_state.time)
    check = check & (created_state.difficulty == returned_state.difficulty)
    check = check & (created_state.gameover == returned_state.gameover)
    check = check & (created_state.Score == returned_state.Score)
    check = check & (created_state.isExit == returned_state.isExit)
    return check

