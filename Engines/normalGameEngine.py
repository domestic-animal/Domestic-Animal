import os
import random
import pygame
import sys
"""
    Normal Game Engine that runs both the Story mode
    and the Endless mode using the level given
"""
from Engines.level import level
#from observer import observer as observe
sys.path.insert(0, './Entities')
from player import player
from weapon import weapon
from bullet import bullet
from powerfactory import PowerUpFactory
from Engines.observer import observer
from Engines.level import endlesslevel
from Engines.menueEngine import menu
from Engines.gameState import gameState
class normalGameEngine:

    # Player player

    def __init__(self,window, level,profile, playerAssets , enemyAssets,
                 gameAssets, settings1, powerUps=0,
                 diff = 1,score=0,is_coop=1):
        """
            Constructor

            parameters:
            window: pygame window to draw in
            level: the level to be played in the engine
            diff: the difficulity chosen
            playerAssets: player's Assets to be drawn on the window
            profile: currently logged in profile
            enemyAssets: enemy Assets to be drawn on the window
            gameAssets: any extra assets such as background
            settings: player's controls
            powerUps: how many powerups are allowed
        """

        self.WIN = window
        self.playerAssets = playerAssets
        self.enemyAssets = enemyAssets
        self.gameAssets = gameAssets
        self.settings1 = settings1
        self.settings2 = settings1
        self.PLAYER1_CONTROLS = [settings1["left"],settings1["right"],settings1["up"],settings1["down"]]
        self.PLAYER2_CONTROLS =  [settings1["left"],settings1["right"],settings1["up"],settings1["down"]]
        self.level = level
        self.profile = profile
        self.is_coop=is_coop
        self.diff = diff

        #rat enemy for higher difficulty
        self.rats = enemyAssets[0]
        # pause menu
        self.menuengine = menu(self.WIN, 600,800)
        self.menuengine.create_menue(1)

        #constant attributes
        self.Enemies = []
        self.Bullets = []
        self.Players = []
        self.powerup=[]
        self.score=score
        self.gameObserver = observer()
        self.powerFactory=PowerUpFactory(self.playerAssets[2],self.playerAssets[2],self.playerAssets[2],self.playerAssets[2],self.playerAssets[2])
        self.main_font = pygame.font.SysFont("comicsans", 40)


    def create_player(self):
        
        #player Entity
        we1 = weapon(self.playerAssets[1], -1, damage=45, fire_rate=20)
        pl1=player(300,600,we1,self.playerAssets[0],self.PLAYER1_CONTROLS,200,7)
        self.Players.append(pl1)

        if self.is_coop==2:
            we2 = weapon(self.playerAssets[3], -1, damage=45, fire_rate=20)
            pl2=player(400,600,we2,self.playerAssets[2],self.PLAYER2_CONTROLS,200,7)
            self.Players.append(pl2)
    
    def move_entities(self,keys):
        #detect player movement
            for player in self.Players:
                player.move(keys, 600, 800)

            #move enemies and shoot
            for enemy in self.Enemies:
                enemy.move()
                Bullet = enemy.shoot()
                if Bullet != None:
                    self.Bullets.append(Bullet)
            
            #move bullets
            for bullet in self.Bullets:
                bullet.move()

            #move powerups
            for powers in self.powerup:
                powers.move()


    def shoot(self,keys):
            if keys[self.settings1["fire"]]: 
                Bullet=self.Players[0].shoot()
                if Bullet!= None:
                    self.Bullets.append(Bullet)
            if self.is_coop==2 and  keys[self.settings2["fire"]]:
                Bullet=self.Players[1].shoot()
                if Bullet!= None:
                    self.Bullets.append(Bullet)
    

    def inviciblility_cooldown(self):
        for player in self.Players:
            if player.cool_down > 0:
                   player.cool_down -= 1


    def generate_rat(self):
            # to do : with difficulity
        if (random.randint(0, (12/self.diff)* 60) == 1):
            player = random.choice(self.Players)
            rat_movement = random.choice([(0, 1), (600, -1)])
            rat = bullet(rat_movement[0], player.y, self.rats, 20*self.diff, 5*self.diff, rat_movement[1], 1)
            self.Bullets.append(rat)
    
    # function to get the current game score
    def getGameState(self):
        return gameState(self.Bullets,self.Players, self.Enemies, self.diff,1,-1,pygame.time.Clock().get_time())

     # function to draw  the window
    def redraw_window(self):
            """
                drawing function to redraw every frame
            """
            # drawing background
            self.WIN.blit(self.gameAssets[0], (0, 0))
            scores_label = self.main_font.render(f"score: {self.score}", 1, (255,255,255))
            self.WIN.blit(scores_label,(10, 10))
            # drawing player
            for i in self.Players:
                i.draw(self.WIN)
            #drawing Enemies
            for i in self.Enemies:
                i.draw(self.WIN)
            #drawing bullets
            for i in self.Bullets:
                i.draw(self.WIN)
            #drawing powerups
            for i in self.powerup:
                i.draw(self.WIN)
            #update the display
            pygame.display.update()


    # function to create the power ups the power 
    def insertpowerup(self):
      if (random.randint(0, (12/self.diff)* 60) == 1):
            powers=["h","d","s","r","i"]
            choice=random.choice(powers)
            x=random.randint(50,550)
            z=self.powerFactory.create(choice,x,-50,self.is_coop)
            self.powerup.append(z)            
        

    def start(self):
        """
            function used to start the game engine 
        """
        ####    Intitalization      ####
        #################################
        self.create_player()
        #storage lists
        FPS = 60
        clock = pygame.time.Clock()
        #generate the wave
        self.Enemies=self.level.getwave(1)

        ####    Main game loop      ####
        ################################
        while True:
            #drawing FPS
            clock.tick(FPS)
            #draw everything
            self.redraw_window()
            #generate a new wave when the wave is cleared
            if len(self.Enemies) == 0:
                self.Enemies = self.level.getwave(1)

            #detect the keys pressed
            keys = pygame.key.get_pressed()
            # detect shooting
            self.shoot(keys)
            #move entities 
            self.move_entities(keys)
            #reduce invicibity cooldowns
            self.inviciblility_cooldown()
            ##generate rat
            self.generate_rat()
            #generate power up
            self.insertpowerup()
            
            #observe game state and update it accordingly
            #observe collisions
            self.gameObserver.collision(self.Bullets, self.Enemies, self.Players)
            #observe dead enemies
            self.score+=self.gameObserver.dead(self.Enemies,self.Players)
            #observe offscreen bullets
            self.gameObserver.off_screen(self.Bullets)
            #insert power up
            self.gameObserver.powerUpdate(self.powerup,self.Players)

            #pasue menu
            if keys[pygame.K_ESCAPE]: # shoot
                selection = self.menuengine.start()
                if selection == "save":
                    pass
                if selection == "runAway":
                    return "menu"
                    
            #on death or quitting
            if self.is_coop > 1:
                if self.Players[0].health <= 0 and self.Players[1].health <= 0:
                        return "menu"
            else:
                if self.Players[0].health <= 0:
                    return "menu"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "runAway"
                    



            
