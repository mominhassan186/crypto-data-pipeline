import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:ui/ux1@localhost:5432/crypto_pipeline"

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