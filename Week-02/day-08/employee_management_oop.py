import json


class Employee:

    def __init__(self, name, department, salary, experience):

        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience


    def display(self):

        print("\nEmployee Details")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Experience:", self.experience)



class EmployeeManagement:


    def __init__(self):

        self.employees = []

        self.load_data()



    # Add Employee

    def add_employee(self):

        name = input("Enter employee name: ")
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        experience = int(input("Enter experience: "))


        employee = Employee(
            name,
            department,
            salary,
            experience
        )


        self.employees.append(employee)

        print("Employee added successfully!\n")



    # View Employees

    def view_employees(self):

        if len(self.employees) == 0:

            print("No employee records found")

        else:

            for employee in self.employees:

                employee.display()



    # Search Employee

    def search_employee(self):

        name = input("Enter employee name: ")


        for employee in self.employees:


            if employee.name.lower() == name.lower():

                print("Employee Found")

                employee.display()

                return


        print("Employee not found")



    # Save Data

    def save_data(self):

        data = []


        for employee in self.employees:

            data.append({

                "name": employee.name,
                "department": employee.department,
                "salary": employee.salary,
                "experience": employee.experience

            })


        file = open("employees.json","w")

        json.dump(data,file,indent=4)

        file.close()


        print("Data saved successfully")



    # Load Data

    def load_data(self):

        try:

            file = open("employees.json","r")

            data = json.load(file)

            file.close()


            for employee in data:

                obj = Employee(

                    employee["name"],
                    employee["department"],
                    employee["salary"],
                    employee["experience"]

                )


                self.employees.append(obj)



        except FileNotFoundError:

            pass




    def menu(self):


        while True:


            print("\n===== Employee Management System =====")

            print("1. Add Employee")
            print("2. View Employee")
            print("3. Search Employee")
            print("4. Save Data")
            print("5. Exit")


            choice = input("Enter choice: ")



            if choice == "1":

                self.add_employee()


            elif choice == "2":

                self.view_employees()


            elif choice == "3":

                self.search_employee()


            elif choice == "4":

                self.save_data()


            elif choice == "5":

                print("Program Closed")

                break


            else:

                print("Invalid Choice")



system = EmployeeManagement()

system.menu()