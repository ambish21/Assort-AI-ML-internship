from fastapi import FastAPI
from .models import Employee
from .data import employees

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Employee API!"}


@app.post("/employees")
def add_employee(employee: Employee):
    new_employee = employee.model_dump()

    new_employee["id"] = len(employees) + 1

    employees.append(new_employee)

    return new_employee