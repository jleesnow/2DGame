import pygame
from pygame import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()

        self.jumping = False

        self.yvel = 0
        self.grav = 1


        self.idle = ["assets/Cowboy/Cowboy6_idle with gun_0.png",
                     "assets/Cowboy/Cowboy6_idle with gun_1.png",
                     "assets/Cowboy/Cowboy6_idle with gun_2.png",
                     "assets/Cowboy/Cowboy6_idle with gun_3.png"]

        self.right_walk = ["assets/Cowboy/Cowboy6_walking with gun_0.png",
                           "assets/Cowboy/Cowboy6_walking with gun_1.png",
                           "assets/Cowboy/Cowboy6_walking with gun_2.png",
                           "assets/Cowboy/Cowboy6_walking with gun_3.png"]



        self.left_walk = [pygame.transform.flip(pygame.image.load(self.right_walk[0]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[1]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[2]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[3]).convert(), True, False)]



        self.direction = "R"

        self.level = None
        self.frame = 0

        self.image = pygame.image.load('assets/Cowboy/Cowboy6_idle with gun_0.png').convert()

        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()

    def update(self, left, right, up, down, idle):
        self.jumpUpdate()
        if left:
            self.frame += 1
            self.image = self.left_walk[self.frame]
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            if self.frame == 3: self.frame = 0
            self.rect.left -= 10

        if right:
            self.frame += 1
            self.image = pygame.image.load(self.right_walk[self.frame])
            if self.frame == 3: self.frame = 0
            self.rect.right += 10

        if idle:
            self.frame += 1
            self.image = pygame.image.load(self.idle[self.frame])
            if self.frame == 3: self.frame = 0


    def jump(self):
        if self.jumping == False:
            self.yvel = -12
            self.jumping = True

    def jumpUpdate(self):
        if self.jumping:
            self.yvel += self.grav
            self.rect.y += self.yvel
            if self.rect.y > (399 - self.rect.height - 100):
                self.jumping = False

    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)