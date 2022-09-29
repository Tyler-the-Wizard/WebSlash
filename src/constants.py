import pygame

FPS = 60

# Converts between tile index and actual tile coordinates.
TILE_DICT = [(i + 1, 26) for i in range(17)]

# Color indices for colors.py
BG = 0
FG = 1
RED = 2
YELLOW = 3
GREEN = 4
BLUE = 5
CYAN = 6
MAGENTA = 7

GRAY = 8
LIGHT_GRAY = 9
PINK = 10
ORANGE = 11
LIGHT_GREEN = 12
DEEP_BLUE = 13
SKY_BLUE = 14
PURPLE = 15

SPRITE_BG_COLOR = pygame.Color(17, 17, 51)
SPRITE_FG_COLOR = pygame.Color(238, 238, 204)
TILE_SCALE = 80