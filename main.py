import pygame
from math import *

from config import *
from function import *
from player import Player

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    player.delta = delta_time()
    player.move()
    screen.fill(pygame.Color('black'))

    ray_casting(screen, player)

    pygame.display.set_caption("FPS " + str(int(clock.get_fps())))
    clock.tick(0)
    pygame.display.flip()