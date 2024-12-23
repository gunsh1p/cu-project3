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
        data = {}

        for i in range(len(weather_data)):
            data[f"temperature_{i}"] = weather_data[i]["Temperature"]["Maximum"]["Value"]
            data[f"wind_speed_{i}"] = weather_data[i]["Day"]["Wind"]["Speed"]["Value"]
            data[f"precipitation_probability_{i}"] = weather_data[i]["Day"].get("PrecipitationProbability", 0)

        return data
    except Exception as e:
        raise ValueError(f"Failed to fetch weather data for city {city_name}: {str(e)}")
