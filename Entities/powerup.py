from entity import entity

#power up main class to keep it dry
class PowerUp(entity):

    # main constructor
    def __init__(self, x, y,image,velocity,threshold):
        super().__init__(x,y,image,velocity)
        self.threshold=threshold
    
    #move function for all the power up
    def move(self):
        self.y=self.y+self.velocity
    
    def add_powerup(self,player):
        pass

    def off_screen(self,height):
        return not(self.y <= height)

class DamagePowerUP(PowerUp):
    
    def __init__(self, x, y,image,velocity,threshold):
        super().__init__(x,y,image,velocity,threshold)
    
    def add_powerup(self,player):
        x=player.weapon.damage
        if x <self.threshold:
            player.weapon.damage=x+10

class HealthPowerUP(PowerUp):
    
    def __init__(self, x, y,image,velocity,threshold):
        super().__init__(x,y,image,velocity,threshold)
    
    def add_powerup(self,player):
        player.health=player.max_health
    
class ImmunityPowerUP(PowerUp):
    
    def __init__(self, x, y,image,velocity,threshold):
        super().__init__(x,y,image,velocity,threshold)
    
    def add_powerup(self,player):
        player.cool_down=10*60     


class FireRatePowerUP(PowerUp):
    
    def __init__(self, x, y,image,velocity,threshold):
        super().__init__(x,y,image,velocity,threshold)
    
    def add_powerup(self,player):
        x=player.weapon.fire_rate
        if x <self.threshold:
            player.weapon.fire_rate=x+5



class ScorePowerUP(PowerUp):
    
    def __init__(self, x, y,image,velocity,threshold):
        super().__init__(x,y,image,velocity,threshold)
    
    def add_powerup(self,player):
        x=player.ScoreMultiplayer
        if x <self.threshold:
            player.ScoreMultiplayer=x+1