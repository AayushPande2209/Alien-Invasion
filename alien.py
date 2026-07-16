'''
alien.py

Contains the Alien class.
'''

import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, game):
        '''Initialize the alien and set its starting position.'''

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            'Assets/enemy_4.png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (60, 60)
        )

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        '''Return True if the alien reaches the screen edge.'''

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        if self.rect.left <= 0:
            return True

        return False

    def update(self):
        '''Move the alien horizontally.'''

        self.x += (
            self.settings.alien_speed *
            self.settings.fleet_direction
        )

        self.rect.x = self.x