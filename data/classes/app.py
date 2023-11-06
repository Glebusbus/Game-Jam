import pygame as pg
import numpy as np
from pygame.locals import *
from data.classes.render import VoxelRender
from data.classes.player import Player
import tkinter


class MainLoop:
    def __init__(self):
        pg.init()





        self.SC = pg.display.set_mode((0, 0), pg.FULLSCREEN)

        self.WIDHT, self.HEIGHT = self.SC.get_size()
        self.CLOCK = pg.time.Clock()
        self.camera = Player(self.WIDHT, self.HEIGHT)
        self.RENDER = VoxelRender(self)


    def update(self):
        self.camera.update()
        self.RENDER.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.flag = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.flag = False


    def draw(self):
        self.RENDER.draw()
        pg.display.flip()

    def run(self):
        self.flag = True
        while self.flag:
            self.update()
            self.draw()
            self.CLOCK.tick(60.0)


