import pygame 
import numpy as np
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.alien_image=pygame.image.load(r"E:\Python_games\Hopstarter-Purple-Monsters-Alien-displeased.256.bmp")
        self.alien_image=pygame.transform.scale(self.alien_image,(50,50))
        self.image = self.alien_image
        self.rect=self.image.get_rect()
        self.rect.x=np.random.randint(0,1200-self.rect.width)
        self.rect.y=np.random.randint(-100,-50)
        self.speed_factor=0.7
    
    def update(self):
        self.rect.y+=self.speed_factor
    def blitme(self):
        self.screen.blit(self.image,self.rect)
