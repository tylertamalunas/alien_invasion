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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()