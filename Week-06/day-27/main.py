from fastapi import FastAPI
from database import students_collection

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Async Student API is running!"}


@app.get("/students")
async def get_students():
    students = await students_collection.find().to_list(length=None)

    for student in students:
        student["_id"] = str(student["_id"])

    return students

from fastapi import FastAPI
from database import students_collection

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Async Student API is running!"}


@app.get("/students")
async def get_students():
    students = await students_collection.find().to_list(length=None)

    for student in students:
        student["_id"] = str(student["_id"])

    return students


@app.post("/students")
async def create_student(student: dict):
    result = await students_collection.insert_one(student)

    return {
        "message": "Student created successfully",
        "student_id": str(result.inserted_id)
    }
    
@app.put("/students/{student_id}")
async def update_student(student_id: str, student: dict):
    from bson import ObjectId

    result = await students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student}
    )

    if result.matched_count == 0:
        return {"message": "Student not found"}

    return {"message": "Student updated successfully"}  

@app.delete("/students/{student_id}")
async def delete_student(student_id: str):
    from bson import ObjectId

    result = await students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Student not found"}

    return {"message": "Student deleted successfully"}
  