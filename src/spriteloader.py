import pygame
import constants

SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16
TEXT_WIDTH = SPRITE_WIDTH // 2
TEXT_HEIGHT = SPRITE_HEIGHT

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
    
    def get_sprite(self, x, y, width, height, color):
        '''Automatically loads the image at the specified sprite coordinate.
        For x=0, y=2, will load image at x=0px, y=32px.'''
        rect = pygame.Rect(x * width, y * height, width, height)
        surf = pygame.Surface(rect.size).convert()
        surf.blit(self.sheet, (0, 0), rect)
        surf = set_color(surf, color)
        surf.set_colorkey(constants.SPRITE_BG_COLOR, pygame.RLEACCEL)
        return surf

main_sheet = Spritesheet('assets/sprites.png')

def sprite(x, y, color):
    sprite = main_sheet.get_sprite(x, y, SPRITE_WIDTH, SPRITE_HEIGHT, color)
    sprite = pygame.transform.scale(sprite, (constants.TILE_SCALE, constants.TILE_SCALE))
    return sprite
def text(x, y):
    sprite = main_sheet.get_sprite(x, y, TEXT_WIDTH, TEXT_HEIGHT)
    sprite = pygame.transform.scale(sprite, (constants.TILE_SCALE // 2, constants.TILE_SCALE))
    return sprite

def set_color(sprite, color):
    new_sprite = pygame.Surface(sprite.get_size())
    new_sprite.fill(color)
    sprite.set_colorkey(constants.SPRITE_FG_COLOR)
    new_sprite.blit(sprite, (0, 0))
    return new_sprite