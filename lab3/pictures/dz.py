import numpy as np
import sys
import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))

running = True
#background
rect(screen,(150,150,150),(0, 0, 900, 350))
#moon
circle(screen,(255,255,255),(800,100),80)
#clouds no blur
pygame.draw.ellipse(screen,(40,40,40),(50,100,720,100))
pygame.draw.ellipse(screen,(120,120,120),(400,50,500,100))
def dom(x,y):
    rect(screen,(63,62,0),(50 + x, 200 + y, 200, 250))
    polygon(screen,(0,0,0),[(25 + x, 200 + y), (35 + x, 180 + y), (240 + 25 + x ,180 + y), (250 + 25 + x,200 + y)])
    rect(screen,(40,40,40),(75 + x, 140 + y, 5, 52))
    rect(screen,(40,40,40),(250 + x, 140 + y, 5, 52))
    rect(screen,(40,40,40),(85 + x, 130 + y, 12, 65))
    rect(screen,(40,40,40),(200 + x, 160 + y, 5, 20))
    rect(screen, (172, 147, 98), (70 + x,200 + y, 20, 100))
    rect(screen, (172, 147, 98), (120 + x,200 + y, 20, 100))
    rect(screen, (172, 147, 98), (175 + x,200 + y, 20, 100))
    rect(screen, (172, 147, 98), (220 + x,200 + y, 20, 100))
    rect(screen, (40,40,40), (25 + x, 300 + y, 250,40))
    rect(screen, (40,40,40), (65 + x, 265 + y, 10, 35))
    rect(screen, (40,40,40), (105 + x, 265 + y, 10, 35))
    rect(screen, (40,40,40), (145 + x, 265 + y, 10, 35))
    rect(screen, (40,40,40), (185 + x, 265 + y, 10, 35))
    rect(screen, (40,40,40), (225 + x, 265 + y, 10, 35))
    rect(screen, (40,40,40), (30 + 12 + x, 255 + y, 220, 20))
    rect(screen, (40,40,40), (32 + x, 275 + y, 10, 25))
    rect(screen, (40,40,40), (260 + x, 275 + y, 10, 25))
    rect(screen,(50, 25, 0), (60 + x, 375 + y, 50, 50))
    rect(screen,(50, 25, 0), (120 + x, 375 + y, 50, 50))
    rect(screen,(210, 210, 0), (190 + x, 375 + y, 50, 50))
    
dom(300,100)
dom(630, 10)

#blured clouds
surf1 = pygame.Surface((500, 100))
pygame.draw.ellipse(surf1,(40,40,40),(0, 0, 500, 100))
surf1.set_colorkey((0,0,0))
surf1.set_alpha(200)
screen.blit(surf1, (400, 250))

surf2 = pygame.Surface((700,100))
pygame.draw.ellipse(surf2,(120,120,120),(0,0,700,100))
surf2.set_colorkey((0,0,0))
surf2.set_alpha(120)
screen.blit(surf2, (150,400))

surf3 = pygame.Surface((500,100))
pygame.draw.ellipse(surf3,(120,120,120),(0,0,500,100))
surf3.set_colorkey((0,0,0))
surf3.set_alpha(120)
screen.blit(surf3, (450,450))

surf4 = pygame.Surface((500,90))
pygame.draw.ellipse(surf4,(120,120,120),(0,0,500,90))
surf4.set_colorkey((0,0,0))
surf4.set_alpha(120)
screen.blit(surf4, (-100,500))

dom(20, 180)

def prividen(x,y):
    ghost = pygame.Surface((300,500))
    priv1 = [0] * 60
    priv2 = [0] * 50
    priv3 = [0] * 110
    circle(ghost,(210,210,210),(100, 50),20)
    for i in range(60):
        priv1[i]=[round(100 - 20 * 0.71) - i , 50 + 50 - 0.02*(-i + 50) ** 2]
    for i in range(110):
        priv3[i] = [round(100 - 74.2) + i, 50 + 40 + 12.7 + 5 * (np.sin((i - 0.5 * np.pi)/10) + np.sin((i - 0.5 * np.pi)/5))]
    for i in range(50):
        priv2[i] = [100 + 46 - i, 50 + 49.26 + 0.02 * (-i + 50) ** 2 - 50]
    polygon(ghost,(210,210,210),priv1 + priv3 + priv2)
    
    circle(ghost,(0,220,255),(100 - 10, 50 - 5),6)
    circle(ghost,(0,220,255),(100 + 10, 50 - 7),6)
    circle(ghost,(0,0,0),(100 - 12,50 - 5),2)
    circle(ghost,(0,0,0), (100 + 8, 50 - 7),2)
    
    el1 = pygame.Surface((20,20))
    pygame.draw.ellipse(el1,(255,255,255),(0,2,6,2))
    el2 = pygame.transform.rotate(el1,30)
    el2.set_colorkey((0,0,0))
    ghost.blit(el2,(100 - 12, 50 - 17))

    el3 = pygame.Surface((20,20))
    pygame.draw.ellipse(el3,(255,255,255),(0,2,6,2))
    el4 = pygame.transform.rotate(el3,30)
    el4.set_colorkey((0,0,0))
    ghost.blit(el4,(100 + 8, 50 - 19))

    ghost.set_colorkey((0,0,0))
    ghost.set_alpha(220)
    screen.blit(ghost, (x,y))
    
