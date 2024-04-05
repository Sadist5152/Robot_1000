import pygame as pg
import sys

import colors

from RobotSprite import Robot

HEIGHT = 600
WIDTH = 1080

FPS = 60

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
NAME_APP = 'Robocop_T1000'
CLOCK = pg.time.Clock()
RUNNING = True

SPEED = 1
ROBOT = Robot(WIDTH // 3.7, HEIGHT // 2.8)

react_width = WIDTH / 17
react_height = HEIGHT / 5
RECT_RED = pg.Rect(WIDTH / HEIGHT * 200, HEIGHT / WIDTH * 300, react_width, react_height)
RECT_BLUE = pg.Rect(WIDTH / HEIGHT * 260, HEIGHT / WIDTH * 300, react_width, react_height)
RECT_YELLOW = pg.Rect(WIDTH / HEIGHT * 320, HEIGHT / WIDTH * 300, react_width, react_height)
RECT_GREEN = pg.Rect(WIDTH / HEIGHT * 380, HEIGHT / WIDTH * 300, react_width, react_height)
COLOR_DRAW1 = colors.WHITE
COLOR_DRAW2 = colors.WHITE


def backend():
    SCREEN.fill(colors.WHITE)
    pg.draw.line(
        SCREEN, colors.BLACK, [WIDTH / HEIGHT * 220, HEIGHT / WIDTH * 280],
        [WIDTH / HEIGHT * 400, HEIGHT / WIDTH * 280], 3)
    pg.draw.line(
        SCREEN, colors.BLACK, [WIDTH / HEIGHT * 160, HEIGHT / WIDTH * HEIGHT / 1.1],
        [WIDTH / HEIGHT * 460, HEIGHT / WIDTH * HEIGHT / 1.1], 3)
    pg.draw.line(
        SCREEN, colors.BLACK, [WIDTH / HEIGHT * 220, HEIGHT / WIDTH * 280],
        [WIDTH / HEIGHT * 220, HEIGHT / WIDTH * HEIGHT / 1.1], 3)
    pg.draw.line(
        SCREEN, colors.BLACK, [WIDTH / HEIGHT * 400, HEIGHT / WIDTH * 280],
        [WIDTH / HEIGHT * 400, HEIGHT / WIDTH * HEIGHT / 1.1], 3)
    pg.draw.line(
        SCREEN, colors.BLACK, [WIDTH / HEIGHT * 400 / 1.45, HEIGHT / WIDTH * 280],
        [WIDTH / HEIGHT * 400 / 1.45, HEIGHT / WIDTH * HEIGHT / 1.1], 3)
    pg.draw.line(
        SCREEN, colors.BLACK, [WIDTH / HEIGHT * 400 / 1.18, HEIGHT / WIDTH * 280],
        [WIDTH / HEIGHT * 400 / 1.18, HEIGHT / WIDTH * HEIGHT / 1.1], 3)

    pg.draw.rect(
        SCREEN, colors.RED, RECT_RED)  # Красный
    pg.draw.rect(
        SCREEN, colors.BLUE, RECT_BLUE)  # Синий
    pg.draw.rect(
        SCREEN, colors.YELLOW, RECT_YELLOW)  # Желтый
    pg.draw.rect(
        SCREEN, colors.GREEN, RECT_GREEN)  # Зеленый
    pg.draw.rect(
        SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 200, HEIGHT / WIDTH * 300, react_width, react_height), 2)
    pg.draw.rect(
        SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 260, HEIGHT / WIDTH * 300, react_width, react_height), 2)
    pg.draw.rect(
        SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 320, HEIGHT / WIDTH * 300, react_width, react_height), 2)
    pg.draw.rect(
        SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 380, HEIGHT / WIDTH * 300, react_width, react_height), 2)

    pg.draw.rect(SCREEN, colors.BLACK,
                 pg.Rect(WIDTH / HEIGHT * 460, HEIGHT / WIDTH * 520, react_width / 2, react_width / 2))
    SCREEN.blit(ROBOT.image, ROBOT.rect)

    pg.draw.rect(SCREEN, COLOR_DRAW1,
                 pg.Rect(WIDTH / HEIGHT * 190, HEIGHT / WIDTH * 690, react_width * 3, react_height / 2))
    pg.draw.rect(SCREEN, COLOR_DRAW2,
                 pg.Rect(WIDTH / HEIGHT * 320, HEIGHT / WIDTH * 690, react_width * 3, react_height / 2))
    pg.draw.rect(
        SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 190, HEIGHT / WIDTH * 690, react_width * 3, react_height / 2), 2)
    pg.draw.rect(
        SCREEN, colors.BLACK, pg.Rect(WIDTH / HEIGHT * 320, HEIGHT / WIDTH * 690, react_width * 3, react_height / 2), 2)
    pg.display.update()


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption(NAME_APP)

    way = (WIDTH / HEIGHT * 460 - WIDTH / HEIGHT * 160) / 5

    color1 = None
    color2 = None
    result = 0

    running = True
    while running:
        backend()
        # Обработка событий
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if event.button == 1:  # Левая кнопка мыши
                    if RECT_RED.collidepoint(x, y):
                        color1 = "R"
                        COLOR_DRAW1 = colors.RED
                    elif RECT_BLUE.collidepoint(x, y):
                        color1 = "B"
                        COLOR_DRAW1 = colors.BLUE
                    elif RECT_YELLOW.collidepoint(x, y):
                        color1 = "Y"
                        COLOR_DRAW1 = colors.YELLOW
                    elif RECT_GREEN.collidepoint(x, y):
                        color1 = "G"
                        COLOR_DRAW1 = colors.GREEN
                elif event.button == 3:  # Правая кнопка мыши
                    if RECT_RED.collidepoint(x, y):
                        color2 = "R"
                        COLOR_DRAW2 = colors.RED
                    elif RECT_BLUE.collidepoint(x, y):
                        color2 = "B"
                        COLOR_DRAW2 = colors.BLUE
                    elif RECT_YELLOW.collidepoint(x, y):
                        color2 = "Y"
                        COLOR_DRAW2 = colors.YELLOW
                    elif RECT_GREEN.collidepoint(x, y):
                        color2 = "G"
                        COLOR_DRAW2 = colors.GREEN

        if (color1 is not None) and (color2 is not None):
            col_map = {"R": 1, "B": 2, "Y": 3, "G": 4}
            x = 0
            run_away = way * col_map[color1]
            result += 1 * col_map[color1]
            while x < run_away:
                ROBOT.move(SPEED, 0)
                x += SPEED
                backend()

            run_away = (HEIGHT / WIDTH * HEIGHT / 1.1) - (HEIGHT / WIDTH * 280)
            result += 1
            x = 0
            while x < run_away:
                ROBOT.move(0, -SPEED)
                x += SPEED
                backend()

            x = 0
            run_away = abs(col_map[color1] - col_map[color2]) * way
            result += abs(col_map[color1] - col_map[color2]) * 1
            if col_map[color1] < col_map[color2]:
                while x < run_away:
                    ROBOT.move(SPEED, 0)
                    x += SPEED
                    backend()
            else:
                while x < run_away:
                    ROBOT.move(-SPEED, 0)
                    x += SPEED
                    backend()

            run_away = (HEIGHT / WIDTH * HEIGHT / 1.1) - (HEIGHT / WIDTH * 280)
            result += 1
            x = 0
            while x < run_away:
                ROBOT.move(0, SPEED)
                x += SPEED
                backend()

            run_away = way * (5 - col_map[color2])
            result += 1 * (5 - col_map[color2])
            x = 0
            while x < run_away:
                ROBOT.move(SPEED, 0)
                x += SPEED
                backend()

            result = "Робот прошел " + str(result) + " отрезов"
            font = pg.font.Font(None, 36)
            text_surface = font.render(result, True, colors.BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 1.2)
            SCREEN.blit(text_surface, text_rect)
            pg.display.flip()
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()

pg.quit()
