from flask import Flask, render_template, jsonify
from packet_sniffer import start_packet_sniffing, get_traffic_data, scan_open_ports

app = Flask(__name__)

# Start the packet sniffing in a separate thread
import threading
threading.Thread(target=start_packet_sniffing, daemon=True).start()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/allowed_traffic')
def allowed_traffic():
    return render_template('allowed_traffic.html')

@app.route('/blocked_traffic')
def blocked_traffic():
    return render_template('blocked_traffic.html')

@app.route('/open_ports')
def open_ports():
    return render_template('open_ports.html')

@app.route('/api/allowed_traffic')
def get_allowed_traffic():
    traffic = get_traffic_data()
    return jsonify({'allowed': traffic['allowed']})

@app.route('/api/blocked_traffic')
def get_blocked_traffic():
    traffic = get_traffic_data()
    return jsonify({'blocked': traffic['blocked']})

@app.route('/api/open_ports')
def get_open_ports():
    open_ports = scan_open_ports()
    return jsonify({'ports': open_ports})

if __name__ == '__main__':
    app.run(debug=True)
