import json
import psycopg2

# Read the JSON file
with open("../data/crypto_data.json", "r") as file:
    data = json.load(file)

# Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="crypto_pipeline",
    user="postgres",
    password="ui/ux1"
)

cursor = connection.cursor()
cursor.execute("DELETE FROM crypto_prices;")

# Inserting data
for coin in data:
    cursor.execute("""
    INSERT INTO crypto_prices
    (coin_name, symbol, current_price, market_cap_rank, last_updated)
    VALUES (%s, %s, %s, %s, %s)
""", (
    coin["name"],
    coin["symbol"],
    coin["current_price"],
    coin["market_cap_rank"],
    coin["last_updated"]
))
connection.commit()

print("✅ Data inserted successfully!")

cursor.close()
connection.close()