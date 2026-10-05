import pandas as pd

# Sales dataset
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

print("================================")
print("      SALES DATA ANALYSIS")
print("================================")

print("\nOriginal Data:")
print(df)

# 1. Statistical analysis
print("\n===== STATISTICS =====")

print("Total Revenue:",
      df["Revenue"].sum())

print("Average Revenue:",
      df["Revenue"].mean())

print("Median Revenue:",
      df["Revenue"].median())

print("Standard Deviation:",
      df["Revenue"].std())

# 2. Product-wise sales
print("\n===== PRODUCT-WISE SALES =====")

product_sales = df.groupby("Product")["Revenue"].sum()

print(product_sales)

# 3. Category-wise sales
print("\n===== CATEGORY-WISE SALES =====")

category_sales = df.groupby("Category")["Revenue"].sum()

print(category_sales)

# 4. Region-wise sales
print("\n===== REGION-WISE SALES =====")

region_sales = df.groupby("Region")["Revenue"].sum()

print(region_sales)

# 5. Best product
best_product = product_sales.idxmax()

print("\nBest Product:", best_product)
print("Revenue:", product_sales.max())

# 6. Best region
best_region = region_sales.idxmax()

print("Best Region:", best_region)
print("Revenue:", region_sales.max())

# 7. Sort by revenue
print("\n===== SALES SORTED BY REVENUE =====")

sorted_data = df.sort_values(
    by="Revenue",
    ascending=False
)

print(sorted_data)

# 8. High-value transactions
print("\n===== HIGH VALUE TRANSACTIONS =====")

high_value = df[df["Revenue"] > 100000]

print(high_value)

# 9. Total quantity sold
print("\nTotal Quantity Sold:",
      df["Quantity"].sum())

# 10. Save analyzed data
df.to_csv("sales_analysis.csv", index=False)

print("\nSales analysis saved successfully.")
