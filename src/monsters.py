import colors
import constants
import settings
import spriteloader

class Monster:
    def __init__(self) -> None:
        self.sprite = spriteloader.sprite(
            3, 8,
            colors.palette_color(constants.C_FG)
        )
        self.x = 2
        self.y = 5
        self.collision = constants.CL_NONE # can not move into anything
    
    def draw(self, surface, camera=(0, 0)):
        surface.blit(self.sprite, (self.x * constants.TILE_SCALE - camera[0], self.y * constants.TILE_SCALE - camera[1]))
    
    def can_move(self, x, y):
        '''Returns true if this monster's collision
        allows it to validly move to the x, y position.'''
        tile_collision = settings.CURRENT_LEVEL.tilemap.tiles[x][y].collision
        return tile_collision == tile_collision & self.collision
    
    def move(self, x, y):
        '''Moves the monster to the x, y position.
        This function can move the monster to an
        "invalid" position according to its collision.'''
        self.x = x
        self.y = y

    def try_move(self, x, y):
        '''Moves the monster to the x, y position
        ONLY if it can validly move there.'''
        can_move = self.can_move(x, y)
        if can_move:
            self.move(x, y)

        return can_move