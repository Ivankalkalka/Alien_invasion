import pygame

class Ship:
    '''Class for ship manage'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("/Users/ivankakalka/Desktop/Alien_invasion/Alien_invasion/Images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)