balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
            print("New balance:", balance)
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount <= balance:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice.")