import numpy as np
import sys
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))

running = True
    
rect(screen,(150,150,150),(0, 0, 900, 400))
#moon
circle(screen,(255,255,255),(750,100),50)
#clouds 1
pygame.draw.ellipse(screen,(120,120,120),(600,120,500,50))
pygame.draw.ellipse(screen,(60,60,60),(400,170,700,60))
#house part 1
rect(screen,(63,62,0),(50, 200, 400, 500))
polygon(screen,(0,0,0),[(0, 200), (60, 160), (500-60,160), (500,200)])
rect(screen,(40,40,40),(85, 110, 10, 65))
rect(screen,(40,40,40),(300, 110, 10, 65))
#clouds 2
pygame.draw.ellipse(screen,(80,80,80),(50,70,500,70))
pygame.draw.ellipse(screen,(120,120,120),(350,70,800-350,50))
#house part 2
rect(screen,(40,40,40),(100, 90, 25, 95))
rect(screen,(40,40,40),(400, 110, 10, 70))
rect(screen, (172, 147,
              98), (70,200, 40, 200))
rect(screen, (172, 147, 98), (170,200, 40, 200))
rect(screen, (172, 147, 98), (280,200, 40, 200))
rect(screen, (172, 147, 98), (370,200, 40, 200))
rect(screen, (40,40,40), (0, 400, 500,80))
rect(screen, (40,40,40), (80, 330, 20, 70))
rect(screen, (40,40,40), (150, 330, 20, 70))
rect(screen, (40,40,40), (230, 330, 20, 70))
rect(screen, (40,40,40), (310, 330, 20, 70))
rect(screen, (40,40,40), (380, 330, 20, 70))
rect(screen, (40,40,40), (30, 310, 440, 40))
rect(screen, (40,40,40), (10, 350, 20, 50))
rect(screen, (40,40,40), (470, 350, 20, 50))
rect(screen,(50, 25, 0), (60, 550, 100, 100))
rect(screen,(50, 25, 0), (200, 550, 100, 100))
rect(screen,(210, 210, 0), (340, 550, 100, 100))



#prividenie


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

el1 = pygame.Surface((50,50))
pygame.draw.ellipse(el1,(255,255,255),(0,3,10,4))
el2 = pygame.transform.rotate(el1,30)
el2.set_colorkey((0,0,0))

el3 = pygame.Surface((50,50))
pygame.draw.ellipse(el3,(255,255,255),(0,3,10,4))
el4 = pygame.transform.rotate(el3,30)
el4.set_colorkey((0,0,0))



    




            
        
        
    

    
    
    
    
     










while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(el2,((round(650 + 30 * 0.61)-20-3,round(549 - 30 * 0.61) - 35)))
    screen.blit(el4,((round(650 + 30 * 0.61)+20-3,round(549 - 30 * 0.61) - 40)))
    pygame.display.update()
