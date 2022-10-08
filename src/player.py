import fov
from los import los
import monsters
import settings

class Player(monsters.Monster):
    def los(self, x, y) -> bool:
        '''Returns True if the player has line
        of sight to the given x, y position.'''
        return los((self.x, self.y), (x, y))

    def refresh_visibility(self):
        fov.refresh_visibility(self.x, self.y)

def make_player(x, y):
    player = monsters.factory('player', x, y)
    player.__class__ = Player
    settings.PLAYER = player
    player.refresh_visibility()
    return player
