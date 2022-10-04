from random import randint, random
import pygame, settings

from math import floor

def player_move(dx, dy):
    '''Convenience function for player movement'''
    if settings.PLAYER.try_attack(
        settings.PLAYER.x + dx,
        settings.PLAYER.y + dy
    ) or settings.PLAYER.try_move(
        settings.PLAYER.x + dx,
        settings.PLAYER.y + dy
    ):
        do_turn()

def do_turn():
    for mon in settings.GAME.get_current_level().monsters:
        if mon is not settings.PLAYER:
            mon.turn_count += mon.speed / settings.PLAYER.speed * (random() + 0.5)
            while mon.turn_count >= 1:
                mon.turn_count -= 1
                do_move = True
                while do_move:
                    dx = randint(-1, 1)
                    dy = randint(-1, 1)
                    if dx == 0 and dy == 0:
                        continue

                    # Try to attack first
                    do_move = not mon.try_attack(mon.x + dx, mon.y + dy)
                    if do_move:
                        # If we can't attack, try to move
                        do_move = not mon.try_move(mon.x + dx, mon.y + dy)

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.DO_MAIN_LOOP = False
        
        if event.type == pygame.KEYDOWN:
            # Standard movement
            if event.key == pygame.K_w:
                player_move(0, -1)
            if event.key == pygame.K_s:
                player_move(0, 1)
            if event.key == pygame.K_a:
                player_move(-1, 0)
            if event.key == pygame.K_d:
                player_move(1, 0)

            # Diagonal movement
            if event.key == pygame.K_q:
                player_move(-1, -1)
            if event.key == pygame.K_e:
                player_move(1, -1)
            if event.key == pygame.K_z:
                player_move(-1, 1)
            if event.key == pygame.K_c:
                player_move(1, 1)
            
            # Holding still for a turn
            if event.key == pygame.K_x:
                do_turn()