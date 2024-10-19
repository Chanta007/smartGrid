# models.py

class Device:
    def __init__(self, device_id, device_type, status="off"):
        """
        Initializes an IoT device.
        Args:
            device_id (str): Unique identifier for the device.
            device_type (str): Type of the device (e.g., light, thermostat, appliance).
            status (str): Initial status of the device (e.g., 'on', 'off').
        """
        self.device_id = device_id
        self.device_type = device_type
        self.status = status

    def to_dict(self):
        """
        Converts the device object to a dictionary.
        Returns:
            dict: A dictionary representing the device.
        """
        return {
            "device_id": self.device_id,
            "type": self.device_type,
            "status": self.status
        }


class GridData:
    def __init__(self, current_price=0.0, grid_saturation=0.0):
        """
        Initializes the grid data model.
        Args:
            current_price (float): Current price of electricity (e.g., $/kWh).
            grid_saturation (float): Current grid saturation percentage (0-100%).
        """
        self.current_price = current_price
        self.grid_saturation = grid_saturation

    def update(self, price, saturation):
        """
        Updates the grid data.
        Args:
            price (float): The updated electricity price.
            saturation (float): The updated grid saturation percentage.
        """
        self.current_price = price
        self.grid_saturation = saturation

    def to_dict(self):
        """
        Converts the grid data object to a dictionary.
        Returns:
            dict: A dictionary representing the grid data.
        """
        return {
            "current_price": self.current_price,
            "grid_saturation": self.grid_saturation
        }


class Battery:
    def __init__(self, battery_id, capacity, current_charge):
        """
        Initializes a battery object.
        Args:
            battery_id (str): Unique identifier for the battery.
            capacity (float): Maximum capacity of the battery (in kWh).
            current_charge (float): Current charge of the battery (in kWh).
        """
        self.battery_id = battery_id
        self.capacity = capacity
        self.current_charge = current_charge

    def release_power(self, amount):
        """
        Releases a specific amount of power from the battery.
        Args:
            amount (float): Amount of power to release (in kWh).
        Returns:
            str: Success or error message based on the operation.
        """
        if self.current_charge >= amount:
            self.current_charge -= amount
            return f"Released {amount} kWh from battery {self.battery_id}."
        return "Insufficient charge in the battery."

    def store_power(self, amount):
        """
        Stores a specific amount of power in the battery.
        Args:
            amount (float): Amount of power to store (in kWh).
        Returns:
            str: Success or error message based on the operation.
        """
        if self.capacity - self.current_charge >= amount:
            self.current_charge += amount
            return f"Stored {amount} kWh in battery {self.battery_id}."
        return "Not enough capacity in the battery."

    def to_dict(self):
        """
        Converts the battery object to a dictionary.
        Returns:
            dict: A dictionary representing the battery.
        """
        return {
            "battery_id": self.battery_id,
            "capacity": self.capacity,
            "current_charge": self.current_charge
        }
