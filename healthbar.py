import pygame

class Health(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.num_hearts = 3
        self.reset = False

        self.image = pygame.image.load('assets/hearts/3hearts.bmp').convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()

        screen.blit(self.image, (10,10))

    def health_update(self, screen):
        if self.reset == True:
            self.num_hearts = 3
            self.image = pygame.image.load('assets/hearts/3hearts.bmp').convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            self.rect = self.image.get_rect()

        if self.num_hearts == 3:
            self.image = pygame.image.load('assets/hearts/3hearts.bmp').convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            self.rect = self.image.get_rect()
            screen.blit(self.image, (10,10))

        elif self.num_hearts == 2:
            self.image = pygame.image.load('assets/hearts/2hearts.bmp').convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            self.rect = self.image.get_rect()
            screen.blit(self.image, (10,10))

        elif self.num_hearts == 1:
            self.image = pygame.image.load('assets/hearts/1hearts.bmp').convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            self.rect = self.image.get_rect()
            screen.blit(self.image, (10,10))

        elif self.num_hearts == 0:
            self.image = pygame.image.load('assets/hearts/0hearts.bmp').convert()
            colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey)
            self.rect = self.image.get_rect()
            screen.blit(self.image, (10,10))