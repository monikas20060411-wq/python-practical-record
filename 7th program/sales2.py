import pandas as pd
import numpy as np

# Create dataset
data = {
    "Product": [
        "Laptop", "Laptop",
        "Phone", "Phone",
        "Tablet", "Tablet",
        "Headphones", "Headphones",
        "Keyboard", "Keyboard"
    ],

    "Category": [
        "Electronics", "Electronics",
        "Electronics", "Electronics",
        "Electronics", "Electronics",
        "Accessories", "Accessories",
        "Accessories", "Accessories"
    ],

    "Region": [
        "Chennai", "Mumbai",
        "Chennai", "Delhi",
        "Mumbai", "Delhi",
        "Chennai", "Mumbai",
        "Delhi", "Chennai"
    ],

    "Quantity": [
        5, 4, 10, 8, 6,
        7, 15, 12, 20, 18
    ],

    "Price": [
        60000, 60000,
        30000, 30000,
        20000, 20000,
        3000, 3000,
        1500, 1500
    ]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print("===================================")
print("       SALES DATA ANALYSIS")
print("===================================")

print(df)

# Total revenue
total_revenue = np.sum(df["Revenue"])

# Average revenue
average_revenue = np.mean(df["Revenue"])

# Median revenue
median_revenue = np.median(df["Revenue"])

# Standard deviation
std_revenue = np.std(df["Revenue"])

print("\n===== STATISTICS =====")
print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Median Revenue:", median_revenue)
print("Standard Deviation:", std_revenue)

# Product-wise revenue
product_sales = df.groupby("Product")["Revenue"].sum()

print("\n===== PRODUCT-WISE SALES =====")
print(product_sales)

# Region-wise revenue
region_sales = df.groupby("Region")["Revenue"].sum()

print("\n===== REGION-WISE SALES =====")
print(region_sales)

# Category-wise revenue
category_sales = df.groupby("Category")["Revenue"].sum()

print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)

# Best product
best_product = product_sales.idxmax()

print("\nBest Product:", best_product)
print("Revenue:", product_sales.max())

# Best region
best_region = region_sales.idxmax()

print("Best Region:", best_region)
print("Revenue:", region_sales.max())

# High-value transactions
high_sales = df[df["Revenue"] > 100000]

print("\n===== HIGH VALUE SALES =====")
print(high_sales)

# Total quantity
total_quantity = np.sum(df["Quantity"])

print("\nTotal Quantity Sold:", total_quantity)

# Save result
df.to_csv("sales_analysis.csv", index=False)

print("\nAnalysis saved to sales_analysis.csv")
