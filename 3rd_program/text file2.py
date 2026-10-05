# Password Validation using XOR Encryption

def validate_password(password):
    if len(password) < 8:
        return False

    upper = lower = digit = special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    return upper and lower and digit and special


def xor_encrypt(password, key=7):
    encrypted = ""

    for ch in password:
        encrypted += chr(ord(ch) ^ key)

    return encrypted


password = input("Enter password: ")

if validate_password(password):
    encrypted_password = xor_encrypt(password)

    with open("encrypted_password.txt", "w") as file:
        file.write(encrypted_password)

    print("Password validated successfully.")
    print("Encrypted data stored in file.")
else:
    print("Password is not strong enough.")
