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