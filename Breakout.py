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

# Fuente para el texto
font = pygame.font.SysFont(None, 40)

#variables
#
HOLD = 0
Inicio = False  
Gameover = False  
score = 0

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
background.set_alpha(60)
PL_image = pygame.image.load(r"C:\Users\rafal\OneDrive\Escritorio\Progra 2\SuperBreakout\Breakout_PL.png").convert()

#definir los fps
#
clock = pygame.time.Clock()

# Tamaño de las losas
#
rw = 50
rh = 20
margen = 10 

#acomodo de las losas
#
num_filas = 6
num_columnas = 20

# Función para Dibujar las losas
#
def crearlosas():
    losas = []
    for fila in range(num_filas):
        for columna in range(num_columnas):
            x = columna * (rw + margen) + 35
            y = fila * (rh + margen) + 35
            vida = num_filas - fila  # Las losas de la fila superior tienen más vidas
            losa_rect = pygame.Rect(x, y, rw, rh)
            losas.append({'rect': losa_rect, 'vida': vida})
    return losas

losas = crearlosas()

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
                    Inicio = True
                    if Gameover == True:
                        score = 0
                    Gameover = False
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

    #Hitbox del jugador
    #
    if BALL.colliderect(PL):
        SBALLY *= -1
        if SBALLX == 0:
            SBALLX += 5

    #Creamos las losas
    #
    for losa in losas[:]:
        color = PURPLE if losa['vida'] == 1 else BLUE if losa['vida'] == 2 else GREEN if losa['vida'] == 3 else YELLOW if losa['vida'] == 4 else ORANGE if losa['vida'] == 5 else RED            
        pygame.draw.rect(screen, color, losa['rect'])
    
    #Hitbox de las losas
    #
    for losa in losas[:]:
        if BALL.colliderect(losa['rect']):
            SBALLY *= -1
            losa['vida'] -= 1 
            if losa['vida'] <= 0:
                losas.remove(losa)  
                score += 10  

    #Gameover
    #
    if BALLY > sh:
        Gameover = True
        Inicio= False
        HOLD = 0
        SBALLX = 0
        SBALLY = 0
        BALLX = 605
        BALLY = 580
        PX = 550

    if Gameover:
        perdiste = font.render("Game Over presiona ESPACIO para reiniciar", True, WHITE)
        screen.blit(perdiste, (sw // 2 - 250, sh // 2))

    #Si se rompen todas las losas
    #
    if len(losas) == 0:
        losas = crearlosas()
        game_started = False
        HOLD = 0
        BALLX = 605
        BALLY = 580
        PX = 550

    #mensaje de inicio
    #
    if not Inicio and not Gameover:
        textitoinicio = font.render("Presiona ESPACIO para empezar", True, WHITE)
        screen.blit(textitoinicio, (sw // 2 - 200, sh // 2))

    # Mostrar la puntuación
    textitopuntos = font.render(f"Score: {score}", True, WHITE)
    screen.blit(textitopuntos, (10, 10))

    #actualizar
    #
    pygame.display.flip()
    clock.tick(60)
    pass    
