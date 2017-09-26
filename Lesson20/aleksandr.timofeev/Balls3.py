#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Игра Шарики 2017
import tkinter # подключение графической биюлиотеки
import random # подключение биюлиотеки генератора случайных чисел

# Заведение констант
WIDTH = 700 # размер окна по горизонтали
HEIGHT = 600 # размер окна по вертикали
BG_COLOR = 'white'
MAIN_BALL_COLOR = 'blue' # цвет основного шара
MAIN_BALL_RADIUS = 23 # радиус основного шара
BAD_COLOR = 'red' # цвет опасных шаров
COLORS = ['aqua', 'fuchsia', BAD_COLOR, 'pink', 'yellow', BAD_COLOR, 'gold', 'chartreuse', BAD_COLOR]
NUM_OF_BALLS = 9
MAX_RADIUS = 35
MIN_RADIUS = 15
DELAY = 8 #  скорость шарика
INIT_DX = 1
INIT_DY = 1
ZERO = 0

# Параметры шириков
# Класс шарика (задание координат, радиуса, цвета, и смещения по осям)
class Ball():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self): #  метод рисования шарика
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color,
                           outline=self.color if self.color != BAD_COLOR else 'black') # стирание окружности вокруг шарика

    def hide(self): # метод стирания шарика
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR,
                           outline=BG_COLOR) # стирание окружности вокруг шарика

    def is_collision(self, ball): # проверка столкновения шаров
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a * a + b * b) ** 0.5 <= self.r + ball.r

    def move(self): # метод движения шарика
        # метод отскакивания шарика от стен
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy = -self.dy
        # изменения после столкновения шаров
        for ball in balls:
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:  # not a bad ball
                    ball.hide()
                    balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:  # bad ball
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        if self.dx * self.dy != 0:
            self.draw()


# Процесс кликанья мыщью
def mouse_click(event):
    global main_ball
    if event.num == 1:  # Левая кнопка мыши
        if 'main_ball' not in globals():  # старт
            main_ball = Ball(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY)
            if main_ball.x > WIDTH / 2:
                main_ball.dx = -main_ball.dx
            if main_ball.y > HEIGHT / 2:
                main_ball.dy = -main_ball.dy
            main_ball.draw()
        else: # поворот на лево
            if main_ball.dy * main_ball.dx > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3:  # поворот на право
        if main_ball.dy * main_ball.dx > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy


# создание россыпи шариков
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Ball(random.choice(range(MAX_RADIUS, WIDTH - MAX_RADIUS)),
                         random.choice(range(MAX_RADIUS, HEIGHT - MAX_RADIUS)),
                         random.choice(range(MIN_RADIUS, MAX_RADIUS)),
                         random.choice(COLORS))
        is_collision = False
        for ball in lst:
            if next_ball.is_collision(ball):
                is_collision = True
                break
        if not is_collision:
            lst.append(next_ball)
            next_ball.draw()
    return lst


# подсчет плохих (красных) шаров
def count_bad_balls(list_of_balls):
    result = 0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            result += 1
    return result


# Вывод результата игры
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Вы выиграли!", font="Arial 20", fill="lime")
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx * main_ball.dy == 0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Вы проиграли!", font="Arial 20", fill="red")
    root.after(DELAY, main)

# Заведение и настройка параметров окна
root = tkinter.Tk() # Основное (корневое) окно
root.title("Шарики мишарики") # Наименование окна
# Выключаем возможность изменять окно
root.resizable (width=False, height=False)
# размер и цвет окна
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack() # Вывод окна на экран

# Назначение кнопок мыши
canvas.bind('<Button-1>', mouse_click) # левая кнопка мыши
canvas.bind('<Button-3>', mouse_click, '+') # правая кнопка мыши
balls = create_list_of_balls(NUM_OF_BALLS) # вызов на экран россыпи шаров
num_of_bad_balls = count_bad_balls(balls)
if 'main_ball' in globals():  
    del main_ball
main()
root.mainloop() # отображение окна