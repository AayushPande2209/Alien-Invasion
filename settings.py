'''
settings.py

Stores all settings for the Alien Shooter game.
'''


class Settings:
    def __init__(self):
        '''Initialize game settings.'''

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 30)
        self.game_title = 'Alien Shooter'

        # Frame rate
        self.FPS = 60

        # Ship settings
        self.ship_speed = 6
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 18
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.alien_speed = 2
        self.fleet_drop_speed = 25
        self.fleet_direction = 1
        self.alien_points = 50

        # Power-up settings
        self.powerup_speed = 3
        self.powerup_spawn_chance = 0.10
        self.powerup_duration = 600
        self.bullets_allowed_boosted = 8

        # Boss settings
        self.boss_speed = 3
        self.boss_health = 50
        self.boss_level_interval = 5
        self.boss_points = 1000

        # Alien variety
        self.strong_alien_chance = 0.15

        # Starfield settings
        self.star_count = 80

        # Difficulty scaling
        self.speedup_scale = 1.15
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Reset settings when a new game starts.'''

        self.ship_speed = 6

        self.bullet_speed = 10

        self.alien_speed = 2

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        '''Increase difficulty after each level.'''

        self.ship_speed *= (
            self.speedup_scale
        )

        self.bullet_speed *= (
            self.speedup_scale
        )

        self.alien_speed *= (
            self.speedup_scale
        )

        self.alien_points = int(
            self.alien_points *
            self.score_scale
        )