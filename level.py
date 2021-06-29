from random import randint, choice
from copy import deepcopy

import constants
import grid
import item
import monster
import random_maze
import settings

# Stores all the levels in the game
levels = []
current_level = 0

level_names = [
    "castle_outer",
    "intro_dungeon",
    "vault",
    "closet"
]

def init():
    global levels

    load_level(level_names[0])

def reset():
    global levels, current_level
    levels.clear()
    current_level = 0

def load_level(filename):
    file_handle = open("levels/" + filename + ".dat", "r")
    file_str = file_handle.read()
    rows = file_str.split("\n")
    cells = [row.split(" ") for row in rows]
    grid = [int(s) for row in cells for s in row]

    height = len(rows)
    width = len([x for x in rows[0] if x != ' '])

    for x in range(width):
        settings.grid.append([])
        for y in range(height):
            tile = grid[x % width + y * width]

            # Check for special flags (negative numbers)
            if tile == -1:
                tile = 1
                settings.player.x = x
                settings.player.y = y

            settings.grid[x].append(tile)

    # Random items
    for _ in range(5):
       rand_x = randint(0, 10)
       rand_y = randint(0, 10)

       if settings.grid[rand_x][rand_y] == 1:
           rand_item = item.make_random_item_stack(rand_x, rand_y)

    # Make lots of monsters
    for i in range(10):
        monster.make_appropriate_monster(randint(0, 10), randint(0, 10))

def next_level():
    global levels, current_level

    if current_level <= len(levels):
        levels.insert(current_level, deepcopy(settings.grid))
        settings.grid.clear()

        # Generate the next level
        load_level(level_names[current_level + 1])
    else:
        levels[current_level] = deepcopy(settings.grid)
        settings.grid.clear()
        settings.grid = levels[current_level + 1]
    current_level += 1

    # Find the up stairs and put the player there
    for x, row in enumerate(settings.grid):
        for y, tile in enumerate(row):
            if tile == constants.STAIRS_U:
                settings.player.x = x
                settings.player.y = y
                break

def prev_level():
    global levels, current_level

    if current_level <= len(levels):
        levels.append(deepcopy(settings.grid))
    else:
        levels[current_level] = deepcopy(settings.grid)
    settings.grid.clear()
    current_level -= 1

    settings.grid = levels[current_level]

    # Find the down stairs and put the player there
    for x, row in enumerate(settings.grid):
        for y, tile in enumerate(row):
            if tile == constants.STAIRS_D:
                settings.player.x = x
                settings.player.y = y
                break
