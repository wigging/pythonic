"""Routes for the application."""

from flask import Blueprint
from flask import current_app

bp = Blueprint("routes", __name__)


@bp.route("/")
def home():
    """Home page."""
    return "<p>Hello there!</p>"


@bp.route("/config")
def read_config():
    """Display config values."""
    config = current_app.config
    username = config["USERNAME"]
    password = config["PASSWORD"]
    return f"<p>USERNAME is {username}</p><p>PASSWORD is {password}</p>"
