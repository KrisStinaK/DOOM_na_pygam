from random import randint

import pygame
from settings import *
from map_ import mini_map
from collections import deque

class Drawing:
    def __init__(self, sc, sc_map, player, sc_xp):
        self.sc = sc
        self.sc_map = sc_map
        self.sc_xp = sc_xp
        self.player = player
        self.F3 = 0
        self.weapon = 0
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
                         90: pygame.image.load('img/sky_7.bmp').convert(),
                         91: pygame.image.load('img/sky_a.bmp').convert(),
                         92: pygame.image.load('img/sky_b.bmp').convert(),

                         # wall
                         20: pygame.image.load('img/WALLlvl4_1.bmp').convert(),
                         21: pygame.image.load('img/WALLlvl4_2.bmp').convert(),
                         22: pygame.image.load('img/WALLlvl4_3.bmp').convert(),
                         23: pygame.image.load('img/wall_lvl_6_1.gif').convert(),
                         24: pygame.image.load('img/wall_lvl_6_2.gif').convert(),
                         25: pygame.image.load('img/wall_lvl_6_3.gif').convert(),
                         26: pygame.image.load('img/wall_lvl_6_4.png').convert(),
                         27: pygame.image.load('img/lift_.bmp').convert(),
                         28: pygame.image.load('img/lift.bmp').convert(),
                         29: pygame.image.load('img/WALL_lvl4_4.bmp').convert(),
                         30: pygame.image.load('img/WALL_lvl4_5.bmp').convert(),
                         31: pygame.image.load('img/WALL_lvl5.bmp').convert(),
                         32: pygame.image.load('img/wall_lvl5.gif').convert(),
                         }
        self.k = randint(12, 19)
        # weapon
        self.weapon_base_sprite_1 = pygame.image.load('resources/gun/static/standart_weapon.png').convert_alpha()
        self.weapon_shot_animation_1 = deque([pygame.image.load(f'resources/gun/shot/{i}.png').convert_alpha()
                                            for i in range(20)])

        self.weapon_base_sprite_2 = pygame.image.load('resources/gun_2/static/0.png').convert_alpha()
        self.weapon_shot_animation_2 = deque([pygame.image.load(f'resources/gun_2/shot/{i}.png').convert_alpha()
                                              for i in range(3)])

        self.weapon_base_sprite_3 = pygame.image.load('resources/gun_3/static/0.png').convert_alpha()
        self.weapon_shot_animation_3 = deque([pygame.image.load(f'resources/gun_3/shot/{i}.png').convert_alpha()
                                              for i in range(5)])

        self.weapon_base_sprite = self.weapon_base_sprite_1 # значение по умолчанию, нужно для смены оружия
        self.weapon_shot_animation = self.weapon_shot_animation_1 # анимация по умолчанию

        self.weapon_rect = self.weapon_base_sprite.get_rect()
        self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 4, 600)
        self.shot_length = len(self.weapon_shot_animation)
        self.shot_length_count = 0
        self.shot_animation_speed = 2
        self.shot_animation_count = 0
        self.shot_animation_trigger = True
        self.shot_sound = pygame.mixer.Sound('song/выстрел.wav')

        # sfx
        self.sfx = deque([pygame.image.load(f'resources/gun/sfx/{i}.png').convert_alpha() for i in range(9)])
        self.sfx_length_count = 0
        self.sfx_length = len(self.sfx)

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
            if self.F3 == 1:
                pygame.draw.rect(self.sc_map, COLOR_CONTROL_POINT, (220, 10, MAP_TILE, MAP_TILE))
            elif self.F3 == 2:
                pygame.draw.rect(self.sc_map, COLOR_CONTROL_POINT, (110, 10, MAP_TILE, MAP_TILE))
            elif self.F3 == 3:
                pygame.draw.rect(self.sc_map, COLOR_CONTROL_POINT, (40, 90, MAP_TILE, MAP_TILE))
            elif self.F3 == 4:
                pygame.draw.rect(self.sc_map, COLOR_CONTROL_POINT, (50, 50, MAP_TILE, MAP_TILE))
            elif self.F3 == 5:
                pygame.draw.rect(self.sc_map, COLOR_CONTROL_POINT, (150, 10, MAP_TILE, MAP_TILE))
            elif self.F3 == 6:
                pygame.draw.rect(self.sc_map, COLOR_CONTROL_POINT, (180, 80, MAP_TILE, MAP_TILE))
            pygame.draw.rect(self.sc_map, SANDY, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

    def player_weapon(self, shots):
        if self.weapon == 1:
            self.weapon_base_sprite = self.weapon_base_sprite_1
            self.weapon_shot_animation = self.weapon_shot_animation_1
            self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 4, 600)
        elif self.weapon == 2:
            self.weapon_base_sprite = self.weapon_base_sprite_2
            self.weapon_shot_animation = self.weapon_shot_animation_2
            self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 4, 500)
        elif self.weapon == 3:
            self.weapon_base_sprite = self.weapon_base_sprite_3
            self.weapon_shot_animation = self.weapon_shot_animation_3
            self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 4, 450)
        if self.player.shot:
            if not self.shot_length_count:
                self.shot_sound.play()
            self.shot_projection = min(shots)[1] // 2
            shot_sprite = self.weapon_shot_animation[0]
            self.sc.blit(shot_sprite, self.weapon_pos)
            self.shot_animation_count += 1
            self.bullet_sfx()
            if self.shot_animation_count == self.shot_animation_speed:
                self.weapon_shot_animation.rotate(-1)
                self.shot_animation_count = 0
                self.shot_length_count += 1
                self.shot_animation_trigger = False
            if self.shot_length_count == self.shot_length:
                self.player.shot = False
                self.shot_length_count = 0
                self.sfx_length_count = 0
                self.shot_animation_trigger = True
        else:
            self.sc.blit(self.weapon_base_sprite, self.weapon_pos)

    def bullet_sfx(self):
        if self.sfx_length_count < self.sfx_length:
            sfx = pygame.transform.scale(self.sfx[0], (self.shot_projection, self.shot_projection))
            sfx_rect = sfx.get_rect()
            self.sc.blit(sfx, (HALF_WIDTH - sfx_rect.w // 2, HALF_HEIGHT - sfx_rect.h // 2))
            self.sfx_length += 1
            self.sfx.rotate(-1)