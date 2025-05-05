# REFERENCE: Dates are Complex

These raw CSV files use the international date format: YYYY-MM-DD.
Different tools handle dates in different ways. 
Here are a few examples we may see later in the processing.

## Dates in Python (pandas)

When reading a CSV, we can parse date columns using:

`df = pd.read_csv("data/raw/sales_data.csv", parse_dates=["SaleDate"])`

We can then filter by date like this:

`df[df["SaleDate"] >= "2024-01-01"]`


## Dates in DuckDB

DuckDB is designed specifically for OLAP (Online Analytical Processing) — analyzing large datasets efficiently.
It can auto-detect date types when reading from CSVs, handles ISO-formatted dates natively, and supports powerful SQL-based date operations:

`SELECT SaleDate, EXTRACT(YEAR FROM SaleDate) AS Year, EXTRACT(MONTH FROM SaleDate) AS Month
FROM sales_data;`


## Dates in SQLite

SQLite stores dates as text, but supports common date functions like `DATE()` and `strftime()` (short for "string format time" from the C programming language):

Filter by date:

```SQL
SELECT * FROM sales_data
WHERE DATE(SaleDate) >= '2024-01-01';
```

Extract just the year using string formats:

```SQL
SELECT strftime('%Y', SaleDate) AS Year FROM sales_data;
```

## Dates in PostgreSQL

PostgreSQL has robust native date types and supports EXTRACT, TO_DATE, and interval operations:

`SELECT EXTRACT(YEAR FROM SaleDate) AS Year FROM sales_data;`

## Dates in SQL Server

SQL Server uses YEAR(), MONTH(), and supports conversion with CAST or CONVERT:

`SELECT YEAR(SaleDate) AS Year FROM sales_data;`
