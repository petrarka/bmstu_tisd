# Анимация.
# Корова ходит, курица бегает на переднем плане
#Сушина АД ИУ7-21б

# screen - окно
# x,y,a,y1,x1 - рабочие пременные
# i - количество кадров
# side, side1 - сторона движения
# h_rect,b_rect,n_rect,n2_rect,rect_rect - прямоугольники
# poligon_points - точки треугольника
# mainloop - цикл
# bg_color - цвет фона

import pygame, sys
from pygame.locals import *
from math import sin,cos

# окно
pygame.init()

screen = pygame.display.set_mode((1200,700), 0, 32)
pygame.display.set_caption("My first animation")

#движение головы
def circle(x,y,i):
    return round(x + 1*cos(i/200)), round(y + 5*sin(i/200))

#движение всей коровы (от трех переменных)
def cow_run(x,y,i):
    return round(x + 130*cos(i/800)), round(y + 50*sin(i/400))

#движение всей коровы(от массива)   
def cow_run_t(a,i):
    return round(a[0] + 130*cos(i/800)), round(a[1]+ 50*sin(i/400))

#движение пары ног
def legs(x,y,i):
    return round(x + 30*cos(i/200)), round(y+ abs(10*sin(i/200)))
    return x,y

#движение второй пары ног
def leg2(x,y,i):
    return round(x - 30*cos(i/200)), round(y+ abs(10*sin(i/200)))

#движение хвоста
def tag(x,y,i):
    return round(x + 10*cos(i/200)), round(y+ abs(2*sin(i/200)))

#движение кончика хвоста
def tag2(x,y,i):
    return round(x + 20*cos(i/200)), round(y- abs(2*sin(i/200)))

    
def cow_head(i,side):
    if side:
        x1,y1 = 400,200
    else:
        x1,y1 = 150,200
    x2,y2 = x1+140,y1+120
    #голова
    x,y = circle(x1,y1,i)
    h_rect = Rect(cow_run(x,y,i),(140,120))
    pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)
    pygame.draw.ellipse(screen, (0,0,0), h_rect, 1)

    #глаза
    x,y = circle(x1+40,y1+40,i)
    pygame.draw.circle(screen, (0,0,0), cow_run(x,y,i), 5, 0)
    pygame.draw.circle(screen, (0,0,0), cow_run(x,y,i), 10, 1)
    x,y = circle(x2-40,y1+40,i)
    pygame.draw.circle(screen, (0,0,0), cow_run(x,y,i) , 5, 0)
    pygame.draw.circle(screen, (0,0,0), cow_run(x,y,i), 10, 1)

    #нос
    x,y = circle(x1+35,y1+60,i)
    n_rect = Rect( cow_run(x,y,i),(70,50))
    pygame.draw.arc(screen, (0,0,0), n_rect, 0.5, 2.64)

    #ноздри
    x,y = circle(x1+55,y1+75,i)
    pygame.draw.circle(screen, (0,0,0),cow_run(x,y,i) , 5, 0)
    x,y = circle(x1+85,y1+75,i)
    pygame.draw.circle(screen, (0,0,0),cow_run(x,y,i), 5, 0)

    #рот
    x,y = circle(x1+40,y1+60,i)
    n2_rect = Rect(cow_run(x,y,i),(60,50))
    pygame.draw.arc(screen, (0,0,0), n2_rect,-2.14 , -1 )

    #рога
    poligon_points = [cow_run_t(circle(x1+20,y1+18,i),i),\
                      cow_run_t(circle(x1+30,y1+10,i),i),\
                      cow_run_t(circle(x1,y1-10,i),i)]
    pygame.draw.polygon(screen, (155,115,75), poligon_points,0)
    pygame.draw.polygon(screen, (0,0,0), poligon_points,1)
    
    poligon_points = [cow_run_t(circle(x2-20,y1+18,i),i),\
                      cow_run_t(circle(x2-30,y1+10,i),i),\
                      cow_run_t(circle(x2,y1-10,i),i)]
    pygame.draw.polygon(screen, (155,115,75), poligon_points,0)
    pygame.draw.polygon(screen, (0,0,0), poligon_points,1)

    #уши
    poligon_points = [cow_run_t(circle(x1+20,y1+18,i),i),\
                      cow_run_t(circle(x1-10,y1+45,i),i),\
                      cow_run_t(circle(x1-22,y1+35,i),i)]
    pygame.draw.polygon(screen, (255,255,255), poligon_points,0)
    pygame.draw.polygon(screen, (0,0,0), poligon_points,2)
    
    poligon_points = [cow_run_t(circle(x2-20,y1+18,i),i),\
                      cow_run_t(circle(x2+10,y1+45,i),i),\
                      cow_run_t(circle(x2+22,y1+35,i),i)]
    pygame.draw.polygon(screen, (255,255,255), poligon_points,0)
    pygame.draw.polygon(screen, (0,0,0), poligon_points,2)

