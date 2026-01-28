import pygame
import sys
pygame.init()
screen=pygame.display.set_mode(size=(1700,1000))
pygame.display.set_caption('Space Invader')
bg=pygame.image.load('PyGame/Space Invaders/Images/Backdrop.png')
red=pygame.image.load('PyGame/Space Invaders/Images/Red Spaceship.png')
yellow=pygame.image.load('PyGame/Space Invaders/Images/Yellow Spaceship.png')
backdrop=pygame.transform.scale(bg,(1700,1000))
redship=pygame.transform.scale(red,(75,75))
yellowship=pygame.transform.scale(yellow,(75,75))
yel=pygame.transform.rotate(yellowship,90.0)
red=pygame.transform.rotate(redship,270.0)
redx=1300
redy=500
yelx=400
yely=500
yelhealth=10
redhealth=10
font=pygame.font.SysFont('Comic sans',50)
bulletsr=[]
bulletsy=[]
gameover=False
yelwins=False
redwins=False

def draw():
    screen.blit(backdrop,(0,0))
    screen.blit(red,(redx,redy))
    screen.blit(yel,(yelx,yely))
    pygame.draw.rect(screen,'grey',(800,0,50,1000))
    text=font.render(str(yelhealth),True,'white')
    screen.blit(text,(10,10))
    text2=font.render(str(redhealth),True,'white')
    screen.blit(text2,(1610,10))
    for bullet in bulletsr:
        pygame.draw.rect(screen,'red',bullet)
    for bullet in bulletsy:
        pygame.draw.rect(screen,'yellow',bullet)
    if redwins==True:
        screen.blit(winr,(800,500))
    if yelwins==True:
        screen.blit(winy,(800,500))
        

def redmovement():
    global redx
    global redy
    pressedkeys=pygame.key.get_pressed()
    if pressedkeys[pygame.K_LEFT] and redx>=850:
        redx=redx-3
    if pressedkeys[pygame.K_RIGHT] and redx<=1620:
        redx=redx+3
    if pressedkeys[pygame.K_UP] and redy>=0:
        redy=redy-3
    if pressedkeys[pygame.K_DOWN] and redy<=920:
        redy=redy+3

def redbullet():
    global yelhealth
    for bullet in bulletsr:
        bullet.x=bullet.x-10
        if bullet.colliderect(yelbox):
            bulletsr.remove(bullet)
            yelhealth=yelhealth-1

def yelmovement():
    global yelx
    global yely
    pressedkeys=pygame.key.get_pressed()
    if pressedkeys[pygame.K_a] and yelx>0:
        yelx=yelx-3
    if pressedkeys[pygame.K_d] and yelx<730:
        yelx=yelx+3
    if pressedkeys[pygame.K_w] and yely>=0:
        yely=yely-3
    if pressedkeys[pygame.K_s] and yely<=920:
        yely=yely+3

def yelbullet():
    global redhealth
    for bullet in bulletsy:
        bullet.x=bullet.x+10
        if bullet.colliderect(redbox):
            bulletsy.remove(bullet)
            redhealth=redhealth-1
def reset():
    global redhealth
    global yelhealth
    global gameover
    global yelwins
    global redwins
    redhealth=10
    yelhealth=10
    gameover=False
    yelwins=False
    redwins=False   

while True:
    draw()
    redmovement()
    yelmovement()
    yelbullet()
    redbullet()
    redbox=pygame.Rect(redx,redy,75,75)
    yelbox=pygame.Rect(yelx,yely,75,75)
    if redhealth<=0:
        winy=font.render('Yellow Wins',True,'white')
        gameover=True
        yelwins=True
        redhealth=0
    if yelhealth<=0:
        winr=font.render('Red Wins',True,'white')
        gameover=True
        redwins=True
        yelhealth=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RCTRL:
                if gameover==False:
                    bulletr=pygame.Rect(redx,redy+35,10,5)
                    bulletsr.append(bulletr)
            if event.key==pygame.K_e:
                if gameover==False:
                    bullety=pygame.Rect(yelx,yely+35,10,5)
                    bulletsy.append(bullety)
            if event.key==pygame.K_r:
                if gameover==True:
                    reset()
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()