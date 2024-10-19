// Update grid price label
function updatePriceLabel() {
    const price = document.getElementById("grid_price").value;
    document.getElementById("price_label").textContent = price;
}

// Update grid saturation label
function updateSaturationLabel() {
    const saturation = document.getElementById("grid_saturation").value;
    document.getElementById("saturation_label").textContent = saturation;
}

// Add a new device
function addDevice() {
    const deviceId = document.getElementById("device_id").value;
    const deviceType = document.getElementById("device_type").value;
    const deviceStatus = document.getElementById("device_status").value;

    fetch('/device/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            device_id: deviceId,
            device_type: deviceType,
            status: deviceStatus,
        })
    })
    .then(response => response.json())
    .then(data => {
        alert("Device added: " + JSON.stringify(data));
    });
}

// Update grid price and saturation
function updateGrid() {
    const price = document.getElementById("grid_price").value;
    const saturation = document.getElementById("grid_saturation").value;

    fetch('/grid/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            price: parseFloat(price),
            saturation: parseInt(saturation),
        })
    })
    .then(response => response.json())
    .then(data => {
        alert("Grid data updated: " + JSON.stringify(data));
    });
}

// Add a new battery
function addBattery() {
    const batteryId = document.getElementById("battery_id").value;
    const capacity = document.getElementById("capacity").value;
    const currentCharge = document.getElementById("current_charge").value;

    fetch('/battery/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            battery_id: batteryId,
            capacity: parseFloat(capacity),
            current_charge: parseFloat(currentCharge),
        })
    })
    .then(response => response.json())
    .then(data => {
        alert("Battery added: " + JSON.stringify(data));
    });
}

// Optimize energy
function optimizeEnergy() {
    fetch('/optimize', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("profit").textContent = "Profit: $" + data.total_profit.toFixed(2);
        document.getElementById("savings").textContent = "Savings: $" + data.total_savings.toFixed(2);
        const recommendationsDiv = document.getElementById("recommendations");
        recommendationsDiv.innerHTML = "";
        for (const [key, value] of Object.entries(data.recommendations)) {
            const p = document.createElement("p");
            p.textContent = `${key}: ${value}`;
            recommendationsDiv.appendChild(p);
        }
    });
}
