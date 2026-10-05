import json

FILE = "phonebook.json"


def load_contacts():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts():
    with open(FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    phone = input("Enter phone number: ")

    if phone in contacts:
        print("Contact already exists.")
        return

    contacts[phone] = {
        "name": input("Enter name: "),
        "email": input("Enter email: ")
    }

    save_contacts()
    print("Contact added.")


def search_contact():
    phone = input("Enter phone number: ")

    if phone in contacts:
        print("Name:", contacts[phone]["name"])
        print("Email:", contacts[phone]["email"])
    else:
        print("Contact not found.")


def delete_contact():
    phone = input("Enter phone number: ")

    if phone in contacts:
        del contacts[phone]
        save_contacts()
        print("Contact deleted.")
    else:
        print("Contact not found.")


def display_all():
    if not contacts:
        print("No contacts.")

    for phone, details in contacts.items():
        print("\nPhone:", phone)
        print("Name:", details["name"])
        print("Email:", details["email"])


contacts = load_contacts()

while True:
    print("\n===== PHONE BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        display_all()

    elif choice == "5":
        save_contacts()
        break

    else:
        print("Invalid choice.")
