from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# === License Keys ===
valid_keys = [
    "EAGLE-001-ACCESS",
    "EAGLE-VIP-999",
    "SCALPER-KEY-777",
    "FREE-TRIAL-KEY-001",
    "EAGLE-X92T3-VB74K-LP998"
]

# === Signal Generator ===
def generate_signal():
    pairs = [
        'XAUUSD', 'NAS100', 'US30', 'GER40', 'EURUSD', 'USDJPY', 'GBPUSD',
        'GBPAUD', 'GBPJPY', 'AUDCAD', 'USDCHF', 'NZDUSD'
    ]
    directions = ['Buy', 'Sell']
    sessions = ['Asian', 'London', 'New York']
    modes = ['Sniper', 'Normal', 'Aggressive']

    signal = {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "session": random.choice(sessions),
        "mode": random.choice(modes),
        "confidence": f"{random.randint(70, 95)}%",
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }
    return signal

# === Routes ===
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Eagle EA Scalper API is live ✅"})

@app.route('/validate', methods=['POST'])
def validate_license():
    data = request.get_json()
    license_key = data.get("license_key")

    if license_key in valid_keys:
        return jsonify({"status": "VALID"})
    else:
        return jsonify({"status": "INVALID"})

@app.route('/latest', methods=['GET'])
def latest_signal():
    signal = generate_signal()
    return jsonify(signal)

# === Run ===
if __name__ == '__main__':
    app.run(debug=True)
