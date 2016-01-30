import sys
import pygame
from Classes.Ship import Ship
import math

FPS = 40
NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
TURN_UP = 3
TURN_DOWN = 4
BACKGROUND_COLOR = (0, 0, 0)
COLOR_SPACEHIP = (25, 0, 100)
COLOR_LINE = (0, 255, 0)
DISPLAY_W = 800
DISPLAY_H = 600


pygame.init()
pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
screen = pygame.display.get_surface()

ship = Ship((20, 100))
clock = pygame.time.Clock()





while True:
    for event in pygame.event.get():
        ship.events(event)
        if event.type == pygame.QUIT:
            sys.exit()
    dt = clock.tick(FPS)

    ship.update(dt)
    screen.fill(BACKGROUND_COLOR)
    ship.render(screen)
    pygame.display.flip()
