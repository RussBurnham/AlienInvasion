import pygame.font
import os

class Title:
    '''Display the title of the game at the top during pregame.'''
    def __init__(self, ai_game, text):
        '''Initialize Title.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the title.
        self.width, self.height = 825, 100
        self.background_color = (0, 0, 0)
        self.text_color = (188, 245, 69)
        self.font = pygame.font.Font(os.path.join(os.environ["Fonts"], "code.ttf"), 52)

        # Build the title rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 250

        # Render the text and store it in a variable
        self.text = self.font.render(text, True, self.text_color, 
            self.background_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
    
    def blitme(self):
        '''Draw Title with text.'''
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.text, self.text_rect)

class Instructions:
    '''Display instructions on the left side during pregame.'''
    def __init__(self, ai_game, text):
        '''Attributes of the instructions class.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Instructions attributes.
        self.width, self.height = 380, 315
        self.background_color = (0, 0, 0)
        self.text_color = (188, 245, 69)
        self.font = pygame.font.Font(os.path.join(os.environ["Fonts"], "code2.ttf"), 24)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx - 400
        self.rect.centery = self.screen_rect.centery + 50
        
        # Split the 'text' argument into strings with \n for formatting.
        self.text = text.split("\n") 
        # Render each string individually.
        self.rendered_text = [self.font.render(t, True, self.text_color, 
            self.background_color) for t in self.text]  
        # Create rects for each rendered string.
        self.text_rect = [t.get_rect() for t in self.rendered_text]  
        
    def blitme(self):
        '''Draw the instructions onto the screen.'''
        self.screen.fill(self.background_color, self.rect)
        # Start at the top of the rect to draw each rendered string.
        y_offset = 0  
        for i, t in enumerate(self.rendered_text):
            text_rect = self.text_rect[i]
            text_rect.left = self.rect.left + 10
            text_rect.top = self.rect.top + y_offset + 15
            self.screen.blit(t, text_rect)
            #  the next string.
            y_offset += text_rect.height  
