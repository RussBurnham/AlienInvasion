import pygame

class Explosion:
    def __init__(self, ai_game, image_number):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('C:/Users/User/Pictures/explosion{}.bmp'.format(image_number))
        self.rect = self.image.get_rect()

    def play(self):
        self.sound = pygame.mixer.Sound('C:/Users/User/Music/boom.wav')
        self.sound.set_volume(0.08)
        self.sound.play()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Music:
    def __init__(self):
        self.sound = pygame.mixer.Sound('C:/Users/User/Music/spaceship.wav')
        self.sound.set_volume(0.2)
        self.sound.play(loops=-1)



