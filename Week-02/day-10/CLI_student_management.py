import json
# ==============================
# Phase 1: Student Class
# ==============================
class Student:

    def __init__(self, roll_no, name, age, department, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def display(self):

        print("-------------------------")
        print(f"Roll No    : {self.roll_no}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")
        print(f"CGPA       : {self.cgpa}")
        print("-------------------------")

    def to_dict(self):

        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "cgpa": self.cgpa
        }



# ==============================
# Phase 2: Student Management
# ==============================

class StudentManagement:


    def __init__(self):

        self.students = []

        self.load_data()



# ==============================
# Phase 3: Add Student
# ==============================


    def add_student(self):

        print("\nAdd New Student")

        roll_no = input("Enter Roll Number: ").upper()


        # Duplicate Check

        for student in self.students:

            if student.roll_no == roll_no:

                print("Student with this Roll Number already exists!")
                return



        name = input("Enter Name: ").strip()


        while True:

            try:

                age = int(input("Enter Age: "))

                if age <= 0:
                    print("Age must be positive")
                    continue

                break

            except ValueError:

                print("Enter valid age")



        department = input("Enter Department: ").strip()



        while True:

            try:

                cgpa = float(input("Enter CGPA: "))


                if cgpa < 0 or cgpa > 4:

                    print("CGPA should be between 0 and 4")
                    continue

                break


            except ValueError:

                print("Enter valid CGPA")



        student = Student(
            roll_no,
            name,
            age,
            department,
            cgpa
        )


        self.students.append(student)

        self.save_data()

        print("Student Added Successfully!")





# ==============================
# Phase 4: View Students
# ==============================


    def view_students(self):

        if len(self.students) == 0:

            print("No Students Found")

            return



        for student in self.students:

            student.display()





# ==============================
# Phase 5: Search Student
# ==============================


    def search_student(self):

        roll_no = input(
            "Enter Roll Number to Search: "
        ).upper()


        for student in self.students:


            if student.roll_no == roll_no:

                print("Student Found")

                student.display()

                return



        print("Student Not Found")





# ==============================
# Phase 6: Update Student
# ==============================


    def update_student(self):

        roll_no = input(
            "Enter Roll Number: "
        ).upper()


        for student in self.students:


            if student.roll_no == roll_no:


                print("Leave blank if you don't want to update")


                name = input(
                    "New Name: "
                )


                if name:

                    student.name = name



                age = input(
                    "New Age: "
                )


                if age:

                    student.age = int(age)



                department = input(
                    "New Department: "
                )


                if department:

                    student.department = department



                cgpa = input(
                    "New CGPA: "
                )


                if cgpa:

                    student.cgpa = float(cgpa)



                self.save_data()


                print("Student Updated")

                return



        print("Student Not Found")





# ==============================
# Phase 7: Delete Student
# ==============================


    def delete_student(self):


        roll_no = input(
            "Enter Roll Number: "
        ).upper()



        for student in self.students:


            if student.roll_no == roll_no:


                self.students.remove(student)


                self.save_data()


                print("Student Deleted")

                return



        print("Student Not Found")





# ==============================
# Phase 8: Save JSON
# ==============================


    def save_data(self):


        data = []


        for student in self.students:

            data.append(
                student.to_dict()
            )



        with open(
            "students.json",
            "w"
        ) as file:


            json.dump(
                data,
                file,
                indent=4
            )






# ==============================
# Phase 9: Load JSON
# ==============================


    def load_data(self):


        try:


            with open(
                "students.json",
                "r"
            ) as file:


                data = json.load(file)



                for student in data:


                    obj = Student(

                        student["roll_no"],
                        student["name"],
                        student["age"],
                        student["department"],
                        student["cgpa"]

                    )


                    self.students.append(obj)



        except FileNotFoundError:


            pass






# ==============================
# Phase 10: Menu System
# ==============================


    def menu(self):


        while True:


            print("\n===== Student Management System =====")

            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Save Data")
            print("7. Exit")



            choice = input(
                "Enter Choice: "
            )



            match choice:


                case "1":

                    self.add_student()



                case "2":

                    self.view_students()



                case "3":

                    self.search_student()



                case "4":

                    self.update_student()



                case "5":

                    self.delete_student()


                case "6":

                    self.save_data()

                    print("Data Saved")
                case "7":

                    print("Goodbye!")

                    break



                case _:

                    print("Invalid Choice")
# ==============================
# Main Program
# ==============================
system = StudentManagement()

system.menu()
