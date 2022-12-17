import random
import sys
sys.path.insert(0, './Entities')
from enemyFactory import enemyFactory
from enemy import enemy


"""level abstract class

"""
class level:
    def __init__(self,diff,ENEMY_SKINS,BULLET_SKINS):
        """constructor

        Args:
            diff (int): difficulity of the level
            ENEMY_SKINS (list of skins): Enemy skin assets
            BULLET_SKINS (list of skins): bullet skin assets
        """
        self.waves=[]
        self.number=None
        self.diff=diff
        self.ENEMY_SKINS = ENEMY_SKINS
        self.BULLET_SKINS = BULLET_SKINS

    def getwave(self,time):
        pass

"""endless level impements the level abstract class
"""
class endlesslevel(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS)
        self.number=-1
    
    def getwave(self,time):
        """generates random waves every time it gets called

        Args:
            time (int): difficulity increases with time

        Returns:
            list of enemies
        """
        enemies=[]
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS)
        x=20
        y=0
        threshy=500
        for _ in range(8):
            threshy-=50
            x=20
            for _ in range(10):
                type=random.choice(["d","c"])
                enemy=factor.create(type,(self.diff),x,y,(600,threshy))
                enemies.append(enemy)
                x+=35
        return enemies


"""
this is level one 
"""
#level 1 
class levelOne(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS)
        self.number=1
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):

        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS)
        x=20
        y=0
        threshy=500
        for _ in range(2):
            enemies=[]
            for _ in range(8):
                threshy-=50
                x=20
                for _ in range(10):
                    enemy=factor.create("d",(self.diff),x,y,(600,threshy))
                    enemies.append(enemy)
                    x+=35
            self.waves.append(enemies)
            
    def getwave(self,time):
        """generates determinstic waves every time it gets called

        Returns:
            list of waves
        """
        if self.waveNumber<len(self.waves)-1:
            self.waveNumber+=1
            return self.waves[self.waveNumber-1]
        else:
            return None


"""
this is level two 
"""
#level 2
class levelTwo(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS)
        self.number=1
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS)
        x=20
        y=0
        threshy=500
        for _ in range(2):
            enemies=[]
            for _ in range(8):
                threshy-=50
                x=20
                for _ in range(10):
                    enemy=factor.create("c",(self.diff),x,y,(600,threshy))
                    enemies.append(enemy)
                    x+=35
            self.waves.append(enemies)

    def getwave(self,time):
        """generates determinstic waves every time it gets called

        Returns:
            list of waves
        """
        if self.waveNumber<len(self.waves)-1:
            self.waveNumber+=1
            return self.waves[self.waveNumber-1]
        else:
            return None


"""
this is level three 
"""
#level 3
class levelThree(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS)
        self.number=1
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS)
        x=20
        y=0
        threshy=500
        type="c"
        for _ in range(4):
            enemies=[]
            for _ in range(8):
                threshy-=50
                x=20
                if type=="c":
                    type="d"
                else:
                    type="c"
                for _ in range(10):
                    enemy=factor.create(type,(self.diff),x,y,(600,threshy))
                    enemies.append(enemy)
                    x+=35
            self.waves.append(enemies)
            
    def getwave(self,time):
        """generates determinstic waves every time it gets called

        Returns:
            list of waves
        """
        if self.waveNumber<len(self.waves)-1:
            self.waveNumber+=1
            return self.waves[self.waveNumber-1]
        else:
            return None


        
    
