import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Manages game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responds to key and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Updates images on the screen, and flips to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()