import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
PORT = int(os.getenv("PORT", 5000))

if MONGO_URI is None:
    raise ValueError("MONGO_URI is not set in environment variables.")

try:
    client = MongoClient(MONGO_URI)
    client.admin.command('ping')
    print("MongoDB connection successful")


    db = client["khanfaizan151515"]

    def get_db():
        return db

except Exception as e:
    print("MongoDB connection failed:", e)
