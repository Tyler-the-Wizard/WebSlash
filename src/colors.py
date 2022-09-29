import pygame
import settings

def palette_color(color_index):
    '''Returns a pygame Color based on the
    given color_index and the current
    palette in settings.PALETTE_INDEX.'''
    return palettes[settings.PALETTE_INDEX][color_index]

palettes = [
    # 0 - default palette
   [pygame.Color( 29,  36,  42), # BG
    pygame.Color(255, 255, 243), # FG
    pygame.Color(235,  78,  91), # RED
    pygame.Color(246, 214, 140), # YELLOW
    pygame.Color(133, 242, 116), # GREEN
    pygame.Color(116, 116, 240), # BLUE
    pygame.Color(116, 233, 240), # CYAN
    pygame.Color(240,  84, 245), # MAGENTA

    pygame.Color( 61,  66,  70), # GRAY
    pygame.Color(234, 234, 223), # LIGHT_GRAY
    pygame.Color(249, 197, 227), # PINK
    pygame.Color(240, 171,  99), # ORANGE
    pygame.Color(198, 249, 144), # LIGHT_GREEN
    pygame.Color( 17,  17, 193), # DEEP_BLUE
    pygame.Color(184, 251, 255), # SKY_BLUE
    pygame.Color(148,  86, 195)] # PURPLE
]