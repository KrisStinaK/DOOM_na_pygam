from math import *

import pygame.key

from config import *


class Player:
    def __init__(self):
        self.x = half_width
        self.y = half_height
        self.angle = 0
        self.delta = 0
        self.speed = 500

    def move(self):
        key = pygame.key.get_pressed()
        cos_t, sin_t = cos(self.angle), sin(self.angle)

        if key[pygame.K_LEFT]:
            self.angle -= 0.3 * self.delta * 13
        if key[pygame.K_RIGHT]:
            self.angle += 0.3 * self.delta * 13

        if key[pygame.K_w]:
            self.x += cos_t * self.delta * self.speed
            self.y += sin_t * self.delta * self.speed
        if key[pygame.K_s]:
            self.x -= cos_t * self.delta * self.speed
            self.y -= sin_t * self.delta * self.speed
        if key[pygame.K_a]:
            self.x += sin_t * self.delta * self.speed
            self.y -= cos_t * self.delta * self.speed
        if key[pygame.K_d]:
            self.x -= sin_t * self.delta * self.speed
            self.y += cos_t * self.delta * self.speed


