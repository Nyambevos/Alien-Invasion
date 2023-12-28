class Settings():
    """A class for storing all Alien Invasion game settings."""

    def __init__(self):
        """Initializes the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship's settings
        self.ship_speed = 1.5
