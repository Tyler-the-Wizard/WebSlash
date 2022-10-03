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

# TEST CODE
test_level = level.load('levels/big.dat')
settings.CURRENT_LEVEL = test_level

# TEST CODE
test_mon = monsters.Monster()
settings.CURRENT_LEVEL.monsters.append(test_mon)
settings.PLAYER = test_mon

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())

    screen.fill(colors.palette_color(constants.C_BG))

    settings.CURRENT_DRAW_CONTEXT(screen)
    
    pygame.display.flip()
    fps_clock.tick(constants.FPS)