import pandas as pd
import numpy as np

items = ["Rice", "Wheat", "Oil", "Milk", "Sugar", "Tea", "Salt", "Bread", "Eggs", "Flour"]
stores = ["DMart", "Reliance", "BigBazaar"]
months = ["Jan", "Feb", "Mar", "Apr"]

data = []

np.random.seed(42)

for item in items:
    for store in stores:
        for month in months:
            price = np.random.randint(20, 200)
            data.append([item, store, month, price])

df = pd.DataFrame(data, columns=["Item", "Store", "Month", "Price"])

df.to_csv("grocery_prices.csv", index=False)

print("Dataset saved as grocery_prices.csv")
