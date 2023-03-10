from settings import *

_ = False
matrix_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 28, 1],
    [1, _, _, _, _, 3, 3, 3, _, 2, _, _, _, _, _, _, _, _, 4, _, _, 27, _, 27],
    [1, _, _, _, _, _, 2, _, _, 2, _, _, _, _, _, _, _, _, 4, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 2, 2, 2, 2, _, _, 4, _, _, 4, _, _, _, _, 1],
    [1, 2, 2, 2, _, _, _, _, _, 2, _, _, 2, _, _, 4, _, _, 4, _, 4, 4, 4, 1],
    [1, _, _, _, _, _, 3, _, _, 4, _, _, 2, _, _, 4, _, _, 4, _, _, _, _, 1],
    [1, _, _, _, _, _, 3, _, _, _, _, _, 2, _, _, 4, _, _, 4, _, _, 4, _, 1],
    [1, 4, 4, 4, _, _, 3, _, _, _, _, _, 2, _, _, 4, _, _, 4, _, _, 4, _, 1],
    [1, _, _, _, _, _, 3, _, _, 4, _, _, 2, _, _, 4, _, _, 4, _, _, 4, 4, 1],
    [1, _, _, _, _, _, 2, _, _, 4, _, _, 2, _, _, 4, _, _, 4, _, _, _, _, 1],
    [1, _, _, 4, _, _, _, _, _, 4, _, _, 2, _, _, 4, _, _, 4, _, _, _, _, 1],
    [1, _, _, 4, _, _, _, _, 3, 3, _, _, 2, _, _, 4, _, _, 4, _, _, _, 3, 1],
    [1, _, _, 4, 4, 4, 4, _, _, _, _, _, 2, _, _, 4, _, _, 4, _, _, _, 3, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, 4, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

matrix_map_level2 = [[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 28, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, _, _, _, _, _, 7, 7, _, 5, 27, _, 27, 4, _, _, 5, _, _, _, _, _, _, 6],
    [6, _, 5, 5, _, 7, _, _, _, 5, _, _, _, 4, _, _, 5, _, _, _, _, _, _, 6],
    [6, _, _, 5, _, 7, _, _, _, 5, _, 4, _, 4, _, _, _, _, _, _, _, _, _, 6],
    [6, 5, 5, 5, _, _, _, _, _, 5, _, 4, _, 3, _, _, _, _, _, _, _, _, _, 6],
    [6, _, _, _, 5, _, _, _, 5, _, _, 4, _, 3, _, _, 5, 5, 5, 5, 5, _, _, 6],
    [6, _, _, _, _, 6, _, 5, _, _, _, _, _, 3, _, _, _, _, _, _, 5, _, _, 6],
    [6, _, _, 5, _, 6, _, 5, _, _, 4, 4, 4, 4, 4, 4, 4, 4, 4, _, 5, _, _, 6],
    [6, _, _, 5, _, 6, _, 5, _, _, _, _, _, _, _, _, _, 4, _, _, 5, _, _, 6],
    [6, _, _, 5, _, _, _, 5, _, _, _, _, _, _, _, _, _, 4, _, 4, 5, _, _, 6],
    [6, _, _, 5, _, _, _, 7, 7, 7, 7, 8, 7, 7, 7, 5, _, 4, _, _, 5, _, _, 6],
    [6, _, _, 5, 5, 5, 5, _, _, _, _, _, _, _, _, 5, _, _, _, _, 5, _, _, 6],
    [6, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, 5, 5, 5, 5, 5, 5, _, _, 6],
    [6, _, _, 5, _, 5, _, 5, 5, 5, 5, 5, _, 5, _, _, _, _, _, _, _, _, _, 6],
    [6, _, _, _, _, 5, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, _, _, _, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
]

matrix_map_level3 = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, _, _, _, _, 3, 3, 3, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, 9],
    [9, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 9],
    [9, _, _, 5, 5, 5, _, _, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, _, _, 5, 9],
    [9, 5, 5, 5, _, 5, _, _, 5, _, _, _, _, 10, _, _, _, _, _, _, _, _, _, 9],
    [9, _, _, _, _, _, 5, 5, 5, _, _, _, _, 10, _, _, _, _, _, _, _, _, _, 9],
    [9, _, _, _, _, 11, _, _, _, _, 5, _, _, 10, 5, 5, _, _, 5, 5, 5, 5, 5, 9],
    [9, _, 5, _, _, 11, _, 5, 5, 5, 5, _, _, _, _, 5, _, _, _, _, _, _, _, 9],
    [9, _, 5, _, _, 11, _, _, _, _, 5, 5, _, _, _, 5, 5, 5, 5, 5, 5, 5, _, 9],
    [9, _, 5, 27, _, 28, 5, 5, 5, _, _, _, 5, _, _, 5, _, _, _, _, _, _, _, 9],
    [9, _, 5, 5, 28, _, _, _, 7, _, _, _, 5, _, _, 5, _, 5, 5, 5, 5, 5, 5, 9],
    [9, _, _, _, 5, _, 5, _, 7, _, _, _, 11, _, _, 5, _, _, _, _, _, _, _, 9],
    [9, _, 5, _, 5, _, 5, _, 7, _, _, _, 5, _, _, 5, 5, 5, 5, 5, 5, 5, _, 9],
    [9, _, 5, _, 5, _, 5, _, 5, _, _, _, 5, _, _, _, _, _, _, _, _, _, _, 9],
    [9, _, 5, _, _, _, 5, _, _, _, _, _, 5, _, _, _, _, _, _, _, _, _, _, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

matrix_map_level4 = [[30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
    [30, _, _, _, _, 22, 22, 22, _, 23, _, _, _, _, _, _, 5, _, _, _, _, _, _, 30],
    [30, _, _, _, _, _, _, _, _, 23, _, _, _, _, _, _, 5, _, _, _, _, _, _, 30],
    [30, _, _, 21, 21, 21, 21, _, _, 23, _, _, 29, 29, _, _, 5, _, _, _, _, _, _, 30],
    [30, _, _, 21, _, 27, _, 24, _, _, 23, _, _, 29, _, _, 29, _, 29, 23, 23, _, _, 30],
    [30, _, _, 21, _, _, 28, 24, _, _, 23, _, _, 29, _, _, 23, _, _, _, 23, _, _, 30],
    [30, _, _, 21, _, 28, 24, _, _, 23, _, _, 29, _, _, 23, 23, 23, _, _, 23, _, _, 30],
    [30, _, _, 22, _, _, _, 24, _, _, 23, _, _, 21, _, _, _, _, _, _, 22, _, _, 30],
    [30, _, _, 22, 24, 24, _, 24, _, _, 23, _, _, 21, _, _, _, _, _, _, 22, _, _, 30],
    [30, _, _, 22, _, _, _, 24, _, _, 23, _, _, 29, 29, 29, 29, 29, 29, 29, _, _, _, 30],
    [30, _, _, 22, _, 24, 24, 24, _, _, 23, _, _, 29, _, _, _, _, _, _, _, _, _, 30],
    [30, _, _, 22, _, _, _, _, _, _, 23, _, _, 29, _, _, _, _, _, _, _, _, _, 30],
    [30, _, _, 29, 29, 29, 29, 29, 29, 29, 23, _, _, 22, _, _, 29, 29, 21, 21, 29, 29, 29, 30],
    [30, _, _, _, _, _, _, _, _, _, _, _, _, 22, _, _, _, _, _, _, _, _, _, 30],
    [30, _, _, _, _, _, _, _, _, _, _, _, _, 22, _, _, _, _, _, _, _, _, _, 30],
    [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
]

matrix_map_level5 = [[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 28, 32, 32, 32, 32, 32, 32, 32, 32],
    [32, _, _, _, _, _, _, _, _, _, 23, _, 23, _, 27, _, 28, _, _, _, _, _, _, 32],
    [32, _, 31, 31, _, 23, _, 23, 23, _, 23, _, 23, _, _, _, 31, _, _, _, _, _, _, 32],
    [32, _, _, _, _, 23, _, _, _, _, _, _, 23, _, _, _, 31, _, _, _, _, _, _, 32],
    [32, 5, 5, 5, _, 23, 23, 23, 23, 23, 23, 23, 23, _, _, _, _, _, _, _, _, _, _, 32],
    [32, _, _, 24, _, 23, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 32],
    [32, _, _, 24, _, 22, _, _, _, _, _, _, _, _, _, _, _, _, 31, 31, 31, 31, 31, 32],
    [32, _, _, 24, _, 22, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 32],
    [32, _, _, 24, _, 22, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 32],
    [32, _, _, _, _, 22, 24, 24, 24, 24, 24, 24, _, 24, 24, 24, 24, 24, 24, 24, 23, _, _, 32],
    [32, _, _, _, _, 22, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 23, _, _, 32],
    [32, _, _, 24, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, _, _, 32],
    [32, _, _, 25, _, _, _, 25, _, _, 25, _, _, _, 24, _, _, 23, _, _, 23, _, _, 32],
    [32, _, _, _, _, 25, _, _, _, 25, _, _, 25, _, _, 24, _, _,23, _, _, _, _, 32],
    [32, _, _, _, 25, _, _, 25, _, _, _, 25, _, _, _, _, _, _, _, _, 23, _, _, 32],
    [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
]

matrix_map_level6 = [[26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26],
    [26, _, 5, _, _, 23, 23, 23, _, _, 5, _, _, _, _, _, 25, _, _, _, _, _, _, 26],
    [26, _, 5, _, _, _, _, _, _, _, _, 5, _, _, _, _, 25, _, _, _, _, _, _, 26],
    [26, _, 5, 5, _, _, _, _, _, _, _, 5, _, _, _, _, 25, _, _, _, _, _, _, 26],
    [26, _, _, 5, _, _, _, _, 5, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, 26],
    [26, _, _, 5, 5, _, _, 5, _, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, _, 5, _, _, _, _, 5, 25, 25, 25, _, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, 5, 5, _, _, _, _, 5, _, 28, _, 5, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, 5, _, _, _, _, _, 5, 27, _, 27, 5, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, 5, 5, 5, _, _, _, 5, _, _, _, 5, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, _, _, _, _, _, _, 5, 5, 5, _, 5, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, _, _, _, _, _, _, 5, _, _, _, 5, _, _, 26],
    [26, _, _, _, _, _, 5, 5, 5, 5, _, 5, 5, 5, 5, 5, 5, _, 5, 5, 5, _, _, 26],
    [26, _, _, _, _, _, 5, _, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, 26],
    [26, _, _, 5, _, _, 5, _, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, 26],
    [26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]
]

# my_map = {'line_1': {'row_1': 1}
#         'line_2': {'row_1': 1},
#         'line_3': {'row_1': 1}
# }

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = {}
mini_map = set()
collision_walls = []

