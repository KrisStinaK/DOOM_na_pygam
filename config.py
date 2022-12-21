from math import *

# screen configuration
width = 1200
height = 800
half_width = width // 2
half_height = height // 2

# doom map
block_size = 100
text_map = ["WWWWWWWWWWWW",
            "W..........W",
            "W..........W",
            "W.......WWWW",
            "W..........W",
            "WWWW.......W",
            "W..........W",
            "WWWWWWWWWWWW"]
block_map = set()
y_block_pos = 0
for row in text_map:
    x_block_pos = 0
    for column in list(row):
        if column == "W":
            block_map.add((x_block_pos, y_block_pos))
        x_block_pos += block_size
    y_block_pos += block_size

# Ray Casting
FOV = pi / 3
half_FOV = FOV / 2
max_depth = width // block_size
num_rays = 600
delta_ray = FOV / (num_rays - 1)
dist = num_rays / (2 * tan(half_FOV))
coefficient = dist * block_size
scale = width // num_rays

