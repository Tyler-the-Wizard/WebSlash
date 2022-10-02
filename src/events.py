import pygame, settings

def player_move(dx, dy):
    '''Convenience function for player movement'''
    if settings.PLAYER.try_move(
        settings.PLAYER.x + dx,
        settings.PLAYER.y + dy,
    ):
        # Advance the turn
        pass # TODO when turns are implemented

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.DO_MAIN_LOOP = False
        
        if event.type == pygame.KEYDOWN:
            # Standard movement
            if event.key == pygame.K_w:
                player_move(0, -1)
            if event.key == pygame.K_s:
                player_move(0, 1)
            if event.key == pygame.K_a:
                player_move(-1, 0)
            if event.key == pygame.K_d:
                player_move(1, 0)

            # Diagonal movement
            if event.key == pygame.K_q:
                player_move(-1, -1)
            if event.key == pygame.K_e:
                player_move(1, -1)
            if event.key == pygame.K_z:
                player_move(-1, 1)
            if event.key == pygame.K_c:
                player_move(1, 1)
            
            # Holding still for a turn
            if event.key == pygame.K_x:
                pass # TODO when turns are implemented