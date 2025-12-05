import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("grocery_prices.csv")

# Create folder for plots
if not os.path.exists("plots"):
    os.makedirs("plots")

print("\n--- SAMPLE DATA ---")
print(df.head())

# Cheapest store per item
cheapest = df.loc[df.groupby("Item")["Price"].idxmin()]
print("\n--- CHEAPEST STORE FOR EACH ITEM ---")
print(cheapest[["Item", "Store", "Price"]])

# Monthly average price
month_avg = df.groupby("Month")["Price"].mean()

plt.figure(figsize=(8, 5))
plt.plot(month_avg.index, month_avg.values, marker="o")
plt.title("Average Grocery Price - Monthly Inflation Trend")
plt.xlabel("Month")
plt.ylabel("Average Price")
plt.grid(True)
plt.savefig("plots/monthly_inflation.png")
plt.close()

# Price stability stats
stats = df.groupby("Item")["Price"].agg(["mean", "std", "var"])
print("\n--- PRICE STABILITY (Mean, STD, Variance) ---")
print(stats)

# Bar charts for each item
for item in df["Item"].unique():
    subset = df[df["Item"] == item]
    plt.figure(figsize=(7, 4))
    plt.bar(subset["Store"], subset["Price"])
    plt.title(f"Price Comparison Across Stores: {item}")
    plt.xlabel("Stores")
    plt.ylabel("Price (₹)")
    plt.grid(True, axis='y')
    plt.savefig(f"plots/{item}_comparison.png")
    plt.close()

# Best store
store_avg = df.groupby("Store")["Price"].mean()
best_store = store_avg.idxmin()

print("\n--- BEST STORE RECOMMENDATION ---")
print(f"Cheapest overall store is: 🏬 {best_store}")
print(store_avg)
