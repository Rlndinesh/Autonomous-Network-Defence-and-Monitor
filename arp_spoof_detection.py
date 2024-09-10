from scapy.all import ARP, sniff, sr1

def get_mac(ip_address):
    arp_request = ARP(pdst=ip_address)
    arp_response = sr1(arp_request, timeout=2, verbose=False)
    if arp_response:
        return arp_response.hwsrc

def detect_arp_spoof(packet):
    if ARP in packet and packet[ARP].op == 2:
        real_mac = get_mac(packet[ARP].psrc)
        response_mac = packet[ARP].hwsrc

        if real_mac != response_mac:
            print(f"ARP Spoofing Detected: {packet[ARP].psrc} is being spoofed!")
            return True
    return False

def start_arp_spoof_detection():
    sniff(prn=detect_arp_spoof, filter="arp", store=False)
