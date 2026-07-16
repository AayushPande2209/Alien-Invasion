'''
ship.py

Contains the Ship class.
'''

import pygame


class Ship:
    def __init__(self, game):
        '''Initialize the ship and set its starting position.'''

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            'Assets/images/ship2(no bg).png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (80, 80)
        )

        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        self.bullet_power = False
        self.power_timer = 0

    def update(self):
        '''Update the ship position based on movement.'''

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

        if self.bullet_power:

            self.power_timer -= 1

            if self.power_timer <= 0:
                self.bullet_power = False

    def center_ship(self):
        '''Move the ship back to the starting position.'''

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20
        self.x = float(self.rect.x)

    def draw(self):
        '''Draw the ship on the screen.'''

        self.screen.blit(self.image, self.rect)