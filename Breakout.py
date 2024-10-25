import pygame
pygame.init()
import sys

#colores
#
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (148,0,111)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (255,127,0)
RED = (255,0,0)
GREY = (65,65,65)

#variables
#
HOLD = 0
#player size
#
PH = 20
PW = 130

#player coords and speed
PX = 550
PY = 600
SPX = 0

#ball coords and speed
BALLX = 605
BALLY = 580
SBALLX = 0
SBALLY = 0

#pantalla 
#
sw = 1280
sh = 720
screen_size = (sw,sh)

screen = pygame.display.set_mode(screen_size)

background = pygame.image.load(r"C:\Users\rafal\OneDrive\Escritorio\Progra 2\SuperBreakout\bg.jpg").convert()
background.set_alpha(128)
PL_image = pygame.image.load(r"C:\Users\rafal\OneDrive\Escritorio\Progra 2\SuperBreakout\Breakout_PL.png").convert()

#definir los fps
#
clock = pygame.time.Clock()

rw = 50
rh = 50
margen = 10 
columna = sw
fila = sh


# List to hold rectangle objects
Losas = []

# Function to create rectangles in a grid layout
def CrearLosas():
    for row in range(fila):
        for col in range(columna):
            x = col * (rw + margen)
            y = row * (rh + margen)
            rectangulo = pygame.Rect(x, y, rw, rh)
            Losas.append(rectangulo)

# Create the grid of rectangles
CrearLosas()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #Controls
        #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                SPX = -8
            if event.key == pygame.K_d:
                SPX = 8
            if HOLD == 0:
                if event.key == pygame.K_SPACE:
                    SBALLY = -8
                    HOLD = 1
            if HOLD == 0:
                if event.key == pygame.K_a:
                    SBALLX = -8
                if event.key == pygame.K_d:
                    SBALLX = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                SPX = 0
            if event.key == pygame.K_d:
                SPX = 0
            if HOLD == 0:
                if event.key == pygame.K_a:
                    SBALLX = 0
                if event.key == pygame.K_d:
                    SBALLX = 0

    #player movement
    #
    if PX < 0:  
        PX = 0
        if HOLD == 0:
            BALLX = 55
    if PX + PW > sw: 
        PX = sw - PW
        if HOLD == 0:
            BALLX = 1280 - (55 + 20)
    PX += SPX

    #ball movement
    #
    BALLX += SBALLX
    BALLY += SBALLY

    #Rebote
    #
    if BALLY < 0:
        SBALLY *= -1
    if BALLX < 0 or BALLX > 1260:
        SBALLX *= -1

    screen.blit(background, [0,0])
    PL = screen.blit(PL_image, [PX,PY])

    #------------Draw
    BALL = pygame.draw.rect(screen,WHITE,(BALLX,BALLY,20,20))
    
    #------------Draw

    #
    #
    if BALL.colliderect(PL):
        SBALLY *= -1

    #actualizar
    #
    pygame.display.flip()
    clock.tick(60)
    pass    
