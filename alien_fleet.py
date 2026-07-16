'''
alien_fleet.py

Contains the AlienFleet class.
'''

import random

import pygame

from alien import Alien


class AlienFleet:
    def __init__(self, game):
        '''Create the alien fleet.'''

        self.game = game

        self.screen = game.screen
        self.settings = game.settings

        self.aliens = pygame.sprite.Group()

        self.create_fleet()

    def create_fleet(self):
        '''Create rows of aliens.'''

        alien = Alien(self.game)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = (
            self.settings.screen_width -
            (2 * alien_width)
        )

        number_aliens = available_space_x // (
            2 * alien_width
        )

        available_space_y = (
            self.settings.screen_height -
            (4 * alien_height)
        )

        number_rows = available_space_y // (
            2 * alien_height
        )

        for row_number in range(number_rows):

            for alien_number in range(number_aliens):

                self.create_alien(
                    alien_number,
                    row_number
                )

    def create_alien(self, alien_number, row_number):
        '''Create one alien in the fleet.'''

        if random.random() < self.settings.strong_alien_chance:
            alien = Alien(self.game, 'strong')
        else:
            alien = Alien(self.game, 'normal')

        alien.x = (
            alien.rect.width +
            2 * alien.rect.width *
            alien_number
        )

        alien.rect.x = alien.x

        alien.rect.y = (
            alien.rect.height +
            2 * alien.rect.height *
            row_number
        )

        self.aliens.add(
            alien
        )

    def check_fleet_edges(self):
        '''Check if the fleet reached an edge.'''

        for alien in self.aliens.sprites():

            if alien.check_edges():

                self.change_fleet_direction()

                break

    def change_fleet_direction(self):
        '''Move the fleet down and reverse direction.'''

        for alien in self.aliens.sprites():

            alien.rect.y += (
                self.settings.fleet_drop_speed
            )

        self.settings.fleet_direction *= -1

    def update(self):
        '''Move the alien fleet.'''

        self.check_fleet_edges()

        self.aliens.update()

    def draw(self):
        '''Draw all aliens.'''

        self.aliens.draw(
            self.screen
        )