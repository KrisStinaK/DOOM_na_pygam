import pygame
from player import Player
from drawing import Drawing
from settings import *
import pygame_menu

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()

drawing = Drawing(sc, sc_map)

# scene
current_scene = None

image_scene_1 = pygame.image.load('img/Сцена1.jpg')
image_scene_2 = pygame.image.load('img/Сцена2.jpg')
image_scene_3 = pygame.image.load('img/Сцена3.jpg')

def swetch_scene(scene):
    global current_scene
    current_scene = scene

def scene_1():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                swetch_scene(None)
            if event.type == pygame.KEYDOWN:
                swetch_scene(scene_2)
                running = False
        sc.blit(image_scene_1, (0, 0))
        pygame.display.flip()


def scene_2():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                swetch_scene(None)
            if event.type == pygame.KEYDOWN:
                swetch_scene(scene_3)
                running = False

        sc.blit(image_scene_2, (0, 0))

        pygame.display.flip()

def scene_3():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                swetch_scene(None)
            if event.type == pygame.KEYDOWN:
                swetch_scene(main_stage)
                running = False
        sc.blit(image_scene_3, (0, 0))
        pygame.display.flip()

def main_stage():
    # >>>>>>> origin/main
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                swetch_scene(None)
        player.movement()
        sc.fill(BLACK)

        drawing.background(player.angle)
        drawing.world(player.pos, player.angle)
        drawing.fps(clock)
        drawing.mini_map(player)

        pygame.display.flip()
        clock.tick()
    # >>>>>>> origin/main


swetch_scene(scene_1)
while current_scene is not None:
    current_scene()