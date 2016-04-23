import pygame
from pygame import *


class Horse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/horse.png").convert()
        self.rect = self.image.get_rect()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)

    def update(self, left, right, up, down, idle):
        if left:
            self.rect.left -= 9
            self.direction = "L"

        if right:
            self.image = pygame.image.load("assets/horse.png").convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            self.rect.right += 6
            self.direction = "R"

        if idle:
            self.image = pygame.image.load("assets/horse.png").convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
