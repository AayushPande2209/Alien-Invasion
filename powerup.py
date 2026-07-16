'''
powerup.py

Contains the PowerUp class.
'''

import pygame


class PowerUp:
    def __init__(self, game, x, y):
        '''Initialize the power-up.'''

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            'Assets/images/beams.png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)

        self.type = 'rapid_fire'

    def update(self):
        '''Move the power-up downward.'''

        self.y += self.settings.powerup_speed
        self.rect.y = self.y

    def draw(self):
        '''Draw the power-up.'''

        self.screen.blit(
            self.image,
            self.rect
        )

    def activate(self, ship):
        '''Apply the power-up effect.'''

        if self.type == 'rapid_fire':
            ship.bullet_power = True
            ship.power_timer = self.settings.powerup_duration