# smart-sales-raw-data

This repo provides **raw data** for the Smart Sales project.

These CSV files represent the **original, messy, real-world data** typically received from point-of-sale systems or other information sources, before any cleaning, transformation, or analysis.

## Instructions

1. Open your smart sales repository in VS Code. 
2. Run `git pull` to ensure you have the most current work from your GitHub repository. 
3. Create a folder named `data`, and in that data folder, create another folder named `raw`. 
4. Save each .csv (comma separated value) file in this repo's `data\raw` folder to the `data/raw` folder of your smart sales repository. 
5. Git add-commit-push your work to your GitHub repository.


## Raw Data Examples

`data/raw/customers_data.csv`

```csv
CustomerID,Name,Region,JoinDate
1000,Robert Gomez,West,2024-02-25
1001,John Silva,East,2020-12-01
```

`data/raw/products_data.csv`

```csv
ProductID,ProductName,Category,UnitPrice
2000,Electronics-Be,Electronics,969.31
2001,Electronics-Be,Clothing,412.35
```

`data/raw/sales_data.csv`

```csv
TransactionID,SaleDate,CustomerID,ProductID,StoreID,CampaignID,SaleAmount
1,2025-05-04,1034,2059,402,0,2048.2
2,2025-05-04,1066,2048,403,1,321.87
```


## Recommended Tools

- VS Code Extension: Rainbow CSV – colors columns for easier reading and alignment
- Optional: Excel or Google Sheets – to explore and preview raw 

## Optional Reference

Learn more about how different tools handle date fields - see [REF-DATES.md](REF-DATES.md)
