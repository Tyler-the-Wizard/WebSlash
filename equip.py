import button
import constants
import dice
import pygame
import settings
import sprites
import text

def new():
    return {
        "head": None,
        "armor": None,
        "r_ring": None,
        "l_ring": None,
        "main_hand": None,
        "off_hand": None,
        "boots": None
    }

weapons = {
    # "name": [num_sides, num_dice, str, one_handed]
    "dagger": [4, 1, False, True],
    "shortsword": [6, 1, True, True],
    "longsword": [8, 1, True, True],
    "broadsword": [4, 2, True, False],
    "rapier": [8, 1, False, False],
    "greatsword": [6, 2, True, False],
    "greataxe": [12, 1, True, False]
}

def add(player, item):
    if item in weapons:
        if player.equip["main_hand"] == None:
            player.equip["main_hand"] = item

def damage_calc(player, drop=0):
    total = 0
    if player.equip["main_hand"] == None:
        total += dice.roll(4, 1, drop)
    else:
        weapon_stats = weapons[player.equip["main_hand"].name]
        if player.equip["main_hand"].name == "longsword" and\
        player.equip["off_hand"] == None:
            total += dice.roll(10, 1, drop) + player.mod(player.str)
        else:
            total += dice.roll(weapon_stats[0], weapon_stats[1], drop)
            total += player.mod( weapon_stats[2] and player.str or player.dex )

        if weapon_stats[3]:
            # This is a one-handed weapon; another weapon could be in offhand
            if player.equip["off_hand"] != None and player.equip["off_hand"].name in weapons:
                off_weapon_stats = weapons[player.equip["off_hand"].name]
                total += dice.roll(off_weapon_stats[0], off_weapon_stats[1], drop)

    return total

equip_slots = [
    ["head", (200, 20), "Head"],
    ["armor", (200, 60), "Armor"],
    ["r_ring", (160, 40), "Ring"],
    ["l_ring", (240, 40), "Ring"],
    ["main_hand", (160, 80), "Main hand"],
    ["off_hand", (240, 80), "Off hand"],
    ["boots", (200, 100), "Boots"]
]

blank_sprite = sprites.load_sprite(0, 4, constants.WHITE)

first_time = True
def draw_equip(surface):
    global first_time
    text.write("Equipment", surface, 10, 10)

    for row in equip_slots:
        # Draw a white square
        equip_rect = pygame.Rect( row[1][0] - 2, row[1][1] - 2, 29, 29)
        pygame.draw.rect(surface, (255, 255, 255), equip_rect)

        if settings.player.equip[row[0]] == None:
            # Draw the blank sprite
            surface.blit(blank_sprite, row[1])
        else:
            surface.blit(settings.player.equip[row[0]].sprite, row[1])

        if equip_rect.collidepoint(\
            (pygame.mouse.get_pos()[0] - 810),\
            (pygame.mouse.get_pos()[1] - 410)):
            text.write(row[2], surface, 10, 40)

            if settings.player.equip[row[0]] != None:
                text.write(settings.player.equip[row[0]].name, surface, 20, 80)

        # Initialize buttons
        if first_time:
            my_button = button.Button(pygame.Rect(
                808 + row[1][0], 408 + row[1][1], 29, 29
            ), equip_button, row[0])
            settings.buttons.append(my_button)
    first_time = False

def equip_button(slot):
    if settings.player.equip[slot] != None:
        text.say("You return the " + settings.player.equip[slot].name + " to your inventory.")
        settings.player.equip[slot] = None