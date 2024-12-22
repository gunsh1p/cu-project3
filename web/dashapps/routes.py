from uuid import uuid4

from flask import Blueprint, request ,render_template

from . import dash1


bp = Blueprint("dashes", __name__,template_folder="templates")


@bp.route("/details", methods=["GET"])
def get_detailed_weather():
    cities = request.args.getlist("city")
    params = ''.join(f"city={city}&" for city in cities)[:-1]

    return render_template('dash1.html', dash_url=dash1.URL_BASE, min_height=dash1.MIN_HEIGHT, cities=params, uuid=str(uuid4()))
