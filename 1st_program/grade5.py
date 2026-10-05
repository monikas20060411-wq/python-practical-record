# Student Grade Analyzer for Multiple Students

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

for student in range(1, students + 1):

    print(f"\nStudent {student}")
    total = 0

    for subject in range(1, subjects + 1):
        mark = float(input(f"Enter mark for subject {subject}: "))
        total += mark

    average = total / subjects

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
