import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

# text for scores
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x1, y1):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x1, y1)
    surf.blit(text_surface, text_rect)
# starting number of points
k=0

# positions,sizes and velocities for balls
kolvosharov = 5
shar = [0] * kolvosharov
for i in range (kolvosharov):
    shar[i] = [0] * 6
for i in range (kolvosharov):
    shar[i][0] = randint(100,1000)
    shar[i][1] = randint(100, 800)
    shar[i][2] = randint(30,80)
    shar[i][3] = randint(-2,2)
    shar[i][4] = randint(-2,2)
    shar[i][5] = COLORS[randint(0, 5)]

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    for i in range (kolvosharov):
        #spawn balls
        circle(screen,shar[i][5],(shar[i][0], shar[i][1]),shar[i][2])
        if shar[i][0] <= shar[i][2] or shar[i][0] + shar[i][2] >= 1200:
            shar[i][3] *= -1
        if shar[i][1] <= shar[i][2] or shar[i][1] + shar[i][2] >= 900:
            shar[i][4] *= -1
        shar[i][0] += shar[i][3]
        shar[i][1] += shar[i][4]
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (kolvosharov):
                #reason for giving points
                if ((shar[i][0] - event.pos[0]) ** 2 + (shar[i][1] - event.pos[1]) ** 2) ** (0.5) <= shar[i][2]:
                    k += 1
                    #spawning new ball
                    shar[i][0] = randint(100,1000)
                    shar[i][1] = randint(100, 800)
                    shar[i][2] = randint(30,80)
                    shar[i][3] = randint(-2,2)
                    shar[i][4] = randint(-2,2)
                    shar[i][5] = COLORS[randint(0, 5)]
                    
    
    pygame.display.update()
    screen.fill(BLACK)
    draw_text(screen, str(k), 80, 600,5)
    

pygame.quit()
