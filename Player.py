import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/Player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (250,350))
        self.gravity = 0


    def move(self):
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_a]:
            self.rect.x -= 5

        if keys[pygame.K_d]:
            self.rect.x += 5

        self.gravity += 0.1
        self.rect.y += self.gravity           


    def update(self,):
        self.move()