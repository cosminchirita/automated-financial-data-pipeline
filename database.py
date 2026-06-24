import sqlite3
import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/stock_market_data.csv")
DB_FILE = Path("financial_pipeline.db")

if not DATA_FILE.exists():
    raise FileNotFoundError("CSV file not found. Run etl.py first.")

df = pd.read_csv(DATA_FILE)

conn = sqlite3.connect(DB_FILE)

df.to_sql(
    "stock_prices",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Data loaded successfully into SQLite database.")
print(f"Database created: {DB_FILE}")
print(f"Rows loaded: {len(df)}")