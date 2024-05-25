import pygame
import random
import sys

SCREEN_WIDTH = 960  # TODO: Розмір екрану можливо зміниться
SCREEN_HEIGHT = 540 #
IMAGES_PATH_MENU = 'images/menu/'
IMAGES_PATH_BG = 'images/background/'
IMAGES_PATH_PLAYER = 'images/player/'
IMAGES_PATH_ENEMY = 'images//'
FONTS_PATH= 'fonts/'

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.img = pygame.image.load(IMAGES_PATH_PLAYER + 'Ship3.png')

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def shoot(self):
        pass


class MainMenu:
    img = None
    panel = None

    def __init__(self):
        self.add_bg()
        self.add_panel()

    def add_bg(self):
        img = pygame.image.load(IMAGES_PATH_MENU + 'bg-03.jpg')
        self.img = pygame.transform.scale(img, (SCREEN_WIDTH,SCREEN_HEIGHT))

    def add_panel(self):
        panel = pygame.image.load(IMAGES_PATH_MENU + 'Table_02.png')
        self.panel = pygame.transform.scale(panel, (500, 200))

    def start_btn(self, color=(0,0,0)):
        font = pygame.font.Font(FONTS_PATH + 'Inconsolata-VariableFont_wdth-wght.ttf', 24)
        text = font.render("Press to start", True, color)
        screen.blit(text, (SCREEN_WIDTH / 2 - 200, 234))

    def exit_btn(self, color=(0,0,0)):
        font = pygame.font.Font(FONTS_PATH + 'Inconsolata-VariableFont_wdth-wght.ttf', 24)
        text = font.render("Press to exit", True, color)
        screen.blit(text, (SCREEN_WIDTH / 2 - 200, 270))

    def draw(self):
        PANEL_POS_X = SCREEN_WIDTH/2-250
        PANEL_POS_Y = SCREEN_HEIGHT/2-100
        screen.blit(self.img, (0, 0))
        screen.blit(self.panel, (PANEL_POS_X, PANEL_POS_Y))
        self.move()

    def click(self):
        btn = pygame.mouse.get_pressed()

        if btn[0] and self.pos_start():
            return 'start'
        elif btn[0] and self.pos_exit():
            return 'exit'

        return None

    def pos_start(self):
        pos = pygame.mouse.get_pos()
        if (280 <= pos[0] and 280 + 160 >= pos[0]) and (234 <= pos[1] and 234 + 22 >= pos[1]):
            return True
        return False

    def pos_exit(self):
        pos = pygame.mouse.get_pos()
        if (pos[0] >= 280 and 280 + 160 >= pos[0]) and (270 <= pos[1] and 270 + 30 >= pos[1]):
            #     if 280 <= pos[0]:
            #         if 280 + 160 >= pos[0]:
            #             if 234 <= pos[1]:
            #                 if 234 + 22 >= pos[1]:
            return True
        return False

    def move(self):
        if self.pos_start():
            self.start_btn((255, 255, 255))
        else:
            self.start_btn()

        if self.pos_exit():
            self.exit_btn((255, 255, 255))
        else:
            self.exit_btn()


class Background:
    img = None

    def __init__(self):
        self.add()

    def add(self):
        self.img = pygame.image.load(IMAGES_PATH_BG + 'bg_03.png')

    def draw(self):
        screen.blit(self.img, (0, 0))


class Game:
    game_run: bool = False

    def __init__(self):
        self.menu = MainMenu()
        self.bg = Background()
        self.player = Player()

    def quit(self):
        pygame.quit()
        sys.exit()

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.quit()
                    if event.key == pygame.K_s:
                        self.run()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.menu.click()
                    if action == 'start':
                        self.run()
                    elif action == 'exit':
                        self.quit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     mouse_cord = pygame.mouse.get_pos()
                #     if 280 <= mouse_cord[0]:
                #         if 280 + 160 >= mouse_cord[0]:
                #             if 234 <= mouse_cord[1]:
                #                 if 234 + 22 >= mouse_cord[1]:
                #                     print('gfyufttyifttyk')
                #
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     mouse_cord = pygame.mouse.get_pos()
                #     print(mouse_cord)
                #     if 280 <= mouse_cord[0]:
                #         if 280 + 160 >= mouse_cord[0]:
                #             if 270 <= mouse_cord[1]:
                #                 if 270 + 30 >= mouse_cord[1]:
                #                     self.quit()

            self.menu.draw()
            pygame.display.update()

    def run(self):
        self.game_run = True
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_run = False
                        break
            self.bg.draw()
            self.player.draw()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.init()
