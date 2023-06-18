from random import randint

from monsters import factory

def populate(level, depth):
    '''Populates the given level with
    monsters appropriate to the depth.'''
    result = ''

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == 0 and randint(1, 100) <= 2:
                result += f'goblin {x} {y}\n'

    return result

