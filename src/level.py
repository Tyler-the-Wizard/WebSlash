import constants
import tiles

# This class is under construction and the level-related
# functions will eventually be moved into the Level class.

class Level:
    '''A Level object represents a single level
    of the dungeon, complete with a map of the
    actual tiles, a list of all items, and a
    list of all monsters on the level.'''
    def __init__(self, tilemap, items, monsters):
        self.tilemap = tilemap
        self.items = items
        self.monsters = monsters

    def draw(self, surface, camera=(0, 0)):
        # Draw the tilemap
        self.tilemap.draw(surface, camera)

        # Draw each item

        # Draw each monster
        for monster in self.monsters:
            monster.draw(surface, camera)

def load(filename) -> Level:
    '''Loads a level from a file.'''
    file = open(filename)
    data = file.read()
    file.close()

    tilemap = tiles.Tilemap([[int(cell) for cell in row.split(' ')] for row in data.split('\n')])
    return Level(tilemap, [], [])

def save(level, filename) -> None:
    '''Saves a level into a file.'''
    data = '\n'.join([' '.join([str(cell) for cell in row]) for row in level.tilemap])

    file = open(filename, 'w')
    file.write(data)
    file.close()