import settings
settings.init()

import pygame
pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)

fps_clock = pygame.time.Clock()

import colors
import constants
import events
import monsters
import level

test_mon = monsters.Monster()
settings.GAME_MONSTERS.append(test_mon)

test_level = level.load('levels/small.dat')

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())

    screen.fill(colors.palette_color(constants.BG))
    # for tile in settings.GAME_TILES:
    #     pass
    level.draw_level(test_level, screen)
    for monster in settings.GAME_MONSTERS:
        monster.draw(screen)
    for item in settings.GAME_ITEMS:
        pass
    
    pygame.display.flip()
    fps_clock.tick(constants.FPS)