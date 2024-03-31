import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,3,15)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=(255,255,255)
        self.speed_factor=1.5
    
    def update(self):
         # decrement in y co-ordinate 
        self.y -=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
