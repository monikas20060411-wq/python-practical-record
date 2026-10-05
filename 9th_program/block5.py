patients = []

while True:
    print("\n===== HOSPITAL MANAGEMENT =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        patient = {
            "id": input("Patient ID: "),
            "name": input("Name: "),
            "age": input("Age: "),
            "disease": input("Disease: ")
        }

        patients.append(patient)
        print("Patient added.")

    elif choice == "2":
        for patient in patients:
            print(patient)

    elif choice == "3":
        pid = input("Enter Patient ID: ")

        found = False

        for patient in patients:
            if patient["id"] == pid:
                print(patient)
                found = True

        if not found:
            print("Patient not found.")

    elif choice == "4":
        pid = input("Enter Patient ID: ")

        for patient in patients:
            if patient["id"] == pid:
                patients.remove(patient)
                print("Patient deleted.")
                break
        else:
            print("Patient not found.")

    elif choice == "5":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
