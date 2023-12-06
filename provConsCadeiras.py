import requests
from pprint import pprint
from flask import Flask, jsonify

app = Flask(__name__)

response = requests.get("http://127.0.0.1:8000/salas")
response.raise_for_status()

salas= response.json()

count = 1
CADEIRAS = []


def criarCadeiras():
    ArrayCad = []
    for i in range(5):
       cad = {"numero": i, "disponivel": True}
       ArrayCad.append(cad)
    return ArrayCad
    

for item in salas:
    item = {"titulo": item["titulo"], "sala": item["sala"], "cadeiras": criarCadeiras()}
    count+=1
    CADEIRAS.append(item)

pprint(CADEIRAS)

@app.route("/cadeiras", methods= ["GET"])
def get_cadeiras():
    return jsonify(CADEIRAS)

if __name__ == "__main__":
    app.run(port = 9000)