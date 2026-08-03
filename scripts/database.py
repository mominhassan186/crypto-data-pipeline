import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="crypto_pipeline",
        user="postgres",
        password="ui/ux1"
    )

    print("✅ Connected to PostgreSQL!")

    connection.close()

except Exception as e:
    print("❌ Connection Failed")
    print(e)