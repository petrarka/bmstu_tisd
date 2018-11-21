import pygame
from math import *
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (0, 0, 255)
YELLOW = (255,255,0)

pygame.init()
clock = pygame.time.Clock()

done = False

screen = pygame.display.set_mode([700,500])
line1_x1 = 350
line1_y1 = 250
line1_x2 = 400
line1_y2 = 250
angle = 9.42
angle1 = 2
ball_x = 350
ball_y = 250
i = 2
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tri1_x1 = ball_x + 30*cos(angle)
    tri1_y1 = ball_y + 30*sin(angle)
    ball_x += i
    angle += 0.05
##    line1_x1 -= 2
##    line1_x2 -= 2

    if ball_x == 670 or ball_x == 30:
        print(ball_x,i)
        print(tri1_x1,tri1_y1)
        i *= -1
    screen.fill(BLUE)
    
    pygame.draw.line(screen, BLACK,[ball_x,ball_y],[ball_x*2 - tri1_x1,ball_y*2 - tri1_y1],4)
    pygame.draw.circle(screen, BLACK,[ball_x,ball_y],30,4)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
