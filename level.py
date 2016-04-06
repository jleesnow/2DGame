import pygame
from pygame import *

class Level():
    def __init__(self, player):

        self.background = None

        self.enemies = None

        self.shifted = 0
        self.player = player


    def update(self):
        self.enemies.update()

    def draw(self, screen):
        screen.blit(self.background, (self.shifted // 3,0))

        #self.enemies.draw(screen)

    def shift(self, Xshift):
        self.shifted += Xshift

        for enemy in self.enemies:
            enemy.rect.x += Xshift

class Level1(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        #self.background = pygame.image.load("sky.png").convert()
        self.background = pygame.image.load("assets/background1.png").convert()


class Level2(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("assets/background2.png").convert()