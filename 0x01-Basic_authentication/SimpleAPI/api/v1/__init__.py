from flask import Blueprint, jsonify

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'])
def get_status() -> dict:
    """Return the API status."""
    return {'status': 'OK'}