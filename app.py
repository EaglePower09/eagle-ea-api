from flask import Flask, jsonify, request
import random
import requests
from datetime import datetime

app = Flask(__name__)

# === Config ===
TELEGRAM_BOT_TOKEN = "7959778482:AAE1O-hPLF-LdldUzRbY50f0RUC4PrmxsAw"
TELEGRAM_CHAT_ID = "6105818531"

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

# === Telegram Sender ===
def send_to_telegram(signal):
    text = (
        f"📢 *Eagle EA Scalper Signal*\n"
        f"Pair: `{signal['pair']}`\n"
        f"Direction: `{signal['direction']}`\n"
        f"Session: `{signal['session']}`\n"
        f"Mode: `{signal['mode']}`\n"
        f"Confidence: `{signal['confidence']}`\n"
        f"🕒 Time: `{signal['time']}`"
    )
    url = f"https://api.telegram.org/bot{7959778482:AAE1O-hPLF-LdldUzRbY50f0RUC4PrmxsAw}/sendMessage"
    payload = {
        "chat_id": 6105818531,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        print("Signal sent to Telegram:", response.text)
    except Exception as e:
        print("Telegram Error:", str(e))

# === Bot Start Message ===
def send_message(text):
    url = f"https://api.telegram.org/bot{7959778482:AAE1O-hPLF-LdldUzRbY50f0RUC4PrmxsAw}/sendMessage"
    payload = {
        "chat_id": 6105818531,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        print("Bot message sent:", response.text)
    except Exception as e:
        print("Send Message Error:", str(e))

# === API Routes ===
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Eagle EA API is live ✅"})

@app.route('/start', methods=['GET'])
def start_bot():
    message = "🤖 Eagle EA Scalper Bot has started!"
    send_message(message)
    return jsonify({"message": "Bot started"})

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
