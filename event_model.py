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
        event_doc["author"] = data.get("pusher", {}).get("name")
        event_doc["to_branch"] = data.get("ref", "").split("/")[-1]

    elif event_type == "pull_request":
        pr = data.get("pull_request", {})
        event_doc["author"] = pr.get("user", {}).get("login")
        event_doc["from_branch"] = pr.get("head", {}).get("ref")
        event_doc["to_branch"] = pr.get("base", {}).get("ref")

    elif event_type == "merge":
        event_doc["author"] = data.get("sender", {}).get("login")
        event_doc["from_branch"] = data.get("pull_request", {}).get("head", {}).get("ref")
        event_doc["to_branch"] = data.get("pull_request", {}).get("base", {}).get("ref")

    return event_doc
