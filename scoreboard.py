'''
scoreboard.py

Contains the Scoreboard class.
'''

import pygame.font


class Scoreboard:
    def __init__(self, game):
        '''Initialize scoreboard settings.'''

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont(
            None,
            36
        )

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        '''Create the score image.'''

        score_text = str(self.stats.score)

        self.score_image = self.font.render(
            score_text,
            True,
            self.text_color
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = (
            self.screen_rect.right - 20
        )
        self.score_rect.top = 20

    def prep_high_score(self):
        '''Create the high score image.'''

        high_score_text = (
            f'High Score: {self.stats.high_score}'
        )

        self.high_score_image = self.font.render(
            high_score_text,
            True,
            self.text_color
        )

        self.high_score_rect = (
            self.high_score_image.get_rect()
        )

        self.high_score_rect.centerx = (
            self.screen_rect.centerx
        )

        self.high_score_rect.top = 20

    def prep_level(self):
        '''Create the level image.'''

        level_text = (
            f'Level: {self.stats.level}'
        )

        self.level_image = self.font.render(
            level_text,
            True,
            self.text_color
        )

        self.level_rect = (
            self.level_image.get_rect()
        )

        self.level_rect.left = 20
        self.level_rect.top = 20

    def check_score(self):
        '''Update scoreboard values.'''

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def draw(self):
        '''Draw scoreboard information.'''

        self.screen.blit(
            self.score_image,
            self.score_rect
        )

        self.screen.blit(
            self.high_score_image,
            self.high_score_rect
        )

        self.screen.blit(
            self.level_image,
            self.level_rect
        )