from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        data = request.get_json()
        x = data["x"]
        y = data["y"]
    else:  # GET request (browser)
        x = int(request.args.get("x", 0))
        y = int(request.args.get("y", 0))
    return jsonify({"result": x + y})

@app.route("/multiply", methods=["POST", "GET"])
def multiply():
    if request.method == "POST":
        data = request.get_json()
        x = data["x"]
        y = data["y"]
    else:  # GET request (browser)
        x = int(request.args.get("x", 0))
        y = int(request.args.get("y", 0))
    return jsonify({"result": x * y})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
