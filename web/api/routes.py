from flask import Blueprint

bp = Blueprint("api", __name__)

@bp.route("/")
def get_api():
    return "The API!"