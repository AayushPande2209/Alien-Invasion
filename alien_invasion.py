'''
alien_invasion.py

Main file for the Alien Shooter game.
'''

import random
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien_fleet import AlienFleet
from boss import Boss
from powerup import PowerUp
from starfield import Starfield
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

        self.starfield = Starfield(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = AlienFleet(self)

        self.boss = None

        self.powerups = []

        self.explosions = []

        self.stats = GameStats(self)

        self.scoreboard = Scoreboard(self)

        self.game_over = False

        self.play_button = Button(
            self,
            'Play'
        )

        self.restart_button = Button(
            self,
            'Restart'
        )

    def run_game(self):
        '''Start the main game loop.'''

        while True:

            self.check_events()

            self.starfield.update()

            if self.stats.game_active:

                self.ship.update()

                self.bullets.update()

                self.aliens.update()

                self.update_bullets()

                self.update_explosions()

                self.update_powerups()

                if self.boss:
                    self.boss.update()

                self.check_ship_collisions()

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

        bullets_allowed = self.settings.bullets_allowed

        if self.ship.bullet_power:
            bullets_allowed = self.settings.bullets_allowed_boosted

        if len(self.bullets) < bullets_allowed:

            bullet = Bullet(self)

            self.bullets.add(
                bullet
            )

    def update_bullets(self):
        '''Update bullets and check hits against aliens and the boss.'''

        for bullet in self.bullets.copy():

            if bullet.rect.bottom <= 0:
                self.bullets.remove(
                    bullet
                )

        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens.aliens,
            True,
            False
        )

        if collisions:

            for aliens in collisions.values():

                for alien in aliens:

                    if alien.hit():

                        self.stats.score += alien.points

                        self.explosions.append(
                            Explosion(
                                self,
                                alien.rect.centerx,
                                alien.rect.centery
                            )
                        )

                        self.maybe_drop_powerup(
                            alien.rect.centerx,
                            alien.rect.centery
                        )

                        self.aliens.aliens.remove(
                            alien
                        )

            self.scoreboard.check_score()

        self.check_boss_hit()

    def check_boss_hit(self):
        '''Check bullet collisions against the boss.'''

        if not self.boss:
            return

        hit_bullets = [
            bullet for bullet in self.bullets
            if bullet.rect.colliderect(self.boss.rect)
        ]

        for bullet in hit_bullets:

            self.bullets.remove(bullet)
            self.boss.take_damage()

        if hit_bullets and self.boss.is_destroyed():

            self.explosions.append(
                Explosion(
                    self,
                    self.boss.rect.centerx,
                    self.boss.rect.centery
                )
            )

            self.stats.score += self.settings.boss_points

            self.scoreboard.check_score()

            self.boss = None
            self.stats.boss_active = False

            self.stats.next_level()

            self.aliens = AlienFleet(self)

    def maybe_drop_powerup(self, x, y):
        '''Occasionally drop a rapid fire power-up where an alien died.'''

        if random.random() < self.settings.powerup_spawn_chance:

            self.powerups.append(
                PowerUp(self, x, y)
            )

    def update_powerups(self):
        '''Move power-ups, remove stray ones, and check pickups.'''

        for powerup in self.powerups[:]:

            powerup.update()

            if powerup.rect.top > self.settings.screen_height:

                self.powerups.remove(powerup)

            elif powerup.rect.colliderect(self.ship.rect):

                powerup.activate(self.ship)

                self.powerups.remove(powerup)

    def check_ship_collisions(self):
        '''Check if an alien has hit the ship or reached the bottom.'''

        for alien in self.aliens.aliens.sprites():

            if alien.rect.colliderect(self.ship.rect):
                self.ship_hit()
                break

            if alien.rect.bottom >= self.settings.screen_height:
                self.ship_hit()
                break

    def ship_hit(self):
        '''Respond to the ship being hit by an alien.'''

        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1

            self.aliens.aliens.empty()
            self.bullets.empty()

            self.ship.center_ship()

        else:

            self.stats.game_active = False
            self.game_over = True

            self.stats.save_high_score()
            self.scoreboard.check_score()

    def check_level_complete(self):
        '''Start a new wave or boss fight when the level is cleared.'''

        if self.stats.boss_active:
            return

        if len(self.aliens.aliens) == 0:

            self.stats.next_level()

            if self.stats.is_boss_level():

                self.boss = Boss(
                    self
                )

                self.stats.boss_active = True

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
        '''Start or restart the game.'''

        if self.stats.game_active:
            return

        if not self.game_over and self.play_button.rect.collidepoint(mouse_pos):
            self.restart_game()

        elif self.game_over and self.restart_button.rect.collidepoint(mouse_pos):
            self.restart_game()

    def restart_game(self):
        '''Reset everything for a new game.'''

        self.settings.initialize_dynamic_settings()

        self.stats.reset_stats()
        self.stats.game_active = True
        self.game_over = False

        self.aliens = AlienFleet(self)
        self.boss = None

        self.bullets.empty()
        self.powerups = []
        self.explosions = []

        self.ship.center_ship()
        self.ship.bullet_power = False
        self.ship.power_timer = 0

        self.scoreboard.check_score()

    def update_screen(self):
        '''Draw everything on the screen.'''

        self.screen.fill(
            self.settings.bg_color
        )

        self.starfield.draw()

        if self.stats.game_active:

            self.ship.draw()

            self.bullets.draw(
                self.screen
            )

            self.aliens.draw()

            if self.boss:

                self.boss.draw()

            for powerup in self.powerups:

                powerup.draw()

            for explosion in self.explosions:

                explosion.draw()

            self.scoreboard.draw()

        elif self.game_over:

            self.draw_game_over()

        else:

            self.play_button.draw()

        pygame.display.flip()

    def draw_game_over(self):
        '''Draw the game over screen with final score and restart button.'''

        title_font = pygame.font.SysFont(None, 64)
        text_font = pygame.font.SysFont(None, 36)

        title_image = title_font.render(
            'Game Over', True, (255, 255, 255)
        )
        title_rect = title_image.get_rect()
        title_rect.center = self.screen.get_rect().center
        title_rect.y -= 120

        score_image = text_font.render(
            f'Final Score: {self.stats.score}', True, (255, 255, 255)
        )
        score_rect = score_image.get_rect()
        score_rect.center = self.screen.get_rect().center
        score_rect.y -= 60

        high_score_image = text_font.render(
            f'High Score: {self.stats.high_score}', True, (255, 255, 255)
        )
        high_score_rect = high_score_image.get_rect()
        high_score_rect.center = self.screen.get_rect().center
        high_score_rect.y -= 20

        self.screen.blit(title_image, title_rect)
        self.screen.blit(score_image, score_rect)
        self.screen.blit(high_score_image, high_score_rect)

        self.restart_button.draw()


if __name__ == '__main__':

    game = AlienInvasion()

    game.run_game()
