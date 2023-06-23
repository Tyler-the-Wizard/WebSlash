import zlib

import items
import monsters
import settings
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
        for item in self.items:
            # Only draw item if player has seen that tile before
            #
            # NOTE not a correct solution... what if items are
            # added/removed to a square player has seen before,
            # but this happens when they are not looking??? Will
            # need more sophisticated tracking of state
            if self.tilemap.tiles[item.x][item.y].seen:
                item.draw(surface, camera)

        # Draw each monster
        for monster in self.monsters:
            if settings.PLAYER.los(monster.x, monster.y):
                monster.draw(surface, camera)

# Loading and saving of Levels

def load_tilemap(rows, level_data):
    tile_array = [row.split(' ') for row in rows]
    # Remove empty lines
    tile_array = [row for row in tile_array if len(row) > 1 and row[0] != '']
    # Hack to rotate the tile array
    tile_array = list(zip(*tile_array))
    tilemap = tiles.Tilemap(tile_array)

    level_data['tilemap'] = tilemap

def save_tilemap(level_data):
    return_string = ''
    tiles = level_data['tilemap'].tiles
    for row in tiles:
        for tile in row:
            tile_data = f'\
                {tile.sprite_index}\
                {tile.collision}\
                {tile.blocks_sight and 1 or 0}\
                {tile.seen and 1 or 0}\
            '
            return_string += ','.join(tile_data.split()) + ' '
        return_string += '\n'

    return return_string

def load_monsters(rows, level_data):
    level_data['monsters'] = []
    for row in rows:
        if len(row) > 0:
            attrs = row.split(' ')
            mon = monsters.factory(
                attrs[0],
                int(attrs[1]),
                int(attrs[2])
            )

            # Check to see if there is extra data on this monster
            if len(attrs) > 3:
                mon.display_name = attrs[3]
                mon.speed = int(attrs[4])
                mon.max_hp = int(attrs[5])
                mon.hp = int(attrs[6])
                mon.collision = int(attrs[7])
                mon.turn_count = float(attrs[8])

            level_data['monsters'].append(mon)

def save_monsters(level_data):
    return_string = ''
    for mon in level_data['monsters']:
        if mon.mon_name == 'player':
            continue

        mon_data = f'\
            {mon.mon_name}\
            {mon.x}\
            {mon.y}\
            {mon.display_name}\
            {mon.speed}\
            {mon.max_hp}\
            {mon.hp}\
            {mon.collision}\
            {mon.turn_count}\
        '
        return_string += ' '.join(mon_data.split()) + '\n'

    return return_string

def load_items(rows, level_data):
    level_data['items'] = []
    for row in rows:
        if len(row) > 0:
            attrs = row.split(' ')
            item = items.factory(
                attrs[0],
                int(attrs[1]),
                int(attrs[2])
            )

            # Check to see if there is extra data on ihis item
            if len(attrs) > 3:
                item.display_name = attrs[3]
                item.count = int(attrs[4])
                item.weight = int(attrs[5])
                item.process_usages(attrs[6])

            level_data['items'].append(item)

def save_items(level_data):
    return_string = ''
    for item in level_data['items']:
        item_data = f'\
            {item.item_name}\
            {item.x}\
            {item.y}\
            {item.display_name}\
            {item.count}\
            {item.weight}\
            {item.get_usages()}\
        '

        return_string += ' '.join(item_data.split()) + '\n'

    return return_string

def load_info(rows, level_data):
    level_data['info'] = {}
    for row in rows:
        if len(row) > 0:
            kv = row.split(' ')
            if kv[0] == 'depth':
                level_data['info']['depth'] = int(kv[1])

def save_info(level_data):
    return_string = ''
    for key in level_data['info'].keys():
        return_string += key + ' ' + str(level_data['info'][key])

    return return_string

file_format_dict = {
    'TILEMAP': (load_tilemap, save_tilemap),
    'MONSTERS': (load_monsters, save_monsters),
    'ITEMS': (load_items, save_items),
    'INFO': (load_info, save_info)
}

def load(filename) -> Level:
    '''Loads a level from a file.'''
    file = open(filename, 'rb')
    data = zlib.decompress(file.read()).decode()
    file.close()

    # Separate by section
    level_data = {}
    for section in data.split('!'):
        rows = section.split('\n')
        if rows[0] in file_format_dict.keys():
            file_format_dict[rows[0]][0](rows[1:], level_data)

    return Level(
        level_data['tilemap'],
        level_data['items'],
        level_data['monsters'],
        level_data['info']['depth']
    )

def save(level, filename) -> None:
    '''Saves a level into a file.'''
    data = ''
    level_data = {
        'tilemap': level.tilemap,
        'items': level.items,
        'monsters': level.monsters,
        'info': {
            'depth': level.depth
        }
    }

    for section_name in file_format_dict.keys():
        data += '!' + section_name + '\n'
        data += file_format_dict[section_name][1](level_data)
        data += '\n'

    file = open(filename, 'wb')
    file.write(zlib.compress(data.encode()))
    file.close()
