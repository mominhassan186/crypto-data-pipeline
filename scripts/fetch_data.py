import requests
import json

url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana,binancecoin,cardano"
}

response = requests.get(url, params=parameters)

data = response.json()

with open("../data/crypto_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Crypto data saved successfully!")