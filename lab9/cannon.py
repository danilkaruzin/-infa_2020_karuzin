import numpy as np
import pygame as pg
from random import randint, gauss

pg.init()
pg.font.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)

SCREEN_SIZE = (800, 600)


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class GameObject:
    pass


class Shell(GameObject):
    '''
    The ball class. Creates a ball, controls it's movement and implement it's rendering.
    '''
    def __init__(self, coord, vel, rad=20, color=None):
        '''
        Constructor method. Initializes ball's parameters and initial values.
        '''
        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True

    def check_corners(self, refl_ort=0.8, refl_par=0.9):
        '''
        Reflects ball's velocity when ball bumps into the screen corners. Implemetns inelastic rebounce.
        '''
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)

    def move(self, time=1, grav=0):
        '''
        Moves the ball according to it's velocity and time step.
        Changes the ball's velocity due to gravitational force.
        '''
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False

    def draw(self, screen):
        '''
        Draws the ball on appropriate surface.
        '''
        pg.draw.circle(screen, self.color, self.coord, self.rad)


class Cannon(GameObject):
    '''
    Cannon class. Manages it's renderring, movement and striking.
    '''
    def __init__(self, coord=[30, 450], angle=0, max_pow=50, min_pow=10, color=BLUE):
        '''
        Constructor method. Sets coordinate, direction, minimum and maximum power and color of the gun.
        '''
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow
        self.speedx = 0
        self.speedy = 0

    def activate(self):
        '''
        Activates gun's charge.
        '''
        self.active = True

    def vel_prop(self, inc1, inc2):
        self.speedx = inc1
        self.speedy = inc2

    def gain(self, inc=2):
        '''
        Increases current gun charge power.
        '''
        if self.active:
            if self.pow < self.max_pow:
                self.pow += inc
            self.color = CYAN
        else:
            self.color = BLUE

    def strike(self):
        '''
        Creates ball, according to gun's direction and current charge power.
        '''
        vel = self.pow
        angle = self.angle
        ball = Shell(list(self.coord), [int(vel * np.cos(angle)), int(vel * np.sin(angle))])
        self.color = BLUE
        self.pow = self.min_pow
        self.active = False
        return ball
        
    def set_angle(self, target_pos):
        '''
        Sets gun's direction to target position.
        '''
        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])

    def move(self):
        '''
        Changes position of the gun.
        '''
        self.coord[0] += self.speedx
        self.coord[1] += self.speedy
        
        

                    


    def draw(self, screen):
        '''
        Draws the gun on the screen.
        '''
        gun_shape = []
        vec_1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.pow*np.cos(self.angle)), int(self.pow*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)


class Target(GameObject):
    '''
    Target class. Creates target, manages it's rendering and collision with a ball event.
    '''
    def __init__(self, coord=None, color=None, rad=30):
        '''
        Constructor method. Sets coordinate, color and radius of the target.
        '''
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad

        if color == None:
            color = rand_color()
        self.color = color

    def check_collision(self, ball):
        '''
        Checks whether the ball bumps into target.
        '''
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist

    def draw(self, screen):
        '''
        Draws the target on the screen
        '''
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self):
        """
        This type of target can't move at all.
        :return: None
        """
        pass


class MovingTarget(Target):
    def __init__(self, coord=None, color=None, rad=30):
        super().__init__(coord, color, rad)
        self.vx = randint(-4, +4)
        self.vy = randint(-2, +2)
        

    def move(self):
        self.coord[0] += self.vx
        self.coord[1] += self.vy
        if self.coord[0] < self.rad or self.coord[0] > SCREEN_SIZE[0] - self.rad:
            self.vx *= -1          
        if self.coord[1] < self.rad or self.coord[1] > SCREEN_SIZE[1] - self.rad:
            self.vy *= -1

class Target2(GameObject):
    def __init__(self,coord =None, color = None, l = 20):
        if coord == None:
            coord = [randint(20, SCREEN_SIZE[0] - l), randint(20, SCREEN_SIZE[1] - l)]
        self.coord = coord
        if color == None:
            color = rand_color()
        self.color = color
        self.l = l

    def check_collision(self, ball):
        if self.coord[0] + self.l > ball.coord[0] - ball.rad and \
           self.coord[0] < ball.coord[0] + ball.rad and \
           self.coord[1] + self.l > ball.coord[1] - ball.rad and \
           self.coord[1] < ball.coord[1] + ball.rad:
            return True

    def draw(self, screen):
        pg.draw.rect(screen,self.color, (self.coord[0],self.coord[1],self.l,self.l))

    def move (self):
        pass

