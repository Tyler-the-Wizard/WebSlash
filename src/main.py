import settings
settings.init()

import pygame
import sys
pygame.init()

# Get display resolution
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

settings.SCREEN_SIZE = (screen_width // 3 * 2, screen_height // 3 * 2)
settings.TILE_SCALE = max(screen_width, screen_height) // 50

screen = pygame.display.set_mode(settings.SCREEN_SIZE)

fps_clock = pygame.time.Clock()

import colors
import constants
import events
import game
import monsters
import player
import text

# TODO implement saving and loading of Games
settings.GAME = game.Game()
settings.GAME.new_level()
settings.GAME.current_level = 0

player_start_x = 10
player_start_y = 10
settings.GAME.get_current_level().monsters.append(
    player.make_player(player_start_x, player_start_y)
)

padding = 10

# Set up canvas
surf_info = pygame.Surface((settings.SCREEN_SIZE[0] * 4 // 5 - (padding * 2), 200 - (padding * 2)))
surf_game = pygame.Surface((settings.SCREEN_SIZE[0] * 4 // 5 - (padding * 2), settings.SCREEN_SIZE[1] - 300 - (padding * 2)))
surf_stat = pygame.Surface((settings.SCREEN_SIZE[0] * 4 // 5 - (padding * 2), 100 - (padding * 2)))
surf_inv = pygame.Surface((settings.SCREEN_SIZE[0] // 5 - (padding * 2), settings.SCREEN_SIZE[1] - (padding * 2)))

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())

    # screen.fill((0, 0, 0))
    surf_info.fill(colors.palette_color(constants.C_BG))
    surf_game.fill(colors.palette_color(constants.C_BG))
    surf_stat.fill(colors.palette_color(constants.C_BG))
    surf_inv.fill(colors.palette_color(constants.C_BG))

    # Test message
    text.write(surf_info, 0, 0, 'HELLO')

    settings.CURRENT_DRAW_CONTEXT(surf_game)

    # Blit all surfaces and display
    screen.blit(surf_info, (padding, padding))
    screen.blit(surf_game, (padding, 200 + padding))
    screen.blit(surf_stat, (padding, settings.SCREEN_SIZE[1] - 100 + padding))
    screen.blit(surf_inv, (settings.SCREEN_SIZE[0] * 4 // 5 + padding, padding))

    pygame.display.flip()
    fps_clock.tick(constants.FPS)

pygame.quit()
sys.exit(0)
