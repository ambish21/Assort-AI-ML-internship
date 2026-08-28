# Day 27 — Async Programming

## Topics

* `async`
* `await`
* Motor MongoDB Driver
* Async FastAPI APIs
* Async CRUD Operations

## Project

### Async Student Management API

Converted FastAPI APIs to an asynchronous architecture using Motor and `async/await`.

## Features

* Get all students
* Create a student
* Update a student
* Delete a student
* Async MongoDB operations
* Local MongoDB integration

## API Endpoints

| Method | Endpoint                 | Purpose          |
| ------ | ------------------------ | ---------------- |
| GET    | `/students`              | Get all students |
| POST   | `/students`              | Create student   |
| PUT    | `/students/{student_id}` | Update student   |
| DELETE | `/students/{student_id}` | Delete student   |

## Technologies

* Python
* FastAPI
* Motor
* MongoDB
* Uvicorn

## Assignment

**Convert APIs to async architecture**

### Completed

FastAPI CRUD APIs were successfully converted to async using `async`, `await`, and Motor.
