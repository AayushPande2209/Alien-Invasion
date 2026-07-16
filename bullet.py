'''
bullet.py

Contains the Bullet class.
'''

import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game):
        '''Create a laser bullet from the ship position.'''

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            'Assets/images/laserBlast.png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (20, 50)
        )

        self.rect = self.image.get_rect()

        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        '''Move the bullet upward.'''

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y