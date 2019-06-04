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
green=(0,200,0)
blue=(0,0,200)
car_width=55
car_height = 140
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)


 

gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("LET'S DRIVE CAR")
clock=pygame.time.Clock()
carImg=pygame.image.load('car1.png')
coinImg = pygame.image.load('coins_02.png')
bgImg=pygame.image.load("download12.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("background2.jpg")
instruction_background=pygame.image.load("background2.jpg")
EnemyImage= ['car.png','car8.png','car2.png','car3.png','car4.png','car5.png','car6.png','car7.png','car8.png',]
missile = pygame.image.load('missile.png')
explosion = pygame.image.load('explosion.png')

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
        TextSurf,TextRect=text_objects("LET'S DRIVE CAR",largetext,)
        TextRect.center=(400,100)
        gameDisplay.blit(TextSurf, TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
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
        gameDisplay.blit(instruction_background, (0, 0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is a journey for driving car",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(textSurf, textRect)
        stextSurf,stextRect=text_objects("press ARROW KEY LEFT : LEFT TURN",smalltext)
        stextRect.center=((100),(400))
        hTextSurf,hTextRect=text_objects("press ARROW KEY RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((100),(450))
        stextSurf,stextRect=text_objects("press ARROW UP : GOING UP ",smalltext)
        stextRect.center=((100),(400))
        hTextSurf,hTextRect=text_objects("press ARROW DOWN : GOING DOWN" ,smalltext)
        hTextRect.center=((100),(450))
        atextSurf,atextRect=text_objects("A : ACCELERATOR",smalltext)
        atextRect.center=((100),(500))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((100),(550))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((100),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gameDisplay.blit(sTextSurf, sTextRect)
        gameDisplay.blit(stextSurf, stextRect)
        gameDisplay.blit(hTextSurf, hTextRect)
        gameDisplay.blit(atextSurf, atextRect)
        gameDisplay.blit(rtextSurf, rtextRect)
        gameDisplay.blit(ptextSurf, ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
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
            gameDisplay.blit(instruction_background, (0, 0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.50)
    y=(display_height*0.77)
    gameDisplay.blit(bgImg, (0, 0))
    gameDisplay.blit(bgImg, (0, 200))
    gameDisplay.blit(bgImg, (0, 400))
    gameDisplay.blit(bgImg, (700, 0))
    gameDisplay.blit(bgImg, (700, 200))
    gameDisplay.blit(bgImg, (700, 400))
    gameDisplay.blit(yellow_strip, (400, 100))
    gameDisplay.blit(yellow_strip, (400, 200))
    gameDisplay.blit(yellow_strip, (400, 300))
    gameDisplay.blit(yellow_strip, (400, 400))
    gameDisplay.blit(yellow_strip, (400, 100))
    gameDisplay.blit(yellow_strip, (400, 500))
    gameDisplay.blit(yellow_strip, (400, 0))
    gameDisplay.blit(yellow_strip, (400, 600))
    gameDisplay.blit(strip, (120, 200))
    gameDisplay.blit(strip, (120, 0))
    gameDisplay.blit(strip, (120, 100))
    gameDisplay.blit(strip, (680, 100))
    gameDisplay.blit(strip, (680, 0))
    gameDisplay.blit(strip, (680, 200))
    gameDisplay.blit(carImg, (x, y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gameDisplay.blit(text, (0, 50))
    gameDisplay.blit(score, (0, 30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")
    
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
            gameDisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gameDisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gameDisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gameloop()




def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,red)
    gameDisplay.blit(text, (0, 50))
    gameDisplay.blit(score, (0, 30))


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
def rotate(ds, x, y, coinImg, degrees):
    rotated = pygame.transform.rotate(coinImg, degrees)
    rect = rotated.get_rect()
    gameDisplay.blit(rotated, (x, y))
    
# the message for collision 
def crash():
    message_display("YOU CRASHED")
##def coins(last_call, coinsx, coinsy):
##    
##    fps1 = 10
##    time_per_frame=1000/fps1
##    last_call_time = 0
##    curr_index = 0
##    coinImg = [pygame.image.load('coins_01.png'),
##    pygame.image.load('coins_02.png'),
##    pygame.image.load('coins_03.png'),
##    pygame.image.load('coins_04.png'),
##    pygame.image.load('coins_05.png'),
##    pygame.image.load('coins_06.png')]
##    max_index = len(coinImg)
##    if pygame.time.get_ticks() - last_call >= time_per_frame:
##        curr_index = (curr_index+1)%max_index
##        gamedisplays.blit(coinImg[curr_index], (coinsx, coinsy))
##        while True:
##            coins(last_call_time, 0, 0)
##            pygame.display.update()


# the background strip but I'm planning to just put an image and not to fill only gray on the background.
#I'm still working on it using photoshop so i think i will delete this 
def background():
    gameDisplay.blit(bgImg, (0, 0))
    gameDisplay.blit(bgImg, (0, 200))
    gameDisplay.blit(bgImg, (0, 400))
    gameDisplay.blit(bgImg, (700, 0))
    gameDisplay.blit(bgImg, (700, 200))
    gameDisplay.blit(bgImg, (700, 400))
    gameDisplay.blit(yellow_strip, (400, 0))
    gameDisplay.blit(yellow_strip, (400, 100))
    gameDisplay.blit(yellow_strip, (400, 200))
    gameDisplay.blit(yellow_strip, (400, 300))
    gameDisplay.blit(yellow_strip, (400, 400))
    gameDisplay.blit(yellow_strip, (400, 500))
    gameDisplay.blit(strip, (120, 0))
    gameDisplay.blit(strip, (120, 100))
    gameDisplay.blit(strip, (120, 200))
    gameDisplay.blit(strip, (680, 0))
    gameDisplay.blit(strip, (680, 100))
    gameDisplay.blit(strip, (680, 200))
# this is the player. just passing the x y arguments for the position of the car
def car(x,y):
    gameDisplay.blit(carImg, (x, y))
#The Game Loop
def gameloop():
    global pause,missile,explosion, Enemy, carImg
    x=(display_width*0.50)
    y=(display_height*0.77)
    
    velocity =5
    obstacle_speed=9
    obs=0
    coins_width = 70
    coinsx=round(random.randrange(150, display_width - 150))
    coinsy=round(random.randrange(-750,display_height- 750))
    coinSPeed = 4  
    coins_height = 100

    Enemy = pygame.image.load(random.choice(EnemyImage))
                              
    EnemySize= Enemy.get_rect().size
    EnemyWidth = EnemySize[0]
    EnemyHeight = EnemySize[1]
    EnemyX= random.randrange(200, display_width- 200)
    EnemyY =-750
    isShot= False
    ShotCount=0
    EnemyPassed= 0
    EnemySpeed=2
    degrees = 0
    passed=0
    level=0
    score=0
    y2=7
    fps=120
    missileXY =[]
    
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
            obstacle_speed+=2
        if keys[pygame.K_b]:
            obstacle_speed-=2
        elif keys[pygame.K_SPACE]:
            missileX = x + car_width/3
            missileY = y - car_height/4
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
                              
        drawObject(Enemy, EnemyX, EnemyY)
        pygame.display.update()
        gameDisplay.fill(gray)                     
        if len(missileXY) != 0:
            for i , bxy in enumerate(missileXY):
                bxy[1]-=10
                missileXY[i][1]= bxy[1]
                if bxy[1] <EnemyY:
                    if bxy[0] > EnemyX and bxy[0] < EnemyX + EnemyWidth:
                        missileXY.remove(bxy)
                        isShot= True
                        ShotCount+=1
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

                              
        if isShot:
            drawObject(explosion, EnemyX, EnemyY)
            Enemy = pygame.image.load(random.choice(EnemyImage))
            EnemySize=Enemy.get_rect().size
            EnemyWidth= EnemySize[0]
            EnemyHeight= EnemySize[1]
            EnemyX= random.randrange(200,  display_width-200)
            EnemyY=-750
            isShot= False
            EnemySpeed+=0.02
            if EnemySpeed>=10:
                EnemySpeed =10
        
                              
        
        
                        
                    
            

        
        pause=True
        
        

        rel_y= y2 % bgImg.get_rect().width
        gameDisplay.blit(bgImg, (0, rel_y - bgImg.get_rect().width))
        gameDisplay.blit(bgImg, (700, rel_y - bgImg.get_rect().width))
        if rel_y<800:
            gameDisplay.blit(bgImg, (0, rel_y))
            gameDisplay.blit(bgImg, (700, rel_y))
            gameDisplay.blit(yellow_strip, (400, rel_y))
            gameDisplay.blit(yellow_strip, (400, rel_y + 100))
            gameDisplay.blit(yellow_strip, (400, rel_y + 200))
            gameDisplay.blit(yellow_strip, (400, rel_y + 300))
            gameDisplay.blit(yellow_strip, (400, rel_y + 400))
            gameDisplay.blit(yellow_strip, (400, rel_y + 500))
            gameDisplay.blit(yellow_strip, (400, rel_y - 100))
            gameDisplay.blit(strip, (120, rel_y - 200))
            gameDisplay.blit(strip, (120, rel_y + 20))
            gameDisplay.blit(strip, (120, rel_y + 30))
            gameDisplay.blit(strip, (680, rel_y - 100))
            gameDisplay.blit(strip, (680, rel_y + 20))
            gameDisplay.blit(strip, (680, rel_y + 30))
       
        y2+=obstacle_speed
        rotate(gameDisplay, coinsx - 100, coinsy, coinImg, degrees)
        drawObject(Enemy,EnemyX,EnemyY)
        
        
        
        
        degrees += 2
      

        coinsy += coinSPeed
        coinsy-=(obstacle_speed/4)

        car(x,y)
        score_system(passed,score)
        if x > coinsx and x < coinsx + coins_height or x + coins_width > coinsx and x + coins_width < coinsx + coins_height:

            if y > coinsy and y < coinsy + coins_height:
                coinsx=round(random.randrange(150, display_width - 150))
                coinsy=round(random.randrange(-750,display_height-750))
                passed=passed+1
                score=passed*10
                if int(passed)%10==0:
                        
                    level=level+1
                    obstacle_speed+2
                    largetext=pygame.font.Font("freesansbold.ttf",80)
                    textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                    textrect.center=((display_width/2),(display_height/2))
                    gameDisplay.blit(textsurf, textrect)
                    pygame.display.update()
                    time.sleep(3)
                    
            elif y + coins_height > coinsy and y + coins_width < coinsy + coins_height:
                coinsx=round(random.randrange(150, display_width - 150))
                coinsy=round(random.randrange(-750,display_height-750))
                passed=passed+1
                score=passed*10
                if int(passed)%10==0:
                        
                    level=level+1
                    obstacle_speed+2
                    largetext=pygame.font.Font("freesansbold.ttf",80)
                    textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                    textrect.center=((display_width/2),(display_height/2))
                    gameDisplay.blit(textsurf, textrect)
                    pygame.display.update()
                    time.sleep(3)
                    

            
        if coinsy>display_height:
            coinsy=0-coins_height
            coinsx=round(random.randrange(150, display_width - 150))
            coinsy=round(random.randrange(-750,display_height-750))

                
                    
        
        if EnemyY>display_height:
            EnemyY=0-EnemyHeight

            

        #actually this is the hardest part of it i don't understand this code but what i understand it is the restriction 
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if y<EnemyY+EnemyHeight:
            if y < EnemyY < y+car_height or y < EnemyY+EnemyHeight < y+car_height:
                if x < EnemyX < x+car_width or x < EnemyX+EnemyWidth < x+car_width:
                 
                     crash()
        
        
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)
intro()
gameloop()
pygame.quit()
quit()
