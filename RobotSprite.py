import pygame as pg


class Robot(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('./robot.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
