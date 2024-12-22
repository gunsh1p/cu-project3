from flask import Flask
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from urllib.parse import parse_qs

from api.methods import get_location_key, get_weather_by_city
from .graphs import create_precipitation_graph, create_temperature_graph, create_wind_speed_graph, create_map

APP_ID = 'dash_app_1'
URL_BASE = '/dash/dash_app_1/'
MIN_HEIGHT = 200

def add_dash(server: Flask):
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
    ]

    app = dash.Dash(
        server=server,
        url_base_pathname=URL_BASE,
        suppress_callback_exceptions=True,
        external_stylesheets=external_stylesheets
    )


    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        dcc.Dropdown(
            id='weather-parameter',
            options=[
                {'label': 'Temperature', 'value': 'temperature'},
                {'label': 'Precipitation', 'value': 'precipitation'},
                {'label': 'Wind Speed', 'value': 'wind_speed'}
            ],
            value='temperature'

        ),
        dcc.Graph(id='weather-graph', style={'height': '500px'}),
        dcc.Graph(id='weather-map', style={'height': '500px'}),
    ])

    @app.callback(
        [
            Output('weather-graph', 'figure'),
            Output('weather-map', 'figure')
        ],
        [
            Input('weather-parameter', 'value'),
            Input('url', 'search'),
        ],
    )
    def update_graph(selected_parameter, cities):
        params = parse_qs(cities[1:])
        cities = params['city']
        uuid = params['uuid'][0]
        if not hasattr(update_graph, "data"):
            update_graph.data = {}
        if update_graph.data.get(uuid) is None:
            data = []

            for city in cities:
                uniq_id, lat, lon = get_location_key(city).values()
                weather_data = get_weather_by_city(uniq_id)
                weather_data["lat"] = lat
                weather_data["lon"] = lon
                data.append(weather_data)
            
            data = pd.DataFrame(data)
            data['city'] = cities
            data = data[['city', 'temperature', 'precipitation_probability', 'wind_speed', 'lat', 'lon']]
            update_graph.data[uuid] = data
            print(data)
        
        if selected_parameter == 'temperature':
            graph = create_temperature_graph(update_graph.data[uuid])
        elif selected_parameter == 'precipitation':
            graph = create_precipitation_graph(update_graph.data[uuid])
        elif selected_parameter == 'wind_speed':
            graph = create_wind_speed_graph(update_graph.data[uuid])

        return graph, create_map(update_graph.data[uuid])
        

    return server
