import pygame as pg

class Robot(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('./robot.png').convert_alpha()
        self.heat_box = self.image.get_rect(center=(x, y))