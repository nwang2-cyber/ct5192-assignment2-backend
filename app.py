from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from Python backend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)