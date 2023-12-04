import requests
from pprint import pprint

response = requests.get("http://127.0.0.1:9000/cadeiras")
response.raise_for_status()

tudo= response.json()

pprint(tudo)