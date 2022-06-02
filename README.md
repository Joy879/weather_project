
---

<h1 align="center">FoRe Weather App</h1>
<p align="center">
  A Python based weather dashboard.
</p>

![Fore_screenshot](https://user-images.githubusercontent.com/70502261/170562199-86f0e025-bb8a-41b8-96e6-fdd851d48b5a.png)


### About the app :bulb:
A simple weather app that takes in data from [OpenWeatherAPI](https://openweathermap.org/) and displays various aspects in a dashboard.
I designed the weather dashboard that will dynamically retrieve and display weather maps and a graph of the temperatures of a specific location

### How it works :feet:

A user selects a location from the dropdowm menu and gets to see the current weather status, temperatures both minimum and maximum, the humidity as a percenatge as well as the weather icon displayed on that location's map. They also get to see a graph of 5-day temperature forecasts. A sneak preview is shown below:


https://user-images.githubusercontent.com/103201519/171522868-43c5661f-f0a0-45ef-b9fb-13dcde3b2394.mp4

Main libraries used are:
* Dash
* Dash leaflet
* Geopy
* Plotly
* pyowm

* View the webapp [here](https://foreweatherapp.herokuapp.com/)
* View the blog [here](https://medium.com/@joywanjiru879/fore-weather-app-745daff2bea7)
* [LinkedIn](https://www.linkedin.com/in/joy-wanjiru-b717a0240/)

### Installation

Prerequisites:
* An OpenWeatherMap free account which will give you access to an API key
* Choose a map tile layer of your choice either by creating a [mapbox free account](https://account.mapbox.com/auth/signup/) and designing your tiles in mapbox studio or choosing from the existing list of available [tile options](http://leaflet-extras.github.io/leaflet-providers/preview/)


         
              git clone this project into your machine
              pip install -r requirements.txt
        


### Usage


### Contributing

### Related projects

### Licensing :lock:
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Her-o1/weather_project/blob/main/LICENSE) file for details.
