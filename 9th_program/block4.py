patient = input("Patient Name: ")

consultation = float(input("Consultation Fee: "))
medicine = float(input("Medicine Cost: "))
room = float(input("Room Charges: "))

total = consultation + medicine + room

print("\n===== HOSPITAL BILL =====")
print("Patient:", patient)
print("Consultation:", consultation)
print("Medicine:", medicine)
print("Room:", room)
print("Total Bill:", total)
