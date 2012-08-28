import random
import pygame
for key in filter(lambda s: s.startswith('K_'), dir(pygame)):
    locals()[key] = vars(pygame)[key]
    

def rand(i):
    return random.randint(0, i - 1)

class Sound(object):
    def __init__(self, filename):
        self.real = pygame.mixer.Sound(filename)

    def play(self):
        self.real.play()

class Sprite(object):
    def __init__(self, filename, x, y):
        self.x = x
        self.y = y
        #self.real = pygame.sprite.Sprite()
        self.image = pygame.image.load(filename)

class Game(object):
    def __init__(self, width, height, tile_width, tile_height):
        self.width = width
        self.height = height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.screen = pygame.display.set_mode(
                        (width * tile_width, height * tile_height))
        self.finished = False
        pygame.init()

    def is_running(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.tick = False
        self.curr_key = None

        if self.finished:
            e = None
            while e != pygame.QUIT:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        e = pygame.QUIT
                        break
            return False
        else:
            while not self.curr_key and not self.tick:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.USEREVENT:
                        self.tick = True
                    elif event.type == pygame.KEYDOWN:
                        self.curr_key = event.key
            return True

    def get_key(self):
        return self.curr_key

    def set_tick(self, ms):
        pygame.time.set_timer(pygame.USEREVENT, ms)

    def is_tick(self):
        return self.tick

    def end(self):
        self.finished = True

    def message(self, x, y, text):
        # calc fontsize based on tileheight; centre in tiles?
        pass

    def draw(self, objs):
        try:
            iter(objs)
        except TypeError:
            objs = [objs]

        for obj in objs:
            self.screen.blit(obj.image,
                    (obj.x * self.tile_width, obj.y * self.tile_height))
