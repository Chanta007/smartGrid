# iot_device_manager.py

class IoTDeviceManager:
    def __init__(self):
        self.devices = {}  # Dictionary to store device information

    def register_device(self, device_id, device_info):
        """
        Registers a new device with the system.
        Args:
            device_id (str): Unique identifier for the device.
            device_info (dict): Information about the device (type, status, etc.).
        """
        self.devices[device_id] = device_info
        return {"message": f"Device {device_id} registered successfully."}

    def get_device_status(self, device_id):
        """
        Retrieves the current status of a registered device.
        Args:
            device_id (str): Unique identifier for the device.
        Returns:
            dict: Device information if found, else an error message.
        """
        if device_id in self.devices:
            return self.devices[device_id]
        return {"error": "Device not found."}

    def set_device_status(self, device_id, status):
        """
        Updates the status of a registered device (e.g., turn off).
        Args:
            device_id (str): Unique identifier for the device.
            status (str): New status to set for the device (e.g., "off", "on").
        Returns:
            dict: Success message or error if the device is not found.
        """
        if device_id in self.devices:
            self.devices[device_id]['status'] = status
            return {"message": f"Device {device_id} status updated to {status}."}
        return {"error": "Device not found."}
