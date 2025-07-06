# webhook_routes.py

from flask import Blueprint, request, jsonify, current_app
from event_model import map_github_event
from db_service import save_event, fetch_events

webhook_bp = Blueprint("webhook_bp", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def handle_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    data = request.json

    if not event_type or not data:
        return jsonify({"error": "Invalid payload"}), 400

    event_doc = map_github_event(event_type, data)
    if event_doc:
        save_event(current_app.config["DB_COLLECTION"], event_doc)
        return jsonify({"message": "Event stored"}), 200
    else:
        return jsonify({"message": "Unknown event type"}), 400


@webhook_bp.route("/events", methods=["GET"])
def get_events():
    events = fetch_events(current_app.config["DB_COLLECTION"])
    return jsonify(events)
