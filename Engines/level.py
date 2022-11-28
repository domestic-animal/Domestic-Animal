import random
import sys
sys.path.insert(0, './Entities')
from enemyFactory import enemyFactory
from enemy import enemy

class level:
    def __init__(self,diff):
        self.waves=[]
        self.index=None
        self.diff=diff

    def getwave(self,time):
        pass


class randomround():
    def easyround(self):
        x=random.random()
        if x<0.7:
            return 1
        elif x>0.7 and x<0.9:
            return 2
        else:
            return 3   

    def mediuamround(self):
        x=random.random()
        if x<0.2:
            return 1
        elif x>0.2 and x<0.9:
            return 2
        else:
            return 3  

    def hardround(self):
        x=random.random()
        if x<0.1:
            return 1
        elif x>0.1 and x<0.3:
            return 2
        else:
            return 3

    def getnumber(self,diff):
        if diff==1:
            return self.easyround()
        if diff==2:
            return self.mediuamround()
        else:
            return self.hardround()



class endlesslevel(level):
    def __init__(self, diff):
        super().__init__(diff)
        self.rand=randomround()
                   
    def getwave(self, time):
        if time>1:
            self.diff=2
        elif time>2:
             self.diff=3
        enemies=[]
        factor=enemyFactory()
        x=20
        y=0
        threshy=400
        for _ in range(5):
            threshy-=50
            for _ in range(5):
                type=random.choice(["d","c"])
                enemy=factor.create(type,self.rand.getnumber(self.diff),x,y,(600,threshy))
                enemies.append(enemy)
                x+=20
        return enemies



        
    
