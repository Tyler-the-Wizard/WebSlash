import player as pl

def init():
    global buttons, dialog_busy, dialog_message, game_state, grid, item_stacks, messages, monsters, player, player_name, tiles

    buttons = []
    dialog_busy = False
    dialog_message = ""
    game_state = 6
    grid = []
    item_stacks = []
    messages = ["Welcome to WebSlash!"]
    monsters = []
    player = pl.Player()
    monsters.append(player)
    tiles = []