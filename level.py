import pygame
from pygame import *

class Level():
    def __init__(self, player):

        self.background = None
        self.sky = None
        self.ground_tile = pygame.image.load("assets/Resources/plainDirt2.png").convert()

        self.enemies = None

        self.shifted = 0
        self.player = player


    def update(self):
        self.enemies.update()

    def draw(self, screen):
        self.background_size = self.background.get_size()
        self.background_rect = self.background.get_rect()
        w,h = self.background_size
        colorkey = self.background.get_at((0, 0))
        self.background.set_colorkey(colorkey)


        screen.blit(self.sky, (0,0))
        screen.blit(self.background, (self.shifted // 3,0))

        #self.enemies.draw(screen)

        ground_w = self.ground_tile.get_width()
        ground_h = self.ground_tile.get_height()

        for x in range(0,w,ground_w):
            for y in range(300,450+1,ground_h):
                screen.blit(self.ground_tile, (x, y))


    def shift(self, Xshift):
        self.shifted += Xshift

        # for enemy in self.enemies:
        #     enemy.rect.x += Xshift

class Level1(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.sky = pygame.image.load("assets/sky.png").convert()
        self.background = pygame.image.load("assets/background1.png").convert()
        # self.background_size = self.background.get_size()
        # self.background_rect = self.background.get_rect()
        # w,h = self.background_size


class Level2(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("assets/background2.png").convert()