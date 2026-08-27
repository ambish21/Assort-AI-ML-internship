Day 16 — MongoDB Fundamentals 📝

1. NoSQL

NoSQL means Not Only SQL.

It uses flexible data structures instead of traditional tables and rows. MongoDB is a NoSQL database.

2. MongoDB

MongoDB is a document-based NoSQL database.

It stores data in JSON-like documents and provides a flexible schema.

3. Database 

A database is a group of related collections.

Example: internshipDB

4. Collection

A collection is similar to a table in SQL.

A collection contains multiple documents.

Examples: students, employees, and products

5. Document

A document is a single record in MongoDB.

It is stored in a JSON-like format.

{
    "name": "Ali",
    "age": 20,
    "marks": 85
}
6. BSON

BSON stands for Binary JSON.

MongoDB internally stores documents in BSON format. BSON supports more data types than standard JSON, such as ObjectId and Date.

7. MongoDB Compass

MongoDB Compass is the GUI tool for MongoDB.

It allows us to visually create, view, and manage databases, collections, and documents.

8. PyMongo

PyMongo is a Python library used to connect Python applications with MongoDB.

from pymongo import MongoClient
9. MongoClient

MongoClient establishes a connection with the MongoDB server.

client = MongoClient(MONGO_URI)
10. insert_many()

insert_many() is used to insert multiple documents into a collection at the same time.

collection.insert_many(data)
11. Seed Data

Seed data is sample data inserted into a database for testing and practice.

In this project:

100 Students + 100 Employees + 100 Products were inserted.

12. MongoDB Structure
Database
   ↓
Collection
   ↓
Document
   ↓
Fields

Example:

internshipDB
    ↓
Students
    ↓
Document
    ↓
name, age, marks

 Day 16 — Core Concept
MongoDB → Database → Collection → Document → Fields