from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 🔓 Allow access from Thunkable and other frontends

# === Valid License Keys ===
valid_keys = [
    "EAGLE-001-ACCESS",
    "EAGLE-VIP-999",
    "SCALPER-KEY-777",
    "FREE-TRIAL-KEY-001",
    "EAGLE-X92T3-VB74K-LP998"
]

# === Store Past Signals ===
past_signals = []

# === Generate a Signal ===
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
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "result": random.choice(["win", "loss", "pending"])  # ← Bonus for signal history
    }
    return signal

# === Routes ===

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Eagle EA Scalper API is live ✅"})

@app.route('/validate', methods=['POST'])
def validate_license():
    try:
        data = request.get_json()
        if not data or "license_key" not in data:
            return jsonify({"status": "ERROR", "message": "Missing license_key"}), 400

        license_key = data["license_key"]
        if license_key in valid_keys:
            return jsonify({"status": "VALID"})
        else:
            return jsonify({"status": "INVALID"})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

@app.route('/latest', methods=['GET'])
def latest_signal():
    signal = generate_signal()
    past_signals.append(signal)
    return jsonify(signal)

@app.route('/previous', methods=['GET'])
def previous_signals():
    return jsonify(past_signals[-10:])  # Returns last 10 signals

# === Run App ===
if __name__ == '__main__':
    app.run(debug=True)