def cow_body(i,side):
    if side:
        #ноги задний план
        pygame.draw.line(screen,(0,0,0), cow_run(470,350,i),\
                     cow_run_t(leg2(470,450,i),i), 22)
        pygame.draw.line(screen,(0,0,0), cow_run(260,350,i),\
                         cow_run_t(leg2(260,450,i),i), 22)

        pygame.draw.line(screen,(255,255,255), cow_run(260,350,i),\
                         cow_run_t(leg2(260,450,i),i), 20)
        pygame.draw.line(screen,(255,255,255), cow_run(470,350,i),\
                         cow_run_t(leg2(470,450,i),i), 20)
        #хвост
        pygame.draw.line(screen,(0,0,0), cow_run(220,288,i),\
                         cow_run_t(tag(220,250,i),i), 2)

        pygame.draw.line(screen,(0,0,0), cow_run(220,288,i),\
                         cow_run_t(tag(220,250,i),i), 2)

        pygame.draw.line(screen,(0,0,0), cow_run_t(tag(220,250,i),i),\
                         cow_run_t(tag2(215,245,i),i), 2)
        
        pygame.draw.line(screen,(0,0,0), cow_run_t(tag(220,250,i),i),\
                         cow_run_t(tag2(220,245,i),i), 2)
        pygame.draw.line(screen,(0,0,0), cow_run_t(tag(220,250,i),i),\
                         cow_run_t(tag2(225,245,i),i), 2)
        #тело 
        b_rect = Rect(cow_run(200,250,i),(300,140))
        pygame.draw.ellipse(screen, (255,255,255), b_rect, 0)
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 1)

        b_rect = Rect(cow_run(300,270,i),(100,50))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        b_rect = Rect(cow_run(310,270,i),(60,80))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        b_rect = Rect(cow_run(270,330,i),(30,40))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        b_rect = Rect(cow_run(420,310,i),(20,30))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        #ноги передний план
        pygame.draw.line(screen,(0,0,0), cow_run(230,350,i),\
                     cow_run_t(legs(230,450,i),i), 22)   
        pygame.draw.line(screen,(0,0,0), cow_run(440,350,i),\
                         cow_run_t(legs(440,450,i),i), 22)
        
        pygame.draw.line(screen,(255,255,255), cow_run(440,350,i),\
                         cow_run_t(legs(440,450,i),i), 20)
        pygame.draw.line(screen,(255,255,255), cow_run(230,350,i),\
                         cow_run_t(legs(230,450,i),i), 20)
    else:
        #ноги задний план
        pygame.draw.line(screen,(0,0,0), cow_run(230,350,i),\
                         cow_run_t(legs(230,450,i),i), 22)   
        pygame.draw.line(screen,(0,0,0), cow_run(440,350,i),\
                         cow_run_t(legs(440,450,i),i), 22)
        
        pygame.draw.line(screen,(255,255,255), cow_run(440,350,i),\
                         cow_run_t(legs(440,450,i),i), 20)
        pygame.draw.line(screen,(255,255,255), cow_run(230,350,i),\
                         cow_run_t(legs(230,450,i),i), 20)
        

        #хвост
        pygame.draw.line(screen,(0,0,0), cow_run(480,288,i),\
                         cow_run_t(tag(480,250,i),i), 2)

        pygame.draw.line(screen,(0,0,0), cow_run_t(tag(480,250,i),i),\
                         cow_run_t(tag2(475,245,i),i), 2)
        
        pygame.draw.line(screen,(0,0,0), cow_run_t(tag(480,250,i),i),\
                         cow_run_t(tag2(480,245,i),i), 2)
        pygame.draw.line(screen,(0,0,0), cow_run_t(tag(480,250,i),i),\
                         cow_run_t(tag2(485,245,i),i), 2)

        #тело        
        b_rect = Rect(cow_run(200,250,i),(300,140))
        pygame.draw.ellipse(screen, (255,255,255), b_rect, 0)
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 1)

        b_rect = Rect(cow_run(300,270,i),(100,50))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        b_rect = Rect(cow_run(330,270,i),(60,80))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        b_rect = Rect(cow_run(400,330,i),(30,40))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        b_rect = Rect(cow_run(260,310,i),(20,30))
        pygame.draw.ellipse(screen, (0,0,0), b_rect, 0)

        #ноги передний план        
        pygame.draw.line(screen,(0,0,0), cow_run(470,350,i),\
                         cow_run_t(leg2(470,450,i),i), 22)
        pygame.draw.line(screen,(0,0,0), cow_run(260,350,i),\
                         cow_run_t(leg2(260,450,i),i), 22)

        pygame.draw.line(screen,(255,255,255), cow_run(260,350,i),\
                         cow_run_t(leg2(260,450,i),i), 20)
        pygame.draw.line(screen,(255,255,255), cow_run(470,350,i),\
                         cow_run_t(leg2(470,450,i),i), 20)

