import pygame
from Player import player
pygame.init()

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700,800))
        self.Clock = pygame.time.Clock()
        self.Player = pygame.sprite.GroupSingle(player())


    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill((50,50,255))
            
            self.Player.draw(self.screen)
            self.Player.update()

            pygame.display.flip()
            self.Clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()