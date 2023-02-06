import pygame
from pygame.sprite import Sprite
from random import randint

class Stars(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        '''Initialize and load random saved stars onto background of screen.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading 4 different saved files, selected at random.
        self.image = pygame.image.load('C:/Users/User/Pictures/star{}.bmp'.format(randint(1, 4)))
        self.rect = self.image.get_rect()

        # Randomize where the star is placed on the game screen.
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(0, self.settings.screen_height)

    def blitme(self):
        '''Draw the star'''
        self.screen.blit(self.image, self.rect)

class StarField:
    '''A class to represent the starfield'''
    def __init__(self, ai_game):
        '''Initialize the starfield'''
        self.stars = pygame.sprite.Group()
        self.ai_game = ai_game

        # Placing 50 stars in game screen.
        for i in range(50):
            star = Stars(self.ai_game)
            self.stars.add(star)
        
    def draw(self):
        '''Draw the starfield'''
        for star in self.stars.sprites():
            star.blitme()

        
        
        