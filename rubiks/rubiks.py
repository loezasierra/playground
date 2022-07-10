# A simple Rubik's Cube game

import pygame
from objects import constants as cn


def game():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
    pygame.display.set_caption(cn.TITLE)

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(cn.WHITE)

    # Event loop
    while True:
        for event in pygame.event.get():
            # Exit if quit
            if event.type == pygame.QUIT:
                return
        
        screen.blit(background, cn.SCREEN_START)
        pygame.display.update()



# Run game
if __name__ == '__main__':
    game()
