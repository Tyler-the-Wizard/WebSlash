import settings
settings.init()

import pygame
pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)

fps_clock = pygame.time.Clock()

import colors
import constants
import events
import game
import monsters
import level

# TODO implement saving and loading of Games
settings.GAME = game.Game()
settings.GAME.new_level()
settings.GAME.current_level = 0

# TEST CODE
player = monsters.factory('player', 1, 1)
settings.PLAYER = player # TODO implement Player subclass of Monster

# Add some monsters to play with
monsters.factory('goblin', 2, 2)
monsters.factory('golem', 3, 3)
monsters.factory('snake', 4, 4)

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())
    screen.fill(colors.palette_color(constants.C_BG))

    settings.CURRENT_DRAW_CONTEXT(screen)
    
    pygame.display.flip()
    fps_clock.tick(constants.FPS)