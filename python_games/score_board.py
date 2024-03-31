import pygame.font
from ship import Ship

class ScoreBoard:
    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=stats

        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,30)
        self.text_font=pygame.font.SysFont(None,30)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_remaining_ship()

    
    def prep_score(self):
        """Turn the score into renderd image"""
        score=int(round(self.stats.score,-1))
        score_str = "{:,}".format(score)
        self.score_image=self.font.render(score_str,True,self.text_color)
        self.score_text = self.text_font.render('Score', True, self.text_color)
        self.score_text_rect=self.score_text.get_rect()

        #Display the score at the top right of screen
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_text_rect.top=self.screen_rect.top+20
        self.score_text_rect.right=self.screen_rect.right-50
        self.score_rect.top=self.screen_rect.top+20
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_text,self.score_text_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.text,self.text_rect)
        self.screen.blit(self.high_score_text,self.high_text_rect)
        self.screen.blit(self.ship_image,self.ship_rect)
        self.screen.blit(self.ship_text,self.ship_text_rect)

        


    
    def prep_high_score(self):
        """Turn the high score into rendered image."""
        high_score=int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color)
        self.high_score_text = self.text_font.render('High Score', True, self.text_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_text_rect=self.high_score_text.get_rect()
        self.high_text_rect.centerx=self.screen_rect.centerx-40
        self.high_score_rect.centerx=self.screen_rect.centerx+30
        self.high_score_rect.top = self.score_rect.top
        self.high_text_rect.top=self.score_rect.top

    
    def prep_level(self):
        """Turn the level into the rendered image"""
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color)
        self.text = self.text_font.render('Level', True, self.text_color)
        self.text_rect=self.text.get_rect()

        #Position the level below the score
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right-20
        self.level_rect.top=self.screen_rect.top+60
        self.text_rect.right=self.screen_rect.right-40
        self.text_rect.top=self.screen_rect.top+60
    
    def prep_remaining_ship(self):
        self.ship_image=self.font.render(str(self.stats.ship_limit+1),True,self.text_color)
        self.ship_text = self.text_font.render('Ships', True, self.text_color)
        self.ship_text_rect=self.ship_text.get_rect()

        #Position the level below the score
        self.ship_rect=self.ship_image.get_rect()
        self.ship_rect.right=self.screen_rect.left+100
        self.ship_rect.top=self.score_rect.top
        self.ship_text_rect.right=self.screen_rect.left+80
        self.ship_text_rect.top=self.score_rect.top



