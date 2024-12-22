from flask import Blueprint, render_template


bp = Blueprint("route_creator", __name__, template_folder="templates")

@bp.route("/", methods=["GET"])
def create_form():
    return render_template("index.html")
