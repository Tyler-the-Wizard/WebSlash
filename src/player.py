from xmlrpc.client import Boolean
from los import los
import monsters
import settings

class Player(monsters.Monster):
    def los(self, x, y) -> Boolean:
        '''Returns True if the player has line
        of sight to the given x, y position.'''
        return los((self.x, self.y), (x, y))

def make_player(x, y):
    player = monsters.factory('player', x, y)
    player.__class__ = Player
    settings.PLAYER = player
    return player
