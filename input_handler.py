import pygame

import settings

def handle(event):
    # Movement
    if event.key == pygame.K_y or event.key == pygame.K_q:
        settings.player.move(-1, -1)
    if event.key == pygame.K_u or event.key == pygame.K_e:
        settings.player.move(1, -1)
    if event.key == pygame.K_h or event.key == pygame.K_a or event.key == pygame.K_LEFT:
        settings.player.move(-1, 0)
    if event.key == pygame.K_j or event.key == pygame.K_s or event.key == pygame.K_DOWN:
        settings.player.move(0, 1)
    if event.key == pygame.K_k or event.key == pygame.K_w or event.key == pygame.K_UP:
        settings.player.move(0, -1)
    if event.key == pygame.K_l or event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        settings.player.move(1, 0)
    if event.key == pygame.K_b or event.key == pygame.K_z:
        settings.player.move(-1, 1)
    if event.key == pygame.K_n or event.key == pygame.K_c:
        settings.player.move(1, 1)

    # Items
    if event.key == pygame.K_RETURN:
        settings.player.pickup()
    if event.key == pygame.K_x:
        pass