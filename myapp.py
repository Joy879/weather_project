#importing libraries

#import datetime as datetime
from pyowm.owm import OWM
from dash import Dash, dcc, html,Input, Output
import dash_leaflet as dl
from datetime import datetime
from geopy.geocoders import Nominatim
import plotly.graph_objects as go

#Initializing Geocoding API, Mapbox tiles  and pyowm
loc = Nominatim(user_agent="GetLoc")
owm = OWM(API_KEY)
mgr = owm.weather_manager()
url ='https://api.mapbox.com/styles/v1/joywanjiru/cl3g3s8od004314qqtvggn6t9/tiles/256/{z}/{x}/{y}@2x?access_token=access_token'

# Create dash app.

app = Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

# Designing the layout using html and dcc components
app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="four columns div-user-controls",
                    children=[
                        html.H2("FoRe Weather app"),
                        html.P(
                            """Select different locations using the drop down menu """
                        ),
                        # Change to side-by-side for mobile layout
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        # Dropdown for locations on map
                                        dcc.Dropdown(
                                            options=[
                                                    {'label': 'Nairobi', 'value': 'Nairobi, KE'},
                                                    {'label': 'Kampala', 'value': 'Kampala, UG'},
                                                    {'label': 'Dodoma', 'value': 'Dodoma, TZ'},
                                                    {'label': 'Bujumbura', 'value': 'Bujumbura, BI'},
                                                    {'label': 'Kigali', 'value': 'Kigali, RW'},
                                                ],
                                            value='Nairobi, KE',
                                            id="location-dropdown",
                                            placeholder="Select a location",
                                        ),
                                    ],
                                ),
                                
                            ],
                        ),
                        # Dis for current weather information
                        html.Div(
                            className="flex-gap",
                            children=[
                                html.Div(id="weather-status", className="status"),                           
                                html.Div( id="temp", className="status"),
                                html.Div( id="max-temp", className="status"),
                                html.Div( id="min-temp", className="status"),
                                html.Div( id="humidity", className="status"),
                            ],
                        ),
                    ],
                ),
                # Column for app graphs and plots
                html.Div(
                    className="eight columns div-for-charts bg-grey",
                    children=[
                        dl.Map(id ="map-graph",
                            style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}
                            ),
                        dcc.Graph(id="histogram"),
                    ],
                ),
            ],
        )
    ]
)
#setting up the callbacks

#Output 1: current weather status
@app.callback(
    Output('weather-status', 'children'),
    Input('location-dropdown', 'value')
)
def update_weather(value):
    """A function that updates the weather status e.g scattered clouds, light rain"""
    weather = mgr.weather_at_place(value).weather
    return f'{weather.detailed_status}'

#Output 2: current temperature
@app.callback(
    Output('temp', 'children'),
    Input('location-dropdown', 'value')
)
def update_temp(value):
    """A function that updates the current temperature in degrees celsius"""
    temperature = mgr.weather_at_place(value).weather.temperature('celsius')["temp"]
    return f'Temp in celsius:  {temperature}'


#Output 3: current minimum temperatures
@app.callback(
    Output('min-temp', 'children'),
    Input('location-dropdown', 'value')
)
def update_tempmin(value):
    """A function that updates current minimum temperature in degrees celsius"""
    temp_min = mgr.weather_at_place(value).weather.temperature('celsius')["temp_min"]
    return f'Min temp:  {temp_min}'

#Output 4: current weather status
@app.callback(
    Output('max-temp', 'children'),
    Input('location-dropdown', 'value')
)
def update_tempmax(value):
    """A function that updates the current maximum temperature in degrees celsius"""
    temp_max = mgr.weather_at_place(value).weather.temperature('celsius')["temp_max"]
    return f'Max temp:  {temp_max}'

#Output 5: current humidity
@app.callback(
    Output('humidity', 'children'),
    Input('location-dropdown', 'value')
)
def update_humidity(value):
    """A function that updates the current humidity in percentage """
    humidity = mgr.weather_at_place(value).weather.humidity
    return f'Humidity is {humidity} %'

#Output 6: current weather icon and temperature displayed on leaflet maps
@app.callback(
    Output('map-graph', 'children'),
    Input('location-dropdown', 'value')
)
def update_map(value):
    """A function that updates the weather icon and temperature of a location and dsipalys them on the location in a map"""
    icon = mgr.weather_at_place(value).weather.weather_icon_url(size='2x')
    temperature = mgr.weather_at_place(value).weather.temperature('celsius')["temp"]
    getloc = loc.geocode(value)
    iconlat = getloc.latitude
    iconlon = getloc.longitude
    icon_={
        "iconUrl":f'{icon}',
    # "shadowUrl": None,
        "iconSize": [100, 100],  # size of the icon
    # size of the shadow
        "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
   
        }
    return dl.Map( 
        [
            dl.TileLayer(url=url ),#setting up custom mapbox tile
            dl.Marker(
                position=(iconlat, iconlon),#centering the icon on the location's coordinates
                icon=icon_,
            ),
            dl.Popup( f'Temperature is {temperature}', position=(iconlat,iconlon))
                
        ],center=(getloc.latitude, getloc.longitude)#centering the map on the location's coordinates
        )

#Output 7: weather forecasts displayed in a bar-graph
@app.callback(
    Output('histogram', 'figure'),
    Input('location-dropdown', 'value')
)
def update_graph(value):
    """A function that updates the graph to show 5-day temperature forecasts """
    days = []
    dates = []
    temp_min = []
    temp_max = []
    forecaster = mgr.forecast_at_place(value, '3h')
    forecast=forecaster.forecast
    for weather in forecast:
        day=datetime.utcfromtimestamp(weather.reference_time())
        #day = gmt_to_eastern(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature('celsius')['temp']
        if not temp_min[-1] or temperature < temp_min[-1]:
            temp_min[-1] = temperature
        if not temp_max[-1] or temperature > temp_max[-1]:
            temp_max[-1] = temperature
    #using plotly graph objects to make two bar graphs
    fig = go.Figure(
        data=[
            go.Bar(
                name='min temps',
                x=days, 
                y=temp_min,
                marker=dict(color=temp_min,
                colorscale='viridis')),
            go.Bar(
                name='max temps',
                x=days,
                y=temp_max,
                marker=dict(color=temp_max,
                colorscale='viridis')
                )
        ],
        layout=dict(
            title =f'Temperature forecast for {value}',
            xaxis = dict(title =None, showgrid=False),
            yaxis = dict(title ="Temperature (C)", showgrid = False)
        ),
    )
    #styling the bar graphs
    fig.update_layout(
        barmode='group',
        paper_bgcolor="rgba(0,0,0,0)", 
        plot_bgcolor = "rgba(0,0,0,0)",
        font_color="#e7d7f1",
        title={'y':0.85,'x':0.5,'xanchor': 'center','yanchor': 'top'},
        title_font_family="Century Gothic",
        title_font_color="#e7d7f1",
        title_font_size=20,
    )
    return fig



if __name__ == '__main__':  
    app.run_server(debug=True)






