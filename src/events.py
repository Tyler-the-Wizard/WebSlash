import pygame, settings

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.DO_MAIN_LOOP = False
        
        if event.type == pygame.KEYDOWN:
            # Standard movement
            if event.key == pygame.K_w:
                settings.PLAYER.y -= 1
            if event.key == pygame.K_s:
                settings.PLAYER.y += 1
            if event.key == pygame.K_a:
                settings.PLAYER.x -= 1
            if event.key == pygame.K_d:
                settings.PLAYER.x += 1

            # Diagonal movement
            if event.key == pygame.K_q:
                settings.PLAYER.y -= 1
                settings.PLAYER.x -= 1
            if event.key == pygame.K_e:
                settings.PLAYER.y -= 1
                settings.PLAYER.x += 1
            if event.key == pygame.K_z:
                settings.PLAYER.y += 1
                settings.PLAYER.x -= 1
            if event.key == pygame.K_c:
                settings.PLAYER.y += 1
                settings.PLAYER.x += 1
            
            # Holding still for a turn
            if event.key == pygame.K_x:
                pass # TODO when turns are implemented