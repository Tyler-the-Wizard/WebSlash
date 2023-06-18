from enum import Enum
from random import choice, randint
import zlib

from generator import monsters

class Generator_Configuration:
    def __init__(self, width, height, num_room_tries, max_room_size, min_room_size, extra_connectors_rarity):
            self.width = width
            self.height = height
            self.num_room_tries = num_room_tries
            self.max_room_size = max_room_size
            self.min_room_size = min_room_size
            self.extra_connectors_rarity = extra_connectors_rarity

            if self.width % 2 == 0:
                self.width -= 1
            if self.height % 2 == 0:
                self.height -= 1
            if self.max_room_size % 2 == 0:
                self.max_room_size -= 1
            if self.min_room_size % 2 == 0:
                self.min_room_size -= 1

class Maze_Tile:
    def __init__(self):
        self.is_carveable = True

# directions:
# 0 = up
# 1 = right
# 2 = down
# 3 = left
def go_dir(x, y, direction):
    match direction:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    return x, y

class Maze:
    def __init__(self, width, height, new_level):
        self.maze_array = [[Maze_Tile() for _ in range(width)] for _ in range(height)]
        # Make bounds of maze uncarveable
        for y in range(height):
            self.maze_array[y][0].is_carveable = False
            self.maze_array[y][width - 1].is_carveable = False
        for x in range(width):
            self.maze_array[0][x].is_carveable = False
            self.maze_array[height - 1][x].is_carveable = False
        self.new_level = new_level

    def is_in_bounds(self, x, y):
        return (x >= 0 and y >= 0
            and y < len(self.maze_array)
            and x < len(self.maze_array[y]))

    def can_carve(self, x, y, direction):
        x, y = go_dir(x, y, direction)
        x, y = go_dir(x, y, direction)
        if (self.is_in_bounds(x, y)):
            return self.maze_array[y][x].is_carveable
        return False

    def get_carve_dirs(self, x, y):
        '''Returns a list of directions (numbers
        0 thru 3) representing where it is valid
        to carve.'''
        dirs = []
        for direction in range(4):
            if self.can_carve(x, y, direction):
                dirs.append(direction)
        return dirs

    def set_carveability(self, x, y, val):
        if self.is_in_bounds(x, y):
            self.maze_array[y][x].is_carveable = val

    def carve(self, x, y, direction):
        self.set_carveability(x+1, y, False)
        self.set_carveability(x-1, y, False)
        self.set_carveability(x, y+1, False)
        self.set_carveability(x, y-1, False)
        self.set_carveability(x, y, False)
        self.new_level[y][x] = 0

        x, y = go_dir(x, y, direction)

        self.set_carveability(x+1, y, False)
        self.set_carveability(x-1, y, False)
        self.set_carveability(x, y+1, False)
        self.set_carveability(x, y-1, False)
        self.set_carveability(x, y, False)
        self.new_level[y][x] = 0

        x, y = go_dir(x, y, direction)

        self.set_carveability(x+1, y, False)
        self.set_carveability(x-1, y, False)
        self.set_carveability(x, y+1, False)
        self.set_carveability(x, y-1, False)
        self.set_carveability(x, y, False)
        self.new_level[y][x] = 0

def dead_end_check(x, y, new_level):
    '''Helper function to get rid of dead ends'''
    # Is this tile surrounded on exactly 3 sides?
    surroundings = []
    if new_level[y+1][x] == 0:
        surroundings.append((x, y+1))
    if new_level[y-1][x] == 0:
        surroundings.append((x, y-1))
    if new_level[y][x+1] == 0:
        surroundings.append((x+1, y))
    if new_level[y][x-1] == 0:
        surroundings.append((x-1, y))

    if len(surroundings) != 1:
        return True

    # Clean up this dead end
    new_level[y][x] = 7
    dead_end_check(surroundings[0][0], surroundings[0][1], new_level)
    return False

LevelType = Enum('LevelType', [
    'PURE_MAZE',
    'PURE_FEATURES',
    'MAZE_AND_FEATURES',
    'DUNGEON'])

def factory(level_type, config, filename):
    '''A function for generating levels.'''
    match level_type:
        case LevelType.PURE_MAZE:
            level = generate_standard(config)
        case LevelType.PURE_FEATURES:
            pass
        case LevelType.MAZE_AND_FEATURES:
            pass
        case LevelType.DUNGEON:
            pass

    finalize(level, filename)

