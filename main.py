import pygame
from pygame import *
import level
from player import Player
from bullets import Bullet
from enemies import Enemy

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

    bullet_list = pygame.sprite.Group()
    all_sprite_list = pygame.sprite.Group()

    player.rect.x = 10
    player.rect.y = 300 - player.rect.height
    active_sprite_list.add(player)


    done = False
    up = down = left = right = idle = False
    while not done:
        for event in pygame.event.get():
            idle = False
            if event.type == pygame.QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    right = True
                elif event.key == K_LEFT:
                    left = True
                elif event.key == K_UP:
                    player.jump()
                elif event.key == K_SPACE:
                    if player.direction == "R":
                        bullet = Bullet("right")
                        bullet.rect.x = player.rect.x + 33
                        bullet.rect.y = player.rect.y + 27
                        all_sprite_list.add(bullet)
                        bullet_list.add(bullet)
                    if player.direction == "L":
                        bullet = Bullet("left")
                        bullet.rect.x = player.rect.x + 20
                        bullet.rect.y = player.rect.y + 27
                        all_sprite_list.add(bullet)
                        bullet_list.add(bullet)
                elif event.key == K_F1:
                    current_level = level_switch(1, player, current_level, levelList)
                elif event.key == K_F2:
                    current_level = level_switch(2, player, current_level, levelList)

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    right = False
                    idle = True
                elif event.key == K_LEFT:
                    left = False
                    idle = True
            else:
                idle = True


        active_sprite_list.update(left, right, up, down, idle)
        all_sprite_list.update()

        current_level.update()

        ##################
        if player.rect.right >= 500 and current_level.totalShift < current_level.level_limit:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift(-diff)

        # this offsets at the beginning
        # if player.rect.right <= 120:
        #     diff = 120 - player.rect.left
        #     player.rect.left = 120
        #     current_level.shift(diff)
        ##################

        if (current_level.totalShift) > 5000:
            player.rect.x = 120
            current_level = levelList[1]
            player.level = current_level
            player.rect.x = 10
            player.rect.y = 300 - player.rect.height

        for bullet in bullet_list:
            dino_hit_list = pygame.sprite.spritecollide(bullet, current_level.enemies, False)

            for dino in dino_hit_list:
                bullet_list.remove(bullet)
                all_sprite_list.remove(bullet)
                dino.health -= 10

                if dino.health == 0:
                    dino.kill_dino()
                    dino_dead = pygame.mixer.Sound('assets/sounds/dead.wav')
                    dino_dead.play()
                    #current_level.enemies.remove(dino)



        current_level.draw(screen)
        active_sprite_list.draw(screen)
        all_sprite_list.draw(screen)


        clock.tick(20)

        pygame.display.flip()

    pygame.quit()

    # level.Level1()

def level_switch(level, player, current_level, levelList):
    if level == 1:
        player.rect.x = 10
        player.rect.y = 300 - player.rect.height
        return levelList[0]
    elif level == 2:
        player.rect.x = 10
        player.rect.y = 300 - player.rect.height
        return levelList[1]

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()

