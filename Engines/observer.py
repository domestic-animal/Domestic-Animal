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
        for i in bullets[:]:
            if i.off_screen(600,800):
                bullets.remove(i)

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


    def collision(self,bullets,enemies,player):
        """checks if all object have collided with something or not

        Args:
            bullets (bullet list): list of current bullets
            enemies (enemy list): list of current enemies
            player (player): current player
        """
        # loop on all bullets and damage the enemy or player
        for i in bullets:
            #if the bullets are friendly (-1)
            if i.is_friendly<0:
                for j in enemies:
                    if self.is_collide(i,j):
                        i.damage(j)
                        break
            #if the bullets are not friendly (1)
            else:
                if player.cool_down <=0 and self.is_collide(i,player):
                   i.damage(player)
        # if the player collided with an enemy there is some invinciblity frames
        if player.cool_down <=0:
            for i in enemies:
                    if self.is_collide(i,player):
                            i.health -= i.damage
                            player.health -= i.damage
                            player.cool_down=30


        
    
    def dead(self,enemies):
        """checks if the given list of enemies are dead

        Args:
            enemies (enemy list): current list of enemies
        """
        for i in enemies[:]:
            if i.health<0:
                enemies.remove(i)