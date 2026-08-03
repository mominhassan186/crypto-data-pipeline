import os
from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)

query = """
SELECT
    coin_name,
    symbol,
    current_price,
    market_cap_rank,
    last_updated
FROM crypto_prices
ORDER BY market_cap_rank;
"""

df = pd.read_sql(query, engine)

st.set_page_config(
    page_title="Crypto Data Pipeline",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Crypto Data Pipeline Dashboard")

st.write("Live cryptocurrency data stored in PostgreSQL.")

st.dataframe(df, use_container_width=True)