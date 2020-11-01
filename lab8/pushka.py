from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

balls = []
targets = []
g = -0.3
prop = 0.5


class ball(object):
    def __init__(self, v_0x, v_0y, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = v_0x
        self.vy = v_0y
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live_time = 30
        self.stopped = False

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if not self.stopped:
            self.vy -= g

        self.x += self.vx
        self.y += self.vy

        if self.y+self.r*2 >= 600:
            self.vx = int(self.vx/1.3)
            self.vy = -int(self.vy/1.3)
        if self.y-self.r <= 0:
            self.vy = -self.vy
        if self.x-self.r <= 0 or self.x+self.r >= 800:
            self.vx = -self.vx

        if self.vx == 0 and self.vy == 0:
            self.stopped = True
        if self.stopped:
            self.live_time -= 1
        if self.live_time <= 0:
            canv.delete(self.id)
            balls.remove(self)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:

            return True
        else:
            return False


class Gun(object):
    def __init__(self):
        self.x = 20
        self.y = 450

        self.bullet_counter = 0
        self.f_power = 10
        self.f_on = False
        self.an = 0
        self.length = 50

        self.id = canv.create_line(0, 0, self.length, 0, width=7)

    def fire_start(self, event):
        self.f_on = True

    def fire_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.bullet_counter += 1


        self.an = math.atan((event.y - self.y) / (event.x - self.x))
        new_ball = ball(self.f_power * math.cos(self.an)*prop,
                              self.f_power * math.sin(self.an)*prop)
        #new_ball.vx = self.f_power * math.cos(self.an)
        #new_ball.vy = -self.f_power * math.sin(self.an)
        self.f_on = False
        self.f_power = 10

        balls.append(new_ball)

    def targeting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-self.y) / (event.x-self.x))

    def draw(self):
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f_power, 20) * math.cos(self.an),
                    self.y + max(self.f_power, 20) * math.sin(self.an)
                    )

        if self.f_on:
            if self.f_power <= 100:
                self.f_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target(object):
    def __init__(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.vx = rnd(-8,8)
        self.vy = rnd(-8,8)

        self.color = 'red'
        self.id = canv.create_oval(0, 0, 0, 0)
        canv.itemconfig(self.id, fill=self.color)

        self.points = 0
        self.alive = True

    def draw(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def hit(self):
        """Hiding the target"""
        self.x = -100
        self.y = -100
        self.alive = False
        targets.remove(self)
    def move(self):

        self.x += self.vx
        self.y += self.vy
        if self.x + self.r > 800 or self.x - self.r < 0:
            self.vx *= -1
        if self.y + self.r < 0 or self.y + self.r > 600:
            self.vy *= -1
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)



screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
screen2 = canv.create_text(20,30, text ='', font = '28')



def new_game(counter):
    for i in range(2):
        targets.append(Target())
        targets[-1].draw()
        targets[-1].move()
        

    canv.bind('<Button-1>', g1.fire_start)
    canv.bind('<ButtonRelease-1>', g1.fire_end)
    canv.bind('<Motion>', g1.targeting)

    while targets or balls:
        g1.draw()
        for t in targets:
            if t.alive:
                t.move()
        for b in balls:
            b.set_coords()
            for t in targets:
                if b.hittest(t) and t.alive:
                    t.hit()
                    t.draw()
                    counter += 1
                    canv.itemconfig(screen2, text = str(counter)) 
                    
                    if not targets:
                        canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(g1.bullet_counter) + ' выстрелов')
                        canv.bind('<Button-1>', '')
                        canv.bind('<ButtonRelease-1>', '')


            b.move()

        canv.update()
        time.sleep(0.03)

    time.sleep(1)
    canv.itemconfig(screen1, text='')


counter = -1 +1
while True:
    new_game(counter)
    g1.bullet_counter = 0
