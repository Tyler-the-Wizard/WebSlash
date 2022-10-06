import settings
settings.init()

import pygame
import sys
pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)

fps_clock = pygame.time.Clock()

import colors
import constants
import events
import game
import monsters
import player

# TODO implement saving and loading of Games
settings.GAME = game.Game()
settings.GAME.new_level()
settings.GAME.current_level = 0

# TEST CODE
player.make_player(1, 1)

monsters.factory('goblin', 10, 10)
monsters.factory('golem', 11, 10)
monsters.factory('snake', 12, 10)

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())
    screen.fill(colors.palette_color(constants.C_BG))

    settings.CURRENT_DRAW_CONTEXT(screen)
    
    pygame.display.flip()
    fps_clock.tick(constants.FPS)

pygame.quit()
sys.exit(0)
