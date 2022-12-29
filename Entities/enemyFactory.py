import enemy
import sys
sys.path.insert(0, './assets_handler')


from weapon import weapon
import random
class enemyFactory:
    def __init__(self, BULLET_SKINS, ENEMY_SKINS,BOSSES_SKINS):
        #change skins according to difficulity
        self.DOG = ENEMY_SKINS[3]
        self.DOG2 = ENEMY_SKINS[2]

        self.CAT = ENEMY_SKINS[0]
        self.CAT2 = ENEMY_SKINS[1]

        self.CAT_LASER = BULLET_SKINS[0]
        self.CAT_LASER2 = BULLET_SKINS[1]
        self.DOG_LASER = BULLET_SKINS[2]
        self.DOG_LASER2 = BULLET_SKINS[3]
        self.DOG_LASER2.scale((30,30))
        self.BOSSCAT = BOSSES_SKINS[1]
        self.BOSSDOG = BOSSES_SKINS[0]


    def create(self,type,diff,x,y,threshold):
        if type=="d":
            w = weapon(self.DOG_LASER, 1, 0,1,int(700/diff),15*diff,2*diff)
            typeSkin=random.randint(1,2)
            if(typeSkin==1):
                return enemy.dog(x, 5*diff, y, w,  self.DOG,  100*diff,  5*diff,  threshold,  15*diff)
            return enemy.dog(x, 5*diff, y, w,  self.DOG2,  100*diff,  5*diff,  threshold,  15*diff)
        elif  type=="c":
            w = weapon(self.CAT_LASER, 1,0,1, int(600/diff),26*diff,2*diff)
            typeSkin=random.randint(1,2)
            if(typeSkin==1):
                return enemy.cat(x,  7*diff,  y,  w,  self.CAT,  50*diff,  5*diff,  threshold,  10*diff)
            return enemy.cat(x,  7*diff,  y,  w,  self.CAT2,  50*diff,  5*diff,  threshold,  10*diff)
        elif type =="bd":
            self.BOSSDOG.scale((200,250))
            w = weapon(self.DOG_LASER, 1,0,1, int(10/diff),20*diff,5*diff)

            w2 = weapon(self.DOG_LASER2, 1, 0,1,int(10/diff),50*diff,2*diff)
            w3 = weapon(self.DOG_LASER2, 1, 0,1,int(10/diff),50*diff,2*diff)
            return enemy.bossDog(x,  20*diff,  y,  w, w2, w3,self.BOSSDOG,  5000*diff,  4*diff,  threshold,  1000*diff)
        elif type == "bc":
            self.BOSSCAT.scale((100,150))
            w = weapon(self.CAT_LASER2, 1, 0,1,int(10/diff),20*diff,5*diff)
            return enemy.bossCat(x,  20*diff,  y,  w,self.BOSSCAT,  1000*diff,  6*diff,  threshold,  1000*diff)
        else: 
            return None

