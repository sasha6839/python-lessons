# Розкоментувати і виправити помилки в програмі

import sys
import pygame as pg

pg.init()
run = True
window = pg.display.set_mode((600, 600))
SkyColor = (124, 255, 235)
window.fill(SkyColor)
hero = pg.image.load("images/pikachu.png")
hero_pos = {'x': 300, 'y': 300}

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()


    window.blit(hero, (44, 64))
    pg.display.update()

