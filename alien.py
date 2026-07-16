'''
alien.py

Contains the Alien class.
'''

import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, game, alien_type='normal'):
        '''Initialize the alien and set its starting position.'''

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.alien_type = alien_type

        self.image = pygame.image.load(
            'Assets/images/enemy_4.png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (60, 60)
        )

        if self.alien_type == 'strong':

            self.image = self.image.copy()

            self.image.fill(
                (255, 60, 60, 255),
                special_flags=pygame.BLEND_RGBA_MULT
            )

            self.health = 2
            self.points = self.settings.alien_points * 2

        else:

            self.health = 1
            self.points = self.settings.alien_points

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

    def hit(self):
        '''Reduce alien health. Return True if the alien is destroyed.'''

        self.health -= 1

        return self.health <= 0

    def update(self):
        '''Move the alien horizontally.'''

        self.x += (
            self.settings.alien_speed *
            self.settings.fleet_direction
        )

        self.rect.x = self.x