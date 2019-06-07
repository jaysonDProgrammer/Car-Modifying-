import pygame
import time
import random
from pygame.locals import *
import pygame.gfxdraw
import math


""""  the logic of this program is that the player will use key left right up down
    to navigate the car. Then the player needs to avoid the other cars. and also
    the grass has restriction so if the player collide on to the grass it will crash too.
    If the player collect coins thats the only time the player should score.
    I'm still planning to add the bullets to have the player like a  bullet to strike the
    other cars."""
pygame.init()
display_width=800
display_height=600
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,117,50)
blue=(0,121,231)
car_width=55
car_height = 140
bright_red=(251,18,34)
bright_green=(154,240,0)
bright_blue=(7,185,252)
brown =(168,95,0)
lightbrown = (254,196,54)


 

gameDisplay=pygame.display.set_mode((display_width, display_height),0,32)


clock=pygame.time.Clock()
carImg=pygame.image.load('car1.png')
coinImg =['coins_01.png','coins_02.png','coins_03.png','coins_05.png','coins_06.png']
bgImg=pygame.image.load("bgImg.png")

intro_background=pygame.image.load("Menu1.png")


EnemyImage= ['car.png','car2.png','car3.png','car4.png','car5.png','car6.png','car7.png','car8.png','car9.png',]
bullet = ['laser.png','laser.png']
missile = pygame.image.load('Nitro1.png')
explosion = pygame.image.load('explosion.png')
flame = pygame.image.load('flame.png')
bonus = pygame.image.load('HP_Bonus.png')
missileSound =pygame.mixer.Sound('missile2.wav' )
crashedSound = pygame.mixer.Sound('crash.wav' )
gameOverSound = pygame.mixer.Sound('gameover.wav')


pause=False


