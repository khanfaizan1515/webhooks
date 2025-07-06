# db_service.py
from flask import current_app

def save_event(event_doc):
    collection = current_app.config["DB_COLLECTION"]
    collection.insert_one(event_doc)

def fetch_events():
    collection = current_app.config["DB_COLLECTION"]
    events = list(collection.find().sort("timestamp", -1))
    for e in events:
        e["_id"] = str(e["_id"])
    return events
    