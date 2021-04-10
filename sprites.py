import pygame
import spritesheets
import constants as cn

color_sheets = []

color_sheets.insert(cn.WHITE, spritesheets.spritesheet("sprites/white.png"))
color_sheets.insert(cn.RED, spritesheets.spritesheet("sprites/red.png"))
color_sheets.insert(cn.GREEN, spritesheets.spritesheet("sprites/green.png"))
color_sheets.insert(cn.BLUE, spritesheets.spritesheet("sprites/blue.png"))
color_sheets.insert(cn.CYAN, spritesheets.spritesheet("sprites/cyan.png"))
color_sheets.insert(cn.MAGENTA, spritesheets.spritesheet("sprites/magenta.png"))
color_sheets.insert(cn.YELLOW, spritesheets.spritesheet("sprites/yellow.png"))
color_sheets.insert(cn.GRAY, spritesheets.spritesheet("sprites/gray.png"))


def load_sprite(x, y, col, half_width=False):
    sheet = color_sheets[col]
    sprite = sheet.image_at((x*(half_width and 8 or 16), y*16, half_width and 8 or 16, 16))
    sprite = pygame.transform.scale(sprite, (cn.TILE_SCALE // (half_width and 2 or 1), cn.TILE_SCALE))
    return sprite
