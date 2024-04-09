import pygame

SCREEN_W = 500
SCREEN_H = 500

pygame.init() 
 

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (106, 90, 205)

FPS = 60
clock = pygame.time.Clock()
running = True
screen.fill(BLACK)

MOVEMENT_SPEED = 20
CIRCLE_RADIUS = 25
INITIAL_X = 250
INITIAL_Y = 250 #начальные координаты 

x = INITIAL_X
y = INITIAL_Y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if y == CIRCLE_RADIUS:  
            y = SCREEN_H
        else:
            y = max(CIRCLE_RADIUS, y - MOVEMENT_SPEED)
    if pressed[pygame.K_DOWN]:
        if y == SCREEN_H - CIRCLE_RADIUS:  
            y = 0
        else:
            y = min(SCREEN_H - CIRCLE_RADIUS, y + MOVEMENT_SPEED)
    if pressed[pygame.K_LEFT]:
        if x < 0:  
            x = SCREEN_W + CIRCLE_RADIUS
        else:
            x = max(-CIRCLE_RADIUS, x - MOVEMENT_SPEED)
    if pressed[pygame.K_RIGHT]:
        if x == SCREEN_W - CIRCLE_RADIUS:  
            x = 0
        else:
            x = min(SCREEN_W - CIRCLE_RADIUS, x + MOVEMENT_SPEED)
    


    screen.fill(WHITE)
    pygame.draw.circle(screen, PURPLE, (x,y), CIRCLE_RADIUS) #каждый раз заливается белым и рисуется круг после заливки
    

    pygame.display.flip()
    clock.tick(FPS)