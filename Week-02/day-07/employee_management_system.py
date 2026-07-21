import json


employees = []


# Add Employee
def add_employee():

    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))
    experience = int(input("Enter experience (years): "))


    employee = {
        "name": name,
        "department": department,
        "salary": salary,
        "experience": experience
    }


    employees.append(employee)

    print("Employee added successfully!\n")



# View All Employees
def view_employees():

    if len(employees) == 0:
        print("No employee records found.\n")

    else:

        print("\nEmployee Records:")

        for index, employee in enumerate(employees, start=1):

            print(f"\nEmployee {index}")

            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            print("Experience:", employee["experience"], "years")

        print()



# Search Employee
def search_employee():

    name = input("Enter employee name to search: ")


    for employee in employees:

        if employee["name"].lower() == name.lower():

            print("\nEmployee Found")

            print(employee)

            return


    print("Employee not found.\n")



# Save Data into JSON File
def save_data():

    file = open("employees.json", "w")

    json.dump(employees, file, indent=4)

    file.close()


    print("Employee data saved successfully!\n")



# Load Data from JSON File
def load_data():

    global employees


    try:

        file = open("employees.json", "r")

        employees = json.load(file)

        file.close()


    except FileNotFoundError:

        employees = []



# Main Menu
def menu():

    load_data()


    while True:

        print("===== Employee Management System =====")

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Save Data")
        print("5. Exit")


        choice = input("Enter your choice: ")


        if choice == "1":

            add_employee()


        elif choice == "2":

            view_employees()


        elif choice == "3":

            search_employee()


        elif choice == "4":

            save_data()


        elif choice == "5":

            print("Program closed.")

            break


        else:

            print("Invalid choice!\n")



menu()