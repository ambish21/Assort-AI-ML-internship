print("===== Student Information System =====")

# Student Details
name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
roll_no = input("Enter Roll Number: ")
course = input("Enter Course Name: ")


# Function to get valid marks
def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} Marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid! Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")


# Get Subject Marks
english = get_marks("English")
math = get_marks("Math")
science = get_marks("Science")

# Calculations
subjects = 3
marks_per_subject = 100

max_marks = subjects * marks_per_subject
obtained_marks = english + math + science
percentage = (obtained_marks / max_marks) * 100

# Result
if percentage >= 50:
    result = "Pass"
else:
    result = "Fail"

# Display Student Information
print("\n========== Student Information ==========")
print("Name           :", name)
print("Age            :", age)
print("Roll Number    :", roll_no)
print("Course         :", course)

print("\n========== Marks ==========")
print("English        :", english)
print("Math           :", math)
print("Science        :", science)

print("\n========== Result ==========")
print("Obtained Marks :", obtained_marks)
print("Total Marks    :", max_marks)
print("Percentage     :", round(percentage, 2), "%")
print("Status         :", result)