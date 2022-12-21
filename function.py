import pygame
import time
from math import *

from config import *

cur_time = time.time_ns()


def delta_time():
    global cur_time
    delta = (time.time_ns() - cur_time) / 1000000000
    cur_time = time.time_ns()
    return delta


def ray_casting(display, player):
    in_block_pos = {'left': player.x - player.x // block_size * block_size,
                    'top': player.y - player.y // block_size * block_size,
                    'right': block_size - (player.x - player.x // block_size * block_size),
                    'bottom': block_size - (player.y - player.y // block_size * block_size)}
    for ray in range(num_rays):
        cur_angle = player.angle - half_FOV + delta_ray * ray
        cos_t, sin_t = cos(cur_angle), sin(cur_angle)
        vd, hd = 0, 0

        # vertical
        for dep in range(max_depth):
            if cos_t > 0:
                vd = in_block_pos['right'] / cos_t + block_size / cos_t * dep + 1
            elif cos_t < 0:
                vd = in_block_pos['left'] / -cos_t + block_size / -cos_t * dep + 1

            x, y = vd * cos_t + player.x, vd * sin_t + player.y
            fixed_x, fixed_y = x // block_size * block_size, y // block_size * block_size
            if (fixed_x, fixed_y) in block_map:
                break

        # horizontal
        for dep in range(max_depth):
            if sin_t > 0:
                hd = in_block_pos['bottom'] / sin_t + block_size / sin_t * dep + 1
            elif sin_t < 0:
                hd = in_block_pos['top'] / -sin_t + block_size / -sin_t * dep + 1

            x, y = hd * cos_t + player.x, hd * sin_t + player.y
            fixed_x, fixed_y = x // block_size * block_size, y // block_size * block_size
            if (fixed_x, fixed_y) in block_map:
                break

        ray_size = min(vd, hd)
        ray_size *= cos(player.angle - cur_angle)
        height_c = coefficient / (ray_size + 0.0001)
        c = 255 / (1 + ray_size**2*0.00001)
        color = (c, c, c)
        pygame.draw.rect(display, color, (ray * scale, half_height - height_c // 2, scale, height_c))
