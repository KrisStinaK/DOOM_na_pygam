from math import *
from settings import *

text_map = ["WWWWWWWWWWWW",
            "W...W......W",
            "W...W......W",
            "W...W...WWWW",
            "W..........W",
            "WWWW.......W",
            "W..........W",
            "WWWWWWWWWWWW"]
block_map = set()
mini_map = set()
y_block_pos = 0
for row in text_map:
    x_block_pos = 0
    for column in list(row):
        if column == "W":
            block_map.add((x_block_pos * tile, y_block_pos * tile))
            mini_map.add((x_block_pos * map_tile, y_block_pos * map_tile))
        x_block_pos += 1
    y_block_pos += 1

# Ray Casting
FOV = pi / 3
half_FOV = FOV / 2
max_depth = width // block_size
num_rays = 300
delta_ray = FOV / (num_rays - 1)
dist = num_rays / (2 * tan(half_FOV))
coefficient = dist * block_size
scale = width // num_rays


