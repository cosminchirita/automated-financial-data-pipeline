import yfinance as yf
import pandas as pd
from pathlib import Path

TICKERS = ["AAPL", "MSFT", "NVDA", "TSLA", "SAP.DE", "BP.L"]

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

all_data = []

for ticker in TICKERS:
    print(f"Downloading data for {ticker}...")

    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")

    if hist.empty:
        print(f"No data found for {ticker}")
        continue

    hist = hist.reset_index()
    hist["Ticker"] = ticker

    hist = hist[[
        "Ticker",
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]]

    all_data.append(hist)

if all_data:
    final_data = pd.concat(all_data, ignore_index=True)

    final_data["Date"] = pd.to_datetime(final_data["Date"], utc=True).dt.date

    final_data["Daily_Return"] = final_data.groupby("Ticker")["Close"].pct_change() * 100
    final_data["MA20"] = final_data.groupby("Ticker")["Close"].transform(
        lambda x: x.rolling(window=20).mean()
    )
    final_data["MA50"] = final_data.groupby("Ticker")["Close"].transform(
        lambda x: x.rolling(window=50).mean()
    )
    final_data["Volatility_20D"] = final_data.groupby("Ticker")["Daily_Return"].transform(
        lambda x: x.rolling(window=20).std()
    )

    final_data.to_csv(DATA_DIR / "stock_market_data.csv", index=False)

    print("ETL completed successfully.")
    print(f"Rows exported: {len(final_data)}")

else:
    print("No data downloaded.")