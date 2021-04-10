import pygame

import constants
import equip
import grid
import input_handler
import inv
import level
import menu
import player
import text
import settings

pygame.init()
settings.init()

size = (1200, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('WebSlash 4.0')

surface_messages = pygame.Surface((790, 90))
surface_grid = pygame.Surface((790, 480))
surface_inv = pygame.Surface((380, 390))
surface_equip = pygame.Surface((380, 180))

surface_dialog_cover = pygame.Surface(size)
surface_dialog_cover.set_alpha(128)
surface_dialog_cover.fill((0, 0, 0))

is_inv = False
mouse_down = False

running = True
# main game loop
while running:
    screen.fill((0, 0, 0))

    if settings.game_state == constants.QUIT:
        running = False

    if settings.game_state == constants.MAIN_MENU or settings.game_state == constants.FIRST_TIME:
        menu.draw_menu(screen)
        pygame.display.flip()
    elif settings.game_state == constants.START:
        # Do some cleanup real quick
        while len(settings.buttons):
            my_button = settings.buttons.pop()
            del my_button

        level.init()
        inv.init()

        settings.game_state = constants.GAMEPLAY

    elif settings.game_state == constants.NAME_CHARACTER:
        menu.draw_character_namer(screen)
        pygame.display.flip()
    elif settings.game_state == constants.BUILD_CHARACTER:
        menu.draw_character_builder(screen)
        pygame.display.flip()

    elif settings.game_state == constants.GAMEPLAY:
        surface_messages.fill(constants.COLOR_BG)
        surface_grid.fill(constants.COLOR_BG)
        surface_inv.fill(constants.COLOR_BG)
        surface_equip.fill(constants.COLOR_BG)

        # Draw messages
        text.draw_messages(surface_messages)

        screen.blit(surface_messages, (10, 10))

        # Draw grid
        grid.draw_grid(settings.grid, surface_grid)
        for v in settings.tiles:
            v.draw(surface_grid)
        for v in settings.item_stacks:
            v.draw(surface_grid)
        for v in settings.monsters:
            v.draw(surface_grid)

        screen.blit(surface_grid, (10, 110))

        # Draw inv
        pygame.draw.rect(surface_inv, (0, 0, 0),
            pygame.Rect(170, 0, 5, 40))
        if is_inv:
            inv.draw_inv(settings.player.inv, surface_inv)
        else:
            player.draw_stats(settings.player, surface_inv)

        screen.blit(surface_inv, (810, 10))

        # Draw equip
        equip.draw_equip(surface_equip)

        screen.blit(surface_equip, (810, 410))

        # If we have a dialog, draw it
        if settings.dialog_busy:
            screen.blit(surface_dialog_cover, (0, 0))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250, 200,
                (len(settings.dialog_message) * 13) + 100, 120))
            pygame.draw.rect(screen, constants.COLOR_BG, pygame.Rect(260, 210,
                (len(settings.dialog_message) * 13) + 80, 100))
            text.write(settings.dialog_message, screen, 300, 250)

        pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If busy (popup), we don't process any more events.
        if settings.dialog_busy:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                settings.dialog_busy = False

                # UGLY HACK
                if settings.player.hp <= 0:
                    old_player = settings.player
                    settings.item_stacks.clear()
                    settings.monsters.clear()

                    settings.player = player.Player()
                    settings.monsters.append(settings.player)

                    settings.game_state = constants.FIRST_TIME
        else:
            if event.type == pygame.KEYDOWN:
                if settings.game_state == constants.GAMEPLAY:
                    input_handler.handle(event)
                    # special case since this happens at game level
                    if event.key == pygame.K_SLASH:
                        is_inv = not is_inv
                elif settings.game_state == constants.BUILD_CHARACTER:
                    menu.input_handler(event)

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if settings.game_state == constants.NAME_CHARACTER:
                    text.read_player_inputs(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_down:
                mouse_down = True
                for button in settings.buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.fun(button.args)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouse_down:
                mouse_down = False
