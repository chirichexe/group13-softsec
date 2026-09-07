from flask import Flask, jsonify, request 
import calculator

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello world!"})


@app.route("/calc", methods=["POST"])
def calc():
    data = request.get_json()

    if data is None or "expression" not in data:
        return jsonify({"error": "expression is required"}), 400

    expression = data["expression"]

    # Temporary mock until the Calculator branch is merged
    result = calculator.calculator(expression)

    return jsonify({
        "expression": expression,
        "result": result,
    })

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
