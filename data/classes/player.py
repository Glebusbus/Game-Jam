import numpy as np
import pygame as pg
import math


class Player:
    def __init__(self, WIDHT, HEIGHT):
        self.WIDHT = WIDHT
        self.HEIGHT = HEIGHT
        pg.mouse.set_pos((200, 200))
        pg.mouse.set_visible(False)
        self.dmx, self.dmy = 200, 200
        self.pos = np.array([0, 0], dtype=float)
        self.angle = math.pi / 4
        self.height = 270
        self.pitch = 40
        self.angle_vel = 0.01
        self.vel = 15

    def update(self):
        dmx, dmy = pg.mouse.get_pos()
        dmx -= self.dmx
        dmy -= self.dmy
        self.dmx, self.dmy = pg.mouse.get_pos()
        if self.dmx <= 10:
            pg.mouse.set_pos((200, 200))
            self.dmx = 200
            self.dmy = 200
        elif self.dmx >= self.WIDHT-10:
            pg.mouse.set_pos((200, 200))
            self.dmx = 200
            self.dmy = 200
        if self.dmy <= 10:
            pg.mouse.set_pos((200, 200))
            self.dmx = 200
            self.dmy = 200
        elif self.dmy >= self.HEIGHT-10:
            pg.mouse.set_pos((200, 200))
            self.dmx = 200
            self.dmy = 200

        self.angle += dmx / 400
        self.pitch -= dmy * 2
        self.pitch = min(max(self.pitch, -1000), 500)
        pressed_key = pg.key.get_pressed()

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        if pressed_key[pg.K_q]:
            self.height += self.vel
        if pressed_key[pg.K_e]:
            self.height -= self.vel

        if pressed_key[pg.K_w]:
            self.pos[0] += self.vel * cos_a
            self.pos[1] += self.vel * sin_a
        if pressed_key[pg.K_s]:
            self.pos[0] -= self.vel * cos_a
            self.pos[1] -= self.vel * sin_a
        if pressed_key[pg.K_a]:
            self.pos[0] += self.vel * sin_a
            self.pos[1] -= self.vel * cos_a
        if pressed_key[pg.K_d]:
            self.pos[0] -= self.vel * sin_a
            self.pos[1] += self.vel * cos_a