class MovingTarget2(Target2):
    def __init__(self, coord=None, color=None, l=20):
        super().__init__(coord, color, l)
        self.vx = randint(-4, +4)
        self.vy = randint(-2, +2)
        self.vel = [self.vx,self.vy]

    def move(self):
        self.vel[1] += -2
        for i in range(2):
            if self.coord[i] < 0:
                self.coord[i] = 0
                self.vel[i] = -int(self.vel[i] * 1)
                self.vel[1-i] = int(self.vel[1-i] * 1)
            elif self.coord[i] + self.l > SCREEN_SIZE[i] :
                self.coord[i] = SCREEN_SIZE[i] - self.l
                self.vel[i] = -int(self.vel[i] * 1)
                self.vel[1-i] = int(self.vel[1-i] * 1)
            self.coord[i] += self.vel[i]
        

        
        
    


class ScoreTable:
    '''
    Score table class.
    '''
    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("dejavusansmono", 25)

    def score(self):
        '''
        Score calculation method.
        '''
        return self.t_destr - self.b_used

    def draw(self, screen):
        score_surf = []
        score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr), True, BLACK))
        score_surf.append(self.font.render("Balls used: {}".format(self.b_used), True, BLACK))
        score_surf.append(self.font.render("Total: {}".format(self.score()), True, RED))
        for i in range(3):
            screen.blit(score_surf[i], [10, 10 + 30*i])


class Manager:
    '''
    Class that manages events' handling, ball's motion and collision, target creation, etc.
    '''
    def __init__(self, n_targets=1):
        self.balls = []
        self.gun = Cannon()
        self.targets = []
        self.score_t = ScoreTable()
        self.n_targets = n_targets
        self.new_mission()

    def new_mission(self):
        '''
        Adds new targets.
        '''
        for i in range(self.n_targets):
            self.targets.append(Target(rad=randint(10,50)))
        for i in range(self.n_targets):
                                
            self.targets.append(MovingTarget(rad=randint(10,50)))
        for i in range (self.n_targets):
            self.targets.append(Target2(l = randint(20, 50)))
        for i in range (self.n_targets):
            self.targets.append(MovingTarget2(l = randint(20, 50)))

    def process(self, events, screen):
        '''
        Runs all necessary method for each iteration. Adds new targets, if previous are destroyed.
        '''
        done = self.handle_events(events)

        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        
        self.move()
        self.collide()
        self.draw(screen)

        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()

        return done

    def handle_events(self, events):
        '''
        Handles events from keyboard, mouse, etc.
        '''
        done = False
        self.gun.vel_prop(0,0)
        keystate = pg.key.get_pressed()
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif keystate[pg.K_UP]:
                self.gun.vel_prop(0,-5)
            elif keystate[pg.K_DOWN]:
                self.gun.vel_prop(0,5)
            elif keystate[pg.K_RIGHT]:
                self.gun.vel_prop(5,0)
            elif keystate[pg.K_LEFT]:
                self.gun.vel_prop(-5,0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.activate()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
                    self.score_t.b_used += 1
        return done

    def draw(self, screen):
        '''
        Runs balls', gun's, targets' and score table's drawing method.
        '''
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)
        self.gun.draw(screen)
        self.score_t.draw(screen)

    def move(self):
        '''
        Runs balls' and gun's movement method, removes dead balls.
        '''
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move(grav=2)
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        for i, target in enumerate(self.targets):
            target.move()
        self.gun.gain()
        self.gun.move()

    def collide(self):
        '''
        Checks whether balls bump into targets, sets balls' alive trigger.
        '''
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for j in reversed(targets_c):
            self.score_t.t_destr += 1
            self.targets.pop(j)


screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

done = False
clock = pg.time.Clock()

mgr = Manager(n_targets=3)

while not done:
    clock.tick(15)
    screen.fill(WHITE)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()
