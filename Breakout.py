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
PL_image = pygame.image.load(r"C:\Users\rafal\OneDrive\Escritorio\Progra 2\SuperBreakout\Breakout_PL.png").convert()

#definir los fps
#
clock = pygame.time.Clock()

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
    PX += SPX

    #ball movement
    #
    BALLX += SBALLX
    BALLY += SBALLY

    screen.blit(background, [0,0])
    PL = screen.blit(PL_image, [PX,PY])

    #------------Draw
    BALL = pygame.draw.rect(screen,WHITE,(BALLX,BALLY,20,20))
    #------------Draw

    #actualizar
    #
    pygame.display.flip()
    clock.tick(60)
    pass    
