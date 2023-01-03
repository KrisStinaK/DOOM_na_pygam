import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprite_types = {'barrel': pygame.image.load('resources/sprites/static_sprites/бочка.png').convert_alpha(),
                             'rip': pygame.image.load('resources/sprites/static_sprites/rip.png').convert_alpha(),
                             'tree': pygame.image.load('resources/sprites/static_sprites/Дерево1.png').convert_alpha(),
                             'torch': pygame.image.load('resources/sprites/static_sprites/Факел.png').convert_alpha(),
                             'devil': [pygame.image.load(f'resources/sprites/devil/{i}.png').convert_alpha() for i in
                                       range(8)]
                             }
        self.list_object = [
            Sprite_obj(self.sprite_types['barrel'], True, (7.1, 2.2), 1.8, 0.4),
            Sprite_obj(self.sprite_types['barrel'], True, (5.9, 2.2), 1.8, 0.4),
            Sprite_obj(self.sprite_types['rip'], True, (8.8, 2.5), 1.8, 0.4),
            Sprite_obj(self.sprite_types['rip'], True, (8.8, 5.6), 1.8, 0.4),
            Sprite_obj(self.sprite_types['tree'], True, (6.8, 6.6), 1.5, 0.4),
            # Sprite_obj(self.sprite_types['torch'], True, (6.8, 5.6), 1.8, 0.4),
            Sprite_obj(self.sprite_types['devil'], False, (7, 4), -0.2, 0.7),

        ]


class Sprite_obj(Sprites):
    def __init__(self, obj, static, pos, shift, scale):
        self.obj = obj
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale

        if not static:
            self.sprite_angels = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angels, self.obj)}

    def obj_locate(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        zeta = math.atan2(dy, dx)
        gamma = zeta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS

        if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance > 30:
            proj_height = min(int(PROJ_COEFF / distance * self.scale), DOUBLE_HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if zeta < 0:
                    zeta += DOUBLE_PI
                zeta = 360 - int(math.degrees(zeta))
                for angles in self.sprite_angels:
                    if zeta in angles:
                        self.obj = self.sprite_positions[angles]
                        break

            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)

            sprite = pygame.transform.scale(self.obj, (proj_height, proj_height))
            return (distance, sprite, sprite_pos)
        else:
            return (False,)
