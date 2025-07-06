# event_model.py
from datetime import datetime

def map_github_event(event_type, data):
    event_doc = {
        "event_type": event_type,
        "author": None,
        "from_branch": None,
        "to_branch": None,
        "timestamp": datetime.utcnow().isoformat()
    }

    if event_type == "push":
        event_doc["author"] = data["pusher"]["name"]
        event_doc["to_branch"] = data["ref"].split("/")[-1]

    elif event_type == "pull_request":
        event_doc["author"] = data["pull_request"]["user"]["login"]
        event_doc["from_branch"] = data["pull_request"]["head"]["ref"]
        event_doc["to_branch"] = data["pull_request"]["base"]["ref"]

    return event_doc
