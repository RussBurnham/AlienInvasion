import pygame

class Ship:
    '''A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Iniitialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.angle = 0

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/User/Pictures/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.rotating_right = False
        self.rotating_left = False

        # Get the original image's rect and then get the rotated image's rect
        self.rect = self.image.get_rect()
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_image.get_rect()

        # Center the rotated rect on the original rect
        self.rotated_rect.center = self.rect.center
    
    def update(self):
        '''Update the ship's position based on the movement flags.'''
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        angle_changed = False
        if self.rotating_right:
            self.angle -= self.settings.ship_rotation_speed
            angle_changed = True
        if self.rotating_left:
            self.angle += self.settings.ship_rotation_speed
            angle_changed = True

        if angle_changed:
            self.rotated_image = pygame.transform.rotate(self.image, self.angle)
            self.rotated_rect = self.rotated_image.get_rect()
            self.rotated_rect.center = self.rect.center
        
        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.rotated_image, self.rect)
