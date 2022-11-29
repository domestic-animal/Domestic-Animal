import pygame
class observer:
    def __init__(self):
        pass
    def off_screen(self,bullets):
        for i in bullets[:]:
            if i.off_screen(600,800):
                bullets.remove(i)

    def is_collide(self,obj1, obj2):
            print(obj1.width)
            print(obj2.height)
            if obj1.x > (obj2.x+obj2.width) or obj2.x > (obj1.x+obj1.width) :
                return False
            if obj1.y+obj1.height > obj2.y or obj2.y+obj2.height > obj1.y:
                return False
            return True

    def collision(self,bullets,enemies,player):
        for i in bullets:
            if i.is_friendly<0:
                for j in enemies:
                    print(self.is_collide(i,j))
                    if self.is_collide(i,j):
                        j.health-=i.damage
                        i.y=-40
                        break

            else:
                if player.cool_down <=0 and self.is_collide(i,player):
                    player.health-=i.damage
                    i.y=-40

        if player.cool_down <=0:
            for i in enemies:
                    if self.is_collide(i,player):
                            i.health -= i.damage
                            player.health -= i.damage
                            player.cool_down=30


        
    
    def dead(self,enemies):
        for i in enemies[:]:
            if i.health<0:
                enemies.remove(i)