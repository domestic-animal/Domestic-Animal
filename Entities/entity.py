class entity:
    def __init__(self,x,y,image, velocity, ):
        self.x =x
        self.y = y
        self.image = image
        self.velocity = velocity

    def move():
        pass
    
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        