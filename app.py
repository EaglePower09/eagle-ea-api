from flask import Flask, request, jsonify

app = Flask(__name__)
latest_signal = {}

@app.route('/')
def home():
    return "Eagle EA API is live!"

@app.route('/send-signal', methods=['POST'])
def send_signal():
    global latest_signal
    data = request.json
    latest_signal = data
    return jsonify({"status": "success", "message": "Signal received."})

@app.route('/get-latest-signal', methods=['GET'])
def get_latest_signal():
    if latest_signal:
        return jsonify({"status": "success", "signal": latest_signal})
    else:
        return jsonify({"status": "no signal", "signal": {}})

if __name__ == '__main__':
    app.run()
