# MongoDB Atlas Database Setup

## What is MongoDB Atlas?
---

## Tasks Completed

- Created a MongoDB Atlas account.
- Created a free cluster.
- Created a database.
- Created a collection.
- Inserted sample documents.
- Viewed inserted documents.

---

# MongoDB Architecture

MongoDB follows a hierarchical structure.

Organization
    ↓
Project
    ↓
Cluster
    ↓
Database
    ↓
Collection
    ↓
Documents

### Organization

The highest level where multiple projects are managed.

### Project

A project groups related clusters together.

### Cluster

A cluster is the server where databases are stored.

### Database

A database contains collections.

### Collection

A collection stores multiple documents.

### Document

A document is a JSON-like object that stores actual data.

Example

{
    "name": "Ali",
    "age": 21,
    "city": "Lahore"
}

---

# MongoDB Compass

MongoDB Compass is a graphical interface (GUI) for MongoDB.

Uses:

- View databases
- Browse collections
- Insert documents
- Update documents
- Delete documents
- Execute queries visually

---

# Local MongoDB vs MongoDB Atlas

Local MongoDB

- Installed on your own computer.
- Works without internet.
- Good for development.
- You manage storage and updates.

MongoDB Atlas

- Hosted on the cloud.
- Accessible from anywhere.
- Automatic backups.
- Easy to scale.
- Suitable for production applications.

---

# FastAPI Project Setup

Today I created a FastAPI project.

Steps:

- Created a project folder.
- Created a virtual environment.
- Activated the virtual environment.
- Installed required packages.

Packages Installed

- FastAPI
- Uvicorn
- Motor
- PyMongo
- python-dotenv

---

# Environment Variables (.env)

The `.env` file stores sensitive information like database connection strings.

Example

MONGODB_URL=your_connection_string

Benefits

- Keeps passwords secure.
- Prevents exposing credentials in code.
- Easy to manage across environments.

---

# FastAPI + MongoDB Connection

Connected FastAPI with MongoDB Atlas using:

- Connection String
- Motor (Async MongoDB Driver)
- python-dotenv
- .env configuration
The application successfully connected to the cloud database.