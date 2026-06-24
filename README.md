# Automated Financial Data Pipeline

Automated ETL pipeline that extracts stock market data from Yahoo Finance, transforms it using financial analytics calculations, and loads it into a SQLite database for reporting and business intelligence purposes.

## Project Overview

This project demonstrates an end-to-end data engineering workflow:

1. Extract financial market data using Yahoo Finance API
2. Transform and enrich the dataset with calculated metrics
3. Load processed data into SQLite
4. Perform SQL analytics on the resulting database

## Features

- Automated ETL process
- Multi-stock market data extraction
- Daily return calculations
- Moving Average indicators (MA20, MA50)
- Volatility analysis
- SQLite data warehouse
- SQL analytical queries
- BI-ready dataset generation

## Data Pipeline Architecture

Yahoo Finance API
↓
Python / Pandas
↓
Data Transformation
↓
SQLite Database
↓
SQL Analytics

## Technologies

- Python
- Pandas
- Yahoo Finance API
- SQLite
- SQL
- Git
- GitHub

## Example Analytics

### Average Stock Price Analysis

![Average Price](screenshots/avgprice.png)

### Dataset Preview

![Dataset Preview](screenshots/dataset_preview.png)

### Volatility Analysis

![Volatility Analysis](screenshots/volatility_analysis.png)

### ETL Execution

![ETL Run](screenshots/etl_run.png)

## Business Value

The pipeline automates the collection and preparation of financial market data, making it suitable for:

- Financial analysis
- Investment research
- Business intelligence dashboards
- Data warehouse development
- Quantitative analytics

## Author

Cosmin-Gabriel Chiriță