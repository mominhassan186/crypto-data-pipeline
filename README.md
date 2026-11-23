# 📈 Crypto Data Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline that fetches live cryptocurrency market data from the CoinGecko API, processes it using Python, stores it in PostgreSQL, and visualizes the results through a Streamlit dashboard.

---

## 🚀 Features

- Fetches live cryptocurrency data from the CoinGecko API
- Processes JSON data using Python
- Stores data in PostgreSQL
- Prevents duplicate records
- Records the timestamp of data collection
- Displays the data in an interactive Streamlit dashboard

---

## 🛠 Tech Stack

- Python
- PostgreSQL
- Streamlit
- SQLAlchemy
- psycopg2
- Pandas
- CoinGecko API

---

## 📂 Project Structure

```text
crypto-data-pipeline/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── crypto_data.json
│
├── scripts/
│   ├── main.py
│   ├── fetch_data.py
│   ├── database.py
│   └── insert_data.py
│
└── screenshots/
```

---

## 🔄 ETL Workflow

```text
CoinGecko API
      │
      ▼
Python ETL Scripts
      │
      ▼
PostgreSQL Database
      │
      ▼
Streamlit Dashboard
```

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the ETL pipeline:

```bash
cd scripts
python3 main.py
```

Run the dashboard:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Scheduled data collection using Airflow or Cron
- Historical price tracking
- Interactive charts
- Docker support
- Cloud deployment (AWS)
