class gameState():

    def __init__(self,powerups,score,bullets,players,enemies,difficulty,isExit,level,time,gameover,is_coop,wavenumber):
        
        self.powerups=powerups
        self.bullets=bullets
        self.players=players
        self.enemies=enemies
        self.difficulty=difficulty
        self.level=level
        self.time=time
        self.Score=score
        self.isExit=isExit
        self.gameover=gameover
        self.is_coop = is_coop
        self.waveNumber = wavenumber
