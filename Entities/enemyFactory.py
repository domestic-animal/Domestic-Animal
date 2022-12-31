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

                               
        self.numbers={1:#easy
                         #dog boss
                        [[15,40, #firerates
                           20,75,#damages
                           7,4, #bullet velocity
                          2500,  #HP
                            3],  #movement velocity
                            #cat boss 
                          [25,  #firerates
                          30,   #damages
                          7,   #bullet velocity
                          1500, #HP
                          6]],   #movement velocity
                                    
                    2:#medium
                    #dog boss
                    [[10,35,    #firerates
                        30,80,  #damages
                        10,5,   #fire velocity
                        3000,   #HP
                        4],     #movement velocity
                        #cat boss
                        [25,    #firerates
                        30,     #damages
                        10,     #bullet velocity          
                        2000,   #HP
                        7]],    #movement velocity

                    3:#hard
                    #dog boss                  
                    [[9,30,     #firerates
                        35,100, #damages
                        11,7,   #fire velocity
                        4000,   #HP
                        5],     #movement velocity 

                        [35,     #firerates
                        40,      #damages
                        10,      #bullet velocity     
                        3000,    #HP
                        8]] }    #movement velocity


    def create(self,type,diff,x,y,threshold):
        if type=="d":
            w = weapon(self.DOG_LASER, 1, 0,1,int(700/diff),15*diff,2*diff)
            typeSkin=random.randint(1,2)
            if(typeSkin==1):
                return enemy.dog(x, 5*diff, y, w,  self.DOG,  100*diff,  2*diff,  threshold,  15*diff)
            return enemy.dog(x, 5*diff, y, w,  self.DOG2,  100*diff,  2*diff,  threshold,  15*diff)
        elif  type=="c":
            w = weapon(self.CAT_LASER, 1,0,1, int(600/diff),20*diff,2*diff)
            typeSkin=random.randint(1,2)
            if(typeSkin==1):
                return enemy.cat(x,  7*diff,  y,  w,  self.CAT,  50*diff,  2.5*diff,  threshold,  10*diff)
            return enemy.cat(x,  7*diff,  y,  w,  self.CAT2,  50*diff,  2.5*diff,  threshold,  10*diff)
        elif type =="bd":
            self.BOSSDOG.scale((200,250))
            holder=self.numbers[diff]
            w = weapon(self.DOG_LASER, 1,0,1, holder[0][0],holder[0][2],holder[0][4])
            w2 = weapon(self.DOG_LASER2, 1, 0,1,holder[0][1],holder[0][3],holder[0][5])
            w3 = weapon(self.DOG_LASER2, 1, 0,1,holder[0][1],holder[0][3],holder[0][5])
            return enemy.bossDog(x,  20*diff,  y,  w, w2, w3,self.BOSSDOG,  holder[0][6] , holder[0][7] ,  threshold,  1000*diff)
        elif type == "bc":
            holder=self.numbers[diff]
            self.BOSSCAT.scale((100,150))
            w = weapon(self.CAT_LASER2, 1, 0,1,holder[1][0],holder[1][1],holder[1][2])
            return enemy.bossCat(x,  20*diff,  y,  w,self.BOSSCAT,  holder[1][3],  holder[1][4],  threshold,  1000*diff)
        else: 
            return None

