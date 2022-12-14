import pygame

""" the game observer observes the game 
    state and updates it accordingly
"""
class observer:
    def __init__(self):
        pass
    def off_screen(self,bullets):
        """checks if bullets are off screen it removes them

        Args:
            bullets (list of bullets): current list of bullets 
        """
        for bullet in bullets[:]:
            if bullet.off_screen(600,800):
                bullets.remove(bullet)


    def is_collide(self,obj1, obj2):
        """checks if 2 objects collided

        Args:
            obj1 (Entity): 1st object
            obj2 (Entity): 2nd object

        Returns:
            boolean: true if collided and false if not
        """
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class gameobserver(observer):
    def __init__(self):
        pass
    def collision(self,bullets,enemies,players):
        """checks if all object have collided with something or not

        Args:
            bullets (bullet list): list of current bullets
            enemies (enemy list): list of current enemies
            player (player): current player
        """
        # loop on all bullets and damage the enemy or player
        for bullet in bullets:
            #if the bullets are friendly (-1)
            if bullet.is_friendly<0:
                for enemy in enemies:
                    if self.is_collide(bullet,enemy):
                        bullet.Objectdamage(enemy)
                        break
            #if the bullets are not friendly (1)
            else:
                for player in players:
                    if player.cool_down <=0 and self.is_collide(bullet,player):
                        bullet.Objectdamage(player)

        # if the player collided with an enemy there is some invinciblity frames
        for player in players:
            if player.cool_down <=0:
                for enemy in enemies:
                    for player in players:
                        if self.is_collide(enemy,player):
                                enemy.health -= enemy.damage
                                player.health -= enemy.damage
                                player.cool_down=30


        
    
    def dead(self,enemies,players):
        """checks if the given list of enemies are dead

        Args:
            enemies (enemy list): current list of enemies
        """
        multi=0
        score=0
        for player in players:
            multi+=player.ScoreMultiplayer
        for enemy in enemies[:]:
            if enemy.health<=0:
                score=multi*enemy.score
                enemies.remove(enemy)
        return score


    def powerUpdate(self,powerup,players):
        for power in powerup[:]:
            for player in players:
                if self.is_collide(power,player):
                    power.add_powerup(player)
                    powerup.remove(power)
                    break
            if power.off_screen(800):
                powerup.remove(power)


class vsobserver(observer):
    def __init__(self):
        pass
    def collision(self,bullets,players):
        """checks if all object have collided with something or not

        Args:
            bullets (bullet list): list of current bullets
            enemies (enemy list): list of current enemies
            player (player): current player
        """
        # loop on all bullets and damage the enemy or player
        for bullet in bullets:
            #if the bullets are friendly (-1)
            if bullet.is_friendly>0:
                if self.is_collide(players[1],bullet):
                  bullet.Objectdamage(players[0])
            else:
                if self.is_collide(players[0],bullet):
                  bullet.Objectdamage(players[1])