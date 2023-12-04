from flask import Flask, jsonify

app = Flask(__name__)


FILMES = [
    {
        "titulo": "filme1"
    },
    {
        "titulo": "filme2"
    },
    {
        "titulo": "filme3"
    }
]

@app.route("/filmes", methods= ["GET"])
def get_filmes():
    return jsonify(FILMES)


if __name__ == "__main__":
    app.run()