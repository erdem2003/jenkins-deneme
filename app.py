from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Jenkins deployed API!"})

@app.route("/bye")
def bye():
    return jsonify({"message": "Goodbye from updated API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
