from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'
import pygame as pg
from network import Network
from constants import *
from dotClass import *
from utiles import *

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.Clock()
network = Network(INFO, ACTIVATOR, NORMALIZER, FACTOR_RANGE, BIAS_RANGE)

while True:
    #events handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                dots.clear()
                network.flush()
            elif event.key == pg.K_z:
                if dots != []:
                    dots.pop(-1)
                else:
                    network.flush()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if pg.mouse.get_pressed()[0]:
                Dot(screen, mouse_x, mouse_y, RADIUS, COLORS[0], BORDER_WIDTH, BORDER_COLOR)
            elif pg.mouse.get_pressed()[1]:
                Dot(screen, mouse_x, mouse_y, RADIUS, COLORS[1], BORDER_WIDTH, BORDER_COLOR)
            elif pg.mouse.get_pressed()[2]:
                Dot(screen, mouse_x, mouse_y, RADIUS, COLORS[2], BORDER_WIDTH, BORDER_COLOR)
        elif event.type == pg.MOUSEWHEEL:
            pass

    #game processes
    if dots != []:
        dataset, answerset = generate_data(dots, WIDTH, HEIGHT)
        network.train_vanilla(dataset, answerset, ALPHA, CYCLES, False)

    #rendering
    screen.fill((0, 0, 0))
    for x in range(0, WIDTH, COLOR_STEP):
        for y in range(0, HEIGHT, COLOR_STEP):
            pg.draw.rect(screen, 255*network.process([x/WIDTH, y/HEIGHT]), pg.Rect(x, y, COLOR_STEP, COLOR_STEP))
    for dot in dots:
        dot.draw()

    pg.display.flip()
    clock.tick(60)