from pymongo import MongoClient
import random


# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")


# 2. Select database
db = client["internshipDB"]


# 3. Select collections
students = db["students"]
employees = db["employees"]
products = db["products"]


# ---------------- STUDENTS ----------------

departments = ["AI", "CS", "SE", "IT"]

student_data = []

for i in range(1, 101):

    student = {
        "student_id": i,
        "name": f"Student {i}",
        "age": random.randint(18, 25),
        "department": random.choice(departments),
        "semester": random.randint(1, 8),
        "marks": random.randint(50, 100)
    }

    student_data.append(student)


students.delete_many({})
students.insert_many(student_data)


# ---------------- EMPLOYEES ----------------

employee_data = []

for i in range(1, 101):

    employee = {
        "employee_id": i,
        "name": f"Employee {i}",
        "department": random.choice(departments),
        "salary": random.randint(40000, 150000),
        "experience": random.randint(0, 10)
    }

    employee_data.append(employee)


employees.delete_many({})
employees.insert_many(employee_data)


# ---------------- PRODUCTS ----------------

categories = [
    "Laptop",
    "Mobile",
    "Accessories",
    "Monitor"
]

product_data = []

for i in range(1, 101):

    product = {
        "product_id": i,
        "name": f"Product {i}",
        "category": random.choice(categories),
        "price": random.randint(1000, 200000),
        "stock": random.randint(0, 100)
    }

    product_data.append(product)


products.delete_many({})
products.insert_many(product_data)


print("100 Students inserted.")
print("100 Employees inserted.")
print("100 Products inserted.")


# Close connection
client.close()