from crud import (
    insert_student,
    insert_students,
    get_students,
    update_student,
    update_students_by_course,
    delete_student,
    delete_students_by_marks
)


def show_menu():
    print("\n===== STUDENT CRUD SYSTEM =====")
    print("1. Insert One Student")
    print("2. Insert Many Students")
    print("3. View Students")
    print("4. Update Student")
    print("5. Update Students by Course")
    print("6. Delete One Student")
    print("7. Delete Students with Low Marks")
    print("8. Exit")


while True:

    show_menu()

    choice = input("\nEnter choice: ")

    match choice:

        # CREATE - Insert One
        case "1":

            student = {
                "name": input("Name: "),
                "age": int(input("Age: ")),
                "course": input("Course: "),
                "marks": int(input("Marks: "))
            }

            student_id = insert_student(student)

            print(f"Student inserted successfully. ID: {student_id}")

        # CREATE - Insert Many
        case "2":

            students = [
                {
                    "name": "Ali",
                    "age": 21,
                    "course": "AI",
                    "marks": 85
                },
                {
                    "name": "Sara",
                    "age": 22,
                    "course": "CS",
                    "marks": 90
                },
                {
                    "name": "Ahmed",
                    "age": 20,
                    "course": "AI",
                    "marks": 78
                }
            ]

            ids = insert_students(students)

            print(f"{len(ids)} students inserted successfully.")

        # READ
        case "3":

            students = get_students()

            if students:
                for student in students:
                    print(student)
            else:
                print("No students found.")

        # UPDATE ONE
        case "4":

            name = input("Student name: ")
            marks = int(input("New marks: "))

            count = update_student(name, marks)

            if count:
                print("Student updated successfully.")
            else:
                print("Student not found or data already same.")

        # UPDATE MANY
        case "5":

            course = input("Course: ")

            count = update_students_by_course(course)

            print(f"{count} students updated.")

        # DELETE ONE
        case "6":

            name = input("Student name: ")

            count = delete_student(name)

            if count:
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        # DELETE MANY
        case "7":

            count = delete_students_by_marks()

            print(f"{count} students deleted.")

        # EXIT
        case "8":

            print("Program ended successfully.")
            break

        # INVALID INPUT
        case _:

            print("Invalid choice. Please try again.")