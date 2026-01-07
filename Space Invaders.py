import pygame
import sys

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
def draw():
    screen.blit(backdrop,(0,0))
    screen.blit(red,(redx,redy))
    screen.blit(yel,(yelx,yely))
    pygame.draw.rect(screen,'grey',(800,0,50,1000))
def redmovement():
    global redx
    global redy
    pressedkeys=pygame.key.get_pressed()
    if pressedkeys[pygame.K_LEFT]:
        redx=redx-2
    if pressedkeys[pygame.K_RIGHT]:
        redx=redx+2
    if pressedkeys[pygame.K_UP]:
        redy=redy-2
    if pressedkeys[pygame.K_DOWN]:
        redy=redy+2

def yelmovement():
    global yelx
    global yely
    pressedkeys=pygame.key.get_pressed()
    if pressedkeys[pygame.K_a]:
        yelx=yelx-2
    if pressedkeys[pygame.K_d]:
        yelx=yelx+2
    if pressedkeys[pygame.K_w]:
        yely=yely-2
    if pressedkeys[pygame.K_s]:
        yely=yely+2


while True:
    draw()
    redmovement()
    yelmovement()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()