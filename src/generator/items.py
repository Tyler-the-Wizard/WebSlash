from random import randint

from items import factory

def populate(level, depth):
    '''Populates the given level with
    items appropriate to the depth.'''
    result = ''

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == 0 and randint(1, 100) <= 1:
                result += f'longsword {x} {y}\n'

    return result