def generate_standard(config):
    '''Generates a standard level. This
    function uses the algorithm found here:
    https://journal.stuffwithstuff.com/2014/12/21/rooms-and-mazes/'''
    new_level = [[7 for _ in range(config.width)] for _ in range(config.height)]

    # Used later for making passages
    maze = Maze(config.width, config.height, new_level)

    # Used to connect everything together
    regions = []

    # Make rooms in the dungeon
    for _ in range(config.num_room_tries):
        room_width = randint(config.min_room_size, config.max_room_size)
        room_height = randint(config.min_room_size, config.max_room_size)
        room_x = randint(1, config.width - 2 - room_width)
        room_y = randint(1, config.height - 2 - room_height)

        if room_width % 2 == 0:
            room_width -= 1
        if room_height % 2 == 0:
            room_height -= 1
        if room_x % 2 == 0:
            room_x -= 1
        if room_y % 2 == 0:
            room_y -= 1

        # Check if this room is valid (doesn't overlap existing rooms)
        for row in range(room_x, room_x + room_width):
            for col in range(room_y, room_y + room_height):
                if new_level[col][row] == 0:
                    break
            else:
                continue
            break
        else:
            # Room is valid, generate it!
            new_room_region = []
            for row in range(room_x, room_x + room_width):
                for col in range(room_y, room_y + room_height):
                    new_level[col][row] = 0
                    new_room_region.append((row, col))
            regions.append(new_room_region)
            # Mark the room and surrounding walls as uncarveable in our Maze
            for row in range(room_x - 1, room_x + room_width + 1):
                for col in range(room_y - 1, room_y + room_height + 1):
                    maze.set_carveability(row, col, False)

    # Generate mazes in between the rooms
    # using the recursive backtracker algorithm
    for x in range(config.width):
        for y in range(config.height):
            if not maze.maze_array[y][x].is_carveable:
                continue

            # Begin a recursive backtracking
            new_maze_region = []
            maze.maze_array[y][x].is_carveable = False
            stack = [(x, y)]

            while len(stack) > 0:
                cur_x, cur_y = stack[-1]
                dirs = maze.get_carve_dirs(cur_x, cur_y)

                if len(dirs) == 0:
                    # Pop the stack and go to the previous node
                    stack.pop()
                else:
                    # Choose a random direction and carve that way
                    new_level[cur_y][cur_x] = 0
                    direction = choice(dirs)
                    maze.carve(cur_x, cur_y, direction)

                    new_maze_region.append((cur_x, cur_y))
                    cur_x, cur_y = go_dir(cur_x, cur_y, direction)
                    new_maze_region.append((cur_x, cur_y))
                    cur_x, cur_y = go_dir(cur_x, cur_y, direction)
                    new_maze_region.append((cur_x, cur_y))

                    stack.append((cur_x, cur_y))

            regions.append(new_maze_region)

    # Unify all regions into one
    for x in range(1,  config.width - 1):
        for y in range(1, config.height - 1):
            if new_level[y][x] == 0:
                continue

            # Check if this tile is surrounded
            # on exactly two sides
            t_up = new_level[y - 1][x]
            t_down = new_level[y + 1][x]
            t_left = new_level[y][x - 1]
            t_right = new_level[y][x + 1]

            adj_tiles = (None, None)
            if (t_up == 0 and t_down == 0
            and t_left != 0 and t_right != 0):
                adj_tiles = ((x-1, y), (x+1, y))

            if (t_left == 0 and t_right == 0
            and t_up != 0 and t_down != 0):
                adj_tiles = ((x-1, y), (x+1, y))

            if adj_tiles == (None, None):
                continue

            # Check to see if the adjacent tiles
            # belong to different regions
            region_0_i = None
            region_1_i = None
            for i, region in enumerate(regions):
                if adj_tiles[0] in region:
                    region_0_i = i
                if adj_tiles[1] in region:
                    region_1_i = i
                if region_0_i != None and region_1_i != None:
                    break
            else:
                #print('WARNING: No region found for:')
                #if region_0_i == None:
                #    print(adj_tiles[0])
                #if region_1_i == None:
                #    print(adj_tiles[1])
                continue

            if region_0_i == region_1_i:
                # 1 in (x) chance to carve this connector anyway
                if randint(1, config.extra_connectors_rarity) == 1:
                    new_level[y][x] = 0
                    regions[region_0_i].append((x, y))
                continue

            # They are from different regions.
            # Carve the tile and merge regions
            new_level[y][x] = 0
            regions[region_0_i].append((x, y))
            for tile in regions[region_1_i]:
                regions[region_0_i].append(tile)
            del regions[region_1_i]

    # Remove dead ends from the maze
    maze_has_dead_ends = True
    while maze_has_dead_ends:
        maze_has_dead_ends = False
        for x in range(1,  config.width - 1):
            for y in range(1, config.height - 1):
                if new_level[y][x] != 0:
                    continue

                # Check this tile
                tmp = dead_end_check(x, y, new_level)
                if maze_has_dead_ends:
                    maze_has_dead_ends = tmp

    return new_level

def finalize(level, filename):
    '''Converts the level to the format where it can
    be written to a file, adds items and monsters
    appropriate to depth, etc.'''

    def convert_to_tile(cell):
        if cell == 0:
            return '0,0,0,0'
        else:
            return f'{cell},1,1,0'

    # Convert the level array to the tilemap format
    data = '!TILEMAP\n'
    for row in level:
        for cell in row:
            data += f'{convert_to_tile(cell)} '
        data += '\n'

    data += '\n!MONSTERS\n'
    data += monsters.populate(level, 1)

    data += '\n!ITEMS\n\n!INFO\ndepth 0'

    file = open(filename, 'wb')
    file.write(zlib.compress(data.encode()))
    file.close()
