import pygame
from random import randint
from settings import *
from collections import deque


class Sprites:
    def __init__(self):
        self.sprite_parametrs = {
            'sprite_devil': {
                'sprite': [pygame.image.load(f'resources/sprites/devil/structure/{i}.png').convert_alpha()
                           for i in range(8)],
                'viewing_angles': True,
                'shift': 0.0,
                'scale': (1.1, 1.1),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/devil/animation/{i}.png').convert_alpha()
                     for i in range(9)]),
                'animation_dist': 500,
                'animation_speed': 15,
                'blocked': True,
                'death_animation': deque([pygame.image.load(f'resources/sprites/devil/death/{i}.png').convert_alpha()
                                          for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'npc',
                'side': 30,
                'obj_action': []
            },
            'sprite_monster': {
                'sprite': pygame.image.load(f'resources/sprites/monster/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.2,
                'scale': (1.1, 1.1),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/monster/animation/{i}.png').convert_alpha() for i in range(6)]),
                'animation_dist': 300,
                'animation_speed': 12,
                'blocked': True,
                'death_animation': deque([pygame.image.load(f'resources/sprites/monster/death/{i}.png').convert_alpha()
                                          for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'npc',
                'side': 30,
                'obj_action': []
            },
            'sprite_brown_ball': {
                'sprite': pygame.image.load(f'resources/sprites/brown ball/static/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': (1.1, 1.1),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/brown ball/animation/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 300,
                'animation_speed': 12,
                'blocked': True,
                'death_animation': deque([pygame.image.load(f'resources/sprites/brown ball/death/{i}.png').convert_alpha()
                                          for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'npc',
                'side': 30,
                'obj_action': []
            },
            'sprite_barrel': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/barrel/structure/бочка.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': (0.4, 0.4),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/static_sprites/barrel/animation/{i}.png').convert_alpha() for i in
                     range(12)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
                'death_animation': deque(
                    [pygame.image.load(f'resources/sprites/static_sprites/barrel/death/{i}.png').convert_alpha() for i in
                     range(4)]),
                'is_dead': None,
                'dead_shift': 2,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },
            'sprite_blue_pin': {
                'sprite': pygame.image.load(f'resources/sprites/blue pin/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6, 0.6),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/blue pin/animation/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
                'death_animation': deque(
                    [pygame.image.load(f'resources/sprites/blue pin/animation/{i}.png').convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },
            'sprite_green_pin': {
                'sprite': pygame.image.load(f'resources/sprites/green pin/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6, 0.6),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/green pin/animation/{i}.png').convert_alpha() for i in
                     range(4)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
                'death_animation': deque(
                    [pygame.image.load(f'resources/sprites/green pin/animation/{i}.png').convert_alpha() for i in
                     range(4)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },
            'sprite_grey_pin': {
                'sprite': pygame.image.load(f'resources/sprites/grey pin/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6, 0.6),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/grey pin/animations/{i}.png').convert_alpha() for i in range(4)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': True,
                'death_animation': deque(
                    [pygame.image.load(f'resources/sprites/grey pin/animations/{i}.png').convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },
            'sprite_rip': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/rip.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': (0.4, 0.4),
                'animation': [],
                'animation_dist': None,
                'animation_speed': None,
                'blocked': None,
                'death_animation': [None],
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },

            'sprite_torch': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/Факел.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': (0.4, 0.4),
                'animation': [],
                'animation_dist': None,
                'animation_speed': None,
                'blocked': None,
                'death_animation': [None],
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },
            'sprite_fire': {
                'sprite': pygame.image.load(f'resources/sprites/static_sprites/fire/structure/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': (0.4, 0.4),
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/static_sprites/fire/animation/{i}.png').convert_alpha() for i in range(3)]),
                'animation_dist': 800,
                'animation_speed': 12,
                'blocked': None,
                'death_animation': [None],
                'is_dead': None,
                'dead_shift': 0.6,
                'flag': 'decor',
                'side': 30,
                'obj_action': []
            },
        }

        self.list_object = [
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_devil'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_barrel'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_barrel'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_fire'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_blue_pin'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_blue_pin'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_green_pin'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_green_pin'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_grey_pin'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_monster'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_monster'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_monster'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_monster'], (randint(5, 23), randint(2, 15))),
            Sprite_obj(self.sprite_parametrs['sprite_brown_ball'], (randint(5, 23), randint(2, 15))),

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
    def __init__(self, parameters, pos):
        self.object = parameters['sprite'].copy()
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation'].copy()
        # ---------------------
        self.death_animation = parameters['death_animation'].copy()
        self.is_dead = parameters['is_dead']
        self.dead_shift = parameters['dead_shift']
        # ---------------------
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.flag = parameters['flag']
        self.obj_action = parameters['obj_action'].copy()
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.side = parameters['side']

        self.dead_animation_count = 0
        self.animation_count = 0
        self.npc_action_trigger = False
        self.door_open_trigger = False
        self.door_prev_pos = self.y if self.flag == 'door_h' else self.x
        self.delete = False
        if self.viewing_angles:
            if len(self.object) == 8:
                self.sprite_angles = [frozenset(range(338, 361)) | frozenset(range(0, 23))] + \
                                     [frozenset(range(i, i + 45)) for i in range(23, 338, 45)]
            else:
                self.sprite_angles = [frozenset(range(348, 361)) | frozenset(range(0, 11))] + \
                                     [frozenset(range(i, i + 23)) for i in range(11, 348, 23)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    @property
    def is_on_fire(self):
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.blocked:
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
        self.zeta -= 1.4 * gamma

        delta_rays = int(gamma / DELTA_ANGLE)
        self.current_ray = CENTER_RAY + delta_rays
        self.distance *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS

        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance > 30:
            self.proj_height = min(int(PROJ_COEFF / self.distance), DOUBLE_HEIGHT)
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            half_sprite_width = sprite_width // 2
            half_sprite_height = sprite_height // 2
            shift = half_sprite_height * self.shift

            if self.is_dead and self.is_dead != 'immortal':
                sprite_obj = self.dead_animation()
                shift = half_sprite_height * self.dead_shift
                sprite_height = int(sprite_height / 1.3)
            # elif self.npc_action_trigger:
            #     sprite_obj = self.npc_in_action()
            else:
                self.object = self.visible_sprite()
                sprite_obj = self.sprite_animation()

            # sprite scale and pos
            sprite_pos = (self.current_ray * SCALE - half_sprite_width, HALF_HEIGHT - half_sprite_height + shift)

            sprite = pygame.transform.scale(sprite_obj, (sprite_width, sprite_height))
            return (self.distance, sprite, sprite_pos)
        else:
            return (False,)

    def sprite_animation(self):
        if self.animation and self.distance < self.animation_dist:
            sprite_obj = self.animation[0]
            if self.animation_count < self.animation_speed:
                self.animation_count += 1
            else:
                self.animation.rotate()
                self.animation_count = 0
            return sprite_obj
        return self.object

    def visible_sprite(self):
        if self.viewing_angles:
            if self.zeta < 0:
                self.zeta += DOUBLE_PI
            self.zeta = 360 - int(math.degrees(self.zeta))
            for angles in self.sprite_angles:
                if self.zeta in angles:
                    return self.sprite_positions[angles]
        return self.object

    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1
            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0
        return self.dead_sprite

    #    if self.animation_count < self.animation_speed:
    #    else:
    #        self.obj_action.rotate()
    #        self.animation_count = 0
    #    return sprite_object
