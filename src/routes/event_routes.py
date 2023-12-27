# event_routes.py
from flask import Blueprint, jsonify
from controllers.event_controller import get_all_events

event_blueprint = Blueprint('event_blueprint', __name__)

@event_blueprint.route('/get-all-events', methods=['GET'])
def get_events_route():
    events = get_all_events()
    return jsonify({'events': events})
