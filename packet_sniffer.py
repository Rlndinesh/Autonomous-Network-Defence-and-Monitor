from scapy.all import sniff, IP, TCP

def detect_anomalies(packet):
    if len(packet) > 1500 or packet[IP].src == '192.168.1.100':
        return True
    return False

def process_packet(packet, blocked_traffic):
    if IP in packet:
        if detect_anomalies(packet):
            blocked_traffic.append({
                'src': packet[IP].src,
                'dst': packet[IP].dst,
                'port': packet[TCP].dport if TCP in packet else None
            })
            print(f"Blocked: {packet[IP].src} -> {packet[IP].dst}")
        else:
            print(f"Allowed: {packet[IP].src} -> {packet[IP].dst}")

def start_packet_sniffing(blocked_traffic):
    sniff(prn=lambda pkt: process_packet(pkt, blocked_traffic), store=False)
