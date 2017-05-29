import pygame as pg
import time
import random as rnd

x = pg.init()

DspH = 600
DspW = 600

gameDsp = pg.display.set_mode((DspW,DspH))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pg.display.set_caption('Revenge of snake')




clock = pg.time.Clock()



img = pg.image.load('snake20.png')
imgp = pg.image.load('applep.png').convert_alpha()
pg.display.set_icon(img)

direction = 'right'

def snake(block_size,snakeList):
    if direction == 'right':
        head = pg.transform.rotate(img,270)
    if direction == 'left':
        head = pg.transform.rotate(img,90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pg.transform.rotate(img,180)
   
            
    
    gameDsp.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    
    for xny in snakeList[ : -2]:
        pg.draw.rect(gameDsp,green,[xny[0],xny[1],block_size ,block_size])
def text_obj(text,color,):
    
    
    return textsurface,textsurface.get_rect()
    
def msg_to_scrn(msg,color,y_disp= 0,x_disp = 0,Font= 'Arial',Size=25):
    font = pg.font.SysFont(Font,Size)
    
    textS = font.render(msg,True,color)
    textrect = textS.get_rect()
    textrect.center = ((DspW/2)+x_disp),((DspH/2)+y_disp)
    #
    #scrn_txt = font.render(msg,True,color)
    gameDsp.blit(textS,textrect)
def start():
    
    intro = True
    while intro:
        gameDsp.fill(white)
        msg_to_scrn('Welcome to game',blue,-150,Font = 'Algerian',Size= 50)
        msg_to_scrn('Collect apples, each apple will increase the length of snake',red)
        msg_to_scrn( 'Dont pass boundries or snake body',red,30)
        msg_to_scrn('Press S to start',green,100,Size = 40)    
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    game_loop()
                    intro = False
        pg.display.update()
def pause():
    pause = True
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    pause = False
                if event.key == pg.K_q:
                    quit()
        gameDsp.fill(white)
        msg_to_scrn('PAUSED',red,-100,Font = 'comicsansms',Size =50 )
        msg_to_scrn('press c to continue and q to quit',blue,Size = 35)
        pg.display.update()
        
def game_loop():
    Xaxis = DspH/2
    Yaxis = DspW/2
    Mov_box = 5
    AppleThick = 30
    block_size = 20
    AppleX = round(rnd.randrange(0,DspH-block_size)/10.0)*10.0 - 2*AppleThick
    AppleY = round(rnd.randrange(0,DspW-block_size)/10.0)*10.0 - 2*AppleThick
    global direction
    Xchng = 5
    Ychng = 0
    FPS = 60
    block_size = 20
    p = 0
    L = 1
    Exit = False
    gameOver = False

    snakeList = [ ]
    snakeLength = 1
    while not Exit:

        while gameOver==True:
            gameDsp.fill(white)
            msg_to_scrn('Game Over',black,-100,Font = 'comicsansms',Size= 70)
            msg_to_scrn('Final Score=> '+str(p),blue,-50)
            msg_to_scrn('press C to play again press Q to exit',red,Font='Arial',Size=25)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key  ==  pg.K_c:
                        start()
                    elif event.key == pg.K_q:
                        Exit = True
                        gameOver = False
                        
       
        Xaxis += Xchng
        Yaxis += Ychng

        if Xaxis > (DspW-10) or Xaxis <0  or Yaxis > (DspH-10) or Yaxis <0:
            gameOver = True
            
        
        gameDsp.fill(white)
        gameDsp.blit(imgp,[AppleX,AppleY ])
        pg.draw.rect(gameDsp,green,[Xaxis,Yaxis,block_size ,block_size ])

        msg_to_scrn('Points= '+str(p),black,-280,+250)
        msg_to_scrn(('Level= '+str(L)),red,-280,-250)
        #scrn_txt = font.render('Points = '+str(p),True,red)
        #gameDsp.blit(scrn_txt,[1,0])
        
       # Level_txt = font.render('Level = '+str(L),True,blue)
        #gameDsp.blit(Level_txt,[500,1])

        snakeHead = [ ]
        snakeHead.append(Xaxis)
        snakeHead.append(Yaxis)
        snakeList.append(snakeHead)
        snake(block_size,snakeList)
        if len(snakeList ) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[ 2: -1]:
            if eachSegment == snakeHead:
                gameOver = True
            
        snake(block_size,snakeList)
        pg.display.update()

        
        if Xaxis > AppleX and Xaxis < AppleX+AppleThick or Xaxis+block_size >AppleX and Xaxis+block_size<AppleX+AppleThick:
            if Yaxis > AppleY and Yaxis< AppleY+AppleThick:
                AppleX = round(rnd.randrange(0,DspH-block_size)/10.0)*10.0
                AppleY = round(rnd.randrange(0,DspW-block_size)/10.0)*10.0
                p +=1
                snakeLength += 2
                
               
            elif Yaxis+block_size > AppleY and Yaxis+block_size< AppleY+AppleThick:
                AppleX = round(rnd.randrange(0,DspH-block_size)/10.0)*10.0
                AppleY = round(rnd.randrange(0,DspW-block_size)/10.0)*10.0
                p +=1
                snakeLength += 1
                
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Exit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    Xchng = 0
                    Xchng -= Mov_box
                    direction = 'left'
                    Ychng = 0
                    
                elif event.key == pg.K_RIGHT:
                    Xchng = 0
                    Xchng += Mov_box
                    direction = 'right'
                    Ychng = 0
                elif event.key == pg.K_UP:
                    Ychng = 0
                    Ychng -= Mov_box
                    direction = 'up'
                    Xchng = 0
                elif event.key == pg.K_DOWN:
                    Ychng = 0
                    direction = 'down'
                    Ychng += Mov_box
                    Xchng = 0
                elif event.key == pg.K_p:
                    pause()
                           
        if p >5 and p<=10:
            L = 2
            FPS = 80
        if p >10 and p<=20:
            L = 3
            FPS = 100       
        if p >20 and p<30 :
            L = 4
            FPS = 120
        if p> 30 and p<40:
            L = 5
            FPS = 140
        if p> 40 and p<50:
            L = 6
            FPS = 160
        clock.tick(FPS)

    pg.quit()
    quit()

start()


