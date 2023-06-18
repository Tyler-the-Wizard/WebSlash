from math import ceil
from random import randint, random

from colors import palette_color as color
import constants
from message import new as say, proper
import settings
from spriteloader import sprite

def factory(mon_name, x, y):
    '''Creates a monster and returns it.'''
    if mon_name not in mon_lib:
        print(f'monsters.py: monster \'{mon_name}\' not found!')
        mon_name = 'unknown'

    args = mon_lib[mon_name]

    mon = Monster(mon_name, x, y, *args)
    return mon

mon_lib = {
#   'mon_name' : ['Display Name', speed, max_health, collision, sprite(x, y, color)]
    'player' : ['PLAYER', 60, 10, constants.CL_NONE, sprite(3, 8, color(constants.C_FG))],
    'unknown' : ['???', 60, -1, 255, sprite(14, 6, color(constants.C_MAGENTA))],
    'goblin' : ['', 60, 3, constants.CL_NONE, sprite(2, 17, color(constants.C_GREEN))],
    'golem' : ['', 30, 50, constants.CL_NONE, sprite(9, 23, color(constants.C_GRAY))],
    'snake' : ['', 180, 5, constants.CL_NONE, sprite(8, 14, color(constants.C_CYAN))],
}

def add_to_level(mon_name, x, y):
    '''Creates a monster on the current level'''
    mon = factory(mon_name, x, y)
    settings.GAME.get_current_level().monsters.append(mon)

class Monster:
    def __init__(self, mon_name, x, y, display_name, speed, hp, collision, sprite) -> None:
        self.mon_name = mon_name
        self.x = x
        self.y = y

        self.display_name = display_name
        self.speed = speed
        self.max_hp = hp
        self.hp = hp

        self.collision = collision
        self.sprite = sprite

        # Used to keep track of when this monster can move
        self.turn_count = 0.0

        self.regen = 10

    def draw(self, surface, camera=(0, 0)):
        surface.blit(self.sprite, (self.x * settings.TILE_SCALE - camera[0], self.y * settings.TILE_SCALE - camera[1]))

    def do_turn(self):
        '''This function is called whenever this
        monster takes its turn. It includes
        things like moving towards the player,
        attacking, and fleeing.'''
        self.turn_count += self.speed / settings.PLAYER.speed * (random() + 0.5)
        self.turn_count = round(self.turn_count, 3)
        while self.turn_count >= 1:
            self.turn_count -= 1
            do_move = True
            tries = 4
            while do_move and tries > 0:
                tries -= 1
                dx = 0
                dy = 0
                if settings.PLAYER.los(self.x, self.y):
                    # The player sees us, we see the player. Move towards it.
                    if settings.PLAYER.x < self.x:
                        dx = -1
                    elif settings.PLAYER.x > self.x:
                        dx = 1

                    if settings.PLAYER.y < self.y:
                        dy = -1
                    elif settings.PLAYER.y > self.y:
                        dy = 1

                else:
                    # Pick a random square to move to
                    dx = randint(-1, 1)
                    dy = randint(-1, 1)

                if dx == 0 and dy == 0:
                    continue

                # Try to attack first
                do_move = not self.try_attack(self.x + dx, self.y + dy)
                if do_move:
                    # If we can't attack, try to move
                    do_move = not self.try_move(self.x + dx, self.y + dy)

    def do_regen(self):
        if self.hp < self.max_hp and randint(1, self.regen) == 1:
            self.hp += 1

    def can_move(self, x, y):
        '''Returns true if this monster's collision
        allows it to validly move to the x, y position.'''
        level = settings.GAME.get_current_level()
        if x < 0 or x >= level.tilemap.size[0] or y < 0 or y >= level.tilemap.size[1]:
            return False

        tile_collision = level.tilemap.tiles[x][y].collision
        return tile_collision == tile_collision & self.collision

    def get_name(self):
        if self.display_name:
            return self.display_name
        return f'the {self.mon_name}'

    def move(self, x, y):
        '''Moves the monster to the x, y position.
        This function can move the monster to an
        "invalid" position according to its collision.'''
        self.x = x
        self.y = y

    def try_move(self, x, y):
        '''Moves the monster to the x, y position
        ONLY if it can validly move there.'''
        can_move = self.can_move(x, y)
        if can_move:
            self.move(x, y)

        return can_move

    def take_damage(self, amount):
        '''Causes this monster to take some damage.'''
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.die()

    def die(self):
        '''This function is called when this monster dies.'''
        if self == settings.PLAYER:
            # TODO Special death functionality
            say('You die...')
        else:
            say(f'{proper(self.get_name())} is killed!')
            settings.GAME.get_current_level().monsters.remove(self)

    def attack(self, target):
        '''Attacks the target monster with a basic attack.'''
        target.take_damage(ceil(self.max_hp / 10))

        # Print a message about what just happened
        if target.hp <= 0:
            return

        if self == settings.PLAYER:
            say(f'You hit {target.get_name()}!')

        elif target == settings.PLAYER:
            say(f'{proper(self.get_name())} hits you!')

    def try_attack(self, x, y):
        '''Attempts to attack the x, y position
        ONLY if there is a monster there.'''
        level = settings.GAME.get_current_level()
        for mon in level.monsters:
            if mon.x == x and mon.y == y:
               self.attack(mon)
               return True

        return False
