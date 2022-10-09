import monsters
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

# Loading and saving of Levels

def load_tilemap(rows, loaded_data):
    tile_array = [row.split(' ') for row in rows]
    # Remove empty lines
    tile_array = [row for row in tile_array if len(row) > 1 and row[0] != '']
    # Hack to rotate the tile array
    tile_array = list(zip(*tile_array))
    tilemap = tiles.Tilemap(tile_array)

    loaded_data['tilemap'] = tilemap

def save_tilemap():
    return ''

def load_monsters(rows, loaded_data):
    loaded_data['monsters'] = []
    for row in rows:
        if len(row) > 0:
            attrs = row.split(' ')
            mon = monsters.factory(
                attrs[0],
                int(attrs[1]),
                int(attrs[2])
            )
            loaded_data['monsters'].append(mon)

def save_monsters():
    return ''

def load_items(rows, loaded_data):
    pass

def save_items():
    return ''

def load_info(rows, loaded_data):
    loaded_data['info'] = {}
    for row in rows:
        if len(row) > 0:
            kv = row.split(' ')
            if kv[0] == 'depth':
                loaded_data['info']['depth'] = int(kv[1])

def save_info():
    return ''

file_format_dict = {
    'TILEMAP': (load_tilemap, save_tilemap),
    'MONSTERS': (load_monsters, save_monsters),
    'ITEMS': (load_items, save_items),
    'INFO': (load_info, save_info)
}

def load(filename) -> Level:
    '''Loads a level from a file.'''
    file = open(filename)
    data = file.read()
    file.close()

    # Separate by section
    loaded_data = {}
    for section in data.split('!'):
        rows = section.split('\n')
        if rows[0] in file_format_dict.keys():
            file_format_dict[rows[0]][0](rows[1:], loaded_data)

    return Level(
        loaded_data['tilemap'],
        [],
        loaded_data['monsters'],
        loaded_data['info']['depth']
    )

def save(level, filename) -> None:
    '''Saves a level into a file.'''
    # TODO This function will not work with current Tilemap class
    data = '\n'.join([' '.join([str(cell) for cell in row]) for row in level.tilemap])

    file = open(filename, 'w')
    file.write(data)
    file.close()
