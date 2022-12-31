import powerup

class PowerUpFactory:

    def __init__(self, health, damage,score,rate,immune):
        self.health_image=health
        self.damage_image=damage
        self.score_image=score
        self.rate_image=rate
        self.immune_image=immune

        
    def create(self,type,x,y,threshold):
        if type=="h":
            return powerup.HealthPowerUP(x,y,self.health_image,5,threshold)

        elif type=="d":
            return powerup.DamagePowerUP(x,y,self.damage_image,5,threshold)

        elif type=="s":
            return powerup.ScorePowerUP(x,y,self.score_image,5,threshold)

        elif type=="r":
            return powerup.FireRatePowerUP(x,y,self.rate_image,5,threshold)

        elif type=="i":
            return powerup.ImmunityPowerUP(x,y,self.immune_image,5,threshold)
            
        else: 
            return None