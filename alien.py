import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        """initialize alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and set rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact horizontal position
        self.x = float(self.rect.x)
        