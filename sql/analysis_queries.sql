-- Latest price by ticker
SELECT
    Ticker,
    Date,
    ROUND(Close, 2) AS latest_close
FROM stock_prices
WHERE Date IN (
    SELECT MAX(Date)
    FROM stock_prices
    GROUP BY Ticker
);

-- Average daily return by ticker
SELECT
    Ticker,
    ROUND(AVG(Daily_Return), 2) AS avg_daily_return
FROM stock_prices
GROUP BY Ticker;

-- Highest volatility stocks
SELECT
    Ticker,
    ROUND(AVG(Volatility_20D), 2) AS avg_20d_volatility
FROM stock_prices
GROUP BY Ticker
ORDER BY avg_20d_volatility DESC;

-- Moving average signal
SELECT
    Ticker,
    Date,
    ROUND(Close, 2) AS Close,
    ROUND(MA20, 2) AS MA20,
    ROUND(MA50, 2) AS MA50,
    CASE
        WHEN MA20 > MA50 THEN 'Bullish'
        WHEN MA20 < MA50 THEN 'Bearish'
        ELSE 'Neutral'
    END AS trend_signal
FROM stock_prices
WHERE Date IN (
    SELECT MAX(Date)
    FROM stock_prices
    GROUP BY Ticker
);

-- Total trading volume by ticker
SELECT
    Ticker,
    SUM(Volume) AS total_volume
FROM stock_prices
GROUP BY Ticker
ORDER BY total_volume DESC;