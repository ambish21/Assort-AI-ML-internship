# Day 24 — FastAPI + MongoDB

## Student Management Backend

A Student Management Backend built using FastAPI and MongoDB. The project implements CRUD operations for managing student records.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* PyMongo
* MongoDB
* python-dotenv

## Project Structure

```text
day-24/
├── README.md
└── student_api/
    ├── main.py
    ├── database.py
    ├── schemas.py
    ├── requirements.txt
    ├── .env
    └── .gitignore
```

## Features

* Add a new student
* Get all students
* Get a student by ID
* Update student information
* Delete a student

## API Endpoints

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| POST   | `/students`              | Add a student     |
| GET    | `/students`              | Get all students  |
| GET    | `/students/{student_id}` | Get student by ID |
| PUT    | `/students/{student_id}` | Update student    |
| DELETE | `/students/{student_id}` | Delete student    |

## MongoDB Connection

The application connects to MongoDB using PyMongo.


