import constants
import sprites

def DEPRECATED_create_grid():
    new_grid = []
    new_grid = [ [0] * constants.GAME_HEIGHT_TILES for n in range(constants.GAME_WIDTH_TILES)]
    for x in range(5, 15):
        for y in range(5, 15):
            new_grid[x][y] = 1

    return new_grid

wall_tiles = {
    "H" : sprites.load_sprite(0, 23, constants.WHITE),
    "V" : sprites.load_sprite(1, 23, constants.WHITE),
    "X" : sprites.load_sprite(2, 23, constants.WHITE),

    "RD" : sprites.load_sprite(3, 23, constants.WHITE),
    "LD" : sprites.load_sprite(4, 23, constants.WHITE),
    "RU" : sprites.load_sprite(5, 23, constants.WHITE),
    "LU" : sprites.load_sprite(6, 23, constants.WHITE),

    "TR" : sprites.load_sprite(7, 23, constants.WHITE),
    "TL" : sprites.load_sprite(8, 23, constants.WHITE),
    "TD" : sprites.load_sprite(9, 23, constants.WHITE),
    "TU" : sprites.load_sprite(10, 23, constants.WHITE),

    "C" : sprites.load_sprite(11, 23, constants.WHITE)
}

tiles = {
    constants.FLOOR : sprites.load_sprite(15, 1, constants.WHITE),
    constants.DOOR : sprites.load_sprite(12, 21, constants.YELLOW),
    constants.WATER : sprites.load_sprite(6, 29, constants.BLUE),
    constants.TREE : sprites.load_sprite(3, 29, constants.GREEN),
    constants.ROAD : sprites.load_sprite(3, 21, constants.GRAY),
    constants.STAIRS_D : sprites.load_sprite(10, 21, constants.WHITE),
    constants.STAIRS_U : sprites.load_sprite(11, 21, constants.WHITE)
}

def draw_grid(grid, surface):
    for x, row in enumerate(grid):
        for y, tile in enumerate(row):
            if tile == constants.WALL:
                pass # special wall rules
            else:
                surface.blit(tiles[tile], (x * constants.TILE_SCALE, y * constants.TILE_SCALE))

    # Draw them walls!
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            width = len(grid)
            height = len(row)
            if tile == constants.WALL:
                u = False if c == 0 else grid[r][c - 1]
                d = False if c == height - 1 else grid[r][c + 1]
                l = False if r == 0 else grid[r - 1][c]
                ri = False if r == width - 1 else grid[r + 1][c]

                u = True if u == constants.WALL or u == constants.DOOR else False
                d = True if d == constants.WALL or d == constants.DOOR else False
                l = True if l == constants.WALL or l == constants.DOOR else False
                ri = True if ri == constants.WALL or ri == constants.DOOR else False

                wall_sprite = wall_tiles["X"]
                if not u and not d and (l or ri):
                    wall_sprite = wall_tiles["H"]
                if (u or d) and not l and not ri:
                    wall_sprite = wall_tiles["V"]

                if not u and d and not l and ri:
                    wall_sprite = wall_tiles["RD"]
                if not u and d and l and not ri:
                    wall_sprite = wall_tiles["LD"]
                if u and not d and not l and ri:
                    wall_sprite = wall_tiles["RU"]
                if u and not d and l and not ri:
                    wall_sprite = wall_tiles["LU"]

                surface.blit(wall_sprite, (r * constants.TILE_SCALE, c * constants.TILE_SCALE))