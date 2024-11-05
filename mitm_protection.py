from scapy.all import ARP, sniff

# Detect ARP spoofing (MITM attacks)
def detect_mitm():
    suspicious_packets = []
    
    def monitor_arp(packet):
        if ARP in packet and packet[ARP].op == 2:
            real_mac = packet[ARP].hwsrc
            known_mac = "00:00:00:00:00:00"  # replace with actual MAC if needed
            if real_mac != known_mac:
                suspicious_packets.append(packet)
                
    sniff(filter="arp", prn=monitor_arp, count=10, timeout=5)
    return len(suspicious_packets) > 0
