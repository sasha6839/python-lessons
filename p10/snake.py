import pygame as pg
import random
import time
import sys

pg.init()
#colors
white = (255,255,255)
yellow = (255,255,100)
balck = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (30,56,186)

#screen
scr_x = 600
scr_y = 600
screen = pg.display.set_mode((scr_x,scr_y))
pg.display.set_caption('Snake Game by Sasha')

clock = pg.time.Clock()

def gameLoop():
    game_over = False
    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                pass
            if event.key == pg.K_RIGHT:
                pass
            if event.key == pg.K_UP:
                pass
            if event.key == pg.K_DOWN:
                pass
        pg.display.update()
gameLoop()
