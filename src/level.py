import tiles

class Level:
    '''A Level object represents a single level
    of the dungeon, complete with a map of the
    actual tiles, a list of all items, and a
    list of all monsters on the level.'''
    def __init__(self, tilemap, items, monsters, depth):
        self.tilemap = tilemap
        self.items = items
        self.monsters = monsters
        self.depth = depth

    def draw(self, surface, camera=(0, 0)):
        # Draw the tilemap
        self.tilemap.draw(surface, camera)

        # Draw each item

        # Draw each monster
        for monster in self.monsters:
            monster.draw(surface, camera)

# TODO Level file format needs to include monsters, items, depth, name? in the file

def load(filename, depth=0) -> Level:
    '''Loads a level from a file.'''
    file = open(filename)
    data = file.read()
    file.close()

    # Get rid of empty lines in the file
    rows = [row for row in data.split('\n') if len(row) > 0]

    tile_array = [[int(cell) for cell in row.split(' ')] for row in rows]
    # Hack to rotate the tile array
    tile_array = list(zip(*tile_array))
    tilemap = tiles.Tilemap(tile_array)

    return Level(tilemap, [], [], depth)

def save(level, filename) -> None:
    '''Saves a level into a file.'''
    # TODO This function will not work with current Tilemap class
    data = '\n'.join([' '.join([str(cell) for cell in row]) for row in level.tilemap])

    file = open(filename, 'w')
    file.write(data)
    file.close()
