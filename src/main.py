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

cam_x = 0
cam_y = 0

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

import colors
import constants
import events
import game
from math import floor
import message
import player
import status

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
surf_info = pygame.Surface((settings.SCREEN_SIZE[0] * 4 // 5 - (padding * 2), 200 - padding))
surf_game = pygame.Surface((settings.SCREEN_SIZE[0] * 4 // 5 - (padding * 2), settings.SCREEN_SIZE[1] - 300 - (padding * 2)))
surf_stat = pygame.Surface((settings.SCREEN_SIZE[0] * 4 // 5 - (padding * 2), 100 - padding))
surf_inv = pygame.Surface((settings.SCREEN_SIZE[0] // 5 - padding, settings.SCREEN_SIZE[1] - (padding * 2)))

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())

    # screen.fill((0, 0, 0))
    surf_info.fill(colors.palette_color(constants.C_BG))
    surf_game.fill(colors.palette_color(constants.C_BG))
    surf_stat.fill(colors.palette_color(constants.C_BG))
    surf_inv.fill(colors.palette_color(constants.C_BG))

    message.draw(surf_info)
    status.draw(surf_stat)

    # Draw gameplay view
    cam_goal_x = settings.PLAYER.x * settings.TILE_SCALE - settings.SCREEN_SIZE[0] * 2 // 5
    cam_goal_y = settings.PLAYER.y * settings.TILE_SCALE - settings.SCREEN_SIZE[1] // 2 + 200

    cam_x = floor(lerp(cam_x, cam_goal_x, constants.CAMERA_SHARPNESS))
    cam_y = floor(lerp(cam_y, cam_goal_y, constants.CAMERA_SHARPNESS))

    settings.GAME.get_current_level().draw(surf_game, (cam_x, cam_y))

    # Blit all surfaces and display
    screen.blit(surf_info, (padding, padding))
    screen.blit(surf_game, (padding, 200 + padding))
    screen.blit(surf_stat, (padding, settings.SCREEN_SIZE[1] - 100))
    screen.blit(surf_inv, (settings.SCREEN_SIZE[0] * 4 // 5, padding))

    pygame.display.flip()
    fps_clock.tick(constants.FPS)

pygame.quit()
sys.exit(0)
