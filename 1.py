import pygame
import time
import random
from pygame.locals import *
import pygame.gfxdraw
import pyganim
''' This is a final project of  mine. My name is Jayson Fernandez currently
studying at MingChuan University in Taiwan. It is a modified game.
'''
## install all the necessary import module first before you can run this program
##pip install pygame
##pip install Pyganim
# initializing and declaring the variables needed for the program.
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
browngame = (104,73,33)
yellow = (255,211,0)

gameDisplay=pygame.display.set_mode((display_width, display_height),0,32)
pygame.display.set_caption(" Car Adventure " )

boltAnim = pyganim.PygAnimation([('bolt_strike_0001.png', 0.2),
                                 ('bolt_strike_0002.png', 0.2),
                                 ('bolt_strike_0003.png', 0.2),
                                 ('bolt_strike_0004.png', 0.2),
                                 ('bolt_strike_0005.png', 0.2),
                                 ('bolt_strike_0006.png', 0.2),
                                 ('bolt_strike_0007.png', 0.2),
                                 ('bolt_strike_0008.png', 0.2),
                                 ('bolt_strike_0009.png', 0.2),
                                 ('bolt_strike_0010.png', 0.2)])


clock=pygame.time.Clock()
carImg=pygame.image.load('car1.png')
coinImg =['coins_01.png','coins_02.png','coins_03.png','coins_05.png','coins_06.png']
bgImg=pygame.image.load("bgImg.png")
instructionbackground=pygame.image.load("menu1.png")
intro_background=pygame.image.load("menufirst.png")
levelSound = pygame.mixer.Sound('up.wav')
missilewindow= pygame.image.load('missilewindow.png')
lifewindow= pygame.image.load('life.png')
speedwindow= pygame.image.load('speed.png')
EnemyImage= ['car.png','car2.png','car3.png','car4.png','car5.png','car6.png','car7.png','car8.png']
bullet = ['laser.png','laser.png']
missile = pygame.image.load('Nitro1.png')
explosion = pygame.image.load('explosion.png')
flame = pygame.image.load('flame.png')
excellent= pygame.image.load('excellent.png')
bonus = ['HP_Bonus.png']
crash = pygame.image.load('crash.png')
FinishImg = pygame.image.load('Finish.png')
missileSound =pygame.mixer.Sound('missile2.wav' )
crashedSound = pygame.mixer.Sound('explosion.wav' )
gameOverSound = pygame.mixer.Sound('gameover.wav')
collect = pygame.mixer.Sound('collect1.wav')
collectMissile = pygame.mixer.Sound('coins.wav')
starts = pygame.mixer.Sound('starts.wav')
explosion = pygame.mixer.Sound('explosion.wav')
introSound = pygame.mixer.Sound('coffee_stains.wav')
clickSound = pygame.mixer.Sound('click.wav')
loseSound = pygame.mixer.Sound('lose.wav')
pause=False
global LIVES, imageX,imageY
LIVES =3
bulletAllow= False
imageX = (display_width/5)
imageY = (display_height/5)


#introduction interface 1. Will ask the player to start or quit and also the instruction
def intro():
    intro=True
    introSound.play()
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

#button function 
def button(msg,x,y,w,h,ic,ac,action=None):
    
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0]==1 and action!=None:
            clickSound.play()
            if action=="play":
                introSound.stop()
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                instruction()
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

#instruction User interface.. It will show the instruction. 
def instruction():
    instruction=True
    introSound.stop()
    while instruction:
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(instructionbackground, (0, 0))
        largetext=pygame.font.Font('freesansbold.ttf',50)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',30)
        obtextSurf,obtextRect=text_objects("Collect coins for points, heart for extra life and laser beam for bullets", smalltext)
        obtextRect.center=((390),(250))
        ob2textSurf,ob2textRect=text_objects('Touching the side-road will be automatically gameover' ,smalltext)
        ob2textRect.center=((400),(270))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(210))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(obtextSurf, obtextRect)
        gameDisplay.blit(ob2textSurf, ob2textRect)
        ktextSurf,ktextRect=text_objects("press SPACE BAR : FOR LASER BEAM",smalltext)
        ktextRect.center=((243),(540))
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
        gameDisplay.blit(ktextSurf, ktextRect)
        button("Menu",600,450,100,50,brown,lightbrown,"menu")
        pygame.display.update()
        clock.tick(30)
