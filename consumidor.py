import requests
from pprint import pprint

response = requests.get("http://127.0.0.1:5000")
response.raise_for_status()

pprint(response.json())