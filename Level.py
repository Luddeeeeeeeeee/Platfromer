import pygame
from settings import *

class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstical_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            print(row)
            print(row_index)

    def run(self):
        pass