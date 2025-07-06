# webhook_routes.py
from flask import Blueprint, request, jsonify
from db_service import save_event, fetch_events
from event_model import map_github_event

webhook_bp = Blueprint('webhook_bp', __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def github_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    data = request.json
    event_doc = map_github_event(event_type, data)
    save_event(event_doc)
    return jsonify({"message": "Event stored"})

@webhook_bp.route("/events", methods=["GET"])
def get_events():
    events = fetch_events()
    return jsonify(events)
