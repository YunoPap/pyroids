import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    sys.exit(1)


if __name__ == "__main__":
    main()
