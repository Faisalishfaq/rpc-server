from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    x = data.get("x")
    y = data.get("y")
    if x is None or y is None:
        return jsonify({"error": "Missing parameters"}), 400
    return jsonify({"result": x + y})

@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    x = data.get("x")
    y = data.get("y")
    if x is None or y is None:
        return jsonify({"error": "Missing parameters"}), 400
    return jsonify({"result": x * y})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
