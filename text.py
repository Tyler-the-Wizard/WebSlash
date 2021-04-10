import button
import constants
import pygame
import settings
import sprites

text_sprites_white = {
    'A' : sprites.load_sprite(0, 55, constants.WHITE, half_width=True),
    'B' : sprites.load_sprite(1, 55, constants.WHITE, half_width=True),
    'C' : sprites.load_sprite(2, 55, constants.WHITE, half_width=True),
    'D' : sprites.load_sprite(3, 55, constants.WHITE, half_width=True),
    'E' : sprites.load_sprite(4, 55, constants.WHITE, half_width=True),
    'F' : sprites.load_sprite(5, 55, constants.WHITE, half_width=True),
    'G' : sprites.load_sprite(6, 55, constants.WHITE, half_width=True),
    'H' : sprites.load_sprite(7, 55, constants.WHITE, half_width=True),
    'I' : sprites.load_sprite(8, 55, constants.WHITE, half_width=True),
    'J' : sprites.load_sprite(9, 55, constants.WHITE, half_width=True),
    'K' : sprites.load_sprite(10, 55, constants.WHITE, half_width=True),
    'L' : sprites.load_sprite(11, 55, constants.WHITE, half_width=True),
    'M' : sprites.load_sprite(12, 55, constants.WHITE, half_width=True),
    'N' : sprites.load_sprite(13, 55, constants.WHITE, half_width=True),
    'O' : sprites.load_sprite(14, 55, constants.WHITE, half_width=True),
    'P' : sprites.load_sprite(15, 55, constants.WHITE, half_width=True),
    'Q' : sprites.load_sprite(16, 55, constants.WHITE, half_width=True),
    'R' : sprites.load_sprite(17, 55, constants.WHITE, half_width=True),
    'S' : sprites.load_sprite(18, 55, constants.WHITE, half_width=True),
    'T' : sprites.load_sprite(19, 55, constants.WHITE, half_width=True),
    'U' : sprites.load_sprite(20, 55, constants.WHITE, half_width=True),
    'V' : sprites.load_sprite(21, 55, constants.WHITE, half_width=True),
    'W' : sprites.load_sprite(22, 55, constants.WHITE, half_width=True),
    'X' : sprites.load_sprite(23, 55, constants.WHITE, half_width=True),
    'Y' : sprites.load_sprite(24, 55, constants.WHITE, half_width=True),
    'Z' : sprites.load_sprite(25, 55, constants.WHITE, half_width=True),

    'a' : sprites.load_sprite(0, 57, constants.WHITE, half_width=True),
    'b' : sprites.load_sprite(1, 57, constants.WHITE, half_width=True),
    'c' : sprites.load_sprite(2, 57, constants.WHITE, half_width=True),
    'd' : sprites.load_sprite(3, 57, constants.WHITE, half_width=True),
    'e' : sprites.load_sprite(4, 57, constants.WHITE, half_width=True),
    'f' : sprites.load_sprite(5, 57, constants.WHITE, half_width=True),
    'g' : sprites.load_sprite(6, 57, constants.WHITE, half_width=True),
    'h' : sprites.load_sprite(7, 57, constants.WHITE, half_width=True),
    'i' : sprites.load_sprite(8, 57, constants.WHITE, half_width=True),
    'j' : sprites.load_sprite(9, 57, constants.WHITE, half_width=True),
    'k' : sprites.load_sprite(10, 57, constants.WHITE, half_width=True),
    'l' : sprites.load_sprite(11, 57, constants.WHITE, half_width=True),
    'm' : sprites.load_sprite(12, 57, constants.WHITE, half_width=True),
    'n' : sprites.load_sprite(13, 57, constants.WHITE, half_width=True),
    'o' : sprites.load_sprite(14, 57, constants.WHITE, half_width=True),
    'p' : sprites.load_sprite(15, 57, constants.WHITE, half_width=True),
    'q' : sprites.load_sprite(16, 57, constants.WHITE, half_width=True),
    'r' : sprites.load_sprite(17, 57, constants.WHITE, half_width=True),
    's' : sprites.load_sprite(18, 57, constants.WHITE, half_width=True),
    't' : sprites.load_sprite(19, 57, constants.WHITE, half_width=True),
    'u' : sprites.load_sprite(20, 57, constants.WHITE, half_width=True),
    'v' : sprites.load_sprite(21, 57, constants.WHITE, half_width=True),
    'w' : sprites.load_sprite(22, 57, constants.WHITE, half_width=True),
    'x' : sprites.load_sprite(23, 57, constants.WHITE, half_width=True),
    'y' : sprites.load_sprite(24, 57, constants.WHITE, half_width=True),
    'z' : sprites.load_sprite(25, 57, constants.WHITE, half_width=True),

    '0' : sprites.load_sprite(0, 54, constants.WHITE, half_width=True),
    '1' : sprites.load_sprite(1, 54, constants.WHITE, half_width=True),
    '2' : sprites.load_sprite(2, 54, constants.WHITE, half_width=True),
    '3' : sprites.load_sprite(3, 54, constants.WHITE, half_width=True),
    '4' : sprites.load_sprite(4, 54, constants.WHITE, half_width=True),
    '5' : sprites.load_sprite(5, 54, constants.WHITE, half_width=True),
    '6' : sprites.load_sprite(6, 54, constants.WHITE, half_width=True),
    '7' : sprites.load_sprite(7, 54, constants.WHITE, half_width=True),
    '8' : sprites.load_sprite(8, 54, constants.WHITE, half_width=True),
    '9' : sprites.load_sprite(9, 54, constants.WHITE, half_width=True),

    '#' : sprites.load_sprite(0, 59, constants.WHITE, half_width=True),
    '%' : sprites.load_sprite(1, 59, constants.WHITE, half_width=True),
    '&' : sprites.load_sprite(2, 59, constants.WHITE, half_width=True),
    '@' : sprites.load_sprite(3, 59, constants.WHITE, half_width=True),
    '$' : sprites.load_sprite(4, 59, constants.WHITE, half_width=True),
    '.' : sprites.load_sprite(5, 59, constants.WHITE, half_width=True),
    ',' : sprites.load_sprite(6, 59, constants.WHITE, half_width=True),
    '!' : sprites.load_sprite(7, 59, constants.WHITE, half_width=True),
    '?' : sprites.load_sprite(8, 59, constants.WHITE, half_width=True),
    ':' : sprites.load_sprite(9, 59, constants.WHITE, half_width=True),
    ';' : sprites.load_sprite(10, 59, constants.WHITE, half_width=True),
   '\'' : sprites.load_sprite(11, 59, constants.WHITE, half_width=True),
    '"' : sprites.load_sprite(12, 59, constants.WHITE, half_width=True),
    '(' : sprites.load_sprite(13, 59, constants.WHITE, half_width=True),
    ')' : sprites.load_sprite(14, 59, constants.WHITE, half_width=True),
    '[' : sprites.load_sprite(15, 59, constants.WHITE, half_width=True),
    ']' : sprites.load_sprite(16, 59, constants.WHITE, half_width=True),
    '*' : sprites.load_sprite(17, 59, constants.WHITE, half_width=True),
    '/' : sprites.load_sprite(18, 59, constants.WHITE, half_width=True),
   '\\' : sprites.load_sprite(19, 59, constants.WHITE, half_width=True),
    '+' : sprites.load_sprite(20, 59, constants.WHITE, half_width=True),
    '-' : sprites.load_sprite(21, 59, constants.WHITE, half_width=True),
    '<' : sprites.load_sprite(22, 59, constants.WHITE, half_width=True),
    '=' : sprites.load_sprite(23, 59, constants.WHITE, half_width=True),
    '>' : sprites.load_sprite(24, 59, constants.WHITE, half_width=True),
    ' ' : sprites.load_sprite(25, 59, constants.WHITE, half_width=True),
    '_' : sprites.load_sprite(15, 60, constants.WHITE, half_width=True)
}

