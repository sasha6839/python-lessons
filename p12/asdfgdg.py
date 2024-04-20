import pygame

pygame.init()
screen = pygame.display.set_mode((300,300))

while True:
    pygame.display.update()



x = pygame.mouse.get_pos()
print(type(x))