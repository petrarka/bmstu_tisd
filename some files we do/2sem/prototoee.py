import pygame
from math import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (10, 200, 10)
RED = (255, 0, 0)
BLUE =  (150, 190, 255)
YELLOW = (255,255,0)

pygame.init()
 
size = [700, 500]
screen = pygame.display.set_mode(size)
 
 
done = False
 

clock = pygame.time.Clock()
angle = 9.42
angle1 = 2
lin1_x1 = 250
lin1_y1 = 150
lin1_x2 = 210
lin1_y2 = 150

lin2_x1 = 250
lin2_y1 = 150
lin2_x2 = 220
lin2_y2 = 150

lin3_x1 = 220
lin3_y1 = 100
lin3_x2 = 220
lin3_y2 = 300

lin4_x1 = 280
lin4_y1 = 100
lin4_x2 = 280
lin4_y2 = 300
i = 1
j = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLUE)

    lin1_x2 = 250 + 40*cos(angle)
    lin1_y2 = 150 + 40*sin(angle)
    lin2_x2 = 250 + 30*cos(angle1 + pi)
    lin2_y2 = 150 + 30*sin(angle1 + pi)
    
    lin3_y2 -= i
    lin4_y2 += j
    
    angle += 0.01
    angle1 += 0.001

    if (lin3_y2 <= 250 or lin3_y2 >= 350):
        i *= -1
        
    if (lin4_y2 <= 250 or lin4_y2 >= 350):
        j *= -1

    pygame.draw.line(screen,BLACK,[lin3_x1, lin3_y1],[lin3_x2,lin3_y2],4)
    pygame.draw.line(screen,BLACK,[lin4_x1, lin4_y1],[lin4_x2,lin4_y2],4)
    
    pygame.draw.polygon(screen,GREEN,([200,100], [200,200],[300,200],[300,100]))
    pygame.draw.polygon(screen,RED,([200,100], [300,100],[250,50]))
    pygame.draw.circle(screen, WHITE, [250, 150], 40)
    pygame.draw.line(screen,BLACK,[lin1_x1, lin1_y1],[lin1_x2,lin1_y2],4)
    pygame.draw.line(screen,BLACK,[lin2_x1, lin2_y1],[lin2_x2,lin2_y2],4)

    pygame.draw.polygon(screen,RED,([lin1_x2,lin1_y2],[lin1_x2-10,lin1_y2-10],[lin1_x2+10,lin1_y2+10]))
    
    pygame.draw.polygon(screen,BLACK,([210,lin3_y2], [230,lin3_y2],[230,lin3_y2 + 50],[210,lin3_y2 + 50]))
    pygame.draw.polygon(screen,BLACK,([270,lin4_y2], [290,lin4_y2],[290,lin4_y2 + 50],[270,lin4_y2 + 50]))
    clock.tick(60)
     
    pygame.display.flip()
 
pygame.quit()
