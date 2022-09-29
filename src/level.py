import colors
import constants
import spriteloader

def draw_level(level, surface):
    '''Draws the passed level onto the surface.
    A level is a list of numbers which correspond
    to the indices in constants.TILE_DICT.'''
    for x, row in enumerate(level):
        for y, i in enumerate(row):
            (sprite_x, sprite_y) = constants.TILE_DICT[i]
            tile_sprite = spriteloader.sprite(
                sprite_x,
                sprite_y,
                colors.palette_color(constants.LIGHT_GRAY)
            )

            surface.blit(
                tile_sprite,
                (x * constants.TILE_SCALE, y * constants.TILE_SCALE)
            )

def load(filename) -> list[list[int]]:
    '''Loads a level from a file.'''
    file = open(filename)
    data = file.read()
    file.close()

    return [[int(cell) for cell in row.split(' ')] for row in data.split('\n')]

def save(level, filename) -> None:
    '''Saves a level into a file.'''
    data = '\n'.join([' '.join([str(cell) for cell in row]) for row in level])

    file = open(filename, 'w')
    file.write(data)
    file.close()