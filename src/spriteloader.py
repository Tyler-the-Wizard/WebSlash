import pygame
import constants

SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16
TEXT_WIDTH = SPRITE_WIDTH // 2
TEXT_HEIGHT = SPRITE_HEIGHT

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
    
    def get_sprite(self, x, y, width, height):
        '''Automatically loads the image at the specified sprite coordinate.
        For x=0, y=2, will load image at x=0px, y=32px.'''
        rect = pygame.Rect(x * width, y * height, width, height)
        surf = pygame.Surface(rect.size).convert()
        surf.blit(self.sheet, (0, 0), rect)
        return surf

main_sheet = Spritesheet('assets/sprites.png')

def sprite(x, y):
    return pygame.transform.scale(main_sheet.get_sprite(x, y, SPRITE_WIDTH, SPRITE_HEIGHT), (constants.TILE_SCALE, constants.TILE_SCALE))
def text(x, y):
    return pygame.transform.scale(main_sheet.get_sprite(x, y, TEXT_WIDTH, TEXT_HEIGHT), (constants.TILE_SCALE // 2, constants.TILE_SCALE))