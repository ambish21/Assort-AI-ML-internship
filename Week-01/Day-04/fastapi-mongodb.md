# FastAPI with MongoDB Atlas

## Project Setup

Created a Python virtual environment.

Installed packages

pip install fastapi

pip install uvicorn

pip install motor

pip install pymongo

pip install python-dotenv

---

## Purpose of Libraries

### FastAPI

Framework for building APIs.

### Uvicorn

ASGI server used to run FastAPI.

### Motor

Asynchronous MongoDB driver for FastAPI.

### PyMongo

Official MongoDB Python driver.

### python-dotenv

Loads environment variables from a `.env` file.

---

## Database Connection

Used a MongoDB Atlas connection string stored inside the `.env` file.

Example

MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/

The application reads the connection string securely without hardcoding credentials.

---

## Learning Outcome

- Built a FastAPI project.
- Connected FastAPI to MongoDB Atlas.
- Learned secure database configuration using environment variables.
- Understood how backend applications communicate with cloud databases.