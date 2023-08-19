from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def home_page():
    return jsonify({
        'message': 'Welcome to flask API server'
    })