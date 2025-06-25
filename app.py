from flask import Flask, jsonify
import random
import requests
from datetime import datetime

app = Flask(__name__)

# === Telegram Bot Settings ===
TELEGRAM_BOT_TOKEN = '7959778482:AAFgqgf01UFX4QCKkYuNBiT4jt557m7LQuE'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

# === Signal Generator ===
def generate_signal():
    pairs = ['XAUUSD', 'NAS100', 'US30', 'GER40', 'EURUSD', 'USDJPY',
             'GBPUSD', 'GBPAUD', 'GBPJPY', 'AUDCAD', 'USDCHF', 'NZDUSD']
    directions = ['Buy', 'Sell']
    sessions = ['Asian', 'London', 'New York']
    modes = ['Sniper', 'Normal', 'Aggressive']

    signal = {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "session": random.choice(sessions),
        "mode": random.choice(modes),
        "confidence": f"{random.randint(70, 95)}%",
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    }
    return signal

# === Telegram Sender ===
def send_to_telegram(signal):
    text = (
        f"📡 *Eagle EA Scalper Signal*\n"
        f"Pair: `{signal['pair']}`\n"
        f"Direction: `{signal['direction']}`\n"
        f"Session: `{signal['session']}`\n"
        f"Mode: `{signal['mode']}`\n"
        f"Confidence: `{signal['confidence']}`\n"
        f"🕒 Time: `{signal['time']}`"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        print("Signal sent to Telegram:", response.status_code)
    except Exception as e:
        print("Telegram Error:", str(e))

# === API Routes ===
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Eagle EA API is live"})

@app.route('/signal', methods=['GET'])
def generate_and_send_signal():
    signal = generate_signal()
    send_to_telegram(signal)
    return jsonify(signal)

@app.route('/latest', methods=['GET'])
def latest_for_app():
    signal = generate_signal()
    return jsonify(signal)

if __name__ == '__main__':
    app.run(debug=True)
