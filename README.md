# Alien Shooter 


A Python Pygame-based space shooter game inspired by the classic Alien Invasion arcade style game.

The player controls a spaceship, fights waves of alien enemies, earns points, and progresses through increasingly difficult levels.

## Features

- Player-controlled spaceship movement
- Laser shooting system
- Alien enemy fleets
- Collision detection
- Score tracking
- Level progression
- Increasing difficulty
- Explosion effects
- Boss battle system
- Power-up system
- Custom spaceship and alien assets
- Space-themed gameplay

## Controls

| Key | Action |
|-----|--------|
| Left Arrow | Move ship left |
| Right Arrow | Move ship right |
| Space | Fire laser |
| Q | Quit game |

## Project Structure


Alien-Invasion/
│
├── alien_invasion.py
├── settings.py
├── ship.py
├── bullet.py
├── alien.py
├── alien_fleet.py
├── boss.py
├── powerup.py
├── explosion.py
├── button.py
├── game_stats.py
├── scoreboard.py
│
└── Assets/
├── ship2(no bg).png
├── enemy_4.png
├── laserBlast.png
├── Starbasesnow.png
└── other game assets


## Requirements

- Python 3.x
- Pygame

Install pygame with:

```bash
pip install pygame
Running the Game

Clone the repository:

git clone https://github.com/AayushPande2209/Alien-Invasion.git

Navigate into the project folder:

cd Alien-Invasion

Run the game:

python alien_invasion.py
How to Play
Start the game.
Move your spaceship using the arrow keys.
Shoot incoming aliens with your laser.
Destroy enemies to earn points.
Survive increasingly difficult waves.
Defeat bosses that appear during progression.
Development

This project was built using object-oriented programming principles.

Major classes include:

Ship - Controls player movement and appearance
Bullet - Handles player projectiles
Alien - Represents enemy ships
AlienFleet - Manages groups of enemies
Boss - Handles boss enemies
PowerUp - Handles special abilities
Scoreboard - Displays game information
Future Improvements

Possible future additions:

More enemy types
Additional weapons
More power-ups
Sound effects
Background music
More boss variations
Saveable player statistics
Credits

Created using Python and Pygame.

Game assets are stored in the Assets folder and are used for educational and personal project purposes.