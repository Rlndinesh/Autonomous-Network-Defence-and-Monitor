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
        print(f"{entry['status']}: {entry['src']} -> {entry['dst']}")

# Start sniffing packets
def start_packet_sniffing():
    sniff(prn=process_packet, store=False)

# Add IP to block list
def add_ip_to_blocklist(ip_address):
    blocked_ips.add(ip_address)

# Remove IP from block list
def remove_ip_from_blocklist(ip_address):
    blocked_ips.discard(ip_address)

# Get allowed traffic
def get_allowed_traffic():
    return traffic_data['allowed']

# Get blocked traffic
def get_blocked_traffic():
    return traffic_data['blocked']
