import pygame
from pygame import *
import textrect
import level
from player import Player
from bullets import Bullet
from horse import Horse

def main():
    pygame.init()
    global screen, clock, current_level_no, current_level, rescued, i
    screen = pygame.display.set_mode([768, 399])
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    rescued = False
    i = 0

    title_screen()

    player = Player()
    horse = Horse()

    levelList = []
    levelList.append(level.Level1(player))
    levelList.append(level.Level2(player))

    current_level_no = 0
    current_level = levelList[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    bullet_list = pygame.sprite.Group()
    all_sprite_list = pygame.sprite.Group()

    player.rect.x = 60
    player.rect.y = 300 - player.rect.height
    active_sprite_list.add(player)

    found_screen = False

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

        if current_level_no == 1 and rescued == False:
            horse.rect.x = 150
            horse.rect.y = 263
            active_sprite_list.add(horse)
            rescued = True
            i = 1


        ##################
        if player.rect.right >= 500 and current_level.totalShift < current_level.level_limit:
            diff = player.rect.right - 500
            diff1 = horse.rect.right - 500
            player.rect.right = 500
            horse.rect.right = 455
            current_level.shift(-diff)

        # this offsets at the beginning
        # if player.rect.right <= 120:
        #     diff = 120 - player.rect.left
        #     player.rect.left = 120
        #     current_level.shift(diff)
        ##################

        if player.rect.x >= 720:
            pygame.time.wait(1000)
            if current_level_no == 0:
                right = False
                current_level_no = end_of_level_screen(player, levelList)
            elif current_level_no == 1:
                right = False
                end_of_game_screen(player, levelList)

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



        current_level.draw(screen, current_level_no)
        active_sprite_list.draw(screen)
        all_sprite_list.draw(screen)


        clock.tick(20)

        pygame.display.flip()

        if current_level_no == 1 and found_screen == False and i == 1:
            pygame.time.wait(2500)
            found_horse_screen()
            found_screen = True
            i += 1

    pygame.quit()

    # level.Level1()

def level_switch(level, player, current_level, levelList):
    if level == 1:
        player.rect.x = 10
        player.rect.y = 300 - player.rect.height
        global current_level_no
        current_level_no = 0
        return levelList[0]
    elif level == 2:
        player.rect.x = 10
        player.rect.y = 300 - player.rect.height
        global current_level_no
        current_level_no = 1
        return levelList[1]

def title_screen():
    customfont = "C:/Users/Jay/Desktop/Programming Assignments/321/2DFinal - Copy/assets/custom.ttf"
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan has got himself into a predicament. His horse wandered into a wormhole and got transported back in " \
        "time to the age of the dinosaurs. Of course Cowboy Dan had to follow to save his favorite horse.\n\nHelp Cowboy " \
        "Dan find his horse and get back to present day!\n\nPress Enter to continue"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_KP_ENTER:
                done = True
        pygame.display.update()
        clock.tick(20)

def end_of_level_screen(player, levelList):
    global current_level
    customfont = "C:/Users/Jay/Desktop/Programming Assignments/321/2DFinal - Copy/assets/custom.ttf"
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan found another wormhole! Will this lead him to his horse?"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_KP_ENTER:
                done = True

        player.rect.x = 120
        current_level = levelList[1]
        player.level = current_level
        player.rect.x = 10
        player.rect.y = 300 - player.rect.height
        pygame.display.update()
        clock.tick(20)
    return 1

def end_of_game_screen(player, levelList):
    customfont = "C:/Users/Jay/Desktop/Programming Assignments/321/2DFinal - Copy/assets/custom.ttf"
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan has saved his horse and made it back to present day! Good job! \n\nThank you for playing! \n\nPress Enter to exit"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_KP_ENTER:
                done = True
        pygame.display.update()
        clock.tick(20)
    pygame.quit()

def found_horse_screen():
    customfont = "C:/Users/Jay/Desktop/Programming Assignments/321/2DFinal - Copy/assets/custom.ttf"
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan has found his horse!\n\nHelp Cowboy " \
        "Dan get back to present day!\n\nPress Enter to continue"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_KP_ENTER:
                done = True
        pygame.display.update()
        clock.tick(20)


if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()

