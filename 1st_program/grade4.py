# Grade Analyzer with validation

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    marks = float(input("Enter marks (0-100): "))

    while marks < 0 or marks > 100:
        print("Invalid marks! Enter a value between 0 and 100.")
        marks = float(input("Enter marks again: "))

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

    if marks >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("Name   :", name)
    print("Marks  :", marks)
    print("Grade  :", grade)
    print("Result :", result)
