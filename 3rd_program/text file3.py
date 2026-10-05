# Password Validation and Base64 Encoding

import base64

password = input("Enter your password: ")

if len(password) >= 8:
    if (any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(not c.isalnum() for c in password)):

        encoded = base64.b64encode(password.encode()).decode()

        with open("password_data.txt", "w") as file:
            file.write(encoded)

        print("Strong password.")
        print("Encoded password saved successfully.")

    else:
        print("Password must contain:")
        print("- Uppercase letter")
        print("- Lowercase letter")
        print("- Number")
        print("- Special character")
else:
    print("Password must contain at least 8 characters.")
