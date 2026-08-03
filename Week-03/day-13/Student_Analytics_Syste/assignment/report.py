"""
Generate Student Report
"""

from student_analytics import (
    calculate_average,
    top_students,
    pass_students,
    fail_students,
    uppercase_names,
    highest_student,
    lowest_student,
)


def generate_report(students):

    print("=" * 60)
    print("        STUDENT ANALYTICS REPORT")
    print("=" * 60)

    print(f"\nAverage Marks : {calculate_average(students):.2f}")

    highest = highest_student(students)
    print(f"Highest Student : {highest['name']} ({highest['marks']})")

    lowest = lowest_student(students)
    print(f"Lowest Student : {lowest['name']} ({lowest['marks']})")

    print("\nTop Students (80+)")
    print("-" * 30)

    for student in top_students(students):
        print(student["name"], "-", student["marks"])

    print("\nPass Students")
    print("-" * 30)

    for student in pass_students(students):
        print(student["name"], "-", student["marks"])

    print("\nFail Students")
    print("-" * 30)

    fails = fail_students(students)

    if len(fails) == 0:
        print("No Failed Students")
    else:
        for student in fails:
            print(student["name"], "-", student["marks"])

    print("\nUppercase Names")
    print("-" * 30)

    for student in uppercase_names(students):
        print(student["name"])

    print("=" * 60)