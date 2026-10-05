doctors = []

def add_doctor():
    doctor = {
        "id": input("Doctor ID: "),
        "name": input("Doctor Name: "),
        "specialization": input("Specialization: ")
    }

    doctors.append(doctor)
    print("Doctor added successfully.")


def view_doctors():
    for doctor in doctors:
        print(doctor)


add_doctor()
view_doctors()
