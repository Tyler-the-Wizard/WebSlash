from colors import palette_color as color
import constants
from player import xp_amounts
import settings
import text

text_size = 50

def draw(surface):
    player = settings.PLAYER

    width, height = surface.get_size()

    # Player name
    text.write(
        surface,
        10,
        height // 2 - text_size // 2,
        player.display_name,
        scale=text_size)

    # HP
    if player.hp <= player.max_hp / 5:
        health_color = color(constants.C_RED)
    elif player.hp <= player.max_hp / 2:
        health_color = color(constants.C_YELLOW)
    else:
        health_color = color(constants.C_FG)

    text.write(
        surface,
        width // 5,
        height // 2 - text_size // 2,
        f'HP: {player.hp}/{player.max_hp}',
        scale=text_size,
        color=health_color)

    # XP
    xp_str = (player.lvl >= 20
              and f'LVL {player.lvl}'
              or f'LVL {player.lvl} ({player.xp}/{xp_amounts[player.lvl]})')

    text.write(
        surface,
        width // 5 * 3,
        height // 2 - text_size // 2,
        xp_str,
        scale=text_size)

    # Turn count
    text.write(
        surface,
        width - text_size * 5,
        height // 2 - text_size // 2,
        f'T: {player.turn_count}',
        scale=text_size)