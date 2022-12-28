import os
import random
import pygame
import sys
import time

"""
    Normal Game Engine that runs both the Story mode
    and the Endless mode using the level given
"""
#from observer import observer as observe
sys.path.insert(0, './Entities')
from Entities.player import player
from Entities.weapon import weapon
import datetime
from Entities.bullet import  bullet
from Entities.powerfactory import PowerUpFactory
from Engines.observer import gameobserver
from Engines.menueEngine import menu
from Engines.gameState import gameState
from file.gamestatesaver import GameStateSaver
from file.profile import Profile
class normalGameEngine:

    # Player player

    def __init__(self,window, level,profile:Profile, playerAssets , enemyAssets,
                 gameAssets,settings1, settings2,gameState=None,
                 diff = 1,score=0,is_coop=1, fileManager=None):
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
        """
        self.fileManager = fileManager
        self.gameState = gameState
        self.WIN = window
        self.playerAssets = playerAssets
        self.enemyAssets = enemyAssets
        self.gameAssets = gameAssets
        self.settings1 = settings1
        self.settings2 = settings2
        self.PLAYER1_CONTROLS = [settings1["left"],settings1["right"],settings1["up"],settings1["down"]]
        self.PLAYER2_CONTROLS =  [settings2["left"],settings2["right"],settings2["up"],settings2["down"]]
        self.level = level
        self.profile = profile
        self.is_coop=is_coop
        self.diff = diff

        #rat enemy for higher difficulty
        self.RAT_SKINS = enemyAssets[0]
        # pause menu
        self.menuengine = menu(self.WIN, self.WIN.get_width(),self.WIN.get_height(),self.profile, self.gameAssets[0],self.level.number)
        self.menuengine.create_menue(1)

        #constant attributes
        self.gameover = 0
        self.exit = 0
        self.Enemies = []
        self.Bullets = []
        self.Players = []
        self.powerup=[]
        self.graveyard = []
        self.score=score
        self.gameObserver = gameobserver(self.WIN.get_width(),self.WIN.get_height())
        self.gamesaver = GameStateSaver()
        self.powerFactory=PowerUpFactory(gameAssets[1][0],gameAssets[1][1],gameAssets[1][2],gameAssets[1][3],gameAssets[1][4])
        self.main_font = pygame.font.Font(os.path.join(".","launcher","assets","game.ttf"), 40)


    def create_player(self):
        
        #player Entity
       
        self.pl1=player(200,600,self.profile.get_current_weapon(),(self.playerAssets[0],self.playerAssets[1]),self.PLAYER1_CONTROLS,200,7)
        self.Players.append(self.pl1)

        if self.is_coop==2:
            self.pl2=player(400,600,self.profile.get_current_weapon(),(self.playerAssets[2],self.playerAssets[3]),self.PLAYER2_CONTROLS,200,7)
            self.Players.append(self.pl2)
    
    def move_entities(self,keys):
        #detect player movement
            for player in self.Players:
                player.move(keys, self.WIN.get_width(), self.WIN.get_height())

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
            if keys[self.settings1["fire"]]and self.pl1.dead ==0: 
                Bullet=self.pl1.shoot()
                if Bullet!= None:
                    self.Bullets.append(Bullet)
            if self.is_coop==2 and  keys[self.settings2["fire"]] and self.pl2.dead ==0:
                Bullet=self.pl2.shoot()
                if Bullet!= None:
                    self.Bullets.append(Bullet)
    

    def inviciblility_cooldown(self):
        for player in self.Players:
            if player.cool_down > 0:
                   player.cool_down -= 1


    def generate_rat(self):
            # to do : with difficulity
        if (random.randint(0, (18/self.diff)* 60) == 1 and (self.level.number>4 or self.level.number ==-1)):
            player = random.choice(self.Players)
            rat_movement = random.choice([(0, 1), (self.WIN.get_width(), -1)])
            RAT_SKIN = random.choice([self.RAT_SKINS[5], self.RAT_SKINS[4]])
            rat = bullet(rat_movement[0], player.y, RAT_SKIN, 30*self.diff, 5*self.diff, rat_movement[1], 0,1)
            self.Bullets.append(rat)
    
    # function to get the current game score
    def getGameState(self):
        return gameState(self.powerup,self.score,self.Bullets,self.Players, self.Enemies
        ,self.diff,self.exit,self.level.number,datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ,self.gameover,self.is_coop)

    def loadGameState(self):
            self.Bullets = self.gameState.bullets
            self.powerup = self.gameState.powerups
            self.score = self.gameState.Score
            self.Players = self.gameState.players
            self.Enemies = self.gameState.enemies
            self.is_coop = self.gameState.is_coop
            
     # function to draw  the window
    def redraw_window(self):
            """
                drawing function to redraw every frame
            """
            # drawing background
            self.WIN.blit(self.gameAssets[0], (0, 0))
            
            scores_label = self.main_font.render(f"score: {self.score}", 1, (255,255,255))
            self.WIN.blit(scores_label,(0, 0))
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
            pygame.display.flip()


    # function to create the power ups the power 
    def insertpowerup(self):
      if (random.randint(0, (18/self.diff)* 60) == 1):
            powers=["h","d","s","r","i"]
            choice=random.choice(powers)
            x=random.randint(50,550)
            z=self.powerFactory.create(choice,x,-50,self.is_coop)
            self.powerup.append(z)            
    

    def endlessDiffculty(self,curr):  
        seconds_in_day = 24 * 60 * 60
        now=datetime.datetime.now()
        gt=divmod((now-curr).seconds * seconds_in_day + (now-curr).seconds, 60)
        if gt[0]>2 and gt[0]<6:
            self.diff=2
        elif gt[0]>6:
            self.diff=3


    def start(self):
        """
            function used to start the game engine 
        """
        ####    Intitalization      ####
        #################################
        if self.gameState != None and self.gameState.gameover !=1:
            self.loadGameState()
        else:
            self.create_player()
            self.Enemies=self.level.getwave(1)
        #storage lists
        FPS = 60
        clock = pygame.time.Clock()
        #generate the wave
        ####    Main game loop      ####
        ################################
        curr=datetime.datetime.now()
        starttime = time.time()
        print(f"start time {starttime}")
        while True:
            #drawing FPS
            clock.tick(FPS)
            #draw everything
            self.redraw_window()
            #generate a new wave when the wave is cleared
            if len(self.Enemies) == 0:
                print("requested wave")
                self.Enemies = self.level.getwave(self.diff)
                if self.Enemies==None:
                    self.gameover = 1
                    self.exit = 1
                    if(self.level.number == self.profile.get_story_progress()):
                        self.profile.set_story_progress(self.profile.get_story_progress()+1)
                    self.profile.set_coins(self.profile.get_coins()+self.score)
                    return ["start", self.getGameState()]

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
            self.score+=self.gameObserver.dead(self.Enemies,self.Players,self.graveyard)
            #observe offscreen bullets
            self.gameObserver.off_screen(self.Bullets)
            #insert power up
            self.gameObserver.powerUpdate(self.powerup,self.Players)

            #pasue menu
            if keys[pygame.K_ESCAPE]: # shoot
                selection = self.menuengine.start()
                if selection[0] == "save":
                    self.gamesaver.save_story(self.profile.get_name(),self.getGameState())
                if selection[0] == "runAway":
                    self.exit = 1
                    self.gameState = None
                    return ["menu", self.getGameState()]
                    
            #on death or quitting
            if self.is_coop > 1:
                if len(self.graveyard) == 2:
                    endtime =time.time()
                    if self.level.number==-1:
                        self.profile.set_coins(self.profile.get_coins()+int(self.score/2))
                        if(self.profile.get_endless_score() < self.score):
                            self.profile.set_endless_score(self.score)
                        self.profile.set_endless_survival_time(endtime-starttime)
                    self.gameover = 1
                    self.exit = 1
                    self.gameState = None
                    return ["menu", self.getGameState()]
            else:
                if len(self.graveyard) == 1:
                    if self.level.number==-1:
                        endtime =time.time()
                        print(f"end time {endtime}")
                        self.profile.set_coins(self.profile.get_coins()+int(self.score/2))
                        if(self.profile.get_endless_score() < self.score):
                            self.profile.set_endless_score(self.score)
                        self.profile.set_endless_survival_time(endtime-starttime)
                        
                    self.exit = 1
                    self.gameover = 1
                    self.gameState = None
                    return ["menu", self.getGameState()]
                    
            if self.level==-1:
                self.endlessDiffculty(curr)






            
