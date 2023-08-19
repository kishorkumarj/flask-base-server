import os
from flask import Flask
from flask.logging import default_handler
from logging.config import dictConfig
from config import Config

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
app.config.from_object(Config)
app.logger.removeHandler(default_handler)


# Register blueprints
from app.main.controller import bp as main_bp
from app.user.controller import bp as user_bp
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)

@app.route('/test')
def test_route():
    return "<h2>Test page</h2>"
