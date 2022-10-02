import pygame
import settings

def palette_color(color_index):
    '''Returns a pygame Color based on the
    given color_index and the current
    palette in settings.PALETTE_INDEX.'''
    return palettes[settings.PALETTE_INDEX][color_index]

palettes = [
    # 0 - default palette
   [pygame.Color( 29,  36,  42), # C_BG
    pygame.Color(255, 255, 243), # C_FG
    pygame.Color(235,  78,  91), # C_RED
    pygame.Color(246, 214, 140), # C_YELLOW
    pygame.Color(133, 242, 116), # C_GREEN
    pygame.Color(116, 116, 240), # C_BLUE
    pygame.Color(116, 233, 240), # C_CYAN
    pygame.Color(240,  84, 245), # C_MAGENTA

    pygame.Color( 61,  66,  70), # C_GRAY
    pygame.Color(178, 178, 172), # C_LIGHT_GRAY
    pygame.Color(249, 197, 227), # C_PINK
    pygame.Color(240, 171,  99), # C_ORANGE
    pygame.Color(198, 249, 144), # C_LIGHT_GREEN
    pygame.Color( 17,  17, 193), # C_DEEP_BLUE
    pygame.Color(184, 251, 255), # C_SKY_BLUE
    pygame.Color(148,  86, 195)] # C_PURPLE
]