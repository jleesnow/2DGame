import pygame
from pygame import *
from enemies import Enemy

class Level():
    def __init__(self, player):

        self.background = None
        self.sky = None
        self.ground_tile = pygame.image.load("assets/Resources/plainDirt2.png").convert()

        self.enemies = pygame.sprite.Group()

        self.shifted = 0
        self.totalShift = 0
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

        self.enemies.draw(screen)

        ground_w = self.ground_tile.get_width()
        ground_h = self.ground_tile.get_height()

        for x in range(0,w,ground_w):
            for y in range(300,450+1,ground_h):
                screen.blit(self.ground_tile, (x, y))


    def shift(self, Xshift):
        self.shifted += Xshift
        self.totalShift += abs(Xshift)

        for enemy in self.enemies:
            enemy.rect.x += Xshift

class Level1(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.sky = pygame.image.load("assets/sky.png").convert()
        self.background = pygame.image.load("assets/background1new.png").convert()
        self.level_limit = 4550

        # enemy1 = Enemy()
        # self.enemies.add(enemy1)
        #
        # enemy1.rect.x = 700
        # enemy1.rect.y = 307 - enemy1.rect.height
        #
        # enemy2 = Enemy()
        # self.enemies.add(enemy2)
        #
        # enemy2.rect.x = 1200
        # enemy2.rect.y = 307 - enemy2.rect.height
        #
        # enemy3 = Enemy()
        # self.enemies.add(enemy3)
        #
        # enemy3.rect.x = 1500
        # enemy3.rect.y = 307 - enemy3.rect.height
        #
        # enemy4 = Enemy()
        # self.enemies.add(enemy4)
        #
        # enemy4.rect.x = 2000
        # enemy4.rect.y = 307 - enemy4.rect.height
        enemy_space = 0

        enemy1 = Enemy()
        self.enemies.add(enemy1)
        enemy2 = Enemy()
        self.enemies.add(enemy2)
        enemy3 = Enemy()
        self.enemies.add(enemy3)
        enemy4 = Enemy()
        self.enemies.add(enemy4)
        enemy5 = Enemy()
        self.enemies.add(enemy5)
        enemy6 = Enemy()
        self.enemies.add(enemy6)
        enemy7 = Enemy()
        self.enemies.add(enemy7)

        for enemy in self.enemies:
            enemy_space += 700
            enemy.rect.x = enemy_space
            enemy.rect.y = 307 - enemy.rect.height




class Level2(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.sky = pygame.image.load("assets/sky.png").convert()
        self.background = pygame.image.load("assets/background2new.png").convert()
        self.level_limit = 4550