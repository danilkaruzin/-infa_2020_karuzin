import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))
white = [219, 219, 219]
screen.fill(white)
circle(screen,(255, 255, 0),(400, 300), 100)
rect(screen, (0, 0, 0), (360, 340, 80,20))
circle(screen,(0, 0, 0),(438, 260), 18)
circle(screen,(0, 0, 0),(362, 260), 14)
circle(screen,(255, 0, 0),(438, 260), 18, 8)
circle(screen,(255, 0, 0),(362, 260), 14, 5)
polygon(screen, (0, 0, 0), [(410-10*0.71,260-10*0.71),(410,260),(410 + 0.71*70,260-0.71*70),(70*0.71+410-10*0.71,260-10*0.71-70*0.71)])
polygon(screen, (0, 0, 0), [(320+30, 250-60),(320-0.5*20+30,250 + 0.87*20 - 60),(320-0.5*20+70 * 0.5+30,250 + 0.87*20 + 70*0.87-60),(320+ 70*0.5+30,250+ 70* 0.87-60)])




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
