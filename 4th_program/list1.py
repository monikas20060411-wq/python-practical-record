contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(contact)
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted.")
            return

    print("Contact not found.")


def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(
                f'{contact["name"]},{contact["phone"]},{contact["email"]}\n'
            )


def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email
                })
    except FileNotFoundError:
        pass


load_contacts()

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Save and Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        save_contacts()
        print("Data saved. Goodbye!")
        break
    else:
        print("Invalid choice.")
