# Student Information System

name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
roll_no = input("Enter Roll Number: ")
course = input("Enter Course Name: ")

english = float(input("English Marks: "))
math = float(input("Math Marks: "))
science = float(input("Science Marks: "))

total = english + math + science
average = total / 3

if average >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\n===== Student Information =====")

print("Name:", name)
print("Age:", age)
print("Roll Number:", roll_no)
print("Course:", course)

print("English:", english)
print("Math:", math)
print("Science:", science)

print("Total:", total)
print("Average:", average)
print("Result:", result)