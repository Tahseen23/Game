import pygame 
from pygame.sprite import Group
from alien import Alien
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    alien_timer = 0
    interval = 5000  # 5 seconds in milliseconds

    # Flag to track if an alien is present
    alien_present = False

    clock = pygame.time.Clock()
    while True:
        gf.check_events(ship, screen, bullets)
        bullets.update()
        ship.update()

        screen.fill(bg_color)
        ship.blitme()

        # Update and draw existing aliens
        aliens.update()
        aliens.draw(screen)

        # If no alien is present, create one after the interval
        if not alien_present:
            alien_timer += clock.get_time()
            if alien_timer >= interval:
                # Reset the timer
                alien_timer = 0
                # Create a new alien
                alien = Alien(screen)
                aliens.add(alien)
                alien_present = True

        pygame.display.flip()
        clock.tick(60)

run_game()
