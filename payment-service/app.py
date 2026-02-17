from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "Payment Service", "status": "Running"})

@app.route('/payments')
def payments():
    return jsonify({"payments": ["Success", "Pending"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
