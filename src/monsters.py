import constants
import spriteloader

class Monster:
    def __init__(self) -> None:
        self.sprite = spriteloader.sprite(3, 8, constants.COLOR_RED)
        self.x = 2
        self.y = 5
    
    def draw(self, surface):
        surface.blit(self.sprite, (self.x * constants.TILE_SCALE, self.y * constants.TILE_SCALE))