import plotly.graph_objs as go
import plotly.express as px
import numpy as np

def create_temperature_graph(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['city'], y=data['temperature'], mode='lines+markers', name='Temperature'))
    fig.update_layout(
        title='Temperature Over Time',
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        hovermode='x unified'
    )
    return fig

def create_precipitation_graph(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['city'], y=data['precipitation_probability'], mode='lines+markers', name='Precipitation'))
    fig.update_layout(
        title='Precipitation Over Time',
        xaxis_title='Date',
        yaxis_title='Precipitation (mm)',
        hovermode='x unified'
    )
    return fig

def create_wind_speed_graph(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['city'], y=data['wind_speed'], mode='lines+markers', name='Wind Speed'))
    fig.update_layout(
        title='Wind Speed Over Time',
        xaxis_title='Date',
        yaxis_title='Wind Speed (m/s)',
        hovermode='x unified'
    )
    return fig

def create_map(data):
    maxlon, minlon = np.amax(data["lon"]), np.amin(data["lon"])
    maxlat, minlat = np.amax(data["lat"]), np.amin(data["lat"])

    center = {
        'lon': round((maxlon + minlon) / 2, 6),
        'lat': round((maxlat + minlat) / 2, 6)
    }
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lat=data['lat'],
        lon=data['lon'],
        hovertext=data['city'] + '<br>Temperature: ' + data['temperature'].astype(str) + '°C' + '<br>Wind Speed: ' + data['wind_speed'].astype(str) + ' km/h' + '<br>Precipitation: ' + data['precipitation_probability'].astype(str) + ' mm',
        mode='lines+markers',
        marker=dict(size=5, color='blue'),
    ))
    
    fig.update_layout(
        title='Weather Forecast for Multiple Locations',
        geo=dict(
            scope='world',
            showland=True,
            landcolor='lightgray',
            countrycolor='white'
        ),
        template='plotly_white',
    )

    return fig
