import sys
import pygame
from settings_1 import Settings1

class AlienInvasion:

    '''General class, that rules game's resources and behevior'''

    def __init__(self):
        
        '''Initiate game,create game resources'''
        pygame.init()
        self.settings = Settings1()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_heights))
        pygame.display.set_caption ('Alien invasion')
        
    def run_game(self):
        '''Begin the main cycle of the game'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill (self.settings.bg_color) 
                pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

