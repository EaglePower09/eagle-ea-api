from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Eagle EA Scalper API is live."})

@app.route('/signal')
def get_signal():
    # This will be replaced with live signal logic
    return jsonify({
        "pair": "XAUUSD",
        "direction": "buy",
        "confidence": "high",
        "mode": "sniper",
        "session": "London"
    })

@app.route('/latest')
def latest_signals():
    return jsonify([
        {"pair": "NAS100", "direction": "sell", "confidence": "medium"},
        {"pair": "USDJPY", "direction": "buy", "confidence": "high"}
    ])

@app.route('/gold')
def gold_only():
    return jsonify({
        "pair": "XAUUSD",
        "direction": "buy",
        "confidence": "high",
        "timestamp": "2025-06-25T11:30:00Z"
    })

if __name__ == '__main__':
    app.run()
