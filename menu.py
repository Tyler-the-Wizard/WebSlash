import button
import constants
import player
import pygame
import settings
import text

def draw_menu(surface):
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
        200, 100, 800, 70
    ))
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        210, 110, 780, 50
    ))
    text.write("Welcome to WebSlash!", surface, 470, 120)

    start_button = pygame.Rect(450, 400, 300, 70)
    quit_button = pygame.Rect(450, 500, 300, 70)

    pygame.draw.rect(surface, (255, 255, 255), start_button)
    pygame.draw.rect(surface, (255, 255, 255), quit_button)
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        460, 410, 280, 50
    ))
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        460, 510, 280, 50
    ))

    text.write("Start", surface, 565, 420)
    text.write("Quit", surface, 570, 520)

    if settings.game_state == constants.FIRST_TIME:
        # Register buttons
        settings.buttons.append(button.Button(start_button, build_character))
        settings.buttons.append(button.Button(quit_button, quit_game))
        settings.game_state = constants.MAIN_MENU


def quit_game(_):
    settings.game_state = constants.QUIT

def build_character(_):
    while len(settings.buttons):
        my_button = settings.buttons.pop()
        del my_button

    settings.game_state = constants.NAME_CHARACTER

def draw_character_namer(surface):
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
        400, 105, 500, 54
    ))
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        402, 107, 496, 50
    ))
    text.write("Your name: " + settings.player.name + "_",
        surface, 470, 120)

def draw_character_builder(surface):
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
        400, 105, 400, 54
    ))
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        402, 107, 396, 50
    ))

    name_and_class = settings.player.name + " the " + player.get_class_name(
        settings.player.str,
        settings.player.dex,
        settings.player.wis
    )

    text.write(name_and_class, surface, 700 - len(name_and_class) * 12, 120)

    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
        500, 255, 200, 214
    ))
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        502, 257, 196, 210
    ))

    text.write("STR: " + str(settings.player.str)
    , surface, 555, 280)
    text.write("DEX: " + str(settings.player.dex)
    , surface, 555, 320)
    text.write("WIS: " + str(settings.player.wis)
    , surface, 555, 360)

    spare_points = 30 - settings.player.str - settings.player.dex - settings.player.wis

    text.write("Q", surface, 520, 280, settings.player.str == 6)
    text.write("A", surface, 520, 320, settings.player.dex == 6)
    text.write("Z", surface, 520, 360, settings.player.wis == 6)

    text.write("W", surface, 670, 280, spare_points == 0 or settings.player.str == 18)
    text.write("S", surface, 670, 320, spare_points == 0 or settings.player.dex == 18)
    text.write("X", surface, 670, 360, spare_points == 0 or settings.player.wis == 18)

    text.write("Points: " + str(spare_points), surface, 520, 430)

    start_button = pygame.Rect(450, 500, 300, 70)
    pygame.draw.rect(surface, (255, 255, 255), start_button)
    pygame.draw.rect(surface, constants.COLOR_BG, pygame.Rect(
        460, 510, 280, 50
    ))
    text.write("Start", surface, 570, 520)


def input_handler(event):
    spare_points = 30 - settings.player.str - settings.player.dex - settings.player.wis

    if event.key == pygame.K_q and settings.player.str > 6:
        settings.player.str -= 1
    if event.key == pygame.K_a and settings.player.dex > 6:
        settings.player.dex -= 1
    if event.key == pygame.K_z and settings.player.wis > 6:
        settings.player.wis -= 1

    if event.key == pygame.K_w and settings.player.str < 18 and spare_points > 0:
        settings.player.str += 1
    if event.key == pygame.K_s and settings.player.dex < 18 and spare_points > 0:
        settings.player.dex += 1
    if event.key == pygame.K_x and settings.player.wis < 18 and spare_points > 0:
        settings.player.wis += 1