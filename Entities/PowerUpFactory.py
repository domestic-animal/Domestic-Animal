import PowerUp
class PowerUpFactory:

    def __init__(self, health, damage,score,rate,immune):
        self.health_image=health
        self.damage_image=damage
        self.score_image=score
        self.rate_image=rate
        self.immune_image=immune

        
    def create(self,type,x,y,velocity,threshold):
        if type=="h":
            return PowerUp.HealthPowerUP(x,y,self.health_image,velocity,threshold)

        elif type=="d":
            return PowerUp.DamagePowerUP(x,y,self.damage_image,velocity,threshold)

        elif type=="s":
            return PowerUp.ScorePowerUP(x,y,self.score_image,velocity,threshold)

        elif type=="r":
            return PowerUp.FireRatePowerUP(x,y,self.rate_image,velocity,threshold)

        elif type=="i":
            return PowerUp.ImmunityPowerUP(x,y,self.immune_image,velocity,threshold)
            
        else: 
            return None