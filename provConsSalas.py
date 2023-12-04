import requests
from pprint import pprint
from flask import Flask, jsonify

app = Flask(__name__)

response = requests.get("http://127.0.0.1:5000/filmes")
response.raise_for_status()

filmes= response.json()

count = 1
SALAS = []

for item in filmes:
    item = {"titulo": item["titulo"], "sala": count}
    count+=1
    SALAS.append(item)

pprint(SALAS)

@app.route("/salas", methods= ["GET"])
def get_filmes():
    return jsonify(SALAS)

if __name__ == "__main__":
    app.run(port = 8000)