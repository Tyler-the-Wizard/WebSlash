from random import choice, randint

import constants
import dice
import settings
import sprites
import text

class Monster:
    def __init__(self, name, x, y, sprite, hp, ac, lvl, speed=12):
        self.x = x
        self.y = y
        self.sprite = sprite

        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.ac = ac
        self.lvl = lvl

        self.inv = []
        self.speed = speed
        self.speed_overflow = 0

    def draw(self, surface):
        surface.blit(self.sprite, (self.x * constants.TILE_SCALE, self.y * constants.TILE_SCALE))

    def move(self, x, y):
        if x == 0 and y == 0:
            return

        if  self.x + x >= 0 and self.x + x < len(settings.grid)\
        and self.y + y >= 0 and self.y + y < len(settings.grid[0])\
        and (\
            settings.grid[self.x + x][self.y + y] == constants.FLOOR\
         or settings.grid[self.x + x][self.y + y] == constants.ROAD\
         or settings.grid[self.x + x][self.y + y] == constants.STAIRS_D\
         or settings.grid[self.x + x][self.y + y] == constants.STAIRS_U\
         or settings.grid[self.x + x][self.y + y] == constants.DOOR):
            # Check to see if there are any other monsters in the way
            for monster in settings.monsters:
                if monster.x == self.x + x and monster.y == self.y + y:
                    # We are attacking!
                    self.attack(monster)
                    break
            else:
                # We move
                self.x += x
                self.y += y

    def move_to_goal(self):
        """This function will be responsible for:
        determining whether the monster should be wandering,
        attacking, or moving towards our target."""

        if abs(self.x - settings.player.x) <= 1 and abs(self.y - settings.player.y) <= 1:
            # Attack the player
            self.attack(settings.player)

        else:
            # Wander
            self.move(randint(-1, 1), randint(-1, 1))

    def attack(self, monster):
        # Roll to hit
        to_hit = dice.roll(20)
        if (to_hit >= monster.ac or to_hit == 20) and to_hit != 1:
            # Hit!
            monster.hp -= dice.roll(4, self.lvl)

            if monster.hp <= 0:
                text.say("The " + self.name + " kills the " + monster.name + "!")
                monster.die()
            else:
                text.say("The " + self.name + " hits the " + monster.name + "!")
        else:
            text.say("The " + self.name + " misses the " + monster.name + ".")

    def die(self):
        settings.monsters.remove(self)
        del self

monsters_by_level = {
    1 : ["bat", "rat"],
    2 : ["garter snake", "jackal"],
    3 : ["goblin"],
    4 : ["ogre", "orc"],
    5 : ["troll"],
    6 : ["golem"],
    7 : ["shade"]
}

def make_appropriate_monster(x, y):
    lvl = 0
    if settings.player.lvl == 1:
        lvl = randint(1, 2)
    else:
        lvl = settings.player.lvl + randint(-3, 3)

    if lvl < 1:
        lvl = 1
    if lvl > len(monsters_by_level):
        lvl = len(monsters_by_level)

    return make_random_monster(lvl, x, y)

def make_random_monster(lvl, x, y):
    return make_monster(choice(monsters_by_level[lvl]), x, y)

def make_monster(name, x, y):
    mon = 0
    if name == "bat":
        mon = Monster(name, x, y, sprites.load_sprite(1, 9, constants.WHITE), hp=1, ac=5, lvl=1, speed=18)
    if name == "rat":
        mon = Monster(name, x, y, sprites.load_sprite(0, 9, constants.YELLOW), hp=1, ac=0, lvl=1, speed=18)

    if name == "garter snake":
        mon = Monster(name, x, y, sprites.load_sprite(6, 9, constants.CYAN), hp=5, ac=5, lvl=2)
    if name == "jackal":
        mon = Monster(name, x, y, sprites.load_sprite(7, 9, constants.YELLOW), hp=10, ac=8, lvl=2)

    if name == "goblin":
        mon = Monster(name, x, y, sprites.load_sprite(0, 12, constants.GREEN), hp=10, ac=10, lvl=3)

    if name == "ogre":
        mon = Monster(name, x, y, sprites.load_sprite(1, 12, constants.GREEN), hp=30, ac=10, lvl=4)
    if name == "orc":
        mon = Monster(name, x, y, sprites.load_sprite(1, 12, constants.BLUE), hp=20, ac=12, lvl=4)

    if name == "troll":
        mon = Monster(name, x, y, sprites.load_sprite(3, 12, constants.CYAN), hp=30, ac=12, lvl=5)

    if name == "golem":
        mon = Monster(name, x, y, sprites.load_sprite(7, 18, constants.GRAY), hp=50, ac=0, lvl=6, speed=3)

    if name == "shade":
        mon = Monster(name, x, y, sprites.load_sprite(7, 15, constants.WHITE), hp=20, ac=20, lvl=7)

    settings.monsters.append(mon)
    return mon