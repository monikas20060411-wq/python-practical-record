# ATM Simulation System

balance = 10000.0
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
                print("New Balance: ₹", balance)
            else:
                print("Invalid deposit amount.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance: ₹", balance)

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

else:
    print("Incorrect PIN. Access denied.")
