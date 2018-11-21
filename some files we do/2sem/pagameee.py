import pygame
from math import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (0, 0, 255)
YELLOW = (255,255,0)

pygame.init()
 
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Don Quixote")
 
done = False
 

clock = pygame.time.Clock()
line1_x1 = 700
line1_y1 = 400
line1_x2 = 680
line1_y2 = 375

line2_x1 = 680
line2_y1 = 375
line2_x2 = 660
line2_y2 = 400

line3_x1 = 680
line3_y1 = 375
line3_x2 = 680
line3_y2 = 330

line4_x1 = 680
line4_y1 = 330
line4_x2 = 700
line4_y2 = 355

line5_x1 = 680
line5_y1 = 330
line5_x2 = 660
line5_y2 = 355

ball_x = 680
ball_y = 315

angle = 9.42
angle1 = 2

r = 10


while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    line1_x1 -= 2
    line1_x2 -= 2
    line2_x1 -= 2
    line2_x2 -= 2
    line3_x1 -= 2
    line3_x2 -= 2
    line4_x1 -= 2
    line4_x2 -= 2
    line5_x1 -= 2
    line5_x2 -= 2
    ball_x -= 2

    tri1_x1 = 300 + 150*cos(angle)
    tri1_y1 = 150 + 150*sin(angle)
    tri1_x2 = 300 + 150*cos(angle1)
    tri1_y2 = 150 + 150*sin(angle1)

    tri2_x1 = 300 + 150*cos(angle+pi)
    tri2_y1 = 150 + 150*sin(angle+pi)
    tri2_x2 = 300 + 150*cos(angle1+pi)
    tri2_y2 = 150 + 150*sin(angle1+pi)

    tri3_x1 = 300 + 150*cos(angle+pi/2)
    tri3_y1 = 150 + 150*sin(angle+pi/2)
    tri3_x2 = 300 + 150*cos(angle1+pi/2)
    tri3_y2 = 150 + 150*sin(angle1+pi/2)

    tri4_x1 = 300 + 150*cos(angle-pi/2)
    tri4_y1 = 150 + 150*sin(angle-pi/2)
    tri4_x2 = 300 + 150*cos(angle1-pi/2)
    tri4_y2 = 150 + 150*sin(angle1-pi/2)
    angle += 0.01
    angle1 += 0.01

    if line1_x1 <= -20:
        line1_x1 = 700
        line1_x2 = 680
        line2_x1 = 680
        line2_x2 = 660
        line3_x1 = 680
        line3_x2 = 680
        line4_x1 = 680
        line4_x2 = 700
        line5_x1 = 680
        line5_x2 = 660
        ball_x = 680

    screen.fill(BLUE)
    
    pygame.draw.polygon(screen,GREEN,([0,400],[700,400],[700,500],[0,500]))
    pygame.draw.polygon(screen,WHITE,([200,400],[400,400],[350,100],[250,100]))
##    pygame.draw.polygon(screen,BLACK,([290,400],[310,400],[310,330],[290,330]))

    
    pygame.draw.line(screen,BLACK,[line1_x1,line1_y1],[line1_x2,line1_y2],4)
    pygame.draw.line(screen,BLACK,[line2_x1,line2_y1],[line2_x2,line2_y2],4)
    pygame.draw.line(screen,BLACK,[line3_x1,line3_y1],[line3_x2,line3_y2],4)
    pygame.draw.line(screen,BLACK,[line4_x1,line4_y1],[line4_x2,line4_y2],4)
    pygame.draw.line(screen,BLACK,[line5_x1,line5_y1],[line5_x2,line5_y2],4)
    pygame.draw.circle(screen, BLACK, [ball_x, ball_y], 15, 4)

    
    pygame.draw.polygon(screen,YELLOW,([300,150],[600 - tri1_x1,300 - tri1_y1],[600-tri1_x2,300-tri1_y2]))
    pygame.draw.polygon(screen,YELLOW,([300,150],[600 - tri2_x1,300 - tri2_y1],[600-tri2_x2,300-tri2_y2]))
    pygame.draw.polygon(screen,YELLOW,([300,150],[600 - tri3_x1,300 - tri3_y1],[600-tri3_x2,300-tri3_y2]))
    pygame.draw.polygon(screen,YELLOW,([300,150],[600 - tri4_x1,300 - tri4_y1],[600-tri4_x2,300-tri4_y2]))

    pygame.draw.circle(screen, BLACK, [300, 150], 30)
    pygame.draw.circle(screen, BLACK, [300, 150], 5)
    
    clock.tick(60)
 
    pygame.display.flip()
 
pygame.quit()
