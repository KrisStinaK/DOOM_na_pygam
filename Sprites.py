import pygame
from settings import *
from collections import deque


class Sprites:
    def __init__(self):
        self.sprite_parametrs = {
            'sprite_devil': {
                'sprite': [pygame.image.load(f'resources/sprites/devil/structure/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': -0.2,
                'scale': 1.1,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/devil/animation/{i}.png').convert_alpha() for i in range(9)]),
                'animation_dist': 200,
                'animation_speed': 15,
                'blocked': True,
            },
            'sprite_monster': {
                'sprite': pygame.image.load(f'resources/sprites/monster/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.2,
                'scale': 1.1,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/monster/animation/{i}.png').convert_alpha() for i in range(6)]),
                'animation_dist': 300,
                'animation_speed': 12,
                'blocked': True,
            },
            'sprite_barrel': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/barrel/structure/бочка.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/static_sprites/barrel/animation/{i}.png').convert_alpha() for i in
                     range(12)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True
            },
            'sprite_blue_pin': {
                'sprite': pygame.image.load(f'resources/sprites/blue pin/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/blue pin/animation/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
            },
            'sprite_green_pin': {
                'sprite': pygame.image.load(f'resources/sprites/green pin/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/green pin/animation/{i}.png').convert_alpha() for i in
                     range(4)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
            },
            'sprite_grey_pin': {
                'sprite': pygame.image.load(f'resources/sprites/grey pin/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': 0.6,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/grey pin/animations/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
            },
            'sprite_rip': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/rip.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.4,
                'animation': None,
                'animation_dist': None,
                'animation_speed': None,
                'blocked': None,
            },
            'sprite_alive': {
                'sprite': [pygame.image.load(f'resources/sprites/sprite/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 1.8,
                'scale': 0.4,
                'animation': None,
                'animation_dist': None,
                'animation_speed': None,
                'blocked': None,
            },
            'sprite_torch': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/Факел.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.4,
                'animation': None,
                'animation_dist': None,
                'animation_speed': None,
                'blocked': None,
            },
            'sprite_fire': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/fire/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/static_sprites/fire/animation/{i}.png').convert_alpha() for i in range(3)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': None,
            },
        }

        self.list_object = [
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (7, 4)),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (5, 10)),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (9, 7)),
            Sprite_obj(self.sprite_parametrs['sprite_barrel'], (7.1, 2.1)),
            Sprite_obj(self.sprite_parametrs['sprite_barrel'], (5.9, 2.1)),
            Sprite_obj(self.sprite_parametrs['sprite_fire'], (20, 2.1)),
            Sprite_obj(self.sprite_parametrs['sprite_blue_pin'], (8.7, 2.5)),
            Sprite_obj(self.sprite_parametrs['sprite_blue_pin'], (5.5, 12.5)),
            Sprite_obj(self.sprite_parametrs['sprite_green_pin'], (10.3, 3.5)),
            Sprite_obj(self.sprite_parametrs['sprite_green_pin'], (7.5, 13.4)),
            Sprite_obj(self.sprite_parametrs['sprite_grey_pin'], (21, 3.7)),
            Sprite_obj(self.sprite_parametrs['sprite_alive'], (13.5, 10)),
            Sprite_obj(self.sprite_parametrs['sprite_monster'], (22.5, 1.7)),

            # static sprite
            Sprite_obj(self.sprite_parametrs['sprite_rip'], (10.5, 7.5)),
            Sprite_obj(self.sprite_parametrs['sprite_rip'], (8.8, 5.6)),
            Sprite_obj(self.sprite_parametrs['sprite_rip'], (5.8, 7)),
            Sprite_obj(self.sprite_parametrs['sprite_torch'], (9.8, 14.8)),
        ]

    @property
    def sprite_shot(self):
        return min([obj.is_on_fire for obj in self.list_object], default=(float('inf'), 0))


class Sprite_obj:
    def __init__(self, parameter, pos):
        self.obj = parameter['sprite']
        self.viewing_angles = parameter['viewing_angles']
        self.shift = parameter['shift']
        self.scale = parameter['scale']
        self.animation = parameter['animation']
        self.animation_dist = parameter['animation_dist']
        self.animation_speed = parameter['animation_speed']
        self.blocked = parameter['blocked']
        self.side = 30
        self.animation_count = 0
        self.x, self.y = pos[0] * TILE, pos[1] * TILE

        if self.viewing_angles:
            self.sprite_angels = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angels, self.obj)}

    @property
    def is_on_fire(self):
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2and self.blocked:
            return self.distance, self.proj_height
        return float('inf'), None

    @property
    def pos(self):
        return self.x - self.side // 2, self.y - self.side // 2

    def obj_locate(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        self.distance = math.sqrt(dx ** 2 + dy ** 2)
        self.zeta = math.atan2(dy, dx)
        gamma = self.zeta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        self.current_ray = CENTER_RAY + delta_rays
        self.distance *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS

        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance > 30:
            self.proj_height = min(int(PROJ_COEFF / self.distance * self.scale), DOUBLE_HEIGHT)
            half_proj_height = self.proj_height // 2
            shift = half_proj_height * self.shift
            # choosing sprite for angle
            if self.viewing_angles:
                if self.zeta < 0:
                    self.zeta += DOUBLE_PI
                self.zeta = 360 - int(math.degrees(self.zeta))
                for angles in self.sprite_angels:
                    if self.zeta in angles:
                        self.obj = self.sprite_positions[angles]
                        break
            # sprite animation
            sprite_obj = self.obj
            if self.animation and self.distance < self.animation_dist:
                sprite_obj = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            # sprite scale and pos

            sprite_pos = (self.current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)

            sprite = pygame.transform.scale(sprite_obj, (self.proj_height, self.proj_height))
            return (self.distance, sprite, sprite_pos)
        else:
            return (False,)