'''
alien_invasion.py

Main file for the Alien Shooter game.
'''

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien_fleet import AlienFleet
from boss import Boss
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from explosion import Explosion


class AlienInvasion:
    def __init__(self):
        '''Initialize the game.'''

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height
            )
        )

        pygame.display.set_caption(
            self.settings.game_title
        )

        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = AlienFleet(self)

        self.boss = None

        self.explosions = []

        self.stats = GameStats(self)

        self.scoreboard = Scoreboard(self)

        self.play_button = Button(
            self,
            'Play'
        )

    def run_game(self):
        '''Start the main game loop.'''

        while True:

            self.check_events()

            if self.stats.game_active:

                self.ship.update()

                self.bullets.update()

                self.aliens.update()

                self.update_bullets()

                self.update_explosions()

                if self.boss:
                    self.boss.update()

                self.check_level_complete()

            self.update_screen()

            self.clock.tick(
                self.settings.FPS
            )

    def check_events(self):
        '''Handle keyboard and mouse input.'''

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_play_button(
                    pygame.mouse.get_pos()
                )

    def check_keydown_events(self, event):
        '''Handle key presses.'''

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        '''Handle key releases.'''

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        '''Create a laser bullet.'''

        if len(self.bullets) < self.settings.bullets_allowed:

            bullet = Bullet(self)

            self.bullets.add(
                bullet
            )

    def update_bullets(self):
        '''Update bullets and check hits.'''

        for bullet in self.bullets.copy():

            if bullet.rect.bottom <= 0:
                self.bullets.remove(
                    bullet
                )

        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens.aliens,
            True,
            True
        )

        if collisions:

            for aliens in collisions.values():

                for alien in aliens:

                    self.stats.score += (
                        self.settings.alien_points
                    )

                    self.explosions.append(
                        Explosion(
                            self,
                            alien.rect.centerx,
                            alien.rect.centery
                        )
                    )

            self.scoreboard.check_score()

    def check_level_complete(self):
        '''Start a new wave when aliens are defeated.'''

        if len(self.aliens.aliens) == 0:

            self.stats.next_level()

            if self.stats.is_boss_level():

                self.boss = Boss(
                    self
                )

            else:

                self.aliens = AlienFleet(
                    self
                )

    def update_explosions(self):
        '''Update explosion effects.'''

        for explosion in self.explosions[:]:

            explosion.update()

            if not explosion.active:

                self.explosions.remove(
                    explosion
                )

    def check_play_button(self, mouse_pos):
        '''Start the game.'''

        if self.play_button.rect.collidepoint(
            mouse_pos
        ):

            self.stats.game_active = True

    def update_screen(self):
        '''Draw everything on the screen.'''

        self.screen.fill(
            self.settings.bg_color
        )

        if self.stats.game_active:

            self.ship.draw()

            self.bullets.draw(
                self.screen
            )

            self.aliens.draw(
                self.screen
            )

            if self.boss:

                self.boss.draw()

            for explosion in self.explosions:

                explosion.draw()

            self.scoreboard.draw()

        else:

            self.play_button.draw()

        pygame.display.flip()


if __name__ == '__main__':

    game = AlienInvasion()

    game.run_game()