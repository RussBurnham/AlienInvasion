import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship.'''

    def __init__(self, ai_game):
        '''Create a bullet object at the ship's current position.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = ai_game.ship.rect.center

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store the angle of the bullet + 90degrees to shoot vertically
        self.angle = ai_game.ship.angle + 90

    def update(self):
        '''Move the bullet in the direction of the rotated ship.'''
        self.x += math.cos(math.radians(self.angle)) * self.settings.bullet_speed
        self.y -= math.sin(math.radians(self.angle)) * self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draw the bullet to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)
