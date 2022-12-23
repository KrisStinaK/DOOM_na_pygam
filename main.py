import pygame
from math import *

from config import *
from function import *
from player import Player
from drawing import Drawing
from settings import *

pygame.font.init()
screen = pygame.display.set_mode((width, height))
sc_map = pygame.Surface((width // map_scale, height // map_scale))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    player.delta = delta_time()
    player.move()
    screen.fill(pygame.Color('black'))


    drawing.backgroun()
    drawing.world(player)
    drawing.fps(clock)
    drawing.mini_map(player)

    ray_casting(screen, player)

    # pygame.draw.circle(screen, red, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(screen, yellow, (player.x, player.y), (player.x + width * cos(player.angle),
    #                                                         player.y + width * sin(player.angle)), 2)
    #
    # for x, y in block_map:
    #     pygame.draw.rect(screen, green, (x, y, tile, tile), 2)

    pygame.display.set_caption("FPS " + str(int(clock.get_fps())))
    clock.tick(0)
    pygame.display.flip()

