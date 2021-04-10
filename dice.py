from random import randint

def roll(num_sides, num_dice=1, drop=0):
    total = 0
    for i in range(num_dice):
        total += randint(drop + 1, num_sides)

    return total