import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.health = 100
        self.dead = False
        self.x_move = 0
        self.image = pygame.image.load("assets/Dino/dino_walk_0.png").convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)

        self.right_walk = ["assets/Dino/dino_walk_0.png",
                           "assets/Dino/dino_walk_1.png",
                           "assets/Dino/dino_walk_2.png",
                           "assets/Dino/dino_walk_3.png",
                           "assets/Dino/dino_walk_4.png",
                           "assets/Dino/dino_walk_5.png",
                           "assets/Dino/dino_walk_6.png"]



        self.left_walk = [pygame.transform.flip(pygame.image.load(self.right_walk[0]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[1]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[2]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[3]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[4]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[5]).convert(), True, False),
                          pygame.transform.flip(pygame.image.load(self.right_walk[6]).convert(), True, False)]

        self.rect = self.image.get_rect()
        self.frame = 0

    def kill_dino(self):
        self.image = pygame.image.load("assets/Dino/dead.png").convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.dead = True


    def update(self):
        if self.dead == False:
            if self.x_move == 50:
                self.frame = 0

            if self.x_move == 100:
                self.x_move = 0

            if self.x_move < 50:
                self.frame += 1
                self.image = pygame.image.load(self.right_walk[self.frame]).convert()
                colorkey = self.image.get_at((0, 0))
                self.image.set_colorkey(colorkey)
                if self.frame == 6: self.frame = 0
                self.rect.left += 1
                self.x_move += 1

            if self.x_move >= 50:
                self.frame += 1
                self.image = self.left_walk[self.frame]
                colorkey = self.image.get_at((0, 0))
                self.image.set_colorkey(colorkey)
                if self.frame == 6: self.frame = 0
                self.rect.left -= 1
                self.x_move += 1