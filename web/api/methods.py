import requests

import config


def get_location_key(city_name):
    url = f"{config.BASE_URL}/locations/v1/cities/search"
    params = {"apikey": config.API_KEY, "q": city_name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            obj = data[0]
            return {
                "uniq_id": obj["Key"],
                "lat": obj["GeoPosition"]["Latitude"],
                "lon": obj["GeoPosition"]["Longitude"],
            }
    return None


def get_weather_forecast(location_key):
    url = f"{config.BASE_URL}/forecasts/v1/daily/5day/{location_key}"
    params = {"apikey": config.API_KEY, "metric": True}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def get_weather_by_city(city_name: str) -> dict:
    """
    Gets weather data by city name with API.

    :param city_name: City name.
    :return: Dictionary with params (temp, wind, precipitation).
    """
    try:
        location_url = f"{config.BASE_URL}/locations/v1/cities/search"
        location_params = {"apikey": config.API_KEY, "q": city_name}
        location_response = requests.get(location_url, params=location_params)
        location_data = location_response.json()
        location_key = location_data[0]["Key"]

        weather_url = f"{config.BASE_URL}/forecasts/v1/daily/5day/{location_key}"
        weather_params = {"apikey": config.API_KEY, "details": "true", "metric": True}
        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()['DailyForecasts']
        print(weather_data)

        return {
            "temperature_one": weather_data[0]["Temperature"]["Maximum"]["Value"],
            "wind_speed_one": weather_data[0]["Day"]["Wind"]["Speed"]["Value"],
            "precipitation_probability_one": weather_data[0]["Day"].get("PrecipitationProbability", 0),
            
            "temperature_three": weather_data[2]["Temperature"]["Maximum"]["Value"],
            "wind_speed_three": weather_data[2]["Day"]["Wind"]["Speed"]["Value"],
            "precipitation_probability_three": weather_data[2]["Day"].get("PrecipitationProbability", 0),
            
            "temperature_five": weather_data[4]["Temperature"]["Maximum"]["Value"],
            "wind_speed_five": weather_data[4]["Day"]["Wind"]["Speed"]["Value"],
            "precipitation_probability_five": weather_data[4]["Day"].get("PrecipitationProbability", 0),
        }
    except Exception as e:
        raise ValueError(f"Failed to fetch weather data for city {city_name}: {str(e)}")
