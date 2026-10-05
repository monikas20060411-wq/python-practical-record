# Secure Password Hashing using SHA-256

import hashlib

password = input("Enter your password: ")

if len(password) >= 8:
    if (any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(not c.isalnum() for c in password)):

        hashed_password = hashlib.sha256(
            password.encode()
        ).hexdigest()

        with open("password_hash.txt", "w") as file:
            file.write(hashed_password)

        print("Password is strong.")
        print("SHA-256 hash stored successfully.")

    else:
        print("Password must contain uppercase, lowercase, digit and special character.")
else:
    print("Password must contain at least 8 characters.")
