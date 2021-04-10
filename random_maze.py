import random

import constants
import settings

def make_room(x, y, width, height):
    for r in range(width):
        for c in range(height):
            if r == y or c == x:
                settings.grid[r+x][c+y] = constants.WALL