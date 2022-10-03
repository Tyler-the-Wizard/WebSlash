import level

class Game:
    '''A Game object contains all information that describes
    the game being played. This includes game info like the
    turn count, plus a list of levels.'''
    def __init__(self):
        self.turn_count = 0
        self.levels = []
        self.current_level = None
    
    def get_current_level(self):
        if self.current_level == None:
            print('game.py: Tried to index current level but none was found')
            return None
        return self.levels[self.current_level]
    
    def new_level(self):
        lvl = level.load('levels/big.dat')
        if self.current_level == None:
            lvl.depth = 0
        else:
            lvl.depth = self.get_current_level().depth + 1

        self.levels.append(lvl)