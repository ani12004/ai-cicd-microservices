from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "User Service", "status": "Running"})

@app.route('/users')
def users():
    return jsonify({"users": ["Anil", "John", "Alice"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
