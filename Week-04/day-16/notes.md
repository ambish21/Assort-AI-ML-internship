Day 16 — MongoDB Fundamentals 📝

1. NoSQL
NoSQL = Not Only SQL
Tables/rows ki jagah flexible data structure use karta hai.
MongoDB ek NoSQL database hai.

2. MongoDB
Document-based NoSQL database.
Data JSON-like documents mein store hota hai.
Flexible schema hota hai.

3. Database
Related collections ka group.
Example: internshipDB

4. Collection
SQL mein table ke similar.
Ek collection mein multiple documents hote hain.
Example: students, employees, products

5. Document
MongoDB ka single record.
JSON-like format mein hota hai.
{
    "name": "Ali",
    "age": 20,
    "marks": 85
}

6. BSON
BSON = Binary JSON
MongoDB documents ko internally BSON format mein store karta hai.
JSON se zyada data types support karta hai, e.g. ObjectId, Date.

7. MongoDB Compass
MongoDB ka GUI tool.
Database, collections aur documents ko visually create/view/manage kar sakte hain.

8. PyMongo
Python ki library jo Python ko MongoDB se connect karti hai.
from pymongo import MongoClient

9. MongoClient
MongoDB server/database ke saath connection establish karta hai.
client = MongoClient(MONGO_URI)

10. insert_many()
Multiple documents ek saath insert karta hai.
collection.insert_many(data)

11. Seed Data
Testing/practice ke liye sample data ko database mein insert karna.
Hamare project mein 100 Students + 100 Employees + 100 Products insert hue.

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
⭐ Day 16 :Core Concept

MongoDB → Database → Collection → Document → Fields