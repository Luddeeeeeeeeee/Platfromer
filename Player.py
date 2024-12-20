import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/Player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (250,350))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        move_vector = [0,0]

        if keys[pygame.K_a]:
            move_vector[0] -= 1

        if keys[pygame.K_d]:
            move_vector[0] += 1

        if keys[pygame.K_w]:
            move_vector[1] -= 1

        if keys[pygame.K_s]:
            move_vector[1] += 1

        if move_vector[0] != 0 and move_vector[1] != 0:
            move_vector[0] *= 0.7071  
            move_vector[1] *= 0.7071

        
        self.rect.x += move_vector[0] * self.speed
        self.rect.y += move_vector[1] * self.speed 


    def update(self,):
        self.move()