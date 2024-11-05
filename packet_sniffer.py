from scapy.all import sniff, IP, TCP
import socket

# Global data to store traffic information and blocked IPs
traffic_data = {'allowed': [], 'blocked': []}
blocked_ips = set()

# Detect anomalies in traffic
def detect_anomalies(packet):
    return len(packet) > 1500 or packet[IP].src in blocked_ips

# Process packets and update traffic data
def process_packet(packet):
    if IP in packet:
        entry = {
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'port': packet[TCP].dport if TCP in packet else None,
            'status': 'Blocked' if detect_anomalies(packet) else 'Allowed'
        }
        
        if entry['status'] == 'Blocked':
            traffic_data['blocked'].append(entry)
        else:
            traffic_data['allowed'].append(entry)

# Start sniffing packets
def start_packet_sniffing():
    sniff(prn=process_packet, store=False)

# Retrieve traffic data
def get_traffic_data():
    return traffic_data

# Scan for open ports on localhost
def scan_open_ports():
    open_ports = []
    for port in range(1, 1024):  # Scan well-known ports
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # 1-second timeout for quick scanning
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                open_ports.append(port)
    return open_ports
