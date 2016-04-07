import pygame
from pygame import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()

        self.change_x = 0
        self.change_y = 0

        # self.idle = [pygame.image.load('assets/Cowboy/Cowboy6_idle with gun_0.png'),
        #              pygame.image.load('assets/Cowboy/Cowboy6_idle with gun_1.png'),
        #              pygame.image.load('assets/Cowboy/Cowboy6_idle with gun_2.png'),
        #              pygame.image.load('assets/Cowboy/Cowboy6_idle with gun_3.png')]

        self.idle = ["assets/Cowboy/Cowboy6_idle with gun_0.png",
                     "assets/Cowboy/Cowboy6_idle with gun_1.png",
                     "assets/Cowboy/Cowboy6_idle with gun_2.png",
                     "assets/Cowboy/Cowboy6_idle with gun_3.png"]


        self.right_walk = ["assets/Cowboy/Cowboy6_walking with gun_0.png",
                           "assets/Cowboy/Cowboy6_walking with gun_1.png",
                           "assets/Cowboy/Cowboy6_walking with gun_2.png",
                           "assets/Cowboy/Cowboy6_walking with gun_3.png"]

        self.left_walk = []

        self.direction = "R"

        self.level = None
        self.frame = 0

        self.image = pygame.image.load('assets/Cowboy/Cowboy6_idle with gun_0.png').convert()

        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()

    def update(self, left, right, up, down, idle):
        if left:
            self.frame += 1
            self.image = pygame.image.load(self.left_walk[self.frame])
            if self.frame == 3: self.frame = 0

        if right:
            self.frame += 1
            self.image = pygame.image.load(self.right_walk[self.frame])
            if self.frame == 3: self.frame = 0

        if idle:
            self.frame += 1
            self.image = pygame.image.load(self.idle[self.frame])
            if self.frame == 3: self.frame = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)