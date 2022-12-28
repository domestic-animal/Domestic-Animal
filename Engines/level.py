import random
import sys
sys.path.insert(0, './Entities')
from Entities.enemyFactory import enemyFactory
from Entities.enemy import enemy


"""level abstract class

"""
class level:
    def __init__(self,diff,ENEMY_SKINS,BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
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
        self.BOSSES_SKINS = BOSSES_SKINS
        self.windowX = windowX
        self.windowY = windowY

    def getwave(self,timediffuclty):
        pass

class storylevel(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
            super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
            self.waveNumber=0
            self.waves = []

    def getwave(self,timediffuclty):
        """generates determinstic waves every time it gets called

        Returns:
            list of waves
        """
        if self.waveNumber<len(self.waves):
            self.waveNumber+=1
            return self.waves[self.waveNumber-1]
        else:
            return None
"""endless level impements the level abstract class
"""
class endlesslevel(level):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=-1
        self.waveNumber=0
    
    def getwave(self,timediffuclty):
        """generates random waves every time it gets called

        Args:
            time (int): difficulity increases with time

        Returns:
            list of enemies
        """
        self.waveNumber+=1
        enemies=[]
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS)
        x=20
        y=0
        threshy=450
        for _ in range(8):
            threshy-=50
            x=20
            for _ in range(10):
                type=random.choice(["d","c"])
                enemy=factor.create(type,timediffuclty,x,y,(self.windowX,threshy))
                enemies.append(enemy)
                x+= self.windowX/10
        return enemies


"""
this is level one 
"""
#level 1 
class levelOne(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=0
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS)
        x=20
        y=0
        threshy=450
        for _ in range(2):
            enemies=[]
            threshy = 450
            for _ in range(7):
                threshy-=50
                x=20
                for _ in range(10):
                    enemy=factor.create("d",self.diff,x,y,(self.windowX,threshy))
                    enemies.append(enemy)
                    x+=self.windowX/10
            self.waves.append(enemies)
            



"""
this is level two 
"""
#level 2
class levelTwo(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=1
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS)
        x=20
        y=0
        threshy=450
        for _ in range(2):
            enemies=[]
            threshy=450
            for _ in range(7):
                threshy-=50
                x=20
                for _ in range(10):
                    enemy=factor.create("c",self.diff,x,y,(self.windowX,threshy))
                    enemies.append(enemy)
                    x+=self.windowX/10
            self.waves.append(enemies)


"""
this is level three 
"""
#level 3
class levelThree(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=2
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS)
        x=20
        y=0
        threshy=500
        type="c"
        for _ in range(3):
            enemies=[]
            threshy=500
            for _ in range(8):
                threshy-=50
                x=20
                if type=="c":
                    type="d"
                else:
                    type="c"
                for _ in range(10):
                    enemy=factor.create(type,self.diff,x,y,(self.windowX,threshy))
                    enemies.append(enemy)
                    x+=self.windowX/10
            self.waves.append(enemies)
            

"""
this is level four 
"""
#level 4
class levelFour(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=3
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS)
        x=20
        y=0
        threshy=500
        type="c"
        for _ in range(5):
            enemies=[]
            threshy=500
            if _ == 4:
                boss_dog = factor.create("bd", self.diff,200,0,(self.windowX,self.windowY/2))
                enemies.append(boss_dog)
            else:
                for _ in range(7):
                    threshy-=50
                    x=20
                    if type=="c":
                        type="d"
                    else:
                        type="c"
                    for _ in range(10):
                        enemy=factor.create(type,self.diff,x,y,(self.windowX,threshy))
                        enemies.append(enemy)
                        x+=self.windowX/10
            self.waves.append(enemies)
            


"""
this is level five 
"""
#level 5
class levelFive(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=4
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS)
        x=20
        y=0
        threshy=550
        type="d"
        for _ in range(5):
            threshy=500
            enemies=[]
            for _ in range(9):
                    threshy-=50
                    x=20
                    if type=="c":
                        type="d"
                    else:
                        type="c"
                    for _ in range(10):
                        enemy=factor.create(type,self.diff,x,y,(self.windowX,threshy))
                        enemies.append(enemy)
                        x+=self.windowX/10
            self.waves.append(enemies)



"""
this is level six
"""
#level 6
class levelSix(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=5
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS )
        x=20
        y=0
        threshy=550
        type="d"
        for _ in range(6):
            threshy=550
            enemies=[]
            for _ in range(9):
                    threshy-=50
                    x=20
                    if type=="c":
                        type="d"
                    else:
                        type="c"
                    for _ in range(10):
                        enemy=factor.create(type,self.diff,x,y,(self.windowX,threshy))
                        enemies.append(enemy)
                        x+=self.windowX/10
            self.waves.append(enemies)
    

"""
this is level seven
"""
#level 7
class levelSeven(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=6
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS )
        x=20
        y=0
        threshy=500
        type="d"
        for _ in range(6):
            enemies=[]
            threshy=500
            if _ == 5:
                boss_cat = factor.create("bc", self.diff,200,0,(self.windowX,self.windowY))
                enemies.append(boss_cat)
            else:
                for _ in range(9):
                        threshy-=50
                        x=20
                        if type=="c":
                            type="d"
                        else:
                            type="c"
                        for _ in range(10):
                            enemy=factor.create(type,self.diff,x,y,(self.windowX,threshy))
                            enemies.append(enemy)
                            x+=self.windowX/10
            self.waves.append(enemies)


"""
this is level Eight
"""
#level 8
class levelEight(storylevel):
    def __init__(self, diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY):
        super().__init__(diff, ENEMY_SKINS, BULLET_SKINS,BOSSES_SKINS, windowX, windowY)
        self.number=7
        self.waveNumber=0
        self.makewaves()
    
    def makewaves(self):
        factor=enemyFactory(self.BULLET_SKINS,self.ENEMY_SKINS, self.BOSSES_SKINS )
        x= 200
        y=0
        threshy= 210
        boss_cat = factor.create("bc", self.diff,x,y,(self.windowX,self.windowY))
        boss_dog = factor.create("bd", self.diff,x,y,(self.windowX,threshy))
        self.waves.append([boss_cat,boss_dog])
        print(self.waves)