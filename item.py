from random import choice

import constants
import settings
import sprites

class Item:
    def __init__(self, name, sprite, stack_size=1, count=1):
        self.name = name
        self.sprite = sprite
        self.stack_size = stack_size
        self.count = count

class Item_Stack:
    def __init__(self, item, x, y):
        self.item = item
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.item.sprite, (self.x * constants.TILE_SCALE, self.y * constants.TILE_SCALE))

def make_item_stack(name, x, y, count=1):
    stack = Item_Stack(make_item(name, count), x, y)
    settings.item_stacks.append(stack)
    return stack

def make_item(name, count=1):
    item = 0
    # Weapons
    if name == "dagger":
        item = Item(name, sprites.load_sprite(0, 40, constants.WHITE))
    elif name == "shortsword":
        item = Item(name, sprites.load_sprite(1, 42, constants.WHITE))
    elif name == "longsword":
        item = Item(name, sprites.load_sprite(0, 42, constants.WHITE))
    elif name == "broadsword":
        item = Item(name, sprites.load_sprite(1, 40, constants.WHITE))
    elif name == "rapier":
        item = Item(name, sprites.load_sprite(2, 42, constants.WHITE))
    elif name == "greatsword":
        item = Item(name, sprites.load_sprite(3, 42, constants.WHITE))
    elif name == "greataxe":
        item = Item(name, sprites.load_sprite(4, 42, constants.WHITE))

    # Armor
    elif name == "helmet":
        item = Item(name, sprites.load_sprite(11, 40, constants.WHITE))
    elif name == "full helm":
        item = Item(name, sprites.load_sprite(12, 40, constants.WHITE))
    elif name == "wizard hat":
        item = Item(name, sprites.load_sprite(13, 40, constants.BLUE))
    elif name == "boots":
        item = Item(name, sprites.load_sprite(0, 41, constants.WHITE))
    elif name == "hide armor":
        item = Item(name, sprites.load_sprite(3, 41, constants.YELLOW))
    elif name == "half plate":
        item = Item(name, sprites.load_sprite(4, 41, constants.WHITE))
    elif name == "full plate":
        item = Item(name, sprites.load_sprite(5, 41, constants.WHITE))

    # Rings
    elif name == "ruby ring":
        item = Item(name, sprites.load_sprite(7, 41, constants.RED))

    # Potions
    elif name == "lesser cure":
        item = Item(name, sprites.load_sprite(3, 37, constants.RED), 99, count)
    elif name == "greater cure":
        item = Item(name, sprites.load_sprite(4, 37, constants.RED), 99, count)
    elif name == "superior cure":
        item = Item(name, sprites.load_sprite(5, 37, constants.RED), 99, count)
    elif name == "lesser potion":
        item = Item(name, sprites.load_sprite(3, 37, constants.BLUE), 99, count)
    elif name == "greater potion":
        item = Item(name, sprites.load_sprite(4, 37, constants.BLUE), 99, count)
    elif name == "superior potion":
        item = Item(name, sprites.load_sprite(5, 37, constants.BLUE), 99, count)
    elif name == "lesser elixir":
        item = Item(name, sprites.load_sprite(3, 37, constants.GREEN), 99, count)
    elif name == "greater elixir":
        item = Item(name, sprites.load_sprite(4, 37, constants.GREEN), 99, count)
    elif name == "superior elixir":
        item = Item(name, sprites.load_sprite(5, 37, constants.GREEN), 99, count)

    # Food
    elif name == "mutton":
        item = Item(name, sprites.load_sprite(0, 36, constants.YELLOW), 99, count)

    # Misc
    elif name == "gold piece":
        item = Item(name, sprites.load_sprite(13, 32, constants.YELLOW), 10000, count)

    return item

# Random item generation
item_table = [
["dagger", "shortsword", "longsword", "broadsword", "rapier", "greatsword", "greataxe", "helmet", "full helm", "wizard hat", "boots", "hide armor", "half plate", "full plate"],
["lesser cure", "greater cure", "superior cure", "lesser potion", "greater potion", "superior potion", "lesser elixir", "greater elixir", "superior elixir"],
["mutton"]
]

def make_random_item():
    return make_item(choice(choice(item_table)))

def make_random_item_stack(x, y):
    stack = Item_Stack(make_random_item(), x, y)
    settings.item_stacks.append(stack)
    return stack