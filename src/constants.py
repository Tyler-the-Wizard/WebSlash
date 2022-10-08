import pygame

FPS = 60

# Converts between tile index and actual tile coordinates.
TILE_DICT = [(i + 1, 26) for i in range(17)]
TILE_DICT[0] = (15, 6)

# Color enum for colors.py
C_BG = 0
C_FG = 1
C_RED = 2
C_YELLOW = 3
C_GREEN = 4
C_BLUE = 5
C_CYAN = 6
C_MAGENTA = 7

C_GRAY = 8
C_LIGHT_GRAY = 9
C_PINK = 10
C_ORANGE = 11
C_LIGHT_GREEN = 12
C_DEEP_BLUE = 13
C_SKY_BLUE = 14
C_PURPLE = 15

# Collision bitmask for tiles.py
CL_NONE = 0
CL_WALL = 1
CL_WATER = 2

# Constants used to know what colors to
# replace on the spritesheet
SPRITE_BG_COLOR = pygame.Color(17, 17, 51)
SPRITE_FG_COLOR = pygame.Color(238, 238, 204)
SPRITE_EMPTY_FG_COLOR = pygame.Color(51, 51, 85)

# 0-1. lower number means lazier camera
CAMERA_SHARPNESS = 0.14
