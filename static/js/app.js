document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('blocked-traffic-table')) {
        fetch('/get_blocked_traffic')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.querySelector('#blocked-traffic-table tbody');
                data.forEach(row => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `<td>${row.src}</td><td>${row.dst}</td><td>${row.port || 'N/A'}</td>`;
                    tableBody.appendChild(tr);
                });
            });
    }

    if (document.getElementById('open-ports')) {
        fetch('/get_open_ports')
            .then(response => response.json())
            .then(data => {
                document.getElementById('open-ports').innerText = data.ports;
            });
    }
});
