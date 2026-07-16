'''
explosion.py

Contains the Explosion class.
'''

import pygame


class Explosion:
    def __init__(self, game, x, y):
        '''Create an explosion effect.'''

        self.screen = game.screen

        self.x = x
        self.y = y

        self.radius = 10
        self.max_radius = 50

        self.active = True

        self.timer = 0

    def update(self):
        '''Animate the explosion.'''

        self.radius += 2
        self.timer += 1

        if self.radius >= self.max_radius:
            self.active = False

    def draw(self):
        '''Draw the explosion.'''

        if self.active:
            pygame.draw.circle(
                self.screen,
                (255, 120, 0),
                (self.x, self.y),
                self.radius
            )

            pygame.draw.circle(
                self.screen,
                (255, 255, 0),
                (self.x, self.y),
                self.radius // 2
            )