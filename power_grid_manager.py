# power_grid_manager.py

import random

class PowerGridDataManager:
    def __init__(self):
        self.current_price = 0.0  # Current electricity price
        self.grid_saturation = 0.0  # Current grid saturation percentage (0-100%)

    def update_price(self):
        """
        Updates the current price of electricity. 
        This would typically retrieve real-time data from a power exchange or public feed.
        """
        # Simulate price update with a random value (this would come from an external API)
        self.current_price = round(random.uniform(0.05, 0.50), 2)  # Price in $/kWh
        return {"message": "Price updated", "price": self.current_price}

    def update_grid_saturation(self):
        """
        Updates the grid saturation level. 
        This would typically retrieve real-time grid load data from a public feed.
        """
        # Simulate grid saturation update with a random value (0% to 100%)
        self.grid_saturation = random.randint(30, 100)  # Simulate grid load as a percentage
        return {"message": "Grid saturation updated", "saturation": self.grid_saturation}

    def get_current_price(self):
        """
        Returns the current price of electricity.
        """
        return {"current_price": self.current_price}

    def get_grid_saturation(self):
        """
        Returns the current grid saturation level.
        """
        return {"grid_saturation": self.grid_saturation}
