'''
boss.py

Contains the Boss class.
'''

import pygame


class Boss:
    def __init__(self, game):
        '''Initialize the boss.'''

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            'Assets/images/Starbasesnow.png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (180, 120)
        )

        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()

        self.rect.midtop = (
            self.screen_rect.centerx,
            40
        )

        self.x = float(self.rect.x)

        self.health = self.settings.boss_health

        self.moving_right = True

    def update(self):
        '''Move the boss across the screen.'''

        if self.moving_right:
            self.x += self.settings.boss_speed
        else:
            self.x -= self.settings.boss_speed

        self.rect.x = self.x

        if self.rect.right >= self.screen_rect.right:
            self.moving_right = False

        if self.rect.left <= 0:
            self.moving_right = True

    def take_damage(self):
        '''Reduce boss health.'''

        self.health -= 1

    def is_destroyed(self):
        '''Return True when boss health reaches zero.'''

        return self.health <= 0

    def draw(self):
        '''Draw the boss.'''

        self.screen.blit(
            self.image,
            self.rect
        )