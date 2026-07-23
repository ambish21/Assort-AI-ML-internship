import json


# =========================
# Parent Class (Employee)
# =========================
class Employee:

    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        self.__salary = salary          # Encapsulation
        self.experience = experience

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary!")

    # Polymorphism (Parent Method)
    def display(self):
        print("\n----- Employee Details -----")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.get_salary())
        print("Experience:", self.experience, "Years")


# =========================
# Child Class (Inheritance)
# =========================
class Manager(Employee):

    def __init__(self, name, department, salary, experience, team_size):
        super().__init__(name, department, salary, experience)
        self.team_size = team_size

    # Polymorphism (Method Overriding)
    def display(self):
        print("\n----- Manager Details -----")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.get_salary())
        print("Experience:", self.experience, "Years")
        print("Team Size:", self.team_size)


# =========================
# Employee Management
# =========================
class EmployeeManagement:

    def __init__(self):
        self.employees = []
        self.load_data()

    # -------------------------
    # Add Employee
    # -------------------------
    def add_employee(self):

        name = input("Enter Name: ").strip()

        # Duplicate Checking
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                print("Employee already exists!\n")
                return

        department = input("Enter Department: ").strip()

        # Salary Validation
        while True:
            try:
                salary = int(input("Enter Salary: "))
                if salary <= 0:
                    print("Salary must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Enter a valid salary.")

        # Experience Validation
        while True:
            try:
                experience = int(input("Enter Experience (Years): "))
                if experience < 0:
                    print("Experience cannot be negative.")
                    continue
                break
            except ValueError:
                print("Enter a valid experience.")

        role = input("Employee or Manager (E/M): ").lower()

        if role == "m":

            while True:
                try:
                    team_size = int(input("Enter Team Size: "))
                    if team_size < 0:
                        print("Team size cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number.")

            employee = Manager(
                name,
                department,
                salary,
                experience,
                team_size
            )

        else:

            employee = Employee(
                name,
                department,
                salary,
                experience
            )

        self.employees.append(employee)

        print("Employee Added Successfully!\n")

    # -------------------------
    # View Employees
    # -------------------------
    def view_employees(self):

        if not self.employees:
            print("No Employee Records Found.\n")
            return

        for emp in self.employees:
            emp.display()

    # -------------------------
    # Search Employee
    # -------------------------
    def search_employee(self):

        name = input("Enter Employee Name: ").strip()

        for emp in self.employees:

            if emp.name.lower() == name.lower():

                print("\nEmployee Found")
                emp.display()
                return

        print("Employee Not Found.\n")

    # -------------------------
    # Save Data
    # -------------------------
    def save_data(self):

        data = []

        for emp in self.employees:

            if isinstance(emp, Manager):

                data.append({
                    "type": "Manager",
                    "name": emp.name,
                    "department": emp.department,
                    "salary": emp.get_salary(),
                    "experience": emp.experience,
                    "team_size": emp.team_size
                })

            else:

                data.append({
                    "type": "Employee",
                    "name": emp.name,
                    "department": emp.department,
                    "salary": emp.get_salary(),
                    "experience": emp.experience
                })

        # Professional File Handling
        with open("employees.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data Saved Successfully!\n")

    # -------------------------
    # Load Data
    # -------------------------
    def load_data(self):

        try:

            with open("employees.json", "r") as file:
                data = json.load(file)

            for emp in data:

                if emp["type"] == "Manager":

                    obj = Manager(
                        emp["name"],
                        emp["department"],
                        emp["salary"],
                        emp["experience"],
                        emp["team_size"]
                    )

                else:

                    obj = Employee(
                        emp["name"],
                        emp["department"],
                        emp["salary"],
                        emp["experience"]
                    )

                self.employees.append(obj)

        except FileNotFoundError:
            pass

    # -------------------------
    # Menu
    # -------------------------
    def menu(self):

        while True:

            print("\n========== Employee Management ==========")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Save Data")
            print("5. Exit")

            choice = input("Enter Choice: ")

            match choice:

                case "1":
                    self.add_employee()

                case "2":
                    self.view_employees()

                case "3":
                    self.search_employee()

                case "4":
                    self.save_data()

                case "5":
                    print("Program Closed.")
                    break

                case _:
                    print("Invalid Choice!")


# =========================
# Main Program
# =========================
system = EmployeeManagement()
system.menu()

