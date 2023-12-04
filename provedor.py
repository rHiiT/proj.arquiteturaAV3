from flask import Flask, jsonify

app = Flask(__name__)


FILMES = [
    {
        "titulo": "Homem Aranha",
        "nota:": 5
    },
    {
        "titulo": "Batman",
        "nota": 4
    },
    {
        "titulo": "Matrix",
        "nota": 4
    }
]

@app.route("/", methods= ["GET"])
def get_filmes():
    return jsonify(FILMES)


if __name__ == "__main__":
    app.run()