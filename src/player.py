import fov
from los import los
from message import new as say
import monsters
import settings

xp_amounts = {
    1: 50,
    2: 120,
    3: 200,
    4: 350,
    5: 600,
    6: 900,
    7: 1350,
    8: 1900,
    9: 2500,
    10: 3200,
    11: 4000,
    12: 5000,
    13: 6400,
    14: 8000,
    15: 10000,
    16: 12500,
    17: 15500,
    18: 19000,
    19: 23000,
}

class Player(monsters.Monster):
    def los(self, x, y) -> bool:
        '''Returns True if the player has line
        of sight to the given x, y position.'''
        return los((self.x, self.y), (x, y))

    def refresh_visibility(self):
        fov.refresh_visibility(self.x, self.y)

    def did_lvl_up(self):
        '''Return True if the player has gained
        enough xp to level up.'''
        if self.lvl >= 20:
            return False

        return self.xp >= xp_amounts[self.lvl]

    def gain_xp(self, amount):
        self.xp += amount
        while self.did_lvl_up():
            self.xp -= xp_amounts[self.lvl]
            self.lvl += 1

            self.max_hp += 10
            self.hp += 10

            say(f'You advance to level {self.lvl}!')

def make_player(x, y):
    player = monsters.factory('player', x, y)
    player.__class__ = Player
    player.turn_count = 0
    player.xp = 0
    player.lvl = 1

    settings.PLAYER = player
    player.refresh_visibility()
    return player
