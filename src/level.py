import colors
import constants
import spriteloader

# This class is under construction and the level-related
# functions will eventually be moved into the Level class.

class Level:
    '''A Level object represents a single level
    of the dungeon, complete with a map of the
    actual tiles, a list of all items, and a
    list of all monsters on the level.'''
    def __init__(self):
        self.tilemap = []
        self.items = []
        self.monsters = []

    def draw(self, surface):
        # Draw the tilemap
        for x, row in enumerate(self.tilemap):
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

        # Draw each item

        # Draw each monster
        for monster in self.monsters:
            monster.draw(surface)

def load(filename) -> Level:
    '''Loads a level from a file.'''
    file = open(filename)
    data = file.read()
    file.close()

    tilemap = [[int(cell) for cell in row.split(' ')] for row in data.split('\n')]

    level = Level()
    level.tilemap = tilemap
    return level

def save(level, filename) -> None:
    '''Saves a level into a file.'''
    data = '\n'.join([' '.join([str(cell) for cell in row]) for row in level.tilemap])

    file = open(filename, 'w')
    file.write(data)
    file.close()