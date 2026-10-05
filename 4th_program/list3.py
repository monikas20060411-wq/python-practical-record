contacts = []


def add_contact():
    contact = {}

    contact["id"] = len(contacts) + 1
    contact["name"] = input("Enter name: ")
    contact["phone"] = input("Enter phone: ")
    contact["email"] = input("Enter email: ")

    contacts.append(contact)
    print("Contact added successfully.")


def display_contacts():
    if not contacts:
        print("No contacts available.")
        return

    for contact in contacts:
        print("\nID:", contact["id"])
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def search_contact():
    keyword = input("Enter name: ").lower()

    found = False

    for contact in contacts:
        if keyword in contact["name"].lower():
            print(contact)
            found = True

    if not found:
        print("No contact found.")


def delete_contact():
    contact_id = int(input("Enter contact ID: "))

    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)
            print("Contact deleted.")
            return

    print("Contact not found.")


def save_data():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(
                f'{contact["id"]}|{contact["name"]}|'
                f'{contact["phone"]}|{contact["email"]}\n'
            )


def load_data():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                contacts.append({
                    "id": int(data[0]),
                    "name": data[1],
                    "phone": data[2],
                    "email": data[3]
                })

    except FileNotFoundError:
        pass


load_data()

while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Save and Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        display_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        save_data()
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
