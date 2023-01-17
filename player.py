from settings import *
import pygame
import math
from map_ import collision_walls


class Player:
    def __init__(self, sprites):
        self.x, self.y = player_pos
        self.F = 0
        self.sprites = sprites
        self.angle = player_angle
        self.sensitivity = 0.004
        # collision parameters
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        # weapon
        self.shot = False

    @property  # всторенный декоратор python, теперь pos яаляется объект-свойством
    def pos(self):
        return self.x, self.y

    # @property
    # def collision_list(self):
    #     return collision_walls + [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in
    #                               self.sprites.list_object if obj.blocked]

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

    def keys_control(self):
        dx = 0
        dy = 0
        self.F *= 0
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_w]:
            dx = player_speed * cos_a * 1.5
            dy = player_speed * sin_a * 1.5
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a * 1.5
            dy = -player_speed * sin_a * 1.5
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a * 1.5
            dy = -player_speed * cos_a * 1.5
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a * 1.5
            dy = player_speed * cos_a * 1.5
            self.detect_collision(dx, dy)
        if self.x > 2210 and self.y < 180:
            self.F = 1
        elif 1200 > self.x > 1100 and 125 < self.y < 200:
            self.F = 2
        elif 475 > self.x > 425 and 970 > self.y > 900:
            self.F = 3
        elif 575 > self.x > 490 and 590 > self.y > 500:
            self.F = 4
        elif 1576 > self.x > 1500 and 200 > self.y > 125:
            self.F = 5
        elif 1900 > self.x > 1800 and 890 < self.y < 900:
            self.F = 6
        elif 855 > self.x > 825 and 855 > self.y > 825:
            self.F = 7
        elif 800 > self.x > 595 and 400 > self.y > 265:
            self.F = 8
        self.angle %= DOUBLE_PI
        # print(self.x, self.y)

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity / 1.5
