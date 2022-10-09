from random import choice, randint

class Generator_Configuration:
    def __init__(self, width, height, num_room_tries, max_room_size, min_room_size):
            self.width = width
            self.height = height
            self.num_room_tries = num_room_tries
            self.max_room_size = max_room_size
            self.min_room_size = min_room_size

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
        match direction:
            case 0:
                y -= 2
            case 1:
                x += 2
            case 2:
                y += 2
            case 3:
                x -= 2
        if (self.is_in_bounds(x, y)):
            return self.maze_array[y][x].is_carveable

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

        match direction:
            case 0:
                y -= 1
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1

        self.set_carveability(x+1, y, False)
        self.set_carveability(x-1, y, False)
        self.set_carveability(x, y+1, False)
        self.set_carveability(x, y-1, False)
        self.set_carveability(x, y, False)
        self.new_level[y][x] = 0

        match direction:
            case 0:
                y -= 1
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1

        self.set_carveability(x+1, y, False)
        self.set_carveability(x-1, y, False)
        self.set_carveability(x, y+1, False)
        self.set_carveability(x, y-1, False)
        self.set_carveability(x, y, False)
        self.new_level[y][x] = 0

def generate_standard(config, filename):
    '''Generates a standard level. This
    function uses the algorithm found here:
    https://journal.stuffwithstuff.com/2014/12/21/rooms-and-mazes/'''
    new_level = [[7 for _ in range(config.width)] for _ in range(config.height)]

    # Used later for making passages
    maze = Maze(config.width, config.height, new_level)

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
            for row in range(room_x, room_x + room_width):
                for col in range(room_y, room_y + room_height):
                    new_level[col][row] = 0
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
                    match direction:
                        case 0:
                            cur_y -= 2
                        case 1:
                            cur_x += 2
                        case 2:
                            cur_y += 2
                        case 3:
                            cur_x -= 2
                    stack.append((cur_x, cur_y))


    # Convert the new_level array to the tilemap format
    data = '!TILEMAP\n'
    for row in new_level:
        for cell in row:
            data += f'{convert_to_tile(cell)} '
        data += '\n'

    data += '\n!MONSTERS\n\n!ITEMS\n\n!INFO\ndepth 0'

    file = open(filename, 'w')
    file.write(data)
    file.close()

def convert_to_tile(cell):
    if cell == 0:
        return '0,0,0,0'
    elif cell == 7:
        # TODO should be: return f'{cell},1,1,0'
        return f'{cell},0,1,0'
