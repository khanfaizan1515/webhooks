# app.py
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
from webhook_routes import webhook_bp
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
PORT = int(os.getenv("PORT", 5000))

client = MongoClient(MONGO_URI)
db = client["webhooks_db"]
collection = db["events"]

app = Flask(__name__)
app.config["DB_COLLECTION"] = collection

app.register_blueprint(webhook_bp)

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
