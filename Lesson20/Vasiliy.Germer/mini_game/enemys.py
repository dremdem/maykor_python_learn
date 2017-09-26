#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os

MOVE_SPEED = 3
WIDTH = 40
HEIGHT = 40
COLOR = "#888888"
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


ANIMATION_STAY = [('%s/images/tank/er.png' % ICON_DIR, 0.1)]
ANIMATION_LEFT = [('%s/images/tank/el.png' % ICON_DIR, 0.1)]
ANIMATION_RIGHT = [('%s/images/tank/er.png' % ICON_DIR, 0.1)]
ANIMATION_UP = [('%s/images/tank/eu.png' % ICON_DIR, 0.1)]
ANIMATION_DOWN = [('%s/images/tank/ed.png' % ICON_DIR, 0.1)]


class Enemy (sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.RIGHT = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным

        #        Анимация движения вправо
        self.boltAnimRight = pyganim.PygAnimation(ANIMATION_RIGHT)
        self.boltAnimRight.play()
        #        Анимация движения влево
        self.boltAnimLeft = pyganim.PygAnimation(ANIMATION_LEFT)
        self.boltAnimLeft.play()
        #        Анимация движения вверх
        self.boltAnimUp = pyganim.PygAnimation(ANIMATION_UP)
        self.boltAnimUp.play()
        #        Анимация движения вниз
        self.boltAnimDown = pyganim.PygAnimation(ANIMATION_DOWN)
        self.boltAnimDown.play()

    def update(self, WIN_WIDTH,WIN_HEIGHT,down, platforms):
        self.collide(self.rect.right, 0, platforms)
        #self.collide(self.rect.left, 0, platforms)
        if self.RIGHT == True:  # если в правом углу
            self.rect.x -= 1 #двигаемся в лево
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
            if self.rect.x < 0:  # если уперлись в лево
                self.RIGHT = False  # двигаемся в право
        else:
            self.rect.x += 1
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))
            if self.rect.x > 300:
                self.RIGHT = True



    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение c платформой
                print (xvel)
                if xvel > 0:
                    if self.RIGHT == True:
                        self.RIGHT = False            # то не движется вправо
                    else:
                        self.RIGHT = True

    def Intersect(x1, x2, y1, y2, db1, db2):
        if (
                        ((x1 + HEIGHT - 10 > x2) and x1 < x2) and
                        ((y1 + WIDTH - 10 > y2) and y1 < y2) or
                        ((x1 < x2 + HEIGHT - 10) and x2 < x1) and
                        ((y1 < y2 + WIDTH - 10) and y2 < y1)
        ):
            return 1
        else:
            return 0