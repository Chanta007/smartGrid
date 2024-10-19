document.addEventListener("DOMContentLoaded", function() {
    // Fetch data when the page loads
    fetchDashboardData();

    // Function to fetch real-time data from the server
    function fetchDashboardData() {
        fetch('/api/dashboard_data')
            .then(response => response.json())
            .then(data => {
                // Display Grid Data
                document.getElementById("grid-price").textContent = data.grid_data.current_price;
                document.getElementById("grid-saturation").textContent = data.grid_saturation.grid_saturation;

                // Display Devices
                const deviceList = document.getElementById("device-list");
                deviceList.innerHTML = '';
                data.devices.forEach(device => {
                    const deviceElement = document.createElement('div');
                    deviceElement.className = 'device';
                    deviceElement.innerHTML = `
                        <p>Device ID: ${device.device_id}</p>
                        <p>Type: ${device.type}</p>
                        <p>Status: ${device.status}</p>
                    `;
                    deviceList.appendChild(deviceElement);
                });

                // Display Battery Data
                const batteryList = document.getElementById("battery-list");
                batteryList.innerHTML = '';
                data.batteries.forEach(battery => {
                    const batteryElement = document.createElement('div');
                    batteryElement.className = 'battery';
                    batteryElement.innerHTML = `
                        <p>Battery ID: ${battery.battery_id}</p>
                        <p>Capacity: ${battery.capacity} kWh</p>
                        <p>Current Charge: ${battery.current_charge} kWh</p>
                    `;
                    batteryList.appendChild(batteryElement);
                });

                // Update Chart Data
                updateGridChart(data.grid_data.current_price, data.grid_saturation.grid_saturation);
            });
    }

    // Function to update the Chart.js chart
    function updateGridChart(price, saturation) {
        const ctx = document.getElementById('gridChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Current Price', 'Grid Saturation'],
                datasets: [{
                    label: 'Grid Data',
                    data: [price, saturation],
                    backgroundColor: ['rgba(75, 192, 192, 0.2)'],
                    borderColor: ['rgba(75, 192, 192, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});

// Fetch profit and savings data
function fetchProfitAndSavings() {
    fetch('/profit')
        .then(response => response.json())
        .then(data => {
            document.getElementById('profit').textContent = `Total Profit: $${data.total_profit.toFixed(2)}`;
        });

    fetch('/savings')
        .then(response => response.json())
        .then(data => {
            document.getElementById('savings').textContent = `Total Savings: $${data.total_savings.toFixed(2)}`;
        });
}

// Call this function when the page loads
fetchProfitAndSavings();
