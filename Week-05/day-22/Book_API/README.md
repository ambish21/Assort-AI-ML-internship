# Day 22 — Book Management API

## Overview

A simple Book Management API built with **FastAPI** to practice API routing, path parameters, and query parameters.

## Features

* Add a book
* Search for books
* Delete a book
* Interactive API testing with Swagger UI

## Endpoints

| Method | Endpoint                     | Purpose               |
| ------ | ---------------------------- | --------------------- |
| POST   | `/books`                     | Add a new book        |
| GET    | `/books/search?title=Python` | Search books by title |
| DELETE | `/books/{book_id}`           | Delete a book         |

## Technologies

* Python
* FastAPI
* Uvicorn

## Run the Project

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Concepts Practiced

* FastAPI routing
* Path parameters
* Query parameters
* HTTP methods
* Request and response handling
* Swagger UI

## Project Status

Day 22 FastAPI Routing assignment completed successfully.
