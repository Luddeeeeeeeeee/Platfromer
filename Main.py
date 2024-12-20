import pygame,sys
from Level import Level
from settings import *
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.Clock = pygame.time.Clock()
        self.level = Level()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((50,50,255))
            self.level.run()
            pygame.display.flip()
            self.Clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()