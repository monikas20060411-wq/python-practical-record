import matplotlib.pyplot as plt
employees = ["Pattu", "sangavi", "Meera", "Kaviya"]
salary = [25000, 30000, 28000, 35000]
plt.bar(employees, salary)
plt.title("Employee Salary")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.savefig("employee_salary.png")
print("Salary chart created successfully!")