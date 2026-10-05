import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
expenses = [5000, 6000, 4500, 7000, 6500]
plt.plot(months, expenses, marker="o")
plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.savefig("expenses.png")
print("Line chart created successfully!")