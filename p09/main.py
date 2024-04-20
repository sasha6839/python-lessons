# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

#h1
pygame.display.set_caption('Spider')

#Налаштування частоти відтворення екрану

clock = pygame.time.Clock()
clock_tick = 60

spyder_image = pygame.image.load('images/spyder.png')
spyder_image_pos = {'x': 300, 'y': 400}

background_surface = pygame.Surface((screen_width, screen_height))
background_surface.fill('Black')

# =====================================================
while True:
    # Слідкуємо за подіями
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if spyder_image_pos['y'] > 0:
            spyder_image_pos['y'] -= 4
    if keys[pygame.K_s]:
        if spyder_image_pos['y'] < 600:
            spyder_image_pos['y'] += 4
    if keys[pygame.K_a]:
        if spyder_image_pos['x'] > 0:
            spyder_image_pos['x'] -= 4
    if keys[pygame.K_d]:
        if spyder_image_pos['x'] < 800:
            spyder_image_pos['x'] += 4

    screen.blit(background_surface, (0,0))



    # added image
    screen.blit(spyder_image, (spyder_image_pos['x'], spyder_image_pos['y']))

    # update area of screen
    pygame.display.update()

    #Обмежуємо швидкість відтворення - FPS
    clock.tick(clock_tick)