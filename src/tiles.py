import colors
import constants
import settings
import spriteloader

class Tile:
    def __init__(self, sprite, sprite_remembered, collision, blocks_sight) -> None:
        self.sprite = sprite
        self.sprite_remembered = sprite_remembered
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
        '''tiles is a 2D array of intstrings. index,collision,blocks_sight.'''
        self.tiles = []
        for row in tiles:

            new_row = []
            for attr_string in row:
                if len(attr_string) == 0:
                    continue

                attrs = attr_string.split(',')
                i = int(attrs[0])
                collision = int(attrs[1])
                blocks_sight = bool(int(attrs[2]))
                seen = bool(int(attrs[3]))

                (x, y) = constants.TILE_DICT[i]

                fg_color = constants.SPRITE_FG_COLOR
                if i == 0:
                    fg_color = constants.SPRITE_EMPTY_FG_COLOR

                new_tile = Tile(
                    spriteloader.sprite(
                        x, y,
                        colors.palette_color(constants.C_LIGHT_GRAY),
                        fg_color
                    ),
                    spriteloader.sprite(
                        x, y,
                        colors.palette_color(constants.C_GRAY),
                        fg_color
                    ),
                    collision,
                    blocks_sight
                )

                new_tile.sprite_index = i
                new_tile.seen = seen
                new_row.append(new_tile)
            if len(new_row) > 0:
                self.tiles.append(new_row)

        self.size = (len(self.tiles), len(self.tiles[0]))

    def draw(self, surface, camera=(0,0)):
        for x, row in enumerate(self.tiles):
            for y, tile in enumerate(row):
                if tile.seen:
                    sprite = tile.is_visible and tile.sprite or tile.sprite_remembered
                    surface.blit(
                        sprite,
                        (x * settings.TILE_SCALE - camera[0], y * settings.TILE_SCALE - camera[1])
                    )
