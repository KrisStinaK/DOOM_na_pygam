from settings import *
from map_ import *
from ray_casting import mapping
from drawing import Drawing
import math
import pygame


def ray_casting_npc_player(npc_x, npc_y, world_map, player_pos):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    delta_x, delta_y = ox - npc_x, oy - npc_y
    cur_angle = math.atan2(delta_y, delta_x)
    cur_angle += math.pi

    sin_a = math.sin(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = math.cos(cur_angle)
    cos_a = cos_a if cos_a else 0.000001

    # verticals
    x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
    for i in range(0, int(abs(delta_x)) // TILE):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        x += dx * TILE

    # horizontals
    y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
    for i in range(0, int(abs(delta_y)) // TILE):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        y += dy * TILE
    return True


class Interaction:
    def __init__(self, player, sprites, drawing, sc, sc_xp):
        self.player = player
        self.sprites = sprites
        self.drawing = drawing
        self.sc = sc
        self.sc_xp = sc_xp
        self.a = None
        self.pain_sound = pygame.mixer.Sound('song/звук монстра.wav')

    def interaction_objects(self):
        if self.player.shot and self.drawing.shot_animation_trigger:
            for obj in sorted(self.sprites.list_object, key=lambda obj: obj.distance):
                if obj.is_on_fire[1] and obj.distance < 500:
                    if obj.is_dead != 'immortal' and not obj.is_dead:
                        if ray_casting_npc_player(obj.x, obj.y, world_map, self.player.pos):
                            if obj.flag == 'npc':
                                self.pain_sound.play()
                            obj.is_dead = True
                            obj.blocked = None
                            self.drawing.shot_animation_trigger = False

                    break

    def npc_action(self):
        for obj in self.sprites.list_object:
            if obj.flag == 'npc' and not obj.is_dead:
                if ray_casting_npc_player(obj.x, obj.y, world_map, self.player.pos):
                    obj.npc_action_trigger = True
                    self.npc_move(obj)
                else:
                    obj.npc_action_trigger = False

    def npc_move(self, obj):
        self.a = abs(obj.distance)
        if abs(obj.distance) < TILE * 7:
            dx = obj.x - self.player.pos[0]
            dy = obj.y - self.player.pos[1]
            obj.x = obj.x + 1 if dx < 0 else obj.x - 1
            obj.y = obj.y + 1 if dy < 0 else obj.y - 1


    def play_music(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()