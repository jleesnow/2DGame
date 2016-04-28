import pygame
import os
from pygame import *
import textrect
import level
from player import Player
from bullet import Bullet
from horse import Horse
from healthbar import Health
from time import sleep, time

def main():
    pygame.init()
    global screen, clock, current_level_num, current_level, rescuedHorse, horse_found_delay, customfont, health
    customfont = os.path.join('assets', 'custom.ttf')
    screen = pygame.display.set_mode([768, 399])
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    pygame.mixer.music.load('assets/sounds/lvl1music.mp3')
    pygame.mixer.music.play(-1)

    title_screen()

    player = Player()
    horse = Horse()
    health = Health(screen)

    levels = []
    levels.append(level.Level1(player))
    levels.append(level.Level2(player))

    current_level_num = 0
    current_level = levels[current_level_num]

    non_enemy_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    player.rect.x = 60
    player.rect.y = 300 - player.rect.height
    non_enemy_sprites.add(player)
    non_enemy_sprites.add(health)

    found_screen = False
    rescuedHorse = False
    horse_found_delay = 0
    damage_time = 0
    super_speed = False

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
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                    if player.direction == "L":
                        bullet = Bullet("left")
                        bullet.rect.x = player.rect.x + 20
                        bullet.rect.y = player.rect.y + 27
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                elif event.key == K_1:
                    current_level = level_switch(1, player, current_level, levels)
                    non_enemy_sprites.remove(horse)
                elif event.key == K_2:
                    current_level = level_switch(2, player, current_level, levels)
                    draw_horse(horse)
                    non_enemy_sprites.add(horse)
                elif event.key == K_F1:
                    menu()
                elif event.key == K_p:
                    super_speed = True
                    player.speed = 30
                elif event.key == K_ESCAPE:
                    pygame.quit()

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    right = False
                    idle = True
                elif event.key == K_LEFT:
                    left = False
                    idle = True
            else:
                idle = True


        non_enemy_sprites.update(left, right, up, down, idle)
        all_sprites.update()
        health.health_update(screen)

        current_level.update()

        player_move(player, horse)

        player_damage = pygame.sprite.spritecollide(player, current_level.enemies, False)
        for enemy in player_damage:
            if enemy.dead == False:
                if player_damage and (time()-damage_time > 1) and super_speed == False:
                    damage_time = time()
                    player.health -= 25
                    damaged = pygame.mixer.Sound('assets/sounds/impact.mp3')
                    damaged.play()
                    health.num_hearts -= 1
                    if player.health == 0:
                        game_over()

        if current_level_num == 1 and rescuedHorse == False:
            draw_horse(horse)
            non_enemy_sprites.add(horse)
            rescuedHorse = True
            horse_found_delay = 1

        if player.rect.x >= 720:
            pygame.time.wait(1000)
            right = False
            if current_level_num == 0:
                current_level_num = end_of_level_screen(player, levels)
            elif current_level_num == 1:
                end_of_game_screen(player, levels)

        for bullet in bullets:
            dino_hit_list = pygame.sprite.spritecollide(bullet, current_level.enemies, False)

            for dino in dino_hit_list:
                bullets.remove(bullet)
                all_sprites.remove(bullet)
                dino.health -= 10
                if dino.health == 0:
                    dino.kill_dino()
                    dino_dead = pygame.mixer.Sound('assets/sounds/dead.wav')
                    dino_dead.play()

        current_level.draw(screen, current_level_num)
        non_enemy_sprites.draw(screen)
        all_sprites.draw(screen)

        clock.tick(20)

        pygame.display.flip()

        if current_level_num == 1 and found_screen == False and horse_found_delay == 1:
            pygame.time.wait(2500)
            found_horse_screen()
            found_screen = True
            horse_found_delay += 1

    pygame.quit()

def player_move(player, horse):
    if player.rect.right >= 500 and current_level.totalShift < current_level.level_limit:
            diff = player.rect.right - 500
            player.rect.right = 500
            horse.rect.right = 455
            current_level.shift(-diff)

def level_switch(level, player, current_level, levelList):
    global current_level_num, health
    if level == 1:
        player.rect.x = 60
        player.rect.y = 300 - player.rect.height
        current_level.shift(-current_level.shifted)
        health.num_hearts = 3
        player.health = 75
        current_level_num = 0
        return levelList[0]
    elif level == 2:
        player.rect.x = 60
        player.rect.y = 300 - player.rect.height
        current_level.shift(-current_level.shifted)
        health.num_hearts = 3
        player.health = 75
        current_level_num = 1
        return levelList[1]

def title_screen():
    #customfont = os.path.join('assets', 'custom.ttf')
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan has got himself into a predicament. His horse wandered into a wormhole and got transported back in " \
        "time to the age of the dinosaurs. Of course Cowboy Dan had to follow to save his favorite horse.\n\nHelp Cowboy " \
        "Dan find his horse and get back to present day!\n\nPress ENTER to continue"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                done = True
        pygame.display.update()
        clock.tick(20)

def end_of_level_screen(player, levelList):
    global current_level
    font = pygame.font.Font(customfont, 36)
    title_string = "\n\nCowboy Dan has found another wormhole! What are the odds? Will this lead him to his horse?\n\n" \
                   "Press ENTER to continue"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                done = True

        player.rect.x = 120
        current_level = levelList[1]
        player.rect.x = 10
        player.rect.y = 300 - player.rect.height
        pygame.display.update()
        clock.tick(20)
    return 1

def end_of_game_screen(player, levelList):
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan has saved his horse and made it back to present day! Good job! \n\nThank you for playing! \n\nPress Esc to exit\nENTER to play again"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            elif event.type == KEYDOWN and event.key == K_RETURN:
                main()
                done = True
        pygame.display.update()
        clock.tick(20)
    pygame.quit()

def found_horse_screen():
    font = pygame.font.Font(customfont, 36)
    title_string = "Cowboy Dan has found his horse!\n\nHelp Cowboy " \
        "Dan get back to present day!\n\nPress ENTER to continue"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 0)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                done = True
        pygame.display.update()
        clock.tick(20)

def menu():
    font = pygame.font.Font(customfont, 36)
    title_string = "\nMove Cowboy Dan: arrow keys\n\nSwitch Levels: " \
    "1 and 2\n\nSuper Speed & Invincibility: P\n\nPress ENTER to return to game"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 2)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                done = True
        pygame.display.update()
        clock.tick(20)

def draw_horse(horse):
    horse.rect.x = 150
    horse.rect.y = 263

def game_over():
    pygame.time.wait(1000)
    font = pygame.font.Font(customfont, 36)
    title_string = "\n\nGAME OVER\n\nPress ENTER to try again\nEsc to exit"
    screen_rect = screen.get_rect()
    title = textrect.render_textrect(title_string, font, screen_rect, (255,255,255), 2)

    done = False
    while not done:
        screen.blit(title, (0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                main()
                done = True
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()

