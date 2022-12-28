from function import *
from player import Player
from drawing import Drawing
from settings import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()

drawing = Drawing(sc, sc_map)

# scene
current_scene = None

image = pygame.image.load('img/Заставка.jpg')

sprite = pygame.sprite.Sprite()
sprite.image = image
sprite.rect = image.get_rect()

font = pygame.font.SysFont('Arial', 50)
text = font.render('Press to Start', True, (255, 255, 255))

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

        sprite.image.blit(text, (440, 700))

        group = pygame.sprite.Group()
        group.add(sprite)
        group.draw(sc)

        pygame.display.flip()

def scene_2():
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
