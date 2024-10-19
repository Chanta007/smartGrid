class PowerGridDataManager:
    def __init__(self):
        self.current_price = 0.0  # Current electricity price
        self.grid_saturation = 0.0  # Current grid saturation percentage (0-100%)

    def update_price(self, price):
        """
        Updates the current price of electricity. 
        This would typically retrieve real-time data from a power exchange or public feed.
        """
        self.current_price = price  # Update with the given price
        return {"message": "Price updated", "price": self.current_price}

    def update_grid_saturation(self, saturation):
        """
        Updates the grid saturation level. 
        This would typically retrieve real-time grid load data from a public feed.
        """
        self.grid_saturation = saturation  # Update with the given saturation level
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
