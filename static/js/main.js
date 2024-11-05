// Function to fetch and display allowed traffic
function fetchAllowedTraffic() {
    fetch('/api/allowed_traffic')
        .then(response => response.json())
        .then(data => {
            const allowedTrafficContainer = document.getElementById('allowed-traffic');
            allowedTrafficContainer.innerHTML = data.allowed.map(item => `<p>${item.src} -> ${item.dst}</p>`).join('');
        })
        .catch(error => console.error('Error fetching allowed traffic:', error));
}

// Function to fetch and display blocked traffic
function fetchBlockedTraffic() {
    fetch('/api/blocked_traffic')
        .then(response => response.json())
        .then(data => {
            const blockedTrafficContainer = document.getElementById('blocked-traffic');
            blockedTrafficContainer.innerHTML = data.blocked.map(item => `<p>${item.src} -> ${item.dst}</p>`).join('');
        })
        .catch(error => console.error('Error fetching blocked traffic:', error));
}

// Function to fetch and display open ports
function fetchOpenPorts() {
    fetch('/api/open_ports')
        .then(response => response.json())
        .then(data => {
            const openPortsContainer = document.getElementById('open-ports');
            openPortsContainer.innerHTML = data.ports.map(port => `<p>Port: ${port.port}, Service: ${port.service}</p>`).join('');
        })
        .catch(error => console.error('Error fetching open ports:', error));
}

// Fetch data every 5 seconds
setInterval(() => {
    fetchAllowedTraffic();
    fetchBlockedTraffic();
    fetchOpenPorts();
}, 5000);