text_sprites_gray = {
    'A' : sprites.load_sprite(0, 55, constants.GRAY, half_width=True),
    'B' : sprites.load_sprite(1, 55, constants.GRAY, half_width=True),
    'C' : sprites.load_sprite(2, 55, constants.GRAY, half_width=True),
    'D' : sprites.load_sprite(3, 55, constants.GRAY, half_width=True),
    'E' : sprites.load_sprite(4, 55, constants.GRAY, half_width=True),
    'F' : sprites.load_sprite(5, 55, constants.GRAY, half_width=True),
    'G' : sprites.load_sprite(6, 55, constants.GRAY, half_width=True),
    'H' : sprites.load_sprite(7, 55, constants.GRAY, half_width=True),
    'I' : sprites.load_sprite(8, 55, constants.GRAY, half_width=True),
    'J' : sprites.load_sprite(9, 55, constants.GRAY, half_width=True),
    'K' : sprites.load_sprite(10, 55, constants.GRAY, half_width=True),
    'L' : sprites.load_sprite(11, 55, constants.GRAY, half_width=True),
    'M' : sprites.load_sprite(12, 55, constants.GRAY, half_width=True),
    'N' : sprites.load_sprite(13, 55, constants.GRAY, half_width=True),
    'O' : sprites.load_sprite(14, 55, constants.GRAY, half_width=True),
    'P' : sprites.load_sprite(15, 55, constants.GRAY, half_width=True),
    'Q' : sprites.load_sprite(16, 55, constants.GRAY, half_width=True),
    'R' : sprites.load_sprite(17, 55, constants.GRAY, half_width=True),
    'S' : sprites.load_sprite(18, 55, constants.GRAY, half_width=True),
    'T' : sprites.load_sprite(19, 55, constants.GRAY, half_width=True),
    'U' : sprites.load_sprite(20, 55, constants.GRAY, half_width=True),
    'V' : sprites.load_sprite(21, 55, constants.GRAY, half_width=True),
    'W' : sprites.load_sprite(22, 55, constants.GRAY, half_width=True),
    'X' : sprites.load_sprite(23, 55, constants.GRAY, half_width=True),
    'Y' : sprites.load_sprite(24, 55, constants.GRAY, half_width=True),
    'Z' : sprites.load_sprite(25, 55, constants.GRAY, half_width=True),

    'a' : sprites.load_sprite(0, 57, constants.GRAY, half_width=True),
    'b' : sprites.load_sprite(1, 57, constants.GRAY, half_width=True),
    'c' : sprites.load_sprite(2, 57, constants.GRAY, half_width=True),
    'd' : sprites.load_sprite(3, 57, constants.GRAY, half_width=True),
    'e' : sprites.load_sprite(4, 57, constants.GRAY, half_width=True),
    'f' : sprites.load_sprite(5, 57, constants.GRAY, half_width=True),
    'g' : sprites.load_sprite(6, 57, constants.GRAY, half_width=True),
    'h' : sprites.load_sprite(7, 57, constants.GRAY, half_width=True),
    'i' : sprites.load_sprite(8, 57, constants.GRAY, half_width=True),
    'j' : sprites.load_sprite(9, 57, constants.GRAY, half_width=True),
    'k' : sprites.load_sprite(10, 57, constants.GRAY, half_width=True),
    'l' : sprites.load_sprite(11, 57, constants.GRAY, half_width=True),
    'm' : sprites.load_sprite(12, 57, constants.GRAY, half_width=True),
    'n' : sprites.load_sprite(13, 57, constants.GRAY, half_width=True),
    'o' : sprites.load_sprite(14, 57, constants.GRAY, half_width=True),
    'p' : sprites.load_sprite(15, 57, constants.GRAY, half_width=True),
    'q' : sprites.load_sprite(16, 57, constants.GRAY, half_width=True),
    'r' : sprites.load_sprite(17, 57, constants.GRAY, half_width=True),
    's' : sprites.load_sprite(18, 57, constants.GRAY, half_width=True),
    't' : sprites.load_sprite(19, 57, constants.GRAY, half_width=True),
    'u' : sprites.load_sprite(20, 57, constants.GRAY, half_width=True),
    'v' : sprites.load_sprite(21, 57, constants.GRAY, half_width=True),
    'w' : sprites.load_sprite(22, 57, constants.GRAY, half_width=True),
    'x' : sprites.load_sprite(23, 57, constants.GRAY, half_width=True),
    'y' : sprites.load_sprite(24, 57, constants.GRAY, half_width=True),
    'z' : sprites.load_sprite(25, 57, constants.GRAY, half_width=True),

    '0' : sprites.load_sprite(0, 54, constants.GRAY, half_width=True),
    '1' : sprites.load_sprite(1, 54, constants.GRAY, half_width=True),
    '2' : sprites.load_sprite(2, 54, constants.GRAY, half_width=True),
    '3' : sprites.load_sprite(3, 54, constants.GRAY, half_width=True),
    '4' : sprites.load_sprite(4, 54, constants.GRAY, half_width=True),
    '5' : sprites.load_sprite(5, 54, constants.GRAY, half_width=True),
    '6' : sprites.load_sprite(6, 54, constants.GRAY, half_width=True),
    '7' : sprites.load_sprite(7, 54, constants.GRAY, half_width=True),
    '8' : sprites.load_sprite(8, 54, constants.GRAY, half_width=True),
    '9' : sprites.load_sprite(9, 54, constants.GRAY, half_width=True),

    '#' : sprites.load_sprite(0, 59, constants.GRAY, half_width=True),
    '%' : sprites.load_sprite(1, 59, constants.GRAY, half_width=True),
    '&' : sprites.load_sprite(2, 59, constants.GRAY, half_width=True),
    '@' : sprites.load_sprite(3, 59, constants.GRAY, half_width=True),
    '$' : sprites.load_sprite(4, 59, constants.GRAY, half_width=True),
    '.' : sprites.load_sprite(5, 59, constants.GRAY, half_width=True),
    ',' : sprites.load_sprite(6, 59, constants.GRAY, half_width=True),
    '!' : sprites.load_sprite(7, 59, constants.GRAY, half_width=True),
    '?' : sprites.load_sprite(8, 59, constants.GRAY, half_width=True),
    ':' : sprites.load_sprite(9, 59, constants.GRAY, half_width=True),
    ';' : sprites.load_sprite(10, 59, constants.GRAY, half_width=True),
   '\'' : sprites.load_sprite(11, 59, constants.GRAY, half_width=True),
    '"' : sprites.load_sprite(12, 59, constants.GRAY, half_width=True),
    '(' : sprites.load_sprite(13, 59, constants.GRAY, half_width=True),
    ')' : sprites.load_sprite(14, 59, constants.GRAY, half_width=True),
    '[' : sprites.load_sprite(15, 59, constants.GRAY, half_width=True),
    ']' : sprites.load_sprite(16, 59, constants.GRAY, half_width=True),
    '*' : sprites.load_sprite(17, 59, constants.GRAY, half_width=True),
    '/' : sprites.load_sprite(18, 59, constants.GRAY, half_width=True),
   '\\' : sprites.load_sprite(19, 59, constants.GRAY, half_width=True),
    '+' : sprites.load_sprite(20, 59, constants.GRAY, half_width=True),
    '-' : sprites.load_sprite(21, 59, constants.GRAY, half_width=True),
    '<' : sprites.load_sprite(22, 59, constants.GRAY, half_width=True),
    '=' : sprites.load_sprite(23, 59, constants.GRAY, half_width=True),
    '>' : sprites.load_sprite(24, 59, constants.GRAY, half_width=True),
    ' ' : sprites.load_sprite(25, 59, constants.GRAY, half_width=True),
    '_' : sprites.load_sprite(15, 60, constants.GRAY, half_width=True)
}