#движение всей курицы
def hen_run(a,i):
    return round(a[0] - 300*cos(i/400)), round(a[1] + 30*abs(sin(i/600)))

#движение одной ноги курицы
def h_leg1(x,y,i):
    return round(x + 15*cos(i/75)), round(y+ abs(5*sin(i/75)))

#движение второй ноги курицы
def h_leg2(x,y,i):
    return round(x - 10*cos(i/75)), round(y+ abs(5*sin(i/75)))


def hen_body(i,side):
    if side:
        #ноги
        pygame.draw.line(screen, (155,115,75),hen_run((725,555),i),\
                         hen_run(h_leg1(725,580,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run((745,555),i),\
                         hen_run(h_leg2(745,580,i),i), 2)

        pygame.draw.line(screen, (155,115,75),hen_run(h_leg1(725,580,i),i),\
                         hen_run(h_leg1(732,583,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg1(725,580,i),i),\
                         hen_run(h_leg1(733,580,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg1(725,580,i),i),\
                         hen_run(h_leg1(734,577,i),i), 2)

        pygame.draw.line(screen, (155,115,75),hen_run(h_leg2(745,580,i),i),\
                         hen_run(h_leg2(752,583,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg2(745,580,i),i),\
                         hen_run(h_leg2(753,580,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg2(745,580,i),i),\
                         hen_run(h_leg2(754,577,i),i), 2)
        
        pygame.draw.circle(screen, (255,255,255),hen_run((725,555),i) , 10, 0)
        pygame.draw.circle(screen, (255,255,255),hen_run((745,555),i) , 10, 0)

        #хвост 
        h_rect = Rect(hen_run((683,487),i),(12,30))
        pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)
        h_rect = Rect(hen_run((692,482),i),(12,30))
        pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)
        h_rect = Rect(hen_run((701,487),i),(12,30))
        pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)

        pygame.draw.line(screen, (255,255,255),hen_run((688,510),i),hen_run((712,545),i), 10)
        pygame.draw.line(screen, (255,255,255),hen_run((690,505),i),hen_run((720,530),i), 25)
        pygame.draw.line(screen, (255,255,255),hen_run((705,500),i),hen_run((725,505),i), 10)

        #тело
        b_rect = Rect(hen_run((700,500),i),(70,60))
        pygame.draw.ellipse(screen, (255,255,255), b_rect, 0)

        #гребешок
        h_rect = Rect(hen_run((765,460),i),(9,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)
        h_rect = Rect(hen_run((772,458),i),(9,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)
        h_rect = Rect(hen_run((780,460),i),(9,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)

        #голова
        pygame.draw.line(screen, (255,255,255),hen_run((735,510),i),hen_run((770,480),i), 25)
        pygame.draw.line(screen, (255,255,255),hen_run((750,515),i),hen_run((770,480),i), 25)
        pygame.draw.line(screen, (255,255,255),hen_run((765,525),i),hen_run((770,482),i), 10)
        pygame.draw.circle(screen, (255,255,255),hen_run((775,480),i) , 15, 0)
        pygame.draw.circle(screen, (0,0,0),hen_run((780,475),i) , 2, 0)

        poligon_points = [hen_run((788,476),i),hen_run((788,484),i),hen_run((800,480),i)]
        pygame.draw.polygon(screen, (155,115,75), poligon_points,0)

        h_rect = Rect(hen_run((786,484),i),(7,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)

        h_rect = Rect(hen_run((710,510),i),(40,30))
        pygame.draw.ellipse(screen, (0,0,0), h_rect, 1)

        pygame.draw.line(screen, (0,0,0),hen_run((730,525),i),\
                         hen_run((711,525),i), 1)
                            
    else:
        #ноги
        pygame.draw.line(screen, (155,115,75),hen_run((725,555),i),\
                         hen_run(h_leg1(725,580,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run((745,555),i),\
                         hen_run(h_leg2(745,580,i),i), 2)

        pygame.draw.line(screen, (155,115,75),hen_run(h_leg1(725,580,i),i),\
                         hen_run(h_leg1(718,583,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg1(725,580,i),i),\
                         hen_run(h_leg1(717,580,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg1(725,580,i),i),\
                         hen_run(h_leg1(716,577,i),i), 2)

        pygame.draw.line(screen, (155,115,75),hen_run(h_leg2(745,580,i),i),\
                         hen_run(h_leg2(738,583,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg2(745,580,i),i),\
                         hen_run(h_leg2(737,580,i),i), 2)
        pygame.draw.line(screen, (155,115,75),hen_run(h_leg2(745,580,i),i),\
                         hen_run(h_leg2(736,577,i),i), 2)
        
        pygame.draw.circle(screen, (255,255,255),hen_run((725,555),i) , 10, 0)
        pygame.draw.circle(screen, (255,255,255),hen_run((745,555),i) , 10, 0)

        # хвост
        h_rect = Rect(hen_run((774,487),i),(12,30))
        pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)
        h_rect = Rect(hen_run((766,482),i),(12,30))
        pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)
        h_rect = Rect(hen_run((758,487),i),(12,30))
        pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)

        pygame.draw.line(screen, (255,255,255),hen_run((779,510),i),\
                         hen_run((758,545),i), 10)
        pygame.draw.line(screen, (255,255,255),hen_run((782,504),i),\
                         hen_run((740,530),i), 25)
        pygame.draw.line(screen, (255,255,255),hen_run((770,500),i),\
                         hen_run((745,505),i), 10)
        # тело
        b_rect = Rect(hen_run((700,500),i),(70,60))
        pygame.draw.ellipse(screen, (255,255,255), b_rect, 0)

        # гребешок
        h_rect = Rect(hen_run((700,460),i),(9,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)
        h_rect = Rect(hen_run((693,458),i),(9,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)
        h_rect = Rect(hen_run((685,460),i),(9,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)

        #голова
        pygame.draw.line(screen, (255,255,255),hen_run((735,510),i),\
                         hen_run((700,480),i), 25)
        pygame.draw.line(screen, (255,255,255),hen_run((720,515),i),\
                         hen_run((700,480),i), 25)
        pygame.draw.line(screen, (255,255,255),hen_run((705,525),i),\
                         hen_run((700,482),i), 10)
        pygame.draw.circle(screen, (255,255,255),hen_run((695,480),i) , 15, 0)
        pygame.draw.circle(screen, (0,0,0),hen_run((690,475),i) , 2, 0)

        poligon_points = [hen_run((680,476),i),hen_run((680,484),i),\
                          hen_run((668,480),i)]
        pygame.draw.polygon(screen, (155,115,75), poligon_points,0)

        h_rect = Rect(hen_run((679,484),i),(7,12))
        pygame.draw.ellipse(screen, (255,0,0), h_rect, 0)

        h_rect = Rect(hen_run((720,510),i),(40,30))
        pygame.draw.ellipse(screen, (0,0,0), h_rect, 1)
        pygame.draw.line(screen, (0,0,0),hen_run((740,525),i),\
                         hen_run((759,525),i), 1)

def o(x,y,i):
    return round(x - 770*cos(i/3000)), round(y + 100*(sin(i/400)))

bgColor = (150,150,255)

mainLoop = True
i = 1
side = False
side1 = True

rect_rect = Rect((0,350),(1200,800))
while mainLoop:
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            mainLoop = False
    screen.fill(bgColor)
    # формирование кода
    pygame.draw.rect(screen,(50,200,50),rect_rect,0)
    
    h_rect = Rect(o(450,100,i),(300,100))
    pygame.draw.ellipse(screen, (255,255,255), h_rect, 0)
        
    cow_body(i,side)
    cow_head(i,side)
    hen_body(i,side1)
    i+=1
    if abs(cos(i/800)-1) < 0.00001:
        side = False
    if abs(cos(i/800)+1) < 0.00001:
        side = True
    if abs(cos(i/400)-1) < 0.00001:
        side1 = True
    if abs(cos(i/400)+1) < 0.00001:
        side1 = False
        
    pygame.display.update() 
pygame.quit() 
