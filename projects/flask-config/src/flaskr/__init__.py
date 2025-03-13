"""Application factory for the Flask app.

Run this Flask app with the following terminal command:
uv run flask --app src/flaskr run
"""

from flask import Flask
from dotenv import dotenv_values
from . import routes


def create_app():
    app = Flask(__name__)

    # Load configuration from .env file then store configuration settings in the
    # config attribute of the flask object
    config = dotenv_values(".env")
    app.config.from_mapping(config)

    app.register_blueprint(routes.bp)

    return app
