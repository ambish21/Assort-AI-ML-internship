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
        print("Student not found")


def main():

    while True:

        print("===== Student Marks System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")


        choice = input("Enter choice: ")


        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            break

        else:
            print("Invalid choice")


main()