import pygame

""" the game observer observes the game 
    state and updates it accordingly
"""
class observer:
    def __init__(self,windowX,windowY):
        self.windowX = windowX
        self.windowY = windowY

    def off_screen(self,bullets):
        """checks if bullets are off screen it removes them

        Args:
            bullets (list of bullets): current list of bullets 
        """
        for bullet in bullets[:]:
            if bullet.off_screen(self.windowX,self.windowY):
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
        return (obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None)

class gameobserver(observer):
    def __init__(self,windowX,windowY):
        super().__init__(windowX,windowY)
    def collision(self,bullets,enemies,players):
        """checks if all object have collided with something or not

        Args:
            bullets (bullet list): list of current bullets
            enemies (enemy list): list of current enemies
            player (player): current player
        """
        # loop on all bullets and damage the enemy or player
        for Bullet in bullets:
            #if the bullets are friendly (-1)
            if Bullet.is_friendly==0:
                for Enemy in enemies:
                    if self.is_collide(Bullet,Enemy):
                        Bullet.Objectdamage(Enemy)
                        break
            #if the bullets are not friendly (1)
            else:
                for Player in players:
                    if Player.cool_down <=0 and self.is_collide(Bullet,Player):
                        Bullet.Objectdamage(Player)

        # if the player collided with an enemy there is some invinciblity frames
        for Player in players:
            if Player.cool_down <=0:
                for Enemy in enemies:
                        if self.is_collide(Enemy,Player):
                                Enemy.health -= Enemy.damage
                                Player.health -= Enemy.damage
                                # Player.cool_down=3


        
    
    def dead(self,enemies,players, graveyard):
        """checks if the given list of enemies are dead

        Args:
            enemies (enemy list): current list of enemies
        """
        multi=0
        score=0
        for Player in players:
            multi+=Player.ScoreMultiplayer
        for Enemy in enemies[:]:
            if Enemy.health<=0:
                score=multi*Enemy.score
                Enemy.skin.playSound()
                enemies.remove(Enemy)
        for Player in players:
            if Player.health <= 0:
                graveyard.append(Player)
                Player.dead = 1
                players.remove(Player)
        return score


    def powerUpdate(self,powerup,players):
        for Power in powerup[:]:
            for Player in players:
                if self.is_collide(Power,Player):
                    Power.add_powerup(Player)
                    Power.skin.playSound()
                    powerup.remove(Power)
                    break
            if Power.off_screen(self.windowY):
                powerup.remove(Power)


class vsobserver(observer):
    def __init__(self,windowX,windowY):
        super().__init__(windowX,windowY)
 
    def collision(self,bullets,players):
        """checks if all object have collided with something or not

        Args:
            bullets (bullet list): list of current bullets
            enemies (enemy list): list of current enemies
            player (player): current player
        """
        # loop on all bullets and damage the enemy or player
        for Bullet in bullets:
            #if the bullets are friendly (-1)
            if Bullet.is_friendly>0:
                if self.is_collide(players[1],Bullet):
                  Bullet.Objectdamage(players[1])
            else:
                if self.is_collide(players[0],Bullet):
                  Bullet.Objectdamage(players[0])