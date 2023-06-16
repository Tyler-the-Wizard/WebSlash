import pygame

from colors import palette_color as color
import constants
import settings
import spriteloader

letters = {}

# Uppercase
for char in range(ord('A'), ord('Z') + 1):
    letters[char] = spriteloader.text(4 + char - ord('A'), 60)

# Lowercase
for char in range(ord('a'), ord('z') + 1):
    letters[char] = spriteloader.text(4 + char - ord('a'), 62)

# Numbers
for char in range(ord('0'), ord('9') + 1):
    letters[char] = spriteloader.text(4 + char - ord('0'), 59)

# Punctuation
for i, symbol in enumerate('#%&@$.,!?:;\'"()[]*/\\+-<=> '):
    letters[ord(symbol)] = spriteloader.text(4 + i, 64)

def write(surface, x, y, text, scale=settings.TILE_SCALE, color=color(constants.C_FG)):
    'Draws the provided text on the surface.'
    for i, char in enumerate(text):
        sprite = letters[ord(char)]
        sprite = pygame.transform.scale(sprite, (scale // 2, scale))
        sprite = spriteloader.set_color(sprite, color, constants.SPRITE_FG_COLOR)

        surface.blit(sprite, (x + i * scale // 2, y))