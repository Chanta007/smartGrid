#!/bin/bash

# Create the main project directory (if not in the root directory already)
mkdir -p energy_controller

# Navigate to the project directory
cd energy_controller

# Create the Python files
touch app.py
touch iot_device_manager.py
touch power_grid_manager.py
touch battery_manager.py
touch optimization_engine.py
touch models.py

# Create the templates directory
mkdir -p templates

# Provide feedback to the user
echo "Project structure created successfully."
echo "Files created:"
echo "  - app.py"
echo "  - iot_device_manager.py"
echo "  - power_grid_manager.py"
echo "  - battery_manager.py"
echo "  - optimization_engine.py"
echo "  - models.py"
echo "Directory created:"
echo "  - templates/"
