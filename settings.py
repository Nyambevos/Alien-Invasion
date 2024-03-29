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
        self.ship_limit = 3

        # Projectile parameters
        self.bullet_speed = 1.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 indicates movement to the right; and -1 indicates movement to the left.
        self.fleet_direction = 1
