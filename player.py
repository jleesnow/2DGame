import pygame
from pygame import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.jumping = False
        self.yvel = 0
        self.grav = 1


        self.idle = ["assets/Cowboy/Cowboy6_idle with gun_0.png",
                     "assets/Cowboy/Cowboy6_idle with gun_1.png",
                     "assets/Cowboy/Cowboy6_idle with gun_2.png",
                     "assets/Cowboy/Cowboy6_idle with gun_3.png"]

        self.idle_left = [pygame.transform.flip(pygame.image.load(self.idle[0]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.idle[1]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.idle[2]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.idle[3]).convert(), True, False)]

        self.right_walk = ["assets/Cowboy/Cowboy6_walking with gun_0.png",
                           "assets/Cowboy/Cowboy6_walking with gun_1.png",
                           "assets/Cowboy/Cowboy6_walking with gun_2.png",
                           "assets/Cowboy/Cowboy6_walking with gun_3.png"]



        self.left_walk = [pygame.transform.flip(pygame.image.load(self.right_walk[0]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[1]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[2]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[3]).convert(), True, False)]



        self.direction = "R"
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
            self.direction = "L"

        if right:
            self.frame += 1
            self.image = pygame.image.load(self.right_walk[self.frame])
            if self.frame == 3: self.frame = 0
            self.rect.right += 10
            self.direction = "R"

        if idle:
            if self.direction == "R":
                self.frame += 1
                self.image = pygame.image.load(self.idle[self.frame])
                if self.frame == 3: self.frame = 0
            if self.direction == "L":
                self.frame += 1
                self.image = self.idle_left[self.frame]
                colorkey = self.image.get_at((0, 0))
                self.image.set_colorkey(colorkey)
                if self.frame == 3: self.frame = 0


    def jump(self):
        jumpsound = pygame.mixer.Sound('assets/sounds/jump.wav')
        jumpsound.play()
        if self.jumping == False:
            self.yvel = -12
            self.jumping = True

    def jumpUpdate(self):
        if self.jumping:
            self.yvel += self.grav
            self.rect.y += self.yvel
            if self.rect.y > (299 - self.rect.height):
                self.jumping = False