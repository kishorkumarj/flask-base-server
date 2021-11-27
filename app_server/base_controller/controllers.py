import os, logging
from flask import Blueprint, request, abort, jsonify, make_response, current_app
from utils import utils

logger = logging.getLogger('app_logger')
bp = Blueprint('api-home', __name__, url_prefix='/api/v1')

@bp.route('/home', methods=(['GET']))
def homepage():
    return jsonify({
        'message': 'Welcome to flask server home API.'
    })

