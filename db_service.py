# db_service.py

def save_event(collection, event_doc):
    collection.insert_one(event_doc)

def fetch_events(collection):
    events = list(collection.find({}, {"_id": 0}).sort("timestamp", -1))
    return events
