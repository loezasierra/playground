# A simple Rubik's Cube game

import pygame

## Constants ##

# Screen
TITLE  = "Rubik's Cube"
WIDTH  = 800
HEIGHT = 600

SCREEN_START = (0, 0)

# Colors
WHITE = (255, 255, 255)


## Game ##

def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    # Event loop
    while True:
        for event in pygame.event.get():
            # Exit if quit
            if event.type == pygame.QUIT:
                return
        
        screen.blit(background, SCREEN_START)
        pygame.display.update()



# Run main
if __name__ == '__main__':
    main()
