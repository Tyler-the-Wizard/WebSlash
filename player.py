from random import randint

import constants
import dialog
import dice
import equip
import inv
import level
import monster
import settings
import sprites
import text

# how much xp does it take to go to the next level?
xp_table = [10, 30, 60, 100, 300, 500] # 1000, 2000, 4000, 8000, etc
def calc_xp(num):
    if num > len(xp_table):
        return (2 ** (num - len(xp_table) + 1)) * 1000
    else:
        return xp_table[num - 1]

player_sprites = {
    "" : sprites.load_sprite(0, 1, constants.WHITE),
    "Sage" : sprites.load_sprite(6, 1, constants.WHITE),
    "Monk" : sprites.load_sprite(0, 1, constants.WHITE),
    "Barbarian" : sprites.load_sprite(2, 1, constants.WHITE),
    "Spellblade" : sprites.load_sprite(2, 1, constants.WHITE),
    "Fighter" : sprites.load_sprite(2, 1, constants.WHITE),
    "Ninja" : sprites.load_sprite(4, 1, constants.WHITE),
    "Thief" : sprites.load_sprite(4, 1, constants.WHITE),
    "Rogue" : sprites.load_sprite(4, 1, constants.WHITE),
    "Sorcerer" : sprites.load_sprite(5, 1, constants.WHITE),
    "Wizard" : sprites.load_sprite(5, 1, constants.WHITE),
    "Warlock" : sprites.load_sprite(5, 1, constants.WHITE),
    "Enigma" : sprites.load_sprite(12, 1, constants.WHITE)
}

class Player(monster.Monster):
    def __init__(self):
        self.str = 10
        self.dex = 10
        self.wis = 10

        self.mp = 5
        self.max_mp = 5

        self.equip = equip.new()
        self.xp = 0

        super().__init__("", 5, 4,
            player_sprites[get_class_name(self.str, self.dex, self.wis)],
            10, 10, 1)

    def mod(self, num):
        return (num - 10) // 2

    def move(self, x, y):
        super().move(x, y)
        # Check to see if we are over an item
        for stack in settings.item_stacks:
            if stack.x == self.x and stack.y == self.y:
                text.say("You see here a " + stack.item.name + ".")

        self.do_enemy_move()

    def draw(self, surface):
        self.sprite = player_sprites[get_class_name(self.str, self.dex, self.wis)]
        super().draw(surface)

    def do_enemy_move(self):
        # Now all the monsters get to move
        ticks = self.speed
        for monster in settings.monsters:
            if monster != self:
                current_speed = monster.speed + monster.speed_overflow
                monster.speed_overflow = 0
                while current_speed >= ticks:
                    current_speed -= ticks
                    monster.move_to_goal()
                monster.speed_overflow += current_speed + randint(-3, 3)

    def attack(self, monster):
        # Roll to hit
        to_hit = dice.roll(20)
        nat_20 = (to_hit == 20)
        nat_1 = (to_hit == 1)

        if not (nat_20 or nat_1):
            # Yes, DEX does get added to bare-handed combat. This is intentional.
            if self.equip["main_hand"] != None and\
            equip.weapons[self.equip["main_hand"].name][2]:
                to_hit += self.mod(self.str)
            else:
                to_hit += self.mod(self.dex)

        if (to_hit >= monster.ac or nat_20) and not nat_1:
            # Hit!
            monster.hp -= equip.damage_calc(self)
            text.say("You hit the " + monster.name + "!")

            if monster.hp <= 0:
                # Get xp!
                self.xp += monster.lvl * 5

                monster.die()
                text.say("You kill the " + monster.name + "!")
                # Level up?
                while self.xp >= calc_xp(self.lvl):
                    # We leveled up!
                    self.xp -= calc_xp(self.lvl)
                    self.lvl += 1
                    self.max_hp += dice.roll(8) + self.mod(self.str)
                    self.max_mp += 5 + self.mod(self.wis)
                    self.hp = self.max_hp
                    self.mp = self.max_mp
                    text.say("You advance to level " + str(self.lvl) + "!")
        else:
            text.say("You miss the " + monster.name + ".")


    def pickup(self):
        # Check to see if there are any items here
        for stack in settings.item_stacks:
            if stack.x == self.x and stack.y == self.y:
                text.say("You pick up the " + stack.item.name + ".")

                # Check to see if there is another stack
                for s in self.inv:
                    if s.name == stack.item.name and s.count < s.stack_size:
                        s.count += 1
                        break
                else:
                    self.inv.append(stack.item)
                    # Connect buttons
                    # inv.set_button_flag(stack.item.name)
                settings.item_stacks.remove(stack)

                self.do_enemy_move()

        # Check to see if there is something to use here
        self.use(settings.grid[self.x][self.y])

    def use(self, tile):
        if tile == constants.STAIRS_D:
            # Go down to the next level!
            text.say("You descend the stairs.")
            level.next_level()
        elif tile == constants.STAIRS_U:
            # Go up to the previous level!
            text.say("You ascend the stairs.")
            level.prev_level()

    def die(self):
        dialog.popup("Oh no! You died!")
        self.inv.clear()

def draw_stats(player, surface):
    text.write("Inventory", surface, 0, 0, True)
    text.write("Status", surface, 190, 0)

    text.write(player.name + " the " + get_class_name(player.str, player.dex, player.wis),
        surface, 20, 40)

    text.write("HP: " + str(player.hp) + "/" + str(player.max_hp), surface, 20, 80)
    text.write("MP: " + str(player.mp) + "/" + str(player.max_mp), surface, 20, 100)

    text.write("AC: " + str(player.ac), surface, 20, 130)

    text.write("LVL: " + str(player.lvl), surface, 190, 80)
    text.write("XP: " + str(player.xp) + "/" + str(calc_xp(player.lvl)), surface, 190, 100)

    text.write("STR: " + str(player.str), surface, 190, 130)
    text.write("DEX: " + str(player.dex), surface, 190, 150)
    text.write("WIS: " + str(player.wis), surface, 190, 170)

def get_class_name(sng, dex, wis):
    if sng == dex and dex == wis:
        if sng >= 16:
            return "Sage"
        else:
            return "Monk"

    elif sng > dex and sng > wis:
        if sng - dex >= 6 and sng - wis >= 6:
            return "Barbarian"
        elif wis > dex:
            return "Spellblade"
        else:
            return "Fighter"

    elif dex > sng and dex > wis:
        if dex - sng >= 6 and dex - wis >= 6:
            return "Ninja"
        elif wis > sng:
            return "Thief"
        else:
            return "Rogue"

    elif wis > sng and wis > dex:
        if wis - sng >= 6 and wis - dex >= 6:
            return "Sorcerer"
        elif sng > dex:
            return "Warlock"
        else:
            return "Wizard"

    elif sng == dex:
        return "Fighter"
    elif dex == wis:
        return "Thief"
    elif wis == sng:
        return "Warlock"

    else:
        return "Enigma"