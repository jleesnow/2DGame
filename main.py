import pygame
from pygame import *
import level
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode([768, 399])
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    player = Player()

    levelList = []
    levelList.append(level.Level1(player))
    levelList.append(level.Level2(player))

    current_level_no = 0
    current_level = levelList[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 10
    player.rect.y = 399 - player.rect.height - 100
    active_sprite_list.add(player)


    done = False
    up = down = left = right = idle = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    right = True
                elif event.key == K_LEFT:
                    left = True
                else:
                    idle = True

        active_sprite_list.update(left, right, up, down, idle)

        ###current_level.update()

        current_level.draw(screen)
        active_sprite_list.draw(screen)



        #pygame.display.flip()

        clock.tick(20)

        pygame.display.flip()

    pygame.quit()

    # level.Level1()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()

