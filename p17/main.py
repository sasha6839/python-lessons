import pygame
import random

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
pygame.init()
screen = pygame.display.set_mode(())


class Game:

    def __init__(self):
        pass

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            pygame.display.update()

    def run(self):
        pass


if __name__ == '__main__':
    game = Game()
    game.init()
