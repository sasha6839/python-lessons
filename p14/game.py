import pygame

IMAGES_PATH: str = 'images/'
screen_width: int = 600
screen_height: int = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Wizard:

    x: int = 100
    y: int = 500
    width: int = 0
    height: int = 0
    speed: int = 10
    image_name = '1_IDLE_000.png'
    image_surface = None

    def __init__(self):
        self.image_surface = pygame.image.load(IMAGES_PATH + self.image_name)
        self.width = self.image_surface.get_width()
        self.height = self.image_surface.get_width()
        self.x = int(screen_width / 2 - self.width / 2)

    def show(self):
        screen.blit(self.image_surface, (self.x, self.y))

    # def move(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_a]:
    #         if self.x > 0 - self.width / 2:
    #             self.x -= self.speed
    #     if keys[pygame.K_d]:
    #         if self.x < screen_width - self.width / 2:
    #             self.x += self.speed

    def move(self, direction: str):
        if direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()

    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x + self.speed <= screen_width - self.width:
            self.x += self.speed
        else:
            self.x = screen_width - self.width



class Game:
    run: bool = True
    background = True
    fps: int = 60
    clock = pygame.time.Clock()
    player = None
    player_move = ''

    def __init__(self):
        pygame.display.set_caption('Wizard')
        self.background_add(IMAGES_PATH + 'background.png')
        self.player = Wizard()

    def background_add(self, image: str):
        self.background = pygame.image.load('images/background.png')

    def background_draw(self, xy: tuple = (0,0)):
        screen.blit(self.background, xy)

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_move = 'left'
                    if event.key == pygame.K_RIGHT:
                        self.player_move = 'right'
                elif event.type == pygame.KEYUP:
                    self.player_move = ''

            if self.run:
                self.background_draw()
                self.player.show()
                self.player.move(self.player_move)

                pygame.display.update()
                self.clock.tick(self.fps)

        pygame.quit()


g = Game()
g.play()
