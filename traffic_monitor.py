import socket

# Retrieve traffic data
def get_traffic_data():
    from packet_sniffer import traffic_data
    return traffic_data

# Scan for open ports on localhost
def scan_open_ports():
    open_ports = []
    for port in range(1, 1024):  # Scan well-known ports
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.5)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                open_ports.append(port)
    return open_ports
