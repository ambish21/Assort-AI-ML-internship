from fastapi import FastAPI

app = FastAPI()


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to my Student API!"}


# Student data
students = [
    {
        "id": 1,
        "name": "Ambish",
        "age": 22,
        "department": "Artificial Intelligence"
    },
    {
        "id": 2,
        "name": "Ali",
        "age": 21,
        "department": "Computer Science"
    }
]


# GET endpoint - Get all students
@app.get("/students")
def get_students():
    return {
        "message": "Students retrieved successfully",
        "students": students
    }
    
from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    age: int
    department: str


@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())

    return {
        "message": "Student added successfully",
        "student": student
    }
    
