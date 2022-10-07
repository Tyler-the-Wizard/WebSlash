import draw_context

def init():

    # This is a function that gets called in the main
    # game loop to update the screen. Different values
    # cause different behaviors, leading to different
    # game states or "screens".
    global CURRENT_DRAW_CONTEXT
    CURRENT_DRAW_CONTEXT = draw_context.standard_gameplay

    global DO_MAIN_LOOP
    DO_MAIN_LOOP = True

    global GAME
    GAME = None

    global PALETTE_INDEX
    PALETTE_INDEX = 0

    global PLAYER
    PLAYER = None

    global SCREEN_SIZE
    SCREEN_SIZE = (2000, 1400)

    global TILE_SCALE
    TILE_SCALE = 100
