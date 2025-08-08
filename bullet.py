import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fire from the ship"""
    
    def __init__(self, ai_game):
        """create a bullet at ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet at 0,0 and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullets position as float
        self.y = float(self.rect.y)

    def update(self):
        """Update the bullet position"""
        # exact position of bullet
        self.y -= self.settings.bullet_speed
        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet at current location"""
        pygame.draw.rect(self.screen, self.color, self.rect)