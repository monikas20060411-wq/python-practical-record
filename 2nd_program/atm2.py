correct_pin = "1234"
balance = 10000

pin = input("Enter your PIN: ")

if pin == correct_pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance: ₹", balance)

        elif choice == 2:
            deposit = float(input("Enter amount to deposit: "))

            if deposit > 0:
                balance += deposit
                print("Deposit successful.")
                print("Balance: ₹", balance)
            else:
                print("Enter a valid amount.")

        elif choice == 3:
            withdrawal = float(input("Enter amount to withdraw: "))

            if withdrawal <= 0:
                print("Enter a valid amount.")
            elif withdrawal > balance:
                print("Insufficient balance.")
            else:
                balance -= withdrawal
                print("Withdrawal successful.")
                print("Balance: ₹", balance)

        elif choice == 4:
            print("Thank you. Visit again!")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN.")
    print("Transaction cancelled.")