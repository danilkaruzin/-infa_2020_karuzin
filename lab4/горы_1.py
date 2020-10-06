import pygame
from pygame.draw import *
import numpy as np
from random import randint 
pygame.init()

FPS = 6
screen = pygame.display.set_mode((1200, 800))
screen.fill((179, 156, 183))

yellow = (255, 255, 0)
beige = (255, 214, 160)
beigewhite = (255, 220, 200)
orange = (255, 138, 0)
brown = (165,42,42)
darkmagenta = (50,0,50)
black = (0,0,0)
blackgrage =(0,0,1)

#background
def background(displaysize1,displaysize2):
    rect(screen, beige, (0, 0, displaysize1, round(displaysize2 * 0.154)))

    rect(screen, beigewhite, (0, round(displaysize2 * 0.154), displaysize1, round(displaysize2 * 0.154)))

    rect(screen, beige, (0, 2 * round(displaysize2 * 0.154), displaysize1, round(displaysize2 * 0.154)))


#sun
def sun(displaysize1,displaysize2):
    circle(screen, yellow, (round(displaysize1 * 0.5) , round(displaysize2 * 0.154)), round(0.5 * (0.05 * displaysize1 + 0.05 * displaysize2)))


# the farrest mountscale
def mountscale1(pos1,pos2):
    surf1 = pygame.Surface((1200,400))
    x = 0.0
    y = 400.0
    gor = [[0, 0]] * 1200
    for x in range(0, 1200):
        gor[x] = [round(x), round(y)]
        if x < 161:
            y = 350 - 100 * (x / 100) * (x / 100)
        if (x > 160) and (x < 201):
            y = y + 1
        if (x > 200) and (x < 211):
            y = y + 5
        if (x > 210) and (x < 401):
            y = y + (375 - y) / 200
        if (x > 400) and (x < 501):
            y = y - 0.5
        if (x > 500) and (x < 541):
            y = y + 0.75
        if (x > 540) and (x < 601):
            y = y - 1 / 3
        if (x > 600) and (x < 801):
            y = y - 2 * (x - 633.3333) / 300
        if (x > 800) and (x < 1001):
            y = y + 2 * (x - 870) / 125
        if (x > 1000) and (x < 1100):
            y = y + (x - 1151) / 100
        if (x > 1100) and (x < 1197):
            y = y + (x - 1200) / 200
        if x > 1197:
            y = y + 150
    polygon(surf1, orange, gor)
    surf1.set_colorkey(black)
    screen.blit(surf1,(pos1,pos2))

    
# montains in the middle
def mountscale2(pos1,pos2):
    surf2 = pygame.Surface((1200,510))
    x = 0
    y = 200
    gor = [[0, 0]] * 1200
    for x in range(x, 1200):
        gor[x] = [round(x), round(y)]
        if x < 151:
            y = y + 2 * 150 * (x - 80) / 5000
        if (x > 150) and (x < 201):
            y = y - 1.5
        if (x > 200) and (x < 261):
            y = y + 1
        if (x > 260) and (x < 301):
            y = y - 2
        if (x > 300) and (x < 431):
            y = y + 0.3
        if (x > 430) and (x < 481):
            y = y + 1.5
        if (x > 480) and (x < 601):
            y = y - 0.15
        if (x > 600) and (x < 801):
            y = y + 2 * (x - 740) / 90
        if (x > 800) and (x < 901):
            y = y - 2 * (x - 980) / 250
        if (x > 900) and (x < 1001):
            y = y - 0.8
        if (x > 1000) and (x < 1031):
            y = y + 2
        if (x > 1030) and (x < 1101):
            y = y - 1.2
        if (x > 1100) and (x < 1151):
            y = y + 0.8
        if (x > 1150) and (x < 1198):
            y = y - 3
        if x > 1197:
            y = 200 
    polygon(surf2, brown, gor)
    surf2.set_colorkey(black)
    screen.blit(surf2,(pos1,pos2))
    
    #montains in front
def mountscale3(pos1,pos2):
    surf3 = pygame.Surface((1200,500))
    x = 0
    y = 400
    gor = [[0, 0]] * 1200
    for x in range (x,1200):
        gor[x] =[round(x),round(y)]
        if  x < 150:
            y = 0 + 0.5 * x
        if x > 149 and x < 250:
            y = y + 2
        if x > 249 and x < 500:
            y = y  -  0.001 * (x - 500)
        if x > 499 and x < 650:
            y = y - 0.75
        if x > 649 and x < 720:
            y = y + 0.5
        if x > 719 and x < 1197:
            y = y - (x - 800)/200
        if x > 1196:
            y = 400
    polygon(surf3,darkmagenta,gor )
    surf3.set_colorkey(black)
    screen.blit(surf3,(pos1,pos2))

def ptichka (x,y,size1,size2):
    ptica = pygame.Surface((3*(size1 + size2),3*(size2 + size1)))
    
    el1 = pygame.Surface((size1,size2))
    ellipse(el1,blackgrage,(0,0,size1,size2))
    el1pov = pygame.transform.rotate(el1,-30)
    el1pov.set_colorkey(black)
    ptica.blit(el1pov,(0,0))

    #circle(ptica, yellow,(round(0.5 * size2 * 0.5 + size1 * 0.86),round(0.5 * size2 * 0.86 + size1 * 0.5)),5)

    el2 = pygame.Surface((size1,size2))
    ellipse(el2,blackgrage,(0,0,size1,size2))
    el2pov = pygame.transform.rotate(el2,10)
    el2pov.set_colorkey(black)
    ptica.blit(el2pov,(round(0.5 * size2 * 0.5 + size1 * 0.86 - size2 *0.5 *0.17), round(0.5 * size2 * 0.86 + size1 * 0.5 - 1.33 * size2  )))
    
    ptica.set_colorkey(black)
    screen.blit(ptica,(x,y))
    
background(1200,800)
sun(1200, 800)
mountscale1(0,0)
mountscale2(0,400)
mountscale3(0,550)

# изначальной программе птиц не было,так что их на главный экран не ввожу







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
