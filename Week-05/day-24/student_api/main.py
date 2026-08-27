from fastapi import FastAPI
from database import students_collection
from schemas import Student

app = FastAPI()


@app.post("/students")
def add_student(student: Student):
    student_data = student.model_dump()

    result = students_collection.insert_one(student_data)

    return {
        "message": "Student added successfully",
        "student_id": str(result.inserted_id)
    }
    
@app.get("/students")
def get_students():
    students = []

    for student in students_collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)

    return students    

from fastapi import HTTPException
from bson import ObjectId


@app.get("/students/{student_id}")
def get_student_by_id(student_id: str):
    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student["_id"] = str(student["_id"])

    return student

@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):
    updated_student = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.model_dump()}
    )

    if updated_student.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully"
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    deleted_student = students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    if deleted_student.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }    