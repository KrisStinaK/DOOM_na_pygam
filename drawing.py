from random import random, choice, randint

import pygame
from settings import *
from map_ import mini_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        # загрузка текстур (можно добавить больше, но потом нужно изменить цифру на карте)
        # под S небо (для него не нужно менять карту)
        self.textures = {1: pygame.image.load('img/стена3.png').convert(),
                         2: pygame.image.load('img/WALL75.bmp').convert(),
                         3: pygame.image.load('img/WALL103.bmp').convert(),
                         4: pygame.image.load('img/WALL1.bmp').convert(),
                         5: pygame.image.load('img/WALLlvl2_1.bmp').convert(),
                         6: pygame.image.load('img/WALLlvl2_2.bmp').convert(),
                         7: pygame.image.load('img/WALLlvl2_3.bmp').convert(),
                         8: pygame.image.load('img/WALLlvl3_1.bmp').convert(),
                         9: pygame.image.load('img/WALLlvl3_2.bmp').convert(),
                         10: pygame.image.load('img/WALLlvl3_3.bmp').convert(),
                         11: pygame.image.load('img/WALLlvl3_4.bmp').convert(),

                         # sky
                         12: pygame.image.load('img/Sky_2.bmp').convert(),
                         13: pygame.image.load('img/sky.png').convert(),
                         14: pygame.image.load('img/Sky_3.bmp').convert(),
                         15: pygame.image.load('img/Sky_4.bmp').convert(),
                         16: pygame.image.load('img/Sky_5.bmp').convert(),
                         17: pygame.image.load('img/Sky2.bmp').convert(),
                         18: pygame.image.load('img/Sky_8.bmp').convert(),
                         19: pygame.image.load('img/Sky_9.bmp').convert(),

                         # wall
                         20: pygame.image.load('img/WALLlvl4_1.bmp').convert(),
                         21: pygame.image.load('img/WALLlvl4_2.bmp').convert(),
                         22: pygame.image.load('img/WALLlvl4_3.bmp').convert(),
                         23: pygame.image.load('img/WALLlvl4_3.bmp').convert(),
                         }
        self.k = randint(12, 19)

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures[self.k], (sky_offset, 0))
        self.sc.blit(self.textures[self.k], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures[self.k], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, SANDY, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)