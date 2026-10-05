balance = 15000
transactions = []

while True:

    print("\n========== ATM ==========")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Mini Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append("Deposited ₹" + str(amount))
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            transactions.append("Withdrawn ₹" + str(amount))
            print("Withdrawal successful.")

    elif choice == "4":
        print("\n===== MINI STATEMENT =====")

        if len(transactions) == 0:
            print("No transactions available.")
        else:
            for transaction in transactions:
                print(transaction)

        print("Current Balance: ₹", balance)

    elif choice == "5":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Try again.")