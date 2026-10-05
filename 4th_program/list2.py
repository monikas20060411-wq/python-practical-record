import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    contact = {
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: ")
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added.")


def search_contact(contacts):
    keyword = input("Enter name or phone: ").lower()

    for contact in contacts:
        if (keyword in contact["name"].lower()
                or keyword in contact["phone"]):
            print(contact)


def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted.")
            return

    print("Contact not found.")


contacts = load_contacts()

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Display All")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        search_contact(contacts)

    elif choice == "3":
        delete_contact(contacts)

    elif choice == "4":
        for contact in contacts:
            print(contact)

    elif choice == "5":
        save_contacts(contacts)
        break

    else:
        print("Invalid choice.")
