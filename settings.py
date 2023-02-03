import pygame

class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (172, 118, 216)
        # Ship settings.
        self.ship_speed = 5.0
        # Bullet settings.
        self.bullet_speed = 8.0
        self.bullet_width = 3.5
        self.bullet_height = 10
        self.bullet_color = (255, 201, 14)
        self.bullets_allowed = 10
        # Ship rotation settings.
        self.ship_rotation_speed = 1.5
        self.ship_image_original = pygame.image.load('C:/Users/User/Pictures/ship.bmp')
        self.ship_image = self.ship_image_original
        self.ship_rect = self.ship_image.get_rect()
        self.ship_angle = 90

