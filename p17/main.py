import pygame
import random
import sys

SCREEN_WIDTH = 800  # TODO: Розмір екрану можливо зміниться
SCREEN_HEIGHT = 600 #
IMAGES_PATH_MENU = 'images/menu/'
IMAGES_PATH_BG = 'images/background/'
IMAGES_PATH_PLAYER = 'images//'
IMAGES_PATH_ENEMY = 'images//'
FONTS_PATH= 'fonts/'

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Player:
    pass


class MainMenu:
    img = None
    panel = None
    text = None
    text2 = None

    def __init__(self):
        self.add_bg()
        self.add_panel()

    def add_bg(self):
        img = pygame.image.load(IMAGES_PATH_MENU + 'bg-03.jpg')
        self.img = pygame.transform.scale(img, (SCREEN_WIDTH,SCREEN_HEIGHT))

    def add_panel(self):
        panel = pygame.image.load(IMAGES_PATH_MENU + 'interface-02.png')
        self.panel = pygame.transform.scale(panel, (500, 200))
        font = pygame.font.Font(FONTS_PATH + 'Inconsolata-VariableFont_wdth-wght.ttf', 24)
        message = "Press 'S' to start"
        self.text = font.render(message, True, (255, 255, 255))
        message = "Press 'X' to exit"
        self.text2 = font.render(message, True, (255, 255, 255))

    def draw(self):
        PANEL_POS_X = SCREEN_WIDTH/2-250
        PANEL_POS_Y = SCREEN_HEIGHT/2-100
        screen.blit(self.img, (0, 0))
        screen.blit(self.panel, (PANEL_POS_X, PANEL_POS_Y))
        screen.blit(self.text, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2-40))
        screen.blit(self.text2, (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 0))


class Background:
    img = None

    def __init__(self):
        self.add()

    def add(self):
        self.img = pygame.image.load(IMAGES_PATH_BG + 'bg_03.png')

    def draw(self):
        screen.blit(self.img, (0, 0))


class Game:
    gama_run: bool = False
    PANEL_POS_X = SCREEN_WIDTH / 2 - 250
    PANEL_POS_Y = SCREEN_HEIGHT / 2 - 100

    def __init__(self):
        self.menu = MainMenu()
        self.bg = Background()

    def quit(self):
        pygame.quit()
        sys.exit()

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.quit()
                    if event.key == pygame.K_s:
                        self.run()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_cord = pygame.mouse.get_pos()
                    if self.PANEL_POS_X <= mouse_cord[0]:
                        print('1')
                        if self.PANEL_POS_X + 500 >= mouse_cord[0]:
                            print('1')
                            if self.PANEL_POS_Y <= mouse_cord[1]:
                                print('1')
                                if self.PANEL_POS_Y + 200 >= mouse_cord[1]:
                                    print('1')
                                    self.quit()


            self.menu.draw()
            pygame.display.update()

    def run(self):
        self.game_run = True
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

if __name__ == '__main__':
    game = Game()
    game.init()
