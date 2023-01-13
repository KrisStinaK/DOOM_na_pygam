import math

## сделал константы большими буквами

# game settings
SIZE = WIDTH, HEIGHT = 1200, 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT

# minimap settings
MINI_MAP_SCALE = 5
MINI_MAP_RES = (WIDTH // MINI_MAP_SCALE, HEIGHT // MINI_MAP_SCALE)
MAP_SCALE = 2 * MINI_MAP_SCALE
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, 0)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
HALF_NUM_RAYS = NUM_RAYS // 2
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2

# player settings
player_pos = (300, 300)
player_pos_lv2 = (1000, 600)
player_pos_lv3 = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_pos_lv4 = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_pos_lv5 = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_pos_lv6 = (HALF_WIDTH // 4, HALF_HEIGHT - 50)

player_angle = 0
player_speed = 1.5

# sprite settings
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
DARKGRAY = (40, 40, 40)
SKYBLUE = (0, 186, 255)
COLOR_CONTROL_POINT = (167, 252, 0)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)