import colors
import constants
import spriteloader

class Tile:
    def __init__(self, sprite, collision, blocks_sight) -> None:
        self.sprite = sprite
        self.collision = collision
        self.blocks_sight = blocks_sight
        self.is_visible = False
        self.seen = False

    def set_visibility(self, new_visibility):
        if new_visibility:
            self.seen = True
        self.is_visible = new_visibility

class Tilemap:
    '''A 2D grid of tiles.'''
    def __init__(self, tiles) -> None:
        '''tiles is a 2D array of ints. (see constants.TILE_DICT)'''
        self.tiles = []
        for row in tiles:
            new_row = []
            for i in row:
                (x, y) = constants.TILE_DICT[i]
                new_tile = Tile(
                    spriteloader.sprite(
                        x, y,
                        colors.palette_color(constants.C_LIGHT_GRAY)
                    ),
                constants.CL_NONE if i == 0 else constants.CL_WALL,
                False if i == 0 else True
                )

                new_row.append(new_tile)
            self.tiles.append(new_row)

        self.size = (len(tiles), len(tiles[0]))
    
    def draw(self, surface, camera=(0,0)):
        for x, row in enumerate(self.tiles):
            for y, tile in enumerate(row):
                if tile.seen:
                    surface.blit(
                        tile.sprite,
                        (x * constants.TILE_SCALE - camera[0], y * constants.TILE_SCALE - camera[1])
                    )
