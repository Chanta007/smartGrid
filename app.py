from flask import Flask, render_template, request, jsonify
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


# Route to register a new IoT device
@app.route('/device/register', methods=['POST'])
def register_device():
    data = request.json
    device_id = data.get('device_id')
    device_type = data.get('device_type')
    status = data.get('status', 'off')

    if not device_id or not device_type:
        return jsonify({"error": "Device ID and type are required."}), 400

    # Register the device using the manager
    response = device_manager.register_device(device_id, {"type": device_type, "status": status})
    return jsonify(response)


# Route to update the status of a device
@app.route('/device/status', methods=['POST'])
def update_device_status():
    data = request.json
    device_id = data.get('device_id')
    status = data.get('status')

    if not device_id or not status:
        return jsonify({"error": "Device ID and status are required."}), 400

    # Update the device status using the manager
    response = device_manager.set_device_status(device_id, status)
    return jsonify(response)


# Route to get the current instructions for a device
@app.route('/device/instructions/<device_id>', methods=['GET'])
def get_device_instructions(device_id):
    response = optimization_engine.generate_instructions(device_id)
    return jsonify(response)


# Route to update power grid data (price and saturation)
@app.route('/grid/update', methods=['POST'])
def update_grid_data():
    data = request.json
    price = data.get('price')
    saturation = data.get('saturation')

    if price is None or saturation is None:
        return jsonify({"error": "Price and saturation are required."}), 400

    # Update grid data using the grid manager
    grid_manager.update_price(price)
    grid_manager.update_grid_saturation(saturation)
    return jsonify({"message": "Grid data updated successfully."})


# Route to register a new battery
@app.route('/battery/register', methods=['POST'])
def register_battery():
    data = request.json
    battery_id = data.get('battery_id')
    capacity = data.get('capacity')
    current_charge = data.get('current_charge')

    if not battery_id or capacity is None or current_charge is None:
        return jsonify({"error": "Battery ID, capacity, and current charge are required."}), 400

    # Register the battery using the manager
    response = battery_manager.register_battery(battery_id, capacity, current_charge)
    return jsonify(response)


# Route to update the battery status (store/release power)
@app.route('/battery/update', methods=['POST'])
def update_battery_status():
    data = request.json
    battery_id = data.get('battery_id')
    action = data.get('action')  # "store" or "release"
    amount = data.get('amount')

    if not battery_id or not action or amount is None:
        return jsonify({"error": "Battery ID, action, and amount are required."}), 400

    # Perform the action (store or release power)
    if action == 'release':
        response = battery_manager.release_power(battery_id, amount)
    elif action == 'store':
        response = battery_manager.store_power(battery_id, amount)
    else:
        return jsonify({"error": "Invalid action. Must be 'store' or 'release'."}), 400

    return jsonify(response)


# Route to get optimization suggestions
@app.route('/optimize', methods=['GET'])
def optimize_energy():
    # Run the optimization engine to get recommendations
    recommendations = optimization_engine.optimize_usage()
    return jsonify(recommendations)

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

# Route for the status page
@app.route('/status')
def status_page():
    return render_template('index.html')  # This is your existing status monitoring page

# Route for the simulation page
@app.route('/simulation')
def simulation_page():
    return render_template('simulation.html')  # This is your energy simulation page


if __name__ == '__main__':
    app.run(debug=True)
