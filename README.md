
# Smart Energy Optimization System

## Project Overview
This project is a **Smart Energy Optimization System** that leverages IoT devices, battery storage, and power grid data to optimize energy usage, save costs, and generate profits by selling stored energy during peak hours.

The system collects real-time data from IoT devices, power grid prices, and battery levels, and makes intelligent decisions to:
- Turn off non-essential devices during peak hours to reduce energy consumption.
- Release stored energy from batteries to sell at higher prices during peak times.
- Calculate total profits from energy sales and savings from reducing device consumption during peak periods.

## Project Structure
The project is built using **Flask** as the backend framework and **HTML/CSS/JavaScript** for the frontend. The system uses a web interface to display real-time data, energy savings, and profits. The components are organized as follows:

```
/energy_controller/
├── app.py                # Flask server entry point
├── iot_device_manager.py  # Manages IoT device communication
├── power_grid_manager.py  # Manages power grid data retrieval
├── battery_manager.py     # Manages battery data and control
├── optimization_engine.py # Optimizes energy consumption and decisions
├── models.py              # Data models for devices, grid, and battery
├── templates/             # HTML templates for the web interface
│   └── index.html         # The dashboard HTML page
├── static/
    ├── css/
    │   └── styles.css     # CSS for styling the web interface
    └── js/
        └── dashboard.js   # JavaScript to handle real-time data and charts
```

## Features
- **IoT Device Integration**: Communicate with smart home devices like lights, appliances, and thermostats.
- **Battery Management**: Store and release power based on grid conditions.
- **Power Grid Data Retrieval**: Track real-time power prices and grid saturation levels.
- **Energy Optimization**: Make smart decisions to reduce energy consumption and maximize profits.
- **Real-Time Dashboard**: View real-time data, including profits and savings, using a web interface.
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/smart-energy-optimization.git
    cd smart-energy-optimization
    ```

2. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask server:
    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://localhost:5000` to access the dashboard.

## API Endpoints
The system exposes several API endpoints to interact with the energy optimization system:

- **POST /device/register**: Register a new IoT device.
- **POST /device/status**: Update the status of a registered device (e.g., on/off).
- **GET /device/instructions/<device_id>**: Get control instructions for a specific device.
- **POST /grid/update**: Update the current power grid price and saturation level.
- **POST /battery/register**: Register a new battery.
- **POST /battery/update**: Store or release power from a battery.
- **GET /optimize**: Optimize energy usage and return recommendations.
- **GET /api/profit**: Get the total profit from selling energy.
- **GET /api/savings**: Get the total savings from shutting down devices.

## License
This project is licensed under the MIT License.
