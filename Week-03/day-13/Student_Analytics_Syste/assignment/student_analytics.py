"""
Student Analytics Functions
"""

from functools import reduce


# Average Marks
def calculate_average(students):
    marks = list(map(lambda student: student["marks"], students))
    total = reduce(lambda x, y: x + y, marks)
    return total / len(marks)


# Top Students
def top_students(students):
    return list(filter(lambda student: student["marks"] >= 80, students))


# Pass Students
def pass_students(students):
    return list(filter(lambda student: student["marks"] >= 50, students))


# Fail Students
def fail_students(students):
    return list(filter(lambda student: student["marks"] < 50, students))


# Uppercase Names
def uppercase_names(students):
    return list(
        map(
            lambda student: {
                "id": student["id"],
                "name": student["name"].upper(),
                "marks": student["marks"],
            },
            students,
        )
    )


# Highest Marks
def highest_student(students):
    return max(students, key=lambda student: student["marks"])


# Lowest Marks
def lowest_student(students):
    return min(students, key=lambda student: student["marks"])