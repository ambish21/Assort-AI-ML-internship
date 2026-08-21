from pymongo import MongoClient
from dotenv import load_dotenv
import os


# =====================================
# DATABASE CONNECTION
# =====================================

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["internshipDB"]

students = db["students"]


# =====================================
# 1. MARKS GREATER THAN 80
# =====================================

print("\n--- Students with Marks > 80 ---")

result = students.find({
    "marks": {"$gt": 80}
})

for student in result:
    print(student)


# =====================================
# 2. MARKS BETWEEN 55 AND 75
# =====================================

print("\n--- Students with Marks Between 55 and 75 ---")

result = students.find({
    "marks": {
        "$gte": 55,
        "$lte": 75
    }
})

for student in result:
    print(student)


# =====================================
# 3. DEPARTMENT FILTERING
# =====================================

print("\n--- Students from AI Department ---")

result = students.find({
    "department": "AI"
})

for student in result:
    print(student)


# =====================================
# CLOSE CONNECTION
# =====================================

client.close()