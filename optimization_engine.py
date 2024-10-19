# optimization_engine.py

class EnergyOptimizationEngine:
    def __init__(self, device_manager, grid_manager, battery_manager):
        self.device_manager = device_manager
        self.grid_manager = grid_manager
        self.battery_manager = battery_manager
        self.savings = 0.0  # Track total cost savings

    def optimize_usage(self):
        grid_price = self.grid_manager.get_current_price()["current_price"]
        grid_saturation = self.grid_manager.get_grid_saturation()["grid_saturation"]

        price_threshold = 0.25  # Example threshold for high price
        recommendations = {}

        # Check if we should release power from batteries
        if grid_price > price_threshold or grid_saturation > 80:
            for battery_id, battery_info in self.battery_manager.batteries.items():
                if battery_info["current_charge"] > 0:
                    recommendations[battery_id] = f"Release power (battery charge: {battery_info['current_charge']} kWh)"
                    self.battery_manager.release_power(battery_id, amount=5, price=grid_price)
                else:
                    recommendations[battery_id] = "Battery is low, no action."

        # Optimize IoT devices (turn off or adjust settings)
        for device_id, device_info in self.device_manager.devices.items():
            device_type = device_info.get("type")
            device_status = device_info.get("status")

            if device_type in ["light", "appliance"]:
                if grid_price > price_threshold:
                    recommendations[device_id] = "Turn off device to save energy."
                    self.device_manager.set_device_status(device_id, "off")
                    
                    # Calculate savings: cost if device ran during peak hours
                    device_energy_usage = 0.5  # Example: 0.5 kWh for the device
                    savings = device_energy_usage * grid_price
                    self.savings += savings
            elif device_type == "thermostat" and device_status == "on":
                if grid_price > price_threshold:
                    recommendations[device_id] = "Lower thermostat to save energy."
                    self.device_manager.set_device_status(device_id, "lower_temp")

        return recommendations

    def get_savings(self):
        return {"total_savings": self.savings}
