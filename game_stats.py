'''
game_stats.py

Contains the GameStats class.
'''


class GameStats:
    def __init__(self, game):
        '''Initialize game statistics.'''

        self.settings = game.settings

        self.reset_stats()

        self.game_active = False

        self.high_score = 0
        self.load_high_score()

        self.boss_active = False

    def reset_stats(self):
        '''Reset statistics for a new game.'''

        self.ships_left = (
            self.settings.ship_limit
        )

        self.score = 0

        self.level = 1

        self.boss_active = False

    def next_level(self):
        '''Increase level after defeating a fleet.'''

        self.level += 1

        self.settings.increase_speed()

    def is_boss_level(self):
        '''Check if current level is a boss level.'''

        return (
            self.level %
            self.settings.boss_level_interval
            == 0
        )

    def load_high_score(self):
        '''Load the saved high score from file, if it exists.'''

        try:
            with open('high_score.txt') as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def save_high_score(self):
        '''Save the high score to file if the current score beats it.'''

        if self.score > self.high_score:
            self.high_score = self.score

        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))