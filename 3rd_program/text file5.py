# Menu-Driven Password Security System

import hashlib

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    return score


while True:

    print("\n===== PASSWORD SECURITY SYSTEM =====")
    print("1. Check Password Strength")
    print("2. Encrypt and Store Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("Enter password: ")
        score = check_strength(password)

        if score == 5:
            print("Password Strength: Very Strong")
        elif score >= 3:
            print("Password Strength: Strong")
        elif score == 2:
            print("Password Strength: Medium")
        else:
            print("Password Strength: Weak")

    elif choice == "2":

        password = input("Enter password: ")

        if check_strength(password) >= 4:

            hashed = hashlib.sha256(
                password.encode()
            ).hexdigest()

            with open("secure_password.txt", "w") as file:
                file.write(hashed)

            print("Password securely hashed and stored.")

        else:
            print("Password is too weak to store.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
1