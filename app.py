from flask import Flask, render_template, jsonify
import subprocess
import threading
from packet_sniffer import start_packet_sniffing
from arp_spoof_detection import start_arp_spoof_detection

app = Flask(__name__)

blocked_traffic = []

# Route for home page to display network traffic and open ports
@app.route('/')
def index():
    return render_template('index.html')

# Route to get blocked traffic
@app.route('/blocked_traffic')
def blocked_traffic_page():
    return render_template('blocked_traffic.html')

@app.route('/get_blocked_traffic')
def get_blocked_traffic():
    return jsonify(blocked_traffic)

# Function to list open ports using netstat
def list_open_ports():
    result = subprocess.run(['netstat', '-tuln'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

# Route to display open ports
@app.route('/open_ports')
def open_ports_page():
    return render_template('open_ports.html')

@app.route('/get_open_ports')
def get_open_ports():
    return jsonify({'ports': list_open_ports()})

# Start the packet sniffer and ARP spoof detection
def start_network_monitoring():
    threading.Thread(target=start_packet_sniffing, args=(blocked_traffic,)).start()
    threading.Thread(target=start_arp_spoof_detection).start()

if __name__ == '__main__':
    start_network_monitoring()
    app.run(debug=True, use_reloader=False)
