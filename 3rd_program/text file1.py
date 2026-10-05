# Password Validation and Caesar Cipher Encryption

import string

def check_password(password):
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    return has_upper and has_lower and has_digit and has_special


def encrypt(password):
    result = ""

    for char in password:
        result += chr(ord(char) + 3)

    return result


password = input("Enter your password: ")

if check_password(password):
    encrypted = encrypt(password)

    with open("password.txt", "w") as file:
        file.write(encrypted)

    print("Password is strong.")
    print("Encrypted password saved successfully.")
else:
    print("Weak password!")
    print("Use at least 8 characters with uppercase, lowercase, digit and special character.")
