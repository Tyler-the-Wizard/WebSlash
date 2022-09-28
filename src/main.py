import settings
settings.init()

import pygame
pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)

import events
import monsters

test_mon = monsters.Monster()
settings.GAME_MONSTERS.append(test_mon)

# Main game loop
while settings.DO_MAIN_LOOP:
    events.handle_events(pygame.event.get())

    for tile in settings.GAME_TILES:
        pass
    for monster in settings.GAME_MONSTERS:
        monster.draw(screen)
    for item in settings.GAME_ITEMS:
        pass
    
    pygame.display.flip()