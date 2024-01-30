class GameStats():
    """Tracking stats for the game Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # The game Alien Invasion is running in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initializes statistics that change over the course of the game."""
        self.ships_left = self.settings.ship_limit