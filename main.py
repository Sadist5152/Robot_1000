import pygame as pg
import colors

from InputBox import InputBox
from RobotSprite import Robot

HEIGHT = 600
WIDTH = 1080

FPS = 60

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
NAME_APP = 'Robocop_T1000'
CLOCK = pg.time.Clock()
RUNNING = True

SPEED = 1
ROBOT = Robot(WIDTH//3.7, HEIGHT//2.8)


def unity(box_with_colors):
    global RUNNING
    CLOCK.tick(FPS)

    while RUNNING:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUNNING = False

        for box in box_with_colors:
            box.update()

        for box in box_with_colors:
            box.draw(SCREEN)

        pg.display.update()


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption(NAME_APP)

    SCREEN.fill(colors.WHITE)
    react_width = WIDTH/17
    react_height = HEIGHT/5

    pg.draw.line(SCREEN, colors.BLACK, [WIDTH/HEIGHT*220, HEIGHT/WIDTH*280], [WIDTH/HEIGHT*400, HEIGHT/WIDTH*280], 3)
    pg.draw.line(SCREEN, colors.BLACK, [WIDTH/HEIGHT*170, HEIGHT/WIDTH*HEIGHT/1.1], [WIDTH/HEIGHT*450, HEIGHT/WIDTH*HEIGHT/1.1], 3)
    pg.draw.line(SCREEN, colors.BLACK, [WIDTH/HEIGHT*220, HEIGHT/WIDTH*280], [WIDTH/HEIGHT*220, HEIGHT/WIDTH*HEIGHT/1.1], 3)
    pg.draw.line(SCREEN, colors.BLACK, [WIDTH/HEIGHT*400, HEIGHT/WIDTH*280], [WIDTH/HEIGHT*400, HEIGHT/WIDTH*HEIGHT/1.1], 3)
    pg.draw.line(SCREEN, colors.BLACK, [WIDTH/HEIGHT*400/1.45, HEIGHT/WIDTH*280], [WIDTH/HEIGHT*400/1.45, HEIGHT/WIDTH*HEIGHT/1.1], 3)
    pg.draw.line(SCREEN, colors.BLACK, [WIDTH/HEIGHT*400/1.18, HEIGHT/WIDTH*280], [WIDTH/HEIGHT*400/1.18, HEIGHT/WIDTH*HEIGHT/1.1], 3)

    pg.draw.rect(SCREEN, colors.RED, pg.Rect(WIDTH / HEIGHT * 200, HEIGHT / WIDTH * 300, react_width, react_height))
    pg.draw.rect(SCREEN, colors.BLUE, pg.Rect(WIDTH / HEIGHT * 260, HEIGHT / WIDTH * 300, react_width, react_height))
    pg.draw.rect(SCREEN, colors.YELLOW, pg.Rect(WIDTH / HEIGHT * 320, HEIGHT / WIDTH * 300, react_width, react_height))
    pg.draw.rect(SCREEN, colors.GREEN, pg.Rect(WIDTH / HEIGHT * 380, HEIGHT / WIDTH * 300, react_width, react_height))
    pg.draw.rect(SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 200, HEIGHT / WIDTH * 300, react_width, react_height), 2)
    pg.draw.rect(SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 260, HEIGHT / WIDTH * 300, react_width, react_height),2)
    pg.draw.rect(SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 320, HEIGHT / WIDTH * 300, react_width, react_height),2)
    pg.draw.rect(SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 380, HEIGHT / WIDTH * 300, react_width, react_height), 2)

    pg.draw.rect(SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 440, HEIGHT / WIDTH * 520, react_width/2, react_width/2))

    input_box_color1 = InputBox(WIDTH / HEIGHT * 150, HEIGHT / WIDTH * 690, react_width, react_height/2)
    input_box_color2 = InputBox(WIDTH / HEIGHT * 280, HEIGHT / WIDTH * 690, react_width, react_height/2)
    pg.draw.rect(SCREEN, colors.GREEN, pg.Rect(WIDTH / HEIGHT * 400, HEIGHT / WIDTH * 689, react_width, react_width))
    input_boxes = [input_box_color1, input_box_color2]

    SCREEN.blit(ROBOT.image, ROBOT.heat_box)

    unity(input_boxes)
    pg.quit()


