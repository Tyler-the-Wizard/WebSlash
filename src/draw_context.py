# This file defines several draw functions. These functions
# describe what state the game is in.

from math import floor

import constants
import settings

cam_x = 0
cam_y = 0

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

def standard_gameplay(surface):
    '''Draws a gameplay view to the surface.'''
    global cam_x, cam_y
    cam_goal_x = settings.PLAYER.x * settings.TILE_SCALE - settings.SCREEN_SIZE[0] * 2 // 5
    cam_goal_y = settings.PLAYER.y * settings.TILE_SCALE - settings.SCREEN_SIZE[1] // 2 + 200

    cam_x = floor(lerp(cam_x, cam_goal_x, constants.CAMERA_SHARPNESS))
    cam_y = floor(lerp(cam_y, cam_goal_y, constants.CAMERA_SHARPNESS))

    settings.GAME.get_current_level().draw(surface, (cam_x, cam_y))
