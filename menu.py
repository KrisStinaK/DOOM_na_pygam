import pygame
from player import Player
from ray_casting import ray_casting, ray_casting_walls
from Sprites import *
from map_ import *
from interaction import *


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface(MINI_MAP_RES)
sc_xp = pygame.Surface((800, 100))
sc_cartridges = pygame.Surface((20, 150))
clock = pygame.time.Clock()
sprites = Sprites()
player = Player(sprites)
drawing = Drawing(sc, sc_map, player, sc_xp)
interaction = Interaction(player, sprites, drawing, sc, sc_xp)
interaction.play_music()
music = pygame.mixer.Sound('song/sound_win.mp3')
music2 = pygame.mixer.Sound('song/01 Title Screen.mp3')
game_musuc = pygame.mixer.Sound('song/игра.mp3')
# scene
current_scene = None


class Menu:
    def __init__(self):
        self.font = pygame.font.Font('fonts/8-BIT WONDER.TTF', 50)
        self.text = self.font.render("New Game", True, (155, 45, 48))
        self.text_2 = self.font.render("Options", True, (155, 45, 48))
        self.text_3 = self.font.render("Quit Game", True, (155, 45, 48))
        self.image = pygame.image.load('img/doom.png')
        self.image_cherepok = pygame.image.load('img/Cherepok.png')
        self.text_x1 = WIDTH // 2 - self.text.get_width() // 2
        self.text_y1 = HEIGHT // 2 - self.text.get_height() // 2
        self.text_x2 = WIDTH // 2 + 50 - self.text.get_width() // 2
        self.text_y2 = HEIGHT // 1.65 - self.text.get_height() // 2
        self.text_x3 = WIDTH // 2 - self.text.get_width() // 2
        self.text_y3 = HEIGHT // 1.4 - self.text.get_height() // 2
        self.ch_x, self.ch_y = self.text_x1 - 120, self.text_y1 - 30
        self.map = matrix_map
        self.F2 = 0

    def draw(self, sc):
        sc.fill((56, 34, 32))
        sc.blit(self.image, (0, 0))
        sc.blit(self.image_cherepok, (self.ch_x, self.ch_y))
        sc.blit(self.text, (self.text_x1, self.text_y1))
        sc.blit(self.text_2, (self.text_x2, self.text_y2))
        sc.blit(self.text_3, (self.text_x3, self.text_y3))

    def swetch_scene(self, scene):
        global current_scene
        current_scene = scene

    def scene_1(self):
        image_scene_1 = pygame.image.load('img/Сцена1.jpg')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                    self.swetch_scene(self.menu)
                    running = False
            music2.play()
            sc.blit(image_scene_1, (0, 0))
            pygame.display.flip()

    def options_scene(self):
        font = pygame.font.SysFont('fonts/8-BIT WONDER.TTF', 50)
        text1 = font.render('Управление:', True, WHITE)
        text2 = font.render('"E"        пауза', True, WHITE)
        text3 = font.render('"W"        вперед', True, WHITE)
        text4 = font.render('"A"        влево', True, WHITE)
        text5 = font.render('"S"        назад', True, WHITE)
        text6 = font.render('"D"        вправо', True, WHITE)
        text7 = font.render('"Escape"        выйти из игры', True, WHITE)
        text8 = font.render('"Enter"        выбрать', True, WHITE)
        text9 = font.render('"Мышь"        управление обзора', True, WHITE)
        textx = font.render('"1, 2, 3"        смена оружия', True, WHITE)
        textx1 = font.render('"R"        перезарядка', True, WHITE)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.swetch_scene(self.menu)
                    running = False
            sc.fill((0, 0, 0))
            sc.blit(text1, (200, 100))
            sc.blit(text2, (WIDTH // 2 - 400, 200))
            sc.blit(text3, (WIDTH // 2 - 400, 300))
            sc.blit(text4, (WIDTH // 2 - 400, 350))
            sc.blit(text5, (WIDTH // 2 - 400, 400))
            sc.blit(text6, (WIDTH // 2 - 400, 450))
            sc.blit(text7, (WIDTH // 2, 250))
            sc.blit(text8, (WIDTH // 2, 300))
            sc.blit(text9, (WIDTH // 2, 350))
            sc.blit(textx, (WIDTH // 2, 400))
            sc.blit(textx1, (WIDTH // 2, 450))
            pygame.display.flip()

    def load_level(self):
        image_1 = pygame.image.load('img/level_0.jpg')
        image_2 = pygame.image.load('img/level_1.jpg')
        image_3 = pygame.image.load('img/level_2.jpg')
        image_4 = pygame.image.load('img/level_3.jpg')
        image_5 = pygame.image.load('img/level_4.jpg')
        image_6 = pygame.image.load('img/level_5.jpg')
        map = matrix_map
        self.F2 = 0
        color = (155, 45, 48)
        x, y = 90, 90
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    if (x, y) == (90, 90):
                        x, y = 440, 90
                    elif (x, y) == (440, 90):
                        x, y = 790, 90
                    elif (x, y) == (90, 450):
                        x, y = 440, 450
                    elif (x, y) == (440, 450):
                        x, y = 790, 450
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    if (x, y) == (790, 90):
                        x = 440
                    elif (x, y) == (440, 90):
                        x = 90
                    elif (x, y) == (790, 450):
                        x = 440
                    elif (x, y) == (440, 450):
                        x = 90
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if (x, y) == (90, 90):
                        x, y = 90, 450
                    elif (x, y) == (440, 90):
                        x, y = 440, 450
                    elif (x, y) == (790, 90):
                        x, y = 790, 450
                    elif y == 450:
                        color = (0, 0, 170)
                        x, y = 90, 1000
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if (x, y) == (90, 450):
                        x, y = 90, 90
                    elif (x, y) == (440, 450):
                        x, y = 440, 90
                    elif (x, y) == (790, 450):
                        x, y = 790, 90
                    if color == (0, 0, 170):
                        color = (155, 45, 48)
                        x, y = 90, 450
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if (x, y) == (90, 90):
                        map = matrix_map
                        self.F2 = 1
                        drawing.F3 = 1
                        running = False
                        self.swetch_scene(self.main_stage)
                    elif (x, y) == (440, 90):
                        map = matrix_map_level2
                        self.F2 = 2
                        drawing.F3 = 2
                        running = False
                        self.swetch_scene(self.main_stage)

                    elif (x, y) == (790, 90):
                        map = matrix_map_level3
                        self.F2 = 3
                        drawing.F3 = 3
                        running = False
                        self.swetch_scene(self.main_stage)

                    elif (x, y) == (90, 450):
                        map = matrix_map_level4
                        self.F2 = 4
                        drawing.F3 = 4
                        player.x, player.y = 2200, 1450
                        running = False
                        self.swetch_scene(self.main_stage)
                    elif (x, y) == (440, 450):
                        map = matrix_map_level5
                        player.x, player.y = 1180, 165
                        self.F2 = 5
                        drawing.F3 = 5
                        running = False
                        self.swetch_scene(self.main_stage)
                    elif (x, y) == (790, 450):
                        map = matrix_map_level6
                        self.F2 = 6
                        drawing.F3 = 6
                        player.x, player.y = 150, 150
                        running = False
                        self.swetch_scene(self.main_stage)

                    if color == (0, 0, 170):
                        running = False
                        self.swetch_scene(self.menu)

                    for j, row in enumerate(map):
                        for i, char in enumerate(row):
                            if char:
                                mini_map.add((i * MAP_TILE, j * MAP_TILE))
                                collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                                if char == 1:
                                    world_map[(i * TILE, j * TILE)] = 1
                                elif char == 2:
                                    world_map[(i * TILE, j * TILE)] = 2
                                elif char == 3:
                                    world_map[(i * TILE, j * TILE)] = 3
                                elif char == 4:
                                    world_map[(i * TILE, j * TILE)] = 4
                                elif char == 5:
                                    world_map[(i * TILE, j * TILE)] = 5
                                elif char == 6:
                                    world_map[(i * TILE, j * TILE)] = 6
                                elif char == 7:
                                    world_map[(i * TILE, j * TILE)] = 7
                                elif char == 8:
                                    world_map[(i * TILE, j * TILE)] = 8
                                elif char == 9:
                                    world_map[(i * TILE, j * TILE)] = 9
                                elif char == 10:
                                    world_map[(i * TILE, j * TILE)] = 10
                                elif char == 11:
                                    world_map[(i * TILE, j * TILE)] = 11
                                elif char == 12:
                                    world_map[(i * TILE, j * TILE)] = 12
                                elif char == 13:
                                    world_map[(i * TILE, j * TILE)] = 13
                                elif char == 14:
                                    world_map[(i * TILE, j * TILE)] = 14
                                elif char == 15:
                                    world_map[(i * TILE, j * TILE)] = 15
                                elif char == 16:
                                    world_map[(i * TILE, j * TILE)] = 16
                                elif char == 17:
                                    world_map[(i * TILE, j * TILE)] = 17
                                elif char == 18:
                                    world_map[(i * TILE, j * TILE)] = 18
                                elif char == 19:
                                    world_map[(i * TILE, j * TILE)] = 19
                                elif char == 20:
                                    world_map[(i * TILE, j * TILE)] = 20
                                elif char == 21:
                                    world_map[(i * TILE, j * TILE)] = 21
                                elif char == 22:
                                    world_map[(i * TILE, j * TILE)] = 22
                                elif char == 23:
                                    world_map[(i * TILE, j * TILE)] = 23
                                elif char == 24:
                                    world_map[(i * TILE, j * TILE)] = 24
                                elif char == 25:
                                    world_map[(i * TILE, j * TILE)] = 25
                                elif char == 26:
                                    world_map[(i * TILE, j * TILE)] = 26
                                elif char == 27:
                                    world_map[(i * TILE, j * TILE)] = 27
                                elif char == 28:
                                    world_map[(i * TILE, j * TILE)] = 28
                                elif char == 29:
                                    world_map[(i * TILE, j * TILE)] = 29
                                elif char == 30:
                                    world_map[(i * TILE, j * TILE)] = 30
                                elif char == 31:
                                    world_map[(i * TILE, j * TILE)] = 31
                                elif char == 32:
                                    world_map[(i * TILE, j * TILE)] = 32
                                elif char == 90:
                                    world_map[(i * TILE, j * TILE)] = 90
                                elif char == 91:
                                    world_map[(i * TILE, j * TILE)] = 91
                                elif char == 92:
                                    world_map[(i * TILE, j * TILE)] = 92

            text = self.font.render("Back", True, color)
            sc.fill((56, 34, 32))
            sc.blit(image_1, (90, 90))
            sc.blit(image_2, (440, 90))
            sc.blit(image_3, (790, 90))
            sc.blit(image_4, (90, 450))
            sc.blit(image_5, (440, 450))
            sc.blit(image_6, (790, 450))
            sc.blit(text, (50, 730))
            pygame.draw.rect(sc, (0, 0, 170), (x, y,
                                               320, 240), 3)
            pygame.display.flip()

    def pause(self):
        font = pygame.font.Font('fonts/8-BIT WONDER.TTF', 50)
        text1 = font.render('Continue', True, (155, 45, 48))
        text2 = font.render('Menu', True, (155, 45, 48))
        ch_x, ch_y = self.text_x1 - 150, self.ch_y
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if ch_y == self.text_y1 - 30:
                        ch_y = self.text_y1 + 55
                    elif ch_y == self.text_y1 + 55:
                        ch_y = self.text_y1 + 135
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if ch_y == self.text_y1 + 135:
                        ch_y = self.text_y1 + 55
                    elif ch_y == self.text_y1 + 55:
                        ch_y = self.text_y1 - 30
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) \
                        and ch_y == self.text_y1 - 30:
                    running = False
                    self.swetch_scene(self.main_stage)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) \
                        and ch_y == self.text_y1 + 55:
                    running = False
                    self.swetch_scene(self.menu)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) \
                        and ch_y == self.text_y1 + 135:
                    exit()

                pygame.display.flip()

            sc.fill((56, 34, 32))
            sc.blit(self.image, (0, 0))
            sc.blit(self.image_cherepok, (ch_x, ch_y))
            sc.blit(text1, (self.text_x1, self.text_y1))
            sc.blit(text2, (self.text_x2 + 20, self.text_y2))
            sc.blit(self.text_3, (self.text_x3 - 20, self.text_y3))
            pygame.display.flip()

    def menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if self.ch_y == self.text_y1 - 30:
                        self.ch_y = self.text_y1 + 55
                    elif self.ch_y == self.text_y1 + 55:
                        self.ch_y = self.text_y1 + 135
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if self.ch_y == self.text_y1 + 135:
                        self.ch_y = self.text_y1 + 55
                    elif self.ch_y == self.text_y1 + 55:
                        self.ch_y = self.text_y1 - 30
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) \
                        and self.ch_y == self.text_y1 - 30:
                    running = False
                    self.swetch_scene(self.load_level)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) \
                        and self.ch_y == self.text_y1 + 55:
                    running = False
                    self.options_scene()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) \
                        and self.ch_y == self.text_y1 + 135:
                    exit()

            self.draw(sc)
            pygame.display.flip()

    def scene_you_win(self):
        music.play()
        game_musuc.stop()
        font = pygame.font.Font('fonts/8-BIT WONDER.TTF', 50)
        font2 = pygame.font.Font('fonts/8-BIT WONDER.TTF', 30)
        text = font.render('LEVEL UP', True, (0, 0, 0))
        text2 = font2.render('press "Enter" to return to the menu', True, (0, 0, 0))
        image = pygame.image.load('img/you_win.jpg')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = False
                    self.swetch_scene(self.load_level)
            sc.blit(image, (0, 0))
            sc.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
            sc.blit(text2, (WIDTH // 2 - 400, HEIGHT // 2 + 100))
            pygame.display.flip()

    def game_over(self):
        music.play()
        game_musuc.stop()
        font = pygame.font.Font('fonts/8-BIT WONDER.TTF', 50)
        font2 = pygame.font.Font('fonts/8-BIT WONDER.TTF', 30)
        text = font.render('GAME OVER', True, (0, 0, 0))
        text2 = font2.render('press "Enter" to return to the menu', True, (0, 0, 0))
        image = pygame.image.load('img/you_win.jpg')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = False
                    self.swetch_scene(self.load_level)
            sc.blit(image, (0, 0))
            sc.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
            sc.blit(text2, (WIDTH // 2 - 400, HEIGHT // 2 + 100))
            pygame.display.flip()

    def main_stage(self):
        music2.stop()
        game_musuc.stop()
        game_musuc.play()
        # >>>>>>> origin/main
        drawing.weapon *= 0
        sc_cartridges.fill((0, 0, 255))
        sc_xp.fill((100, 100, 100))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    running = False
                    self.swetch_scene(self.pause)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    drawing.weapon = 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    drawing.weapon = 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    drawing.weapon = 3
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    drawing.count_ammo = 15
                    sc_cartridges.fill((0, 0, 255))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not player.shot:
                        player.shot = True
                        drawing.count_ammo -= 1
                        if drawing.count_ammo < 0:
                            player.shot = False
                            drawing.count_ammo = 0
                if interaction.a < 20:
                    drawing.count_armor -= 1
                    if drawing.count_armor < 0:
                        drawing.count_armor = 0
                        if drawing.count_health < 0:
                            drawing.count_health = 0
                            running = False
                            self.swetch_scene(self.game_over)
                if player.F == 1 and self.F2 == 1:
                    running = False
                    self.swetch_scene(self.scene_you_win)
                elif player.F == 2 and self.F2 == 2:
                    running = False
                    self.swetch_scene(self.scene_you_win)
                elif player.F == 3 and self.F2 == 3:
                    running = False
                    self.swetch_scene(self.scene_you_win)
                elif player.F == 4 and self.F2 == 4:
                    running = False
                    self.swetch_scene(self.scene_you_win)
                elif player.F == 5 and self.F2 == 5:
                    running = False
                    self.swetch_scene(self.scene_you_win)
                elif player.F == 6 and self.F2 == 6:
                    running = False
                    self.swetch_scene(self.scene_you_win)

            player.movement()
            sc.fill(BLACK)

            drawing.ammo()
            drawing.background(player.angle)
            walls, wall_shot = ray_casting_walls(player, drawing.textures)
            drawing.world(walls + [ob.obj_locate(player) for ob in sprites.list_object])
            drawing.fps(clock)
            drawing.mini_map(player)
            drawing.player_weapon([wall_shot, sprites.sprite_shot])
            interaction.interaction_objects()
            interaction.npc_action()
            sc.blit(sc_xp, (200, 700))

            pygame.display.flip()
            clock.tick()

    def run(self):
        self.swetch_scene(self.scene_1)
        while current_scene is not None:
            current_scene()
            # >>>>>>> origin/main