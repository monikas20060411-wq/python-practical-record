patients = []

def add_patient():
    patient = {
        "id": input("Patient ID: "),
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "disease": input("Disease: ")
    }

    patients.append(patient)
    print("Patient added successfully.")


def view_patients():
    for p in patients:
        print(p)


add_patient()
view_patients()
