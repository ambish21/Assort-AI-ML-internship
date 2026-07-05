# Day 02 - FastAPI Fundamentals

**Date:** 3 July 2026

---

# What is FastAPI?

FastAPI is a modern, high-performance Python web framework used to build APIs quickly and efficiently. It is designed for speed, ease of development, and automatic documentation generation.

It is built on top of:
- Starlette (for web features)
- Pydantic (for data validation)

### Key Features

- High Performance
- Automatic API Documentation
- Data Validation
- Type Hint Support
- Asynchronous Programming
- Easy to Learn

---

# Why is FastAPI Popular?

FastAPI has become one of the most popular backend frameworks because it combines simplicity with excellent performance.

### Advantages

- Very fast execution
- Minimal code
- Easy API development
- Built-in Swagger UI documentation
- Automatic request validation
- Suitable for AI/ML projects
- Easy integration with databases

---

# What is an API?

API stands for **Application Programming Interface**.

An API allows two different software applications to communicate with each other.

Example:

A mobile app requests user data from a server.

```
Mobile App
      │
      ▼
API Request
      │
      ▼
Backend Server
      │
      ▼
Database
      │
      ▼
JSON Response
      │
      ▼
Mobile App
```

---

# What is a REST API?

REST stands for **Representational State Transfer**.

A REST API follows a set of rules that allow clients and servers to communicate over HTTP.

Characteristics:

- Client-Server Architecture
- Stateless Communication
- Uses HTTP Methods
- Data exchanged using JSON
- Resource-based URLs

Example:

```
/users
/products
/orders
/books
```

---

# CRUD Operations

CRUD represents the four basic operations performed on data.

| Operation | HTTP Method | Description          |
|-----------|-------------|----------------------|
| Create    | POST        | Add new data         |
| Read      | GET         | Retrieve data        |
| Update    | PUT         | Modify existing data |
| Delete    | DELETE      | Remove data          |

Example:

```
GET    /students
POST   /students
PUT    /students/1
DELETE /students/1
```

---

# HTTP Methods

## GET

Retrieves data from the server.

Example:

```
GET /users
```

Returns:

```json
[
    {
        "id":1,
        "name":"Ali"
    }
]
```

---

## POST

Creates new data.

Example:

```
POST /users
```

---

## PUT

Updates existing data.

Example:

```
PUT /users/1
```

---

## DELETE

Deletes existing data.

Example:

```
DELETE /users/1
```

---

# JSON

JSON stands for **JavaScript Object Notation**.

It is the standard format used for exchanging data between the client and server.

Example:

```json
{
    "id":1,
    "name":"John",
    "age":22
}
```

Advantages:

- Lightweight
- Easy to Read
- Language Independent
- Widely Supported

---

# Request and Response

A client sends a **Request** to the server.

The server processes it and returns a **Response**.

Example Flow

```
Client
   │
   ▼
HTTP Request
   │
   ▼
FastAPI Server
   │
   ▼
Business Logic
   │
   ▼
JSON Response
   │
   ▼
Client
```

---

# Client-Server Communication

The client (browser, mobile app, frontend) communicates with the backend through APIs.

Workflow:

1. Client sends an HTTP request.
2. FastAPI receives the request.
3. FastAPI executes the required function.
4. Data is processed.
5. JSON response is generated.
6. Client receives and displays the result.

Example

```
Browser
    │
 GET /users
    │
    ▼
FastAPI
    │
Retrieve Data
    │
    ▼
JSON
    │
    ▼
Browser
```

---

# Summary

On Day 02, I learned:

- FastAPI fundamentals
- API architecture
- REST principles
- CRUD operations
- HTTP methods
- JSON data exchange
- Client-server communication
- FastAPI development workflow
- Swagger UI for API testing