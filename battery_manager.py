# battery_manager.py

class BatteryManager:
    def __init__(self):
        self.batteries = {}  # Dictionary to store information about all batteries
        self.profit = 0.0  # Track the total profit made from selling energy

    def register_battery(self, battery_id, capacity, current_charge):
        if battery_id in self.batteries:
            return {"error": "Battery already registered."}
        self.batteries[battery_id] = {
            "capacity": capacity,
            "current_charge": current_charge,
            "stored_at_price": 0.0  # Store the price when energy was stored
        }
        return {"message": f"Battery {battery_id} registered successfully."}

    def store_power(self, battery_id, amount, price):
        if battery_id in self.batteries:
            battery = self.batteries[battery_id]
            available_capacity = battery["capacity"] - battery["current_charge"]
            if available_capacity >= amount:
                battery["current_charge"] += amount
                battery["stored_at_price"] = price  # Track price when stored
                return {"message": f"Stored {amount} kWh in battery {battery_id} at {price} $/kWh."}
            return {"error": "Not enough capacity in the battery."}
        return {"error": "Battery not found."}

    def release_power(self, battery_id, amount, price):
        if battery_id in self.batteries:
            battery = self.batteries[battery_id]
            if battery["current_charge"] >= amount:
                battery["current_charge"] -= amount

                # Calculate profit: (Release Price - Stored Price) * Amount Released
                profit = (price - battery["stored_at_price"]) * amount
                self.profit += profit  # Accumulate profit
                return {"message": f"Released {amount} kWh from battery {battery_id} at {price} $/kWh. Profit: {profit} $."}
            return {"error": "Insufficient charge in the battery."}
        return {"error": "Battery not found."}

    def get_profit(self):
        return {"total_profit": self.profit}