#pause function will enable the user to pause anytime by pressing p
def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gameDisplay.blit(instructionbackground, (0, 0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            button("CONTINUE",40,500,150,50,brown,lightbrown,"unpause")
            button("RESTART",270,500,150,50,brown,lightbrown,"play")
            button("INSTRUCTION",500,500,150,50,brown,lightbrown,"menu")
            pygame.display.update()
            clock.tick(30)
#unpause
def unpaused():
    global pause
    pause=False

#background while counting 
def countdown_background():
    
    font=pygame.font.SysFont(None,35)
    x=(display_width*0.50)
    y=(display_height*0.77)
    gameDisplay.blit(bgImg, (0, 0))   
    gameDisplay.blit(carImg, (x, y))
    cointext=font.render("COINS: 0",True, blue)
    carshoot=font.render("CAR SHOOT: 0",True, yellow)
    score=font.render("SCORE: 0",True,bright_green)
    heart=font.render("HEART: 3",True,red)
    gameDisplay.blit(heart, (0, 90))
    
    gameDisplay.blit(cointext, (0, 30))
    gameDisplay.blit(carshoot, (0, 50))
    gameDisplay.blit(score, (0, 70))
    
    
    
#This code is for the countdown at the beginning of the game.
    
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
            starts.play()
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



#scoring system, when the user collect coins and shoot car using laser beam it will add to score.
#collecting heart will add life 
def score_system(coinCollect, carShoot,score, LIVES):
    font=pygame.font.SysFont(None,35)
    Collect=font.render("COINS: "+str(coinCollect),True,blue)
    Shoot=font.render("CAR SHOOT: "+str(carShoot),True,yellow)
    score=font.render("SCORE: " +str(score),True,bright_green)
    heart=font.render("HEART: "+str(LIVES),True,red)
    gameDisplay.blit(Collect, (0, 30))
    gameDisplay.blit(Shoot, (0, 50))
    gameDisplay.blit(score, (0, 70))
    gameDisplay.blit(heart, (0, 90))
#showing text function
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()


    
    
    
   

#function for showing image after the collision        
def drawObject(obj, x, y):
    global gameDisplay
    gameDisplay.blit(obj, (x, y))

    
    
#gameOver function when the user dies 3 times or collided on the side road
    
def GameOver():
    explosion.stop()
    gameOverSound.play()
    Enemy= pygame.image.load(random.choice(EnemyImage))
    EnemySize= Enemy.get_rect().size
    EnemyWidth = EnemySize[0]
    EnemyHeight = EnemySize[1]
    EnemyX= random.randrange(200, display_width- 200)
    EnemyY = -750
    text =(' Game Over ')
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    
    gameloop()
    
      
# this is the player. just passing the x y arguments for the position of the car
def car(x,y):
    gameDisplay.blit(carImg, (x, y))
#The Game Loop
def gameloop():
    global pause,missile,explosion, Enemy, coins,bonus,carShoot,flame, keys, missileXY, LIVES,life
    x=(display_width*0.50)
    y=(display_height*0.77)
    velocity =5
    bulletBonus = pygame.image.load(random.choice(bullet))
    bulletSize= bulletBonus.get_rect().size
    bulletWidth = bulletSize[0]
    bulletHeight = bulletSize[1]
    bulletX= random.randrange(200, display_width- 200)
    bulletY = -750
    bulletSpeed=4
    bulletAllow = False
    
    LIVES =3 
    coins = pygame.image.load(random.choice(coinImg))            
    coinSize= coins.get_rect().size
    coinWidth = coinSize[0]
    coinHeight = coinSize[1]
    coinX= random.randrange(200, display_width- 200)
    coinY =-750
    life = pygame.image.load(random.choice(bonus))            
    lifeSize= coins.get_rect().size
    lifeWidth = coinSize[0]
    lifeHeight = coinSize[1]
    lifeX= random.randrange(200, display_width- 200)
    lifeY =-750
    lifeSpeed=4
    
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
    coinCollect=0
    carShoot=0
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

        #by pressing keys will allow the user to navigate the game        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
           
        if keys[pygame.K_RIGHT]:
            x += velocity
            
        if keys[pygame.K_UP]:
            y -= velocity
           
        if keys[pygame.K_DOWN]:
            y +=velocity
        if keys[pygame.K_p]:
            paused()
        # will allow the user to use accelerator and brake if the score is above 50    
        if score >=50:
            if keys[pygame.K_a]:
                EnemySpeed+=1
            if keys[pygame.K_b]:
                EnemySpeed-=1
        #else the window message will popup
        if score< 49:
            if keys[pygame.K_a]:
                gameDisplay.blit(speedwindow, (imageX, imageY))
                pygame.display.update()
                time.sleep(3)
            if keys[pygame.K_b]:
                gameDisplay.blit(speedwindow, (imageX, imageY))
                pygame.display.update()
                time.sleep(3)
            
        #can only use laser beam function if the player collected the missile icon        
        if bulletAllow == True:
             if keys[pygame.K_SPACE]:
                missileSound.play()
                missileX = x + car_width/5
                missileY = y - car_height/2
                missileXY.append([missileX,missileY])
        #missile icon will only show once every level
        if  int(score)%10==0:
            if bulletAllow == False:
                bulletY += bulletSpeed
                if bulletY > display_height:
                    bulletBonus = pygame.image.load(random.choice(bullet))
                    bulletSize= bulletBonus.get_rect().size
                    bulletWidth = bulletSize[0]
                    bulletHeight = bulletSize[1]
                    bulletX= random.randrange(200, display_width- 200)
                    bulletY = -750
        #the level is set until 10th level if the player got 100 score then the game is finish
        if score ==100:
            gameDisplay.blit(FinishImg, (0, 200))
            pygame.display.update()
            time.sleep(3)    
            intro()
        #the heart icon will only show once the player has 1 life left
        if LIVES <= 1:
            lifeY += lifeSpeed
            if lifeY > display_height:
                life = pygame.image.load(random.choice(bonus))            
                lifeSize= coins.get_rect().size
                lifeWidth = coinSize[0]
                lifeHeight = coinSize[1]
                lifeX= random.randrange(200, display_width- 200)
                lifeY =-750
        #collision for heart icon
        if y<lifeY+lifeHeight:
            if y > lifeY and y < lifeY + lifeHeight or y+car_width > lifeY and x+car_height < lifeY+lifeHeight:
            
                if x > lifeX and x < lifeX + lifeWidth or x+car_width > lifeX and x+car_width < lifeX+lifeWidth:
                    drawObject(excellent, lifeX,lifeY)
                    life = pygame.image.load(random.choice(bonus))
                
                    lifeSize= coins.get_rect().size
                    lifeWidth = coinSize[0]
                    lifeHeight = coinSize[1]
                    lifeX= random.randrange(200, display_width- 200)
                    lifeY =-750
                    LIVES+=1
                    collectMissile.play()
                    gameDisplay.blit(lifewindow, (imageX, imageY))
                    pygame.display.update()
                    time.sleep(3)
 

        #collision for missile icon            
        if y<bulletY+bulletHeight:
            if y > bulletY and y < bulletY + bulletHeight or y+car_width > bulletY and x+car_height < bulletY+bulletHeight:
            
                if x > bulletX and x < bulletX + bulletWidth or x+car_width > bulletX and x+car_width < bulletX+bulletWidth:
                    drawObject(excellent, bulletX,bulletY)
                    bulletBonus = pygame.image.load(random.choice(bullet))
                    bulletSize= bulletBonus.get_rect().size
                    bulletWidth = bulletSize[0]
                    bulletHeight = bulletSize[1]
                    bulletX= random.randrange(200, display_width- 200)
                    bulletY = -750
                    bulletAllow = True
                    collectMissile.play()
                    gameDisplay.blit(missilewindow, (imageX, imageY))
                    pygame.display.update()
                    time.sleep(3)
        
        if len(missileXY) !=0:
            for bx, by in missileXY:
                drawObject(missile, bx,by)
        EnemyY += EnemySpeed
        #initializing enemy icon
        if EnemyY > display_height:
            Enemy= pygame.image.load(random.choice(EnemyImage))
            EnemySize= Enemy.get_rect().size
            EnemyWidth = EnemySize[0]
            EnemyHeight = EnemySize[1]
            EnemyX= random.randrange(200, display_width- 200)
            EnemyY = -750
                            
        #initializing coin icon
        coinY += coinSpeed
        if coinY>display_height:
            coins= pygame.image.load(random.choice(coinImg))
            coinSize= coins.get_rect().size
            coinWidth = coinSize[0]
            coinHeight = coinSize[1]
            coinX= random.randrange(200, display_width- 200)
            coinY = -750
        #animating the coins  
        rotated = pygame.transform.rotate(coins, degrees)
        rect = rotated.get_rect()
        
        pygame.display.update()
        gameDisplay.fill(gray)

        #background position
        rel_y= y2 % bgImg.get_rect().height
        
        gameDisplay.blit(bgImg,(0,rel_y-bgImg.get_rect().height))
       
        if rel_y<600:
            gameDisplay.blit(bgImg, (0, rel_y))

        y2+=EnemySpeed
        score_system(coinCollect, carShoot,score, LIVES)

        
            
            
        #missile collision with enemy
        if len(missileXY) != 0:
            for i , bxy in enumerate(missileXY):
                bxy[1]-=10
                missileXY[i][1]= bxy[1]
                if bxy[1] <EnemyY:
                    if bxy[0] > EnemyX and bxy[0] < EnemyX + EnemyWidth:
                        missileXY.remove(bxy)
                        isShot= True
                        carShoot= carShoot+1
                        score=coinCollect + carShoot
                        pygame.display.update()
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass                              
        if isShot:
            
            Enemy = pygame.image.load(random.choice(EnemyImage))
            boltAnim.blit(gameDisplay, (EnemyX, EnemyY))
            boltAnim.play()
            pygame.display.update()
            boltAnim.play()
            EnemySize=Enemy.get_rect().size
            EnemyWidth= EnemySize[0]
            EnemyHeight= EnemySize[1]
            EnemyX= random.randrange(200,  display_width-200)
            
            EnemyY=-750
            
            isShot= False
      
        pause=True
        
        #showing image
        drawObject(life,lifeX,lifeY)
        drawObject(bulletBonus,bulletX,bulletY)

        drawObject(Enemy,EnemyX,EnemyY)
           
        y2+=coinSpeed
        rotated = pygame.transform.rotate(coins, degrees)
        degrees += 2
        car(x,y)

        
        
        #collision for coin icon
                    
        if y<coinY+coinHeight:
            if y > coinY and y < coinY + coinHeight or y+car_width > coinY and x+car_height < coinY+coinHeight:
            
                if x > coinX and x < coinX + coinWidth or x+car_width > coinX and x+car_width < coinX+coinWidth:   
                    collect.play()
                    drawObject(excellent, coinX,coinY)
                    coins = pygame.image.load(random.choice(coinImg))
                    coinSize=coins.get_rect().size
                    coinWidth= coinSize[0]
                    coinHeight= coinSize[1]
                    coinX= random.randrange(200,  display_width-200)
                    coinY=-750
                    coinCollect= coinCollect+1
                    score=coinCollect + carShoot
                    
    
                    if int(score)%10==0:
                        levelSound.play()
                        level=level+1
                        EnemySpeed+=2
                        
                        largetext=pygame.font.Font("freesansbold.ttf",80)
                        textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                        textrect.center=((display_width/2),(display_height/2))
                        gameDisplay.blit(textsurf, textrect)
                        pygame.display.update()
                        time.sleep(3)
       
        #collision for side road and player          
        if x>690-car_width or x<110:
            drawObject(crash, x,y)
            explosion.play()
            pygame.display.update()
            time.sleep(2)
            
            GameOver()
            
        if x>display_width-(car_width+110) or x<110:
            drawObject(crash, x,y)
            explosion.play()
            pygame.display.update()
            time.sleep(2)
            
            GameOver()

            
        #collision with enemy and player  
        if y<EnemyY+EnemyHeight:
            if y < EnemyY < y+car_height or y < EnemyY+EnemyHeight < y+car_height:
                if x < EnemyX < x+car_width or x < EnemyX+EnemyWidth < x+car_width:
                    boltAnim.blit(gameDisplay, (x, y))
                    boltAnim.play()
                    pygame.display.update()
                    explosion.play()
                    time.sleep(2)
                    pygame.display.update()
                    bulletAllow = False

                    car(x,y)
                    Enemy= pygame.image.load(random.choice(EnemyImage))
                    EnemySize= Enemy.get_rect().size
                    EnemyWidth = EnemySize[0]
                    EnemyHeight = EnemySize[1]
                    EnemyX= random.randrange(200, display_width- 200)
                    EnemyY = -750
                    LIVES -=1
                    if LIVES >= 1:
                        loseSound.play()
                        text = (' You lose one life')
                        largetext=pygame.font.Font("freesansbold.ttf",80)
                        textsurf,textrect=text_objects(text,largetext)
                        textrect.center=((display_width/2),(display_height/2))
                        gameDisplay.blit(textsurf, textrect)
                        
                        pygame.display.update()
                        time.sleep(2)
                    
                        
                    
                    
                    if LIVES ==0:
                        GameOver()
                    else:
                        pass
                     
        
        gameDisplay.blit(rotated, (coinX, coinY))
        
        pygame.display.update()
        clock.tick(60)
intro()
gameloop()
pygame.quit()
quit()
