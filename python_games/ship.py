import pygame

class Ship:
    def __init__(self,screen):
        self.screen=screen

        #Load the ship image
        self.image=pygame.image.load(r"E:\Python_games\Daco_1402867.bmp")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.background=pygame.image.load(r"C:\Users\hp\Downloads\images.bmp")
        self.background=pygame.transform.scale(self.background,(1200,800))

        #  Start each new ship at the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.move_right=False
        self.move_left=False

        self.count=3
    
    def blitme(self):
        """Draw the ship the bottom"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.move_right:
            if self.rect.centerx<=1200:
                self.rect.centerx+=1.53
        if self.move_left:
            if self.rect.centerx>=0:
                self.rect.centerx-=1.53
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.center=self.screen_rect.centerx
