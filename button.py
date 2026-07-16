'''
button.py

Contains the Button class.
'''

import pygame.font


class Button:
    def __init__(self, game, message):
        '''Create a button.'''

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 200
        self.height = 60

        self.button_color = (0, 200, 0)
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont(
            None,
            48
        )

        self.rect = pygame.Rect(
            0,
            0,
            self.width,
            self.height
        )

        self.rect.center = self.screen_rect.center

        self.prep_message(message)

    def prep_message(self, message):
        '''Turn message into an image.'''

        self.message_image = self.font.render(
            message,
            True,
            self.text_color
        )

        self.message_rect = (
            self.message_image.get_rect()
        )

        self.message_rect.center = (
            self.rect.center
        )

    def draw(self):
        '''Draw the button and text.'''

        pygame.draw.rect(
            self.screen,
            self.button_color,
            self.rect
        )

        self.screen.blit(
            self.message_image,
            self.message_rect
        )