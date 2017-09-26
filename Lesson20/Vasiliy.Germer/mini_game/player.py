#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os

MOVE_SPEED = 3
WIDTH = 40
HEIGHT = 40
COLOR =  "#888888"
ANIMATION_DELAY = 0.1 # скорость смены кадров
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами

ANIMATION_STAY =  [('%s/images/tank/tr.png' % ICON_DIR, 0.1)]
ANIMATION_LEFT =  [('%s/images/tank/tl.png' % ICON_DIR, 0.1)]
ANIMATION_RIGHT = [('%s/images/tank/tr.png' % ICON_DIR, 0.1)]
ANIMATION_UP =    [('%s/images/tank/tu.png' % ICON_DIR, 0.1)]
ANIMATION_DOWN =  [('%s/images/tank/td.png' % ICON_DIR, 0.1)]

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х
        self.startY = y
        self.yvel = 0 # скорость вертикального перемещения
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным

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

    def update(self, left, right, up, down, platforms):
        
        if up:
            self.yvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))
            self.rect.y += self.yvel

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
            self.rect.x += self.xvel
 
        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))
            self.rect.x += self.xvel

        if down:
            self.yvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.boltAnimDown.blit(self.image, (0, 0))
            self.rect.y += self.yvel

        self.collide(0, self.yvel, platforms)


        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не движется вниз

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0

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