prividen(520,320)
prividen(550,360)




# big ghost from last program


priv1 = [0] * 150
priv2 = [0] * 100
privsin1 = [0] * 160
privsin2 = [0] * 140
for i in range(150):
    priv1[i] = [500 + i, 700 - 0.05 * (i/3 + 5) ** 2]
for i in range(100):
    priv2[i] = [698 + i, 531 + 0.01 * i ** 2]

circle(screen, (220,220,220),(round(650 + 30 * 0.61), round(549 - 30 * 0.61)),40)
priv3 = [round(650 + 30 * 0.61) + 30, round(549 - 30 * 0.61)]
priv = priv1 + priv2
polygon(screen, (220,220,220), priv)
#1 part of bottom of ghost
for i in range(160):
    privsin1[i] = [ i, 100 + 10 * np.sin((i - 0.5 * np.pi)/20)]
crek1 = pygame.Surface((160,500))
polygon  (crek1, (220,220,220), privsin1 +[[130,0]])
crek2 = pygame.transform.rotate(crek1, -5)
crek2.set_colorkey((0,0,0))
screen.blit(crek2, (500, 590))
#second part of bottom of a ghost
crek3 = pygame.Surface((160,300))
for i in range(140):
    privsin2[i] = [i, 100 + 10 * np.sin((i - 0.5 * np.pi)/20)]
polygon  (crek3, (220,220,220),[[50,0]] + privsin2 + [[130,50]] )
crek4 = pygame.transform.rotate(crek3, 35)
crek4.set_colorkey((0,0,0))
screen.blit(crek4,(630,542))
#eyes
circle(screen,(0,220,255),(round(650 + 30 * 0.61)-20,round(549 - 30 * 0.61) - 5),10)
circle(screen,(0,220,255),(round(650 + 30 * 0.61)+20,round(549 - 30 * 0.61) - 10),10)
circle(screen,(0,0,0),(round(650 + 30 * 0.61)-20-3,round(549 - 30 * 0.61) - 5),2)
circle(screen,(0,0,0),(round(650 + 30 * 0.61)+20 - 3,round(549 - 30 * 0.61) - 10),2)

eli1 = pygame.Surface((50,50))
pygame.draw.ellipse(eli1,(255,255,255),(0,3,10,4))
eli2 = pygame.transform.rotate(eli1,30)
eli2.set_colorkey((0,0,0))
screen.blit(eli2,((round(650 + 30 * 0.61)-20-3,round(549 - 30 * 0.61) - 35)))

eli3 = pygame.Surface((50,50))
pygame.draw.ellipse(eli3,(255,255,255),(0,3,10,4))
eli4 = pygame.transform.rotate(eli3,30)
eli4.set_colorkey((0,0,0))
screen.blit(eli4,((round(650 + 30 * 0.61)+20-3,round(549 - 30 * 0.61) - 40)))



prividen(500,550)

# inverted ghosts

def privideninv(x,y):
    ghost = pygame.Surface((300,500))
    priv1 = [0] * 60
    priv2 = [0] * 50
    priv3 = [0] * 110
    circle(ghost,(210,210,210),(100, 50),20)
    for i in range(60):
        priv1[i]=[round(100 - 20 * 0.71) - i , 50 + 50 - 0.02*(-i + 50) ** 2]
    for i in range(110):
        priv3[i] = [round(100 - 74.2) + i, 50 + 40 + 12.7 + 5 * (np.sin((i - 0.5 * np.pi)/10) + np.sin((i - 0.5 * np.pi)/5))]
    for i in range(50):
        priv2[i] = [100 + 46 - i, 50 + 49.26 + 0.02 * (-i + 50) ** 2 - 50]
    polygon(ghost,(210,210,210),priv1 + priv3 + priv2)
    
    circle(ghost,(0,220,255),(100 - 10, 50 - 5),6)
    circle(ghost,(0,220,255),(100 + 10, 50 - 7),6)
    circle(ghost,(0,0,0),(100 - 12,50 - 5),2)
    circle(ghost,(0,0,0), (100 + 8, 50 - 7),2)
    
    el1 = pygame.Surface((20,20))
    pygame.draw.ellipse(el1,(255,255,255),(0,2,6,2))
    el2 = pygame.transform.rotate(el1,30)
    el2.set_colorkey((0,0,0))
    ghost.blit(el2,(100 - 12, 50 - 17))

    el3 = pygame.Surface((20,20))
    pygame.draw.ellipse(el3,(255,255,255),(0,2,6,2))
    el4 = pygame.transform.rotate(el3,30)
    el4.set_colorkey((0,0,0))
    ghost.blit(el4,(100 + 8, 50 - 19))

    ghostinv = pygame.transform.flip(ghost,True, False)
    ghostinv.set_colorkey((0,0,0))
    ghostinv.set_alpha(220)
    screen.blit(ghostinv, (x,y))
    
privideninv(20,550)    
privideninv(30, 600)






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
