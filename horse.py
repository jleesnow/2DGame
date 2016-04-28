import pygame
from pygame import *


class Horse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.direction = "R"

        self.right_walk = ["assets/horse/horse0.png",
                           "assets/horse/horse1.png",
                           "assets/horse/horse2.png",
                           "assets/horse/horse3.png",
                           "assets/horse/horse4.png"]

        self.left_walk = ["assets/horse/horse0L.png",
                           "assets/horse/horse1L.png",
                           "assets/horse/horse2L.png",
                           "assets/horse/horse3L.png",
                           "assets/horse/horse4L.png"]

        self.frame = 0
        self.image = pygame.image.load("assets/horse/horse0.png").convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()



    def update(self, left, right, up, down, idle):
        if right:
            self.image = pygame.image.load(self.right_walk[self.frame]).convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            if self.frame == 4: self.frame = 0
            self.rect.right += 6
            self.direction = "R"
            self.frame += 1
        if left:
            self.image = pygame.image.load(self.left_walk[self.frame]).convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            if self.frame == 4: self.frame = 0
            self.rect.right -= 6 #9
            self.direction = "L"
            self.frame += 1

        if idle:
            if self.direction == "R":
                self.image = pygame.image.load("assets/horse/horse0.png").convert()
                colorkey = self.image.get_at((0, 0))
                self.image.set_colorkey(colorkey)
            if self.direction == "L":
                self.image = pygame.image.load("assets/horse/horse0L.png").convert()
                colorkey = self.image.get_at((0, 0))
                self.image.set_colorkey(colorkey)





















