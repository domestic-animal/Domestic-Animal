import random
import sys
sys.path.insert(0, './Entities')
from enemyFactory import enemyFactory
from enemy import enemy

class level:
    def __init__(self,diff,ENEMY_SKINS,BULLET_SKINS):
        self.waves=[]
        self.index=None
        self.diff=diff
        self.ENEMY_SKINS = ENEMY_SKINS
        self.BULLET_SKINS = BULLET_SKINS

    def getwave(self,time):
        pass

class endlesslevel(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS)
                   
    def getwave(self,time):
        enemies=[]
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS)
        x=20
        y=0
        threshy=450
        for _ in range(8):
            threshy-=50
            x=20
            for _ in range(10):
                type=random.choice(["d","c"])
                enemy=factor.create(type,(self.diff),x,y,(600,threshy))
                enemies.append(enemy)
                x+=35
        return enemies



        
    
