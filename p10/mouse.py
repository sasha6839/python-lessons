import pygame

pygame.init()
screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
def main():
    is_draw = False
    is_draw2 = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_draw = True
                if event.button == 2:
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                if event.button == 3:
                    is_draw2 = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_draw = False
                if event.button == 3:
                    is_draw2 = False
            if is_draw:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (225, 0, 50), pos, 20)
                pygame.display.update()
            if is_draw2:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (0,0,0), pos, 30)
                pygame.display.update()




        clock.tick(60)

main()