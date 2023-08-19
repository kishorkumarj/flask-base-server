from flask import Blueprint, jsonify

bp = Blueprint('user-blueprint', __name__, url_prefix='/api/v1')

@bp.route('register', methods=['POST'])
def user_register():
    return jsonify({
        'message': 'Register here'
    })

@bp.route('login', methods=['POST'])
def user_login():
    return jsonify({
        'message': 'login here'
    })