from flask import Flask, request, jsonify, render_template
from iot_device_manager import IoTDeviceManager
from power_grid_manager import PowerGridDataManager
from battery_manager import BatteryManager
from optimization_engine import EnergyOptimizationEngine
from models import Device, GridData, Battery

app = Flask(__name__)

# Initialize core components
device_manager = IoTDeviceManager()
grid_manager = PowerGridDataManager()
battery_manager = BatteryManager()
optimization_engine = EnergyOptimizationEngine(device_manager, grid_manager, battery_manager)

# Route for the main dashboard
@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/profit', methods=['GET'])
def get_profit():
    # Get the total profit from the BatteryManager
    return jsonify(battery_manager.get_profit())


@app.route('/savings', methods=['GET'])
def get_savings():
    # Get the total cost savings from the EnergyOptimizationEngine
    return jsonify(optimization_engine.get_savings())


# API endpoint for fetching real-time data for the dashboard
@app.route('/api/dashboard_data', methods=['GET'])
def get_dashboard_data():
    # Gather the data you want to display
    devices = [device_manager.get_device_status(device_id) for device_id in device_manager.devices]
    grid_data = grid_manager.get_current_price()
    grid_saturation = grid_manager.get_grid_saturation()
    batteries = [battery_manager.get_battery_status(battery_id) for battery_id in battery_manager.batteries]

    # Return the data in JSON format
    return jsonify({
        "devices": devices,
        "grid_data": grid_data,
        "grid_saturation": grid_saturation,
        "batteries": batteries
    })

if __name__ == '__main__':
    app.run(debug=True)
