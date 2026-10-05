appointments = []

def book_appointment():
    appointment = {
        "patient": input("Patient Name: "),
        "doctor": input("Doctor Name: "),
        "date": input("Appointment Date: "),
        "time": input("Appointment Time: ")
    }

    appointments.append(appointment)
    print("Appointment booked successfully.")


def view_appointments():
    for appointment in appointments:
        print(appointment)


book_appointment()
view_appointments()
