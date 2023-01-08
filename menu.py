from player import Player
from drawing import Drawing
from ray_casting import ray_casting
from Sprites import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface(MINI_MAP_RES)
clock = pygame.time.Clock()
player = Player()
sprites = Sprites()
drawing = Drawing(sc, sc_map)

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
        self.Flag = 0
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
            sc.blit(image_scene_1, (0, 0))
            pygame.display.flip()

    def options_scene(self):
        font = pygame.font.Font('fonts/8-BIT WONDER.TTF', 30)
        text1 = font.render('in the development', True, (155, 45, 48))
        text2 = font.render('Press the "p" button to go back', True, (155, 45, 48))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.swetch_scene(self.menu)
                    running = False
            sc.fill((0, 0, 255))
            sc.blit(text1, (WIDTH // 2 - 300, HEIGHT // 2))
            sc.blit(text2, (WIDTH // 2 - 400, HEIGHT // 2 + 100))
            pygame.display.flip()
    def load_level(self):
        image_1 = pygame.image.load('img/level_0.jpg')
        image_2 = pygame.image.load('img/level_1.jpg')
        image_3 = pygame.image.load('img/level_2.jpg')
        image_4 = pygame.image.load('img/level_3.jpg')
        image_5 = pygame.image.load('img/level_4.jpg')
        image_6 = pygame.image.load('img/level_5.jpg')
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
                        running = False
                        self.swetch_scene(self.main_stage)
                    # if (x, y) == (90, 90):
                    #     self.Flag = 1
                    #     running = False
                    #     self.swetch_scene(self.main_stage)
                    # elif (x, y) == (440, 90):
                    #     self.Flag = 2
                    #     running = False
                    #     self.swetch_scene(self.main_stage)
                    if color == (0, 0, 170):
                        running = False
                        self.swetch_scene(self.menu)
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
                    self.menu()
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
                    self.swetch_scene(self.load_level)
                    running = False
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)\
                        and self.ch_y == self.text_y1 + 55:
                    self.options_scene()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)\
                        and self.ch_y == self.text_y1 + 135:
                    exit()

            self.draw(sc)
            pygame.display.flip()


    def main_stage(self):
        # >>>>>>> origin/main
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    self.swetch_scene(None)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    running = False
                    self.swetch_scene(self.pause)
            player.movement()
            sc.fill(BLACK)

            drawing.background(player.angle)
            walls = ray_casting(player, drawing.textures)
            drawing.world(walls + [ob.obj_locate(player) for ob in sprites.list_object])
            drawing.fps(clock)
            drawing.mini_map(player)

            pygame.display.flip()
            clock.tick()

    def run(self):
        self.swetch_scene(self.scene_1)
        while current_scene is not None:
            current_scene()
            # >>>>>>> origin/main