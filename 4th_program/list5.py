import json

FILE = "contacts.json"


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data():
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact():
    contact = {
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: "),
        "address": input("Address: ")
    }

    contacts.append(contact)
    save_data()

    print("Contact added successfully.")


def search_contact():
    name = input("Enter name: ").lower()

    results = [
        contact for contact in contacts
        if name in contact["name"].lower()
    ]

    if results:
        for contact in results:
            print(contact)
    else:
        print("No contact found.")


def update_contact():
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            contact["phone"] = input("New phone: ")
            contact["email"] = input("New email: ")
            contact["address"] = input("New address: ")

            save_data()
            print("Contact updated.")
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_data()
            print("Contact deleted.")
            return

    print("Contact not found.")


contacts = load_data()

while True:

    print("\n===== CONTACT MANAGER =====")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        save_data()
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
