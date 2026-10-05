# Grade Analyzer using while loop

count = 1

while count <= 5:
    print("\nStudent", count)

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Name:", name)
    print("Grade:", grade)

    count += 1
