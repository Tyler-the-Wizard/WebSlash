from colors import palette_color as color
import constants
import spriteloader

def get_sprite_from_char(char, color):
    char = ord(char)

    if ord('A') <= char <= ord('Z'):
        return spriteloader.text(4 + char - ord('A'), 60, color)

def write(surface, x, y, text, font_size=12, color=color(constants.C_FG)):
    'Draws the provided text on the surface.'
    for i, char in enumerate(text):
        sprite = get_sprite_from_char(char, color)
        surface.blit(sprite, (x + i * 32, y))