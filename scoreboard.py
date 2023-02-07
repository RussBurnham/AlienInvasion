from pygame import transform
import pygame.font
from pygame.sprite import Group
from ship import Ship
import os

class Scoreboard:
    '''A class to report scoring information.'''

    def __init__(self, ai_game):
        '''Initialize scorekeeping attributes.'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (188, 245, 69)
        self.black_fill = (0, 0, 0)
        self.font = pygame.font.Font(os.path.join(os.environ["Alien_Invasion"], "code2.ttf"), 24)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''Turn the score into a rendered image.'''
        rounded_score = round(self.stats.score, -1)
        score_str = f"score {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        '''Turn the high score into a rendered image.'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"high_score {high_score:,}"
        high_score_font = pygame.font.Font(os.path.join(os.environ["Alien_Invasion"], "code2.ttf"), 28)
        self.high_score_image = high_score_font.render(high_score_str, 
            True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def check_high_score(self):
        '''Check to see if there's a new high score.'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        '''Turn the level into a renedered image.'''
        level_str = str(self.stats.level)
        level = f"level {level_str}"
        self.level_image = self.font.render(level, True, 
            self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        '''Show how many ships are left on top left of screen.'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            # Transform the ship to smaller image for asthetics.
            ship_image = pygame.transform.scale(ship.image, (43, 49))
            ship_rect = ship_image.get_rect()
            ship.image, ship.rect = ship_image, ship_rect
            ship.rect.x = 20 + ship_number * (ship.rect.width + 20)
            self.ships.add(ship)

    def show_score(self):
        '''Draw scores, ships, and level to the screen.'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    # Extra.

    def level_up(self):
        '''Display LEVEL UP when all aliens cleared.'''
        level_up_font = pygame.font.Font(os.path.join(os.environ["Alien_Invasion"], "code.ttf"), 88)
        self.level_up_image = level_up_font.render("LEVEL UP!!!", True, 
            self.text_color, self.black_fill)
        self.level_up_rect = self.level_up_image.get_rect()
        self.level_up_rect.center = self.screen_rect.center
        self.screen.blit(self.level_up_image, self.level_up_rect)
        self.levelup_sound = pygame.mixer.Sound(os.path.join
            (os.environ["Music"], "levelup.wav"))
        self.levelup_sound.set_volume(0.8)
        self.levelup_sound.play()
        pygame.display.update()
        pygame.time.wait(1000)

