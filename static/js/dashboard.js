document.addEventListener("DOMContentLoaded", function() {
    fetchDashboardData();
    setInterval(fetchDashboardData, 5000); // Refresh every 5 seconds

    function fetchDashboardData() {
        fetch('/api/dashboard_data')
            .then(response => response.json())
            .then(data => {
                // Update Grid Data
                document.getElementById("grid-price").textContent = data.grid_data.current_price;
                document.getElementById("grid-saturation").textContent = data.grid_saturation.grid_saturation;

                // Update Profit and Savings
                fetch('/profit')
                    .then(response => response.json())
                    .then(profitData => {
                        document.getElementById("profit").textContent = `Total Profit: $${profitData.total_profit.toFixed(2)}`;
                    });
                fetch('/savings')
                    .then(response => response.json())
                    .then(savingsData => {
                        document.getElementById("savings").textContent = `Total Savings: $${savingsData.total_savings.toFixed(2)}`;
                    });

                // Update Device List
                const deviceList = document.getElementById("device-list");
                deviceList.innerHTML = '';
                data.devices.forEach(device => {
                    const deviceElement = document.createElement('div');
                    deviceElement.className = 'device';
                    deviceElement.innerHTML = `<p>Device ID: ${device.device_id}, Type: ${device.type}, Status: ${device.status}</p>`;
                    deviceList.appendChild(deviceElement);
                });

                // Update Battery List
                const batteryList = document.getElementById("battery-list");
                batteryList.innerHTML = '';
                data.batteries.forEach(battery => {
                    const batteryElement = document.createElement('div');
                    batteryElement.className = 'battery';
                    batteryElement.innerHTML = `<p>Battery ID: ${battery.battery_id}, Capacity: ${battery.capacity} kWh, Current Charge: ${battery.current_charge} kWh</p>`;
                    batteryList.appendChild(batteryElement);
                });

                // Update Chart Data
                updateGridChart(data.grid_data.current_price, data.grid_saturation.grid_saturation);
            });
    }

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
