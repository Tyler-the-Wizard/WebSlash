import pygame, settings

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.DO_MAIN_LOOP = False