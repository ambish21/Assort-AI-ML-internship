import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load .env variables
load_dotenv()

# Get MongoDB connection URL
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Test connection
client.admin.command("ping")

# Day 17 database
db = client["day17_crud_db"]

# Students collection
students_collection = db["students"]

print("MongoDB connected successfully!")