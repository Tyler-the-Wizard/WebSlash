'''This file contains everything related to line-of-sight calculations.'''

import settings

def los(p0, p1):
    '''Retruns True if point p0 (x, y)
    has line of sight to point p1 (x, y).'''
    tiles = settings.GAME.get_current_level().tilemap.tiles

    for p in cast(p0, p1):
        if p == p1:
            # Stop if we reached the end. We can see it
            return True
        if tiles[p[0]][p[1]].blocks_sight:
            # This tile blocked the los.
            return False

    # Should never get executed, but just in case.
    return True

# https://steemit.com/programming/@woz.software/roguelike-line-of-sight-calculation
class Point:
    '''Helper class to make the cast function work'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Abs(self):
        return Point(abs(self.x), abs(self.y))

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

def cast(p0, p1):
    '''Returns a list of points (x, y)
    representing the ray from p0 to p1.'''
    start = Point(p0[0], p0[1])
    end = Point(p1[0], p1[1])

    xIncrement = (end.x > start.x) and 1 or -1
    yIncrement = (end.y > start.y) and 1 or -1

    delta = (start - end).Abs()
    error = delta.x - delta.y
    errorCorrect = delta * 2

    current = start
    while (True):
        if ((current == end) or
            (current != start and current != end)):
            yield (current.x, current.y)

        if (current == end):
            break

        if (error > 0):
            current = Point(current.x + xIncrement, current.y)
            error -= errorCorrect.y
        elif (error < 0):
            current = Point(current.x, current.y + yIncrement)
            error += errorCorrect.x
        else:
            current = Point(
                current.x + xIncrement,
                current.y + yIncrement
            )
