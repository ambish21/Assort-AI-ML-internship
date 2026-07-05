from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


# About Route
@app.get("/about")
def about():
    return {
        "framework": "FastAPI",
        "language": "Python"
    }


# Path Parameter
@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }


# Query Parameter
@app.get("/search")
def search(name: str):
    return {
        "student_name": name
    }