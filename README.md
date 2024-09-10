# Network Monitor App

This Flask app captures network traffic, detects anomalies, and prevents ARP spoofing attacks. It displays blocked traffic and open ports on a simple UI.

## Features
- Capture network traffic and detect anomalies
- Block suspicious traffic
- Detect and prevent ARP spoofing (MITM)
- Display open ports
- User-friendly interface for monitoring

## Project Structure
Autonomous-Network-Defence-and-Monitor/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── templates/
│   ├── index.html
│   └── blocked_traffic.html
│   └── open_ports.html
├── app.py
├── packet_sniffer.py
├── arp_spoof_detection.py
├── requirements.txt
└── README.md

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
## Run the app:
```bash
python app.py

