import level
from generator import level as level_gen

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
        # Test code for now. Will change later
        config = level_gen.Generator_Configuration(
            width=50,
            height=30,
            num_room_tries=1000,
            max_room_size=11,
            min_room_size=3,
            extra_connectors_rarity=10
        )

        test_filename = 'levels/generated.dat'

        level_gen.factory(
            level_gen.LevelType.PURE_MAZE,
            config,
            test_filename)

        lvl = level.load(test_filename)
        self.levels.append(lvl)

    def save_level(self):
        level.save(self.get_current_level(), 'levels/save_test.dat')
