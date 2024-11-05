from flask import Flask, render_template, jsonify
from packet_sniffer import start_packet_sniffing, get_allowed_traffic, get_blocked_traffic
from traffic_monitor import scan_open_ports

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
def api_allowed_traffic():
    allowed_traffic = get_allowed_traffic()
    return jsonify({"allowed": allowed_traffic})

@app.route('/api/blocked_traffic')
def api_blocked_traffic():
    blocked_traffic = get_blocked_traffic()
    return jsonify({"blocked": blocked_traffic})

@app.route('/api/open_ports')
def api_open_ports():
    ports = scan_open_ports()
    return jsonify({"ports": ports})

if __name__ == '__main__':
    start_packet_sniffing()  # Start sniffing packets in the background
    app.run(debug=True)
