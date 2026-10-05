balance = 8000
correct_pin = "4321"

attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Your account is blocked.")
else:

    while True:
        print("\n===== ATM =====")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance = ₹", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance = balance + amount
                print("Successfully deposited ₹", amount)
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance = balance - amount
                print("Successfully withdrawn ₹", amount)

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Please select a valid option.")