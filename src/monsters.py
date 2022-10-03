from colors import palette_color as color
import constants
import settings
from spriteloader import sprite

def factory(mon_name, x, y):
    if mon_name not in mon_lib:
        print(f'monsters.py: monster \'{mon_name}\' not found!')
        mon_name = 'unknown'

    args = mon_lib[mon_name]

    mon = Monster(mon_name, x, y, *args)
    settings.GAME.get_current_level().monsters.append(mon)
    return mon

mon_lib = {
#   'mon_name' : ['Display Name', speed, max_health, collision, sprite(x, y, color)]
    'player' : ['PLAYER', 60, 10, constants.CL_NONE, sprite(3, 8, color(constants.C_FG))],
    'unknown' : ['???', 60, -1, 256, sprite(14, 6, color(constants.C_MAGENTA))]
}

class Monster:
    def __init__(self, mon_name, x, y, display_name, speed, hp, collision, sprite) -> None:
        self.mon_name = mon_name
        self.x = x
        self.y = y

        self.display_name = display_name
        self.speed = speed
        self.max_hp = hp
        self.hp = hp

        self.collision = collision
        self.sprite = sprite
    
    def draw(self, surface, camera=(0, 0)):
        surface.blit(self.sprite, (self.x * constants.TILE_SCALE - camera[0], self.y * constants.TILE_SCALE - camera[1]))
    
    def can_move(self, x, y):
        '''Returns true if this monster's collision
        allows it to validly move to the x, y position.'''
        tile_collision = settings.GAME.get_current_level().tilemap.tiles[x][y].collision
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