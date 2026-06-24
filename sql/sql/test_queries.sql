SELECT
    ticker,
    ROUND(AVG(close),2) AS avg_price
FROM stock_prices
GROUP BY ticker
ORDER BY avg_price DESC;
SELECT COUNT(*)
FROM stock_prices;
SELECT *
FROM stock_prices
LIMIT 10;
SELECT
    ticker,
    ROUND(AVG(close),2) AS avg_price

