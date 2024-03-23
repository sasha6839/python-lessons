import pygame
import random
import time
import sys

pygame.init()
#colors
white = (255,255,255)
yellow = (255,255,100)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (30,56,186)


#screen
scr_x = 600
scr_y = 600
screen = pygame.display.set_mode((scr_x,scr_y))
pygame.display.set_caption('Snake Game by Sasha')

clock = pygame.time.Clock()
snake_pos = {'x':10,'y':10}
def our_snake():
    pygame.draw.rect(screen, green, [snake_pos['x'],snake_pos['y'],50,50])



def gameLoop():
    game_over = False
    snake_list = []
    length_of_snake = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jyj1 = True
                while jyj1:
                    snake_pos['x'] -= 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            jyj1 = False
                        if event.key == pygame.K_UP:
                            jyj1 = False
                        if event.key == pygame.K_DOWN:
                            jyj1 = False

            if event.key == pygame.K_RIGHT:
                jyj2 = True
                while jyj2:
                    snake_pos['x'] += 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            jyj2 = False
                        if event.key == pygame.K_UP:
                            jyj2 = False
                        if event.key == pygame.K_DOWN:
                            jyj2 = False
            if event.key == pygame.K_UP:
                jyj3 = True
                while jyj3:
                    snake_pos['y'] -= 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            jyj3 = False
                        if event.key == pygame.K_LEFT:
                            jyj3 = False
                        if event.key == pygame.K_DOWN:
                            jyj3 = False
            if event.key == pygame.K_DOWN:
                jyj4 = True
                while jyj4:
                    snake_pos['y'] += 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            jyj4 = False
                        if event.key == pygame.K_UP:
                            jyj4 = False
                        if event.key == pygame.K_LEFT:
                            jyj4= False

        pygame.display.update()
        clock.tick(60)
        our_snake()

    pygame.quit()
    sys.exit()


gameLoop()








