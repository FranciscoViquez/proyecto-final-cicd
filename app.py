from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "status": "online",
            "message": "Microservicio De Cero a Producción Activo",
            "version": "1.0.0",
        }
    )


@app.route("/calc/sum/<int:a>/<int:b>")
def suma(a, b):
    return jsonify(
        {
            "operacion": "suma",
            "a": a,
            "b": b,
            "resultado": a + b,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