def write(text, surface, x, y, gray=False):
    # Draw the sprites
    for i, letter in enumerate(text):
        sprite = gray and text_sprites_gray[letter] or text_sprites_white[letter]
        surface.blit(sprite, (x + i * constants.TILE_SCALE // 2, y))

def draw_messages(surface):
    for i, message in enumerate(settings.messages):
        write(message, surface, 5, 5 + i * 25, i > 0)

def say(message):
    settings.messages.insert(0, message)
    if len(settings.messages) > 3:
        settings.messages.pop()

text_input_key = {
    pygame.K_a : ["a", "A"],
    pygame.K_b : ["b", "B"],
    pygame.K_c : ["c", "C"],
    pygame.K_d : ["d", "D"],
    pygame.K_e : ["e", "E"],
    pygame.K_f : ["f", "F"],
    pygame.K_g : ["g", "G"],
    pygame.K_h : ["h", "H"],
    pygame.K_i : ["i", "I"],
    pygame.K_j : ["j", "J"],
    pygame.K_k : ["k", "K"],
    pygame.K_l : ["l", "L"],
    pygame.K_m : ["m", "M"],
    pygame.K_n : ["n", "N"],
    pygame.K_o : ["o", "O"],
    pygame.K_p : ["p", "P"],
    pygame.K_q : ["q", "Q"],
    pygame.K_r : ["r", "R"],
    pygame.K_s : ["s", "S"],
    pygame.K_t : ["t", "T"],
    pygame.K_u : ["u", "U"],
    pygame.K_v : ["v", "V"],
    pygame.K_w : ["w", "W"],
    pygame.K_x : ["x", "X"],
    pygame.K_y : ["y", "Y"],
    pygame.K_z : ["z", "Z"],
    pygame.K_SPACE : [" ", " "]
}

shift_down = False
def read_player_inputs(event):
    global shift_down
    if event.key == pygame.K_BACKSPACE and event.type == pygame.KEYDOWN:
        settings.player.name = settings.player.name[:-1]
    elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
        shift_down = (event.type == pygame.KEYDOWN)
    elif event.key == pygame.K_RETURN and event.type == pygame.KEYDOWN:
        settings.buttons.append(button.Button(pygame.Rect(
            450, 500, 300, 70
        ), start_game))

        settings.game_state = constants.BUILD_CHARACTER
    else:
        if len(settings.player.name) < 11 and event.type == pygame.KEYDOWN and event.key in text_input_key.keys():
            settings.player.name += text_input_key[event.key][
                shift_down and 1 or 0
            ]

# ugly ugly ugly
def start_game(_):
    settings.game_state = constants.START