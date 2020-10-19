import pygame
from pygame.draw import *
import random
from os import path
img_dir = path.join(path.dirname(__file__), "img")
pygame.init()
clock = pygame.time.Clock()
FPS = 30
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]
WIDTH = 1200
HEIGHT = 800


f = open("filer", "a")

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = skull_img
        self.image = skull_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.centerx = self.rect.center[0]
        self.centery = self.rect.center[1]
        self.last_update = pygame.time.get_ticks()
        
    def rotate(self):
         now = pygame.time.get_ticks()
         if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        self.centerx = self.rect.center[0]
        self.centery = self.rect.center[1]
        
    def tichka(self,x,y):
        if ( (self.centerx - x) ** 2 + (self.centery - y) ** 2 ) ** (0.5) <= self.radius:
            return True
        else:
            return False
    
    def remake(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = skull_img
        self.image = skull_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.centerx = self.rect.center[0]
        self.centery = self.rect.center[1]
        self.last_update = pygame.time.get_ticks()
    

class Shar(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.square = random.randint(30,100)
       self.image = pygame.Surface((self.square,self.square))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()
       self.radius = int(self.rect.width / 2)
       self.color = COLORS[random.randint(0, 5)]
       self.rect.x = random.randrange(WIDTH - self.rect.width)
       self.rect.y = random.randrange(HEIGHT - self.rect.height)
       self.speedy = random.randrange(-5, 5)
       self.speedx = random.randrange(-5, 5)
       self.centerx = self.rect.center[0]
       self.centery = self.rect.center[1]
       circle(self.image, self.color, (self.radius, self.radius), self.radius)
       
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speedy *= -1
        self.centerx = self.rect.center[0]
        self.centery = self.rect.center[1]
            
    def tichka(self, x, y):
        if ( (self.centerx - x) ** 2 + (self.centery - y) ** 2 ) ** (0.5) <= self.radius:
            return True
        else:
            return False
    def remake(self):
       pygame.sprite.Sprite.__init__(self)
       self.square = random.randint(30,100)
       self.image = pygame.Surface((self.square,self.square))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()
       self.radius = int(self.rect.width / 2)
       self.color = COLORS[random.randint(0, 5)]
       self.rect.x = random.randrange(WIDTH - self.rect.width)
       self.rect.y = random.randrange(HEIGHT - self.rect.height)
       self.speedy = random.randrange(-5, 5)
       self.speedx = random.randrange(-5, 5)
       self.centerx = int(self.square * 0.5)
       self.centery = int(self.square * 0.5)
       circle(self.image, self.color, (self.centerx, self.centery), self.radius)
       
       

skull_img = pygame.image.load(path.join(img_dir, "skull.png")).convert()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
shars = pygame.sprite.Group()
for i in range (10):
    s = Shar()
    all_sprites.add(s)
    shars.add(s)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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


screen.fill(BLACK)
draw_text(screen, "ENTER YOUR NAME", 120, 600,300)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


name = input()

          
while not finished:
        
    clock.tick(FPS)   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos[0],event.pos[1]
            for shar in shars:
                if shar.tichka(x,y):
                    k += 1
                    shar.remake()
            for scull in mobs:
                if scull.tichka(x,y):
                    k += 3
                    scull.remake()
      
    
    
    
    
    screen.fill(BLACK)
    draw_text(screen, str(k), 80, 600, 10)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    
   
    draw_text(screen, str(k), 80, 600,5)
f.write(name + ' ' + str(k) + '\n')
    

pygame.quit()
f.close()
# sorting massiv to find leaders
f = open("filer", 'r')
A = []
x = f.readline()
while x:
    name,k = x.split()
    k = int(k)
    A.append((name,k))
    x = f.readline()
f.close()
A.sort(key = lambda x: -x[1])
f = open('filer', 'w')
for i in A:
    print (*i, file = f)
f.close()
    



