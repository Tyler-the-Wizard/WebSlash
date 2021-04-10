import button as button_class
import dialog
import equip
import info
import item as item_class
import pygame
import settings
import text

def use_button(i):
    if i < len(settings.player.inv):
        item = settings.player.inv[i]

        if item.name in list(equip.weapons.keys()):
            # Equip the weapon!
            if settings.player.equip["main_hand"] == None:
                settings.player.equip["main_hand"] = item
                text.say("You now wield the " + item.name + ".")

            elif settings.player.equip["off_hand"] == None\
            and id(settings.player.equip["main_hand"]) != id(item)\
            and equip.weapons[ settings.player.equip["main_hand"].name ][3]\
            and equip.weapons[item.name][3]:
                settings.player.equip["off_hand"] = item
                text.say("You equip the " + item.name + " to your off-hand.")

                settings.player.do_enemy_move()
            return

        if item.name in list(consumables.keys()):
            # Consume the item!
            if consumables[item.name][0] == 0:
                settings.player.hp += consumables[item.name][1]
            if consumables[item.name][0] == 1:
                settings.player.mp += consumables[item.name][1]
            if consumables[item.name][0] == 2:
                settings.player.hp += consumables[item.name][1]
                settings.player.mp += consumables[item.name][1]

            if settings.player.hp > settings.player.max_hp:
                settings.player.hp = settings.player.max_hp
            if settings.player.mp > settings.player.max_mp:
                settings.player.mp = settings.player.max_mp

            text.say("You used the " + item.name + " and restored "
            + str(consumables[item.name][1]) + " " + consume_key[consumables[item.name][0]] + ".")

            if item.count > 1:
                item.count -= 1
            else:
                settings.player.inv.remove(item)

                sprite_button = []
                text_button = []
                for button in settings.buttons:
                    if button.args == item:
                        sprite_button = button
                    elif button.args == item.name:
                        text_button = button

                del item

            settings.player.do_enemy_move()

def info_button(i):
    if i < len(settings.player.inv):
        name = settings.player.inv[i].name
        if name not in info.info_dict:
            dialog.popup("Oops, no info for this object! Tyler forgot to do something")
        else:
            dialog.popup(info.info_dict[name])

# Initialize buttons
def init():
    for i in range(10):
        sprite_box = pygame.Rect( 830, 30 * (i + 1) + 30, 25, 25)
        info_box = pygame.Rect( 1110, 30 * (i + 1) + 20, 50, 30)

        sprite_button = button_class.Button(sprite_box, use_button, i)
        text_button = button_class.Button(info_box, info_button, i)
        settings.buttons.append(sprite_button)
        settings.buttons.append(text_button)

def draw_inv(player_inv, surface):
    global button_flags, cached_len, cached_buttons
    text.write("Inventory", surface, 0, 0)
    text.write("Status", surface, 190, 0, True)

    for i, item in enumerate(player_inv):
        # Do the mousoverbutton
        sprite_box = pygame.Rect( 830, 30 * (i + 1) + 30, 25, 25)
        info_box = pygame.Rect( 1110, 30 * (i + 1) + 20, 50, 30)
        bounding_box = pygame.Rect( 810, 30 * (i + 1) + 20, 380, 30)

        if item in settings.player.equip.values():
            pygame.draw.rect(surface, (99, 99, 99), pygame.Rect(
                18, 30 * (i + 1) + 18, 29, 29
            ))

        if sprite_box.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
                18, 30 * (i + 1) + 18, 29, 29
            ))

        if info_box.collidepoint(pygame.mouse.get_pos()):
            text.write("Info", surface, 300, 20 + 30 * (i + 1))


        elif bounding_box.collidepoint(pygame.mouse.get_pos()):
            text.write("Info", surface, 300, 20 + 30 * (i + 1), True)

        surface.blit(item.sprite, (20, 30 * (i + 1) + 20))

        text.write("- " + str(item.count) + " " + item.name + (item.count > 1 and "s" or ""),\
            surface, 60, 30 * (i + 1) + 20)

consumables = {
    # name: [0=hp, 1=mp, 2=both], amount
    "lesser cure": [0, 10],
    "greater cure": [0, 25],
    "superior cure": [0, 50],
    "lesser potion": [1, 10],
    "greater potion": [1, 25],
    "superior potion": [1, 50],
    "lesser elixir": [2, 10],
    "greater elixir": [2, 25],
    "superior elixir": [2, 50],

    "mutton": [0, 3]
}
consume_key = ["HP", "MP", "HP and MP"]

