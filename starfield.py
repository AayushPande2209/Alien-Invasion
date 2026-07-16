'''
starfield.py

Contains the Starfield class for the moving space background.
'''

import random
import pygame


class Starfield:
    def __init__(self, game):
        '''Create a field of stars.'''

        self.screen = game.screen
        self.settings = game.settings

        self.stars = [
            self.new_star(random.randint(0, self.settings.screen_height))
            for _ in range(self.settings.star_count)
        ]

    def new_star(self, y):
        '''Create one star with a random position and speed.'''

        return {
            'x': random.randint(0, self.settings.screen_width),
            'y': y,
            'size': random.randint(1, 3),
            'speed': random.uniform(1, 3)
        }

    def update(self):
        '''Move stars downward and recycle ones that leave the screen.'''

        for star in self.stars:

            star['y'] += star['speed']

            if star['y'] > self.settings.screen_height:
                star.update(self.new_star(0))

    def draw(self):
        '''Draw all stars.'''

        for star in self.stars:

            pygame.draw.circle(
                self.screen,
                (255, 255, 255),
                (int(star['x']), int(star['y'])),
                star['size']
            )
