import pygame
import sys
from ship import Ship
from bullets import Bullet
from time import sleep
from alien import Alien
import sound_effect
from stats import Gamestats
from time import sleep
def check_events(sb,ship,screen,bullets,button,stats,aliens):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(sb,screen,mouse_x,mouse_y,button,stats,aliens,bullets,ship)

def check_play_button(sb,screen,mouse_x,mouse_y,button,stats,aliens,bullets,ship):
    button_clicked=button.rect.collidepoint(mouse_x,mouse_y)
    if button.rect.collidepoint(mouse_x,mouse_y):
        stats.reset_score()
        stats.game_active=True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_remaining_ship()


        aliens.empty()
        bullets.empty()
        ship.center_ship()


        
def check_keydown_events(event,ship,screen,bullets):
    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    elif event.key==pygame.K_LEFT:
        ship.move_left=True
    elif event.key==pygame.K_SPACE:
        create_and_update_bullet(screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()
        
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.move_right=False
    elif event.key==pygame.K_LEFT:
        ship.move_left=False

def create_and_update_bullet(screen ,ship,bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    if len(bullets)<3:
        new_bullets=Bullet(screen,ship)
        bullets.add(new_bullets)
        sound_effect.bullet_sound.play()
        
    
    
def generate_aliens(aliens, screen, last_alien_time, interval):
    current_time = pygame.time.get_ticks()
    time_since_last_alien = current_time - last_alien_time

    if time_since_last_alien >= interval:
        # Create a new alien if the interval has elapsed
        alien = Alien(screen)
        #aliens.empty()  # Remove any existing aliens
        aliens.add(alien)  # Add the new alien to the group
        last_alien_time = current_time  # Update the last alien time

    # Update and draw the aliens
    aliens.update()
    for alien in aliens.sprites():
        alien.blitme()

    return last_alien_time  # Return the updated last alien time

def collision(bullets,aliens,stats,sb):
    collision=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collision:
        sound_effect.blast_sound.play()
        for aliens in collision.values():
            stats.score+=10
            sb.prep_score()
        check_high_score(stats,sb)
    if 0 <= stats.score <= 50 and stats.level == 1:
        stats.level = 1
        sb.prep_level()
    elif stats.score > 50 and (stats.score ) // 50 > stats.level - 1:
        stats.level += 1
        sb.prep_level()



def check_aliens_bottom(ship,screen,aliens,count,button,stats,bullets,sb):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            count-=1
    if count<=0:
        if stats.ship_limit>0:
            count=3
            stats.ship_limit -=1
            sb.prep_remaining_ship()
            aliens.empty()
            bullets.empty()
            ship.center_ship()

            sleep(0.5)
        else:
            stats.game_active=False




def check_high_score(stats,sb):
    """Check to see if there's a new high score"""
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()