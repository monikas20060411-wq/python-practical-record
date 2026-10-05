import pandas as pd
import numpy as np

# Create dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Quantity": [5, 10, 8, 15, 12],
    "Price": [60000, 30000, 20000, 3000, 1500]
}

df = pd.DataFrame(data)

# Calculate sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("SALES DATA")
print(df)

# Statistical calculations
print("\nSTATISTICAL ANALYSIS")
print("Total Sales:", np.sum(df["Total_Sales"]))
print("Average Sales:", np.mean(df["Total_Sales"]))
print("Maximum Sales:", np.max(df["Total_Sales"]))
print("Minimum Sales:", np.min(df["Total_Sales"]))
print("Standard Deviation:", np.std(df["Total_Sales"]))

# Highest selling product
index = np.argmax(df["Total_Sales"])

print("\nBest Selling Product:",
      df.loc[index, "Product"])
