import os
from flask import Flask
from flask.logging import default_handler
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'app_logger': {
        'handlers': ['oam_handler'],
        'level': os.environ.get('LOG_LEVEL', 'INFO'),
        'propagate': True,
    }
})

app = Flask(__name__)
app.config.from_object('config')
app.logger.removeHandler(default_handler)

# register blueprints
from app_server.base_controller.controllers import bp as base_bp
app.register_blueprint(base_bp)