from colors import palette_color as color
import constants
import settings
from spriteloader import sprite

def factory(item_name, x, y, count=1):
    'Creates an item and returns it.'
    if item_name not in item_lib:
        print(f'items.py: item \'{item_name}\' not found!')
        item_name = 'glitch'

    args = item_lib[item_name]

    item = Item(item_name, x, y, *args)
    return item

item_lib = {
#   'item_name' : ['Display Name', count, weight, 'usage', sprite(x, y, color)]
    'longsword' : ['', 1, 20, 'melee:1d8', sprite(3, 45, color(constants.C_CYAN))]
}

class Item:
    def __init__(self, item_name, x, y, display_name, count, weight, usage, sprite) -> None:
        self.item_name = item_name
        self.x = x
        self.y = y

        self.display_name = display_name
        self.count = count
        self.weight = weight

        self.handlers = {}
        self.process_usages(usage)

        self.sprite = sprite

    def draw(self, surface, camera=(0, 0)):
        surface.blit(self.sprite, (self.x * settings.TILE_SCALE - camera[0], self.y * settings.TILE_SCALE - camera[1]))

    def process_usages(self, usage):
        '''A complicated function that will figure
        out all the ways this item can be used, and
        add them. The format of a usage string
        will be determined later.'''
        for func in usage.split(';'):
            args = func.split(':')
            if args[0] == 'melee':
                # This is a melee weapon
                self.handlers['melee'] = args[1]
