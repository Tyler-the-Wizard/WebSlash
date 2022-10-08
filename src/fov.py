'''This file contains everything related to field-of-view calculations.'''

import settings

# https://journal.stuffwithstuff.com/2015/09/07/what-the-hero-sees/

class Shadow_Line:
    def __init__(self):
        self.shadows = [] # list of Shadow

    def is_in_shadow(self, projection) -> bool:
        for shadow in self.shadows:
            if shadow.contains(projection):
                return True
        return False
    
    def add(self, shadow) -> None:
        # Figure out where to slot the new shadow in the list.
        index = 0
        while index < len(self.shadows):
            # Stop when we hit the insertion point.
            if self.shadows[index].start >= shadow.start:
                break
            index += 1

        # The new shadow is going here. See if it overlaps the
        # previous or next.
        overlapping_previous = None
        if index > 0 and self.shadows[index - 1].end > shadow.start:
            overlapping_previous = self.shadows[index - 1]

        overlapping_next = None
        if (index < len(self.shadows)
        and self.shadows[index].start < shadow.end):
            overlapping_next = self.shadows[index]

        # Insert and unify with overlapping shadows.
        if overlapping_next != None:
            if overlapping_previous != None:
                # Overlaps both, so unify one and delete the other.
                overlapping_previous.end = overlapping_next.end
                del self.shadows[index]
            else:
                # Overlaps the next one, so unify it with that.
                overlapping_next.start = shadow.start
        else:
            if overlapping_previous != None:
                # Overlaps the previous one, so unify it with that.
                overlapping_previous.end = shadow.end
            else:
                # Does not overlap anything, so insert.
                self.shadows.insert(index, shadow)

    def is_full_shadow(self):
        return (len(self.shadows) == 1
        and self.shadows[0].start == 0
        and self.shadows[0].end == 1)

class Shadow:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, other) -> bool:
        '''Returns True if other is
        completely covered by this shadow.'''
        return self.start <= other.start and self.end >= other.end

# Creates a [Shadow] that corresponds to the projected
# silhouette of the tile at [row], [col].
def project_tile(row, col) -> Shadow:
    '''Creates a Shadow that corresponds to the
    projected silhouette of the tile at row, col.'''
    top_left = col / (row + 2)
    bottom_right = (col + 1) / (row + 1)
    return Shadow(top_left, bottom_right)

class Point:
    '''Helper class to assist with octant transformations'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def refresh_visibility(player_x, player_y):
    for octant in range(8):
        refresh_octant(Point(player_x, player_y), octant)

def refresh_octant(player_pos, octant):
    line = Shadow_Line()
    tiles = settings.GAME.get_current_level().tilemap.tiles

    row = 0
    while True:
        row += 1
        # Stop once we go out of bounds.
        pos = player_pos + transform_octant(row, 0, octant)
        if not is_in_bounds(pos):
            break

        for col in range(0, row + 1):
            pos = player_pos + transform_octant(row, col, octant)

            # If we've traversed out of bounds, bail on this row.
            if not is_in_bounds(pos):
                break

            projection = project_tile(row, col)

            # Set the visibility of this tile.
            visible = not line.is_in_shadow(projection)
            tiles[pos.x][pos.y].set_visibility(visible)

            # Add any opaque tiles to the shadow map.
            if visible and tiles[pos.x][pos.y].blocks_sight:
                line.add(projection)

def is_in_bounds(point):
    bounds = settings.GAME.get_current_level().tilemap.size
    return (point.x >= 0 and point.x < bounds[0]
        and point.y >= 0 and point.y < bounds[1])

def transform_octant(row, col, octant):
    match octant:
        case 0:
            return Point( col, -row)
        case 1:
            return Point( row, -col)
        case 2:
            return Point( row,  col)
        case 3:
            return Point( col,  row)
        case 4:
            return Point(-col,  row)
        case 5:
            return Point(-row,  col)
        case 6:
            return Point(-row, -col)
        case 7:
            return Point(-col, -row)
