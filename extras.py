import pygame
import os

class Explosion:
    '''Create an explosion that hits aliens. 2 pics saved.'''
    def __init__(self, ai_game, image_number):
        '''Initialize the explosion.'''  
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(os.path.join(
            os.environ["Pictures"], "explosion{}.bmp".format(image_number)))
        self.rect = self.image.get_rect()

    def play(self):
        '''Play boom sound.'''
        self.sound = pygame.mixer.Sound(os.path.join(os.environ["Music"], "boom.wav"))
        self.sound.set_volume(0.08)
        self.sound.play()

    def blitme(self):
        '''Draw the explosion.'''
        self.screen.blit(self.image, self.rect)


class Music:
    def __init__(self):
        '''Looping game theme music.'''
        self.sound = pygame.mixer.Sound(os.path.join(os.environ["Music"], "spaceship.wav"))
        self.sound.set_volume(0.2)
        self.sound.play(loops=-1)



