students = {}


def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    students[name] = marks

    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No student record available.\n")
    else:
        print("\nStudent Records:")
        for name, marks in students.items():
            print(name, ":", marks)
        print()


def search_student():
    name = input("Enter student name: ")

    if name in students:
        print("Marks:", students[name])
    else:
        print("Student not found.\n")


def main():
    while True:
        print("===== Student Marks System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                add_student()

            case "2":
                view_students()

            case "3":
                search_student()

            case "4":
                print("Thank you for using Student Marks System!")
                break

            case _:
                print("Invalid choice. Please try again.\n")


main()