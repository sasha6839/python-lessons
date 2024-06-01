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

class Ammunition:
    def __init__(self):
        self.bullets = []

    def add(self, x, y):
        b = pygame.Surface((4, 6))
        b.fill((0, 0, 0))
        rect = b.get_rect(center=(x, y))

        self.bullets.append({'b':b, 'rect': rect})

    def move(self):
        for bullet in self.bullets:
            bullet['rect'].cetery -= 5

            if bullet['rect'].cetery < 0:
                self.bullets.remove(bullet)

    def draw(self):
        for bullet in self.bullets:
            screen.blit(bullet['surf'], bullet['rect'].center)


class Player:
    def __init__(self):
        self.img = pygame.image.load(IMAGES_PATH_PLAYER + 'Ship3.png')
        self.rect = self.img.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 70))
        self.speed = 5
        self.moving = []
        self.dt = 1

        self.ammo = Ammunition()

    def draw(self):
        self.move()
        screen.blit(self.img, self.rect.center)

    def move(self):
        if len(self.moving) > 0:
            if pygame.K_a == self.moving[0]:
                self.left()
            elif pygame.K_d == self.moving[0]:
                self.right()
        # self.moving = None
        # if self.moving == 'left':
        #     self.left()
        # elif self.moving == 'right':
        #     self.right()

    def left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = SCREEN_WIDTH
        # self.x = self.x - self.speed
        # screen.blit(self.img, (self.x, self.y))

    def right(self):
        if self.rect.right <= SCREEN_WIDTH:
            self.rect.right += self.speed
        else:
            self.rect.right = 0
        # self.x = self.x + self.speed
        # screen.blit(self.img, (self.x, self.y))

    def shoot(self):
        self.ammo.add(self.rect.center)
        # self.ammo.move()
        # self.ammo.draw()


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

        self.dt = 1
        self.clock = pygame.time.Clock()
        self.fps = 1000

    def quit(self):
        pygame.quit()
        sys.exit()

    def init(self):
        while True:
            if self.game_run:
                self.run()
            else:
                self.main_menu()

            pygame.display.update()
    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    self.quit()
                if event.key == pygame.K_s:
                    self.game_run = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                action = self.menu.click()
                if action == 'start':
                    self.game_run = True
                elif action == 'exit':
                    self.quit()
        self.menu.draw()

    def run(self):
        self.player.dt = self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_run = False
                    break
                elif event.type == pygame.K_SPACE:
                    self.player.shoot()
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player.moving.append(event.key)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player.moving.remove(event.key)
        self.bg.draw()
        self.player.draw()


if __name__ == '__main__':
    game = Game()
    game.init()