#introduction interface 1. Will ask the player to start or quit and also the instruction
def intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(intro_background, (0, 0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        
        
        button("START",40,500,180,50,brown,lightbrown,"play")
        button("QUIT",270,500,180,50,brown,lightbrown,"quit")
        button("INSTRUCTION",500,500,180,50,brown,lightbrown,"intro")
        pygame.display.update()
        clock.tick(50)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textsurf, textrect)

#instruction User interface.. It will show the instruction. but i  haven't add the arrow up and down.
def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(intro_background, (0, 0))
        largetext=pygame.font.Font('freesansbold.ttf',50)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',30)
        obtextSurf,obtextRect=text_objects("The objective is to collect the coins", smalltext)
        obtextRect.center=((400),(250))
        ob2textSurf,ob2textRect=text_objects("to make points and destroy the other cars to add points",smalltext)
        ob2textRect.center=((400),(270))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(210))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(obtextSurf, obtextRect)
        gameDisplay.blit(ob2textSurf, ob2textRect)
        ltextSurf,ltextRect=text_objects("press ARROW KEY LEFT : LEFT TURN",smalltext)
        ltextRect.center=((238),(510))
        rtextSurf,rtextRect=text_objects("press ARROW KEY RIGHT : RIGHT TURN" ,smalltext)
        rtextRect.center=((255),(480))
        utextSurf,utextRect=text_objects("press ARROW UP : GOING UP ",smalltext)
        utextRect.center=((205),(450))
        dtextSurf,dtextRect=text_objects("press ARROW DOWN : GOING DOWN" ,smalltext)
        dtextRect.center=((240),(420))
        atextSurf,atextRect=text_objects("press A : ACCELERATOR",smalltext)
        atextRect.center=((178),(390))
        btextSurf,btextRect=text_objects("press B : BRAKE ",smalltext)
        btextRect.center=((140),(360))
        ptextSurf,ptextRect=text_objects("press P : PAUSE  ",smalltext)
        ptextRect.center=((140),(330))
        ctextSurf,ctextRect=text_objects("CONTROLS:",mediumtext)
        ctextRect.center=((150),(300))
        gameDisplay.blit(ctextSurf, ctextRect)
        gameDisplay.blit(ptextSurf, ptextRect)
        gameDisplay.blit(btextSurf, btextRect)
        gameDisplay.blit(atextSurf, atextRect)
        gameDisplay.blit(dtextSurf, dtextRect)
        gameDisplay.blit(utextSurf, utextRect)
        gameDisplay.blit(rtextSurf, rtextRect)
        gameDisplay.blit(ltextSurf, ltextRect)
      
        button("Menu",600,450,100,50,brown,lightbrown,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gameDisplay.blit(intro_background, (0, 0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            button("CONTINUE",40,500,150,50,brown,lightbrown,"unpause")
            button("RESTART",270,500,150,50,brown,lightbrown,"play")
            button("INSTRUCTION",500,500,150,50,brown,lightbrown,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False


def countdown_background():
    font=pygame.font.SysFont(None,35)
    x=(display_width*0.50)
    y=(display_height*0.77)
    gameDisplay.blit(bgImg, (0, 0))



    gameDisplay.blit(carImg, (x, y))
    text=font.render("COINS: 0",True, blue)
    text2=font.render("CAR SHOOT: 0",True, red)
    score=font.render("SCORE: 0",True,bright_green)
    gameDisplay.blit(text, (0, 30))
    gameDisplay.blit(text2, (0, 50))
    gameDisplay.blit(score, (0, 70))
    button("PAUSE",650,0,150,50,brown,lightbrown,"pause")
    
"""This code is for the countdown at the beginning of the game.
    I don't understand this much but I think this will just count 1 to 3 and
    then the game will start."""

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gameDisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
  
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gameloop()




def score_system(coinCollect, carShoot,score):
    font=pygame.font.SysFont(None,35)
    Collect=font.render("COINS: "+str(coinCollect),True,blue)
    Shoot=font.render("CAR SHOOT: "+str(carShoot),True,red)
    score=font.render("SCORE: " +str(score),True,bright_green)
    gameDisplay.blit(Collect, (0, 30))
    gameDisplay.blit(Shoot, (0, 50))
    gameDisplay.blit(score, (0, 70))
    

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    gameloop()
# This is the bonus coins but I can't figure out wheres the error it says pygame.Surface not list

def drawObject(obj, x, y):
    global gameDisplay
    gameDisplay.blit(obj, (x, y))

    
    
# the message for collision 
def crash():
    crashedSound.play()
    message_display("YOU CRASHED")
    
  



# the background strip but I'm planning to just put an image and not to fill only gray on the background.
#I'm still working on it using photoshop so i think i will delete this 


# this is the player. just passing the x y arguments for the position of the car
def car(x,y):
    gameDisplay.blit(carImg, (x, y))
#The Game Loop
def gameloop():
    global pause,missile,explosion, Enemy, coins,bonus,carShoot,flame, keys
    x=(display_width*0.50)
    y=(display_height*0.77)
    velocity =5
    bulletBonus = pygame.image.load(random.choice(bullet))
    bulletSize= bulletBonus.get_rect().size
    bulletWidth = bulletSize[0]
    bulletHeight = bulletSize[1]
    bulletX= random.randrange(200, display_width- 200)
    bulletY = -750
    bulletSpeed=5
    coins = pygame.image.load(random.choice(coinImg))
                              
    coinSize= coins.get_rect().size
    coinWidth = coinSize[0]
    coinHeight = coinSize[1]
    coinX= random.randrange(200, display_width- 200)
    coinY =-750
    isCollect = False
    coinSpeed=4
    Enemy = pygame.image.load(random.choice(EnemyImage))
                              
    EnemySize= Enemy.get_rect().size
    EnemyWidth = EnemySize[0]
    EnemyHeight = EnemySize[1]
    EnemyX= random.randrange(200, display_width- 200)
    EnemyY =-750
    isShot= False
    carShoot=0
    EnemySpeed=4
    degrees = 0
    coinCollect=9
    carShoot=0
    level=1
    score=9
    y2=7
    fps=120
    missileXY =[]
    coinXY =[]
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
                    

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
           
        if keys[pygame.K_RIGHT]:
            x += velocity
            
        if keys[pygame.K_UP]:
            y -= velocity
           
        if keys[pygame.K_DOWN]:
            y +=velocity
            
        if keys[pygame.K_a]:
            EnemySpeed+=1
        if keys[pygame.K_b]:
            EnemySpeed-=1
        if int(score)%10==0:
            bulletY += bulletSpeed
            if bulletY > display_height:
                bulletBonus = pygame.image.load(random.choice(bullet))
                bulletSize= bulletBonus.get_rect().size
                bulletWidth = bulletSize[0]
                bulletHeight = bulletSize[1]
                bulletX= random.randrange(200, display_width- 200)
                bulletY = -750 
        if y < bulletY < y+car_height or y < bulletY+bulletHeight < y+car_height:
            if x < bulletX < x+car_width or x < bulletX+bulletWidth < x+car_width:
                
                bulletBonus = pygame.image.load(random.choice(bullet))
                bulletSize= bulletBonus.get_rect().size
                bulletWidth = bulletSize[0]
                bulletHeight = bulletSize[1]
                bulletX= random.randrange(200, display_width- 200)
                bulletY = -750
                pygame.display.update()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    
                    missileSound.play()
                    missileX = x + car_width/5
                    missileY = y - car_height/2
                    missileXY.append([missileX,missileY])
                    
          
        
        if len(missileXY) !=0:
            for bx, by in missileXY:
                drawObject(missile, bx,by)
        EnemyY += EnemySpeed
        if EnemyY > display_height:
            Enemy= pygame.image.load(random.choice(EnemyImage))
            EnemySize= Enemy.get_rect().size
            EnemyWidth = EnemySize[0]
            EnemyHeight = EnemySize[1]
            EnemyX= random.randrange(200, display_width- 200)
            EnemyY = -750
                            
        
        coinY += coinSpeed
        if coinY>display_height:
            coins= pygame.image.load(random.choice(coinImg))
            coinSize= coins.get_rect().size
            coinWidth = coinSize[0]
            coinHeight = coinSize[1]
            coinX= random.randrange(200, display_width- 200)
            coinY = -750
        
        
       
            
        rotated = pygame.transform.rotate(coins, degrees)
        rect = rotated.get_rect()
        
        pygame.display.update()
        gameDisplay.fill(gray)
        rel_y= y2 % bgImg.get_rect().height
        
        gameDisplay.blit(bgImg,(0,rel_y-bgImg.get_rect().height))
       
        if rel_y<600:
            gameDisplay.blit(bgImg, (0, rel_y))
            

       
        y2+=EnemySpeed
        score_system(coinCollect, carShoot,score)
        
            
            
        
        if len(missileXY) != 0:
            for i , bxy in enumerate(missileXY):
                bxy[1]-=10
                missileXY[i][1]= bxy[1]
                if bxy[1] <EnemyY:
                    if bxy[0] > EnemyX and bxy[0] < EnemyX + EnemyWidth:
                        missileXY.remove(bxy)
                        isShot= True
                        carShoot= carShoot+1
                        
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

                              
        if isShot:
            drawObject(flame,EnemyX,EnemyY)
            Enemy = pygame.image.load(random.choice(EnemyImage))
            EnemySize=Enemy.get_rect().size
            EnemyWidth= EnemySize[0]
            EnemyHeight= EnemySize[1]
            EnemyX= random.randrange(200,  display_width-200)
            EnemyY=-750
            isShot= False
            
            
           
       

        
        pause=True
        
        

        drawObject(bulletBonus,bulletX,bulletY)

        drawObject(Enemy,EnemyX,EnemyY)
           
        y2+=coinSpeed
        rotated = pygame.transform.rotate(coins, degrees)
        degrees += 2
        car(x,y)
        
        

                    
        if y<coinY+coinHeight:
            if y > coinY and y < coinY + coinHeight or y+car_width > coinY and x+car_height < coinY+coinHeight:
            
                if x > coinX and x < coinX + coinWidth or x+car_width > coinX and x+car_width < coinX+coinWidth:   
                     
                    drawObject(bonus, coinX, coinY)
                    coins = pygame.image.load(random.choice(coinImg))
                    coinSize=coins.get_rect().size
                    coinWidth= coinSize[0]
                    coinHeight= coinSize[1]
                    coinX= random.randrange(200,  display_width-200)
                    coinY=-750
                    coinCollect= coinCollect+1
                    score=coinCollect + carShoot

                    if int(score)%10==0:                             
                        level=level+1
                        EnemySpeed+=2
                        pygame.display.update()
                        largetext=pygame.font.Font("freesansbold.ttf",80)
                        textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                        textrect.center=((display_width/2),(display_height/2))
                        gameDisplay.blit(textsurf, textrect)
                        time.sleep(3)
       
        
            

        if coinY>display_height:
            conY=0-coinHeight
        if EnemyY>display_height:
            EnemyY=0-EnemyHeight           
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if y<EnemyY+EnemyHeight:
            if y < EnemyY < y+car_height or y < EnemyY+EnemyHeight < y+car_height:
                if x < EnemyX < x+car_width or x < EnemyX+EnemyWidth < x+car_width:
                 
                     crash()
        
        gameDisplay.blit(rotated, (coinX, coinY))
        button("Pause",650,0,150,50,brown,lightbrown,"pause")
        pygame.display.update()
        clock.tick(60)
intro()
gameloop()
pygame.quit()
quit()
