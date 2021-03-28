import requests

url = "https://blockchain.info/latestblock"

resp = requests.get(url)

j = resp