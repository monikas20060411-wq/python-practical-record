import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]
products = ["Laptop", "Phone", "Tablet", "Watch"]
product_sales = [40, 30, 20, 10]
plt.figure()
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("line_chart1.png")
plt.close()
plt.figure()
plt.bar(months, sales)
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("bar_chart1.png")
plt.close()
plt.figure()
plt.pie(product_sales, labels=products, autopct="%1.1f%%")
plt.title("Product Sales Distribution")
plt.savefig("pie_chart1.png")
plt.close()
print("Line, Bar and Pie charts created successfully!")