import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, direction):
        super().__init__()

        gunshot = pygame.mixer.Sound('assets/sounds/gun.wav')
        gunshot.play()

        self.direction = direction

        self.image = pygame.Surface([10, 4])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()

    def update(self):
        if self.direction == "right":
            self.rect.x += 15

        elif self.direction == "left":
            self.rect.x -= 15