''' 
create.py

This script generates synthetic data for a sales database, including customers, products, and sales records.        
It creates three CSV files with realistic data, including some intentional errors and duplicates to simulate real-world scenarios.
'''

import pandas as pd
import numpy as np
import random
from faker import Faker
from pathlib import Path

# Setup
fake = Faker()
random.seed(42)
np.random.seed(42)

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------- CUSTOMERS ----------
regions = ["East", "West", "South", "North", "Central"]
customers = []

for cid in range(1000, 1200):
    customers.append({
        "CustomerID": cid,
        "Name": fake.name(),
        "Region": random.choice(regions + ["east", "EAST", "south-west"]),
        "JoinDate": fake.date_between(start_date='-5y', end_date='-1y')
    })

# Add a duplicate
customers.append(customers[5])
customers_df = pd.DataFrame(customers)
customers_df.to_csv(OUTPUT_DIR / "customers_data.csv", index=False)

# ---------- PRODUCTS ----------
categories = ["Electronics", "Clothing", "Home", "Office"]
products = []

for pid in range(2000, 2100):
    pname = f"{random.choice(categories)}-{fake.word().capitalize()}"
    products.append({
        "ProductID": pid,
        "ProductName": pname,
        "Category": random.choice(categories),
        "UnitPrice": round(random.uniform(10, 1000), 2)
    })

products[1]["ProductName"] = products[0]["ProductName"]  # name overlap
products_df = pd.DataFrame(products)
products_df.to_csv(OUTPUT_DIR / "products_data.csv", index=False)

# ---------- SALES ----------
sales = []
store_ids = [401, 402, 403, 404]
campaign_ids = [0, 1, 2, 3]  # 0 = none

for tid in range(1, 2001):
    cust_id = random.choice(customers_df["CustomerID"])
    prod_id = random.choice(products_df["ProductID"])
    store_id = random.choice(store_ids)
    campaign_id = random.choice(campaign_ids)
    date = fake.date_between(start_date='-6mo', end_date='today')
    quantity = np.random.poisson(2)
    unit_price = products_df.loc[products_df['ProductID'] == prod_id, 'UnitPrice'].values[0]
    
    if campaign_id == 1:  # 10% off
        unit_price *= 0.9
    elif campaign_id == 2:  # 20% off
        unit_price *= 0.8
    elif campaign_id == 3 and quantity >= 2:  # BOGO
        quantity += 1

    total = round(unit_price * quantity, 2)

    sales.append({
        "TransactionID": tid,
        "SaleDate": date,
        "CustomerID": cust_id,
        "ProductID": prod_id,
        "StoreID": store_id,
        "CampaignID": campaign_id,
        "SaleAmount": total
    })

# Add some data errors
sales[10]["CampaignID"] = ""
sales[20]["SaleAmount"] = "?"
sales[30]["SaleDate"] = "2023-13-01"  # Invalid date
sales[40]["CustomerID"] = 9999  # Non-existent customer

# Add a duplicate
sales.append(sales[5])

sales_df = pd.DataFrame(sales)
sales_df.to_csv(OUTPUT_DIR / "sales_data.csv", index=False)

print("Raw data saved to data/raw/:")
print("- customers_data.csv")
print("- products_data.csv")
print("- sales_data.csv")
print("Note: Some data contains intentional errors and duplicates to simulate real-world scenarios.")
