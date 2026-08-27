import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["studentDB"]
students_collection = db["students"]
print("MongoDB Connected:", client.admin.command("ping"))