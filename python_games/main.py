import sys
import pygame
from ship import Ship
import game_functions as gf
from bullets import Bullet
from pygame.sprite import Group
from alien import Alien
from stats import Gamestats
from button import Button
from score_board import ScoreBoard

def run_game():
    """Iniatialize game and create a screen object"""
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    # Set background color
    bg_color=(230,230,230)
    ship=Ship(screen)
    button=Button(screen,'Play')
    bullets=Group()
    aliens=Group()
    count=3
    stats=Gamestats()
    last_alien_time=0
    interval=3000
    sb=ScoreBoard(screen,stats)
    #Start the main loop
    while True:
        if stats.game_active:
            gf.check_events(sb,ship,screen,bullets,button,stats,aliens)
            bullets.update()
            ship.update()
            screen.blit(ship.background,(0,0))
            ship.blitme()
            for bullet in bullets.sprites():
                bullet.draw_bullet()
            last_alien_time=gf.generate_aliens(aliens,screen, last_alien_time,interval)
            gf.collision(bullets,aliens,stats,sb)
            gf.check_aliens_bottom(ship, screen, aliens, count, button, stats, bullets,sb)
            sb.show_score()
            if not stats.game_active:
                button.draw_button()
            pygame.display.flip()
        else:
            gf.check_events(sb,ship,screen,bullets,button,stats,aliens)
            button.draw_button()
run_game()