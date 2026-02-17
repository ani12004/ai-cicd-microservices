from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "Order Service", "status": "Running"})

@app.route('/orders')
def orders():
    return jsonify({"orders": ["Order1", "Order2"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
