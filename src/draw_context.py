# This file defines several draw functions. These functions
# describe what state the game is in.

import settings

def standard_gameplay(surface):
    '''Draws a gameplay view to the surface.'''
    settings.CURRENT_LEVEL.draw(surface)