import sys
import pygame

class AlienInvasion:

    '''General class, that rules game's resources and behevior'''

    def __init__(self):
        
        '''Initiate game,create game resources'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption ('Alien invasion')
        self.bg_color = (230,230,230)

    def run_game(self):
        '''Begin the main cycle of the game'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill (self.bg_color) 
                pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

