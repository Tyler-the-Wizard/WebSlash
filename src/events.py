import random

import colors
from message import new as say
import pygame
import settings
import spriteloader

def player_move(dx, dy):
    '''Convenience function for player movement'''
    if settings.PLAYER.try_attack(
        settings.PLAYER.x + dx,
        settings.PLAYER.y + dy
    ) or settings.PLAYER.try_move(
        settings.PLAYER.x + dx,
        settings.PLAYER.y + dy
    ):
        settings.PLAYER.turn_count += 1
        do_turn()

def do_turn():
    settings.PLAYER.do_regen()
    for mon in settings.GAME.get_current_level().monsters:
        if mon is not settings.PLAYER:
            mon.do_regen()
            mon.do_turn()
    settings.PLAYER.refresh_visibility()

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.DO_MAIN_LOOP = False

        if event.type == pygame.KEYDOWN:
            # Handle ctrl keys
            if pygame.key.get_mods() & pygame.KMOD_CTRL:
                if event.key == pygame.K_s:
                    settings.GAME.save_level()
                # Bow easter egg
                if event.key == pygame.K_b:
                    spriteloader.add_bow_to_sprite(settings.PLAYER.sprite)

            else:
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
                    # player gets 2x regen when holding still
                    settings.PLAYER.do_regen()
                    do_turn()

                # Debug print player pos
                if event.key == pygame.K_p:
                    print(f'p: {settings.PLAYER.x}, {settings.PLAYER.y}')

                # Debug add new message
                if event.key == pygame.K_m:
                    say('Message: ' + str(random.randint(1, 1000)))

                # Debug change color palette
                if event.key == pygame.K_r:
                    colors.load_palette(1)
