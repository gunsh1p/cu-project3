from flask import Blueprint, request

from .methods import get_weather_by_city, get_location_key
import config


bp = Blueprint("api", __name__)

@bp.route("/get-weather",  methods=["GET"])
def get_weather():
    city_name = request.args.get("city")
    try:
        weather_data = get_weather_by_city(get_location_key(city_name))
    except ValueError:
        return {
            "status": "error",
            "message": f"Ошибка в городе \"{city_name}\", проверьте название",
        }, 400
    if weather_data:
        return {
            "status": "success",
            "data": weather_data
        }, 200
    else:
        return {
            "status": "error",
            "message": "Не удалось получить данные о погоде"
        }, 404
