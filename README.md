
---

<h1 align="center">FoRe Weather App</h1>
<p align="center">
  A Python based weather dashboard.
</p>

![Fore_screenshot](https://user-images.githubusercontent.com/70502261/170562199-86f0e025-bb8a-41b8-96e6-fdd851d48b5a.png)


### About the app :bulb:
A simple weather app that takes in data from [OpenWeatherAPI](https://openweathermap.org/) and displays various aspects in a dashboard. 

I wanted to explore Python based tools for frontend development especially because Python is the go to language for Data Science projects. Most of the time I have found that most python developers have to deal with the stress of working with JavaScript to build responsive web apps for their projects.
I designed the weather dashboard that will dynamically retrieve and display weather maps and a graph of the temperatures of a specific location. Hard as it may be to imagine, a lot of the code for this app is in pure Python thanks to Dash and other wrapper libraries.

* View the webapp [here](https://foreweatherapp.herokuapp.com/)
* View the blog [here](https://medium.com/@joywanjiru879/fore-weather-app-745daff2bea7)



### How it works :feet:

A user selects a location from the dropdowm menu and gets to see the current weather status, temperatures both minimum and maximum, the humidity as a percentage as well as the weather icon displayed on that location's map. They also get to see a graph of 5-day temperature forecasts. A sneak preview is shown below:


https://user-images.githubusercontent.com/103201519/171522868-43c5661f-f0a0-45ef-b9fb-13dcde3b2394.mp4

### Main libraries used: :books:

| Tool/Library                                                   | Purpose                      |
| -------------------------------------------------------------- | -----------------------------|
| [Dash](https://dash.plotly.com/)                               | Dashboard design            |
| [Dash Leaflet](https://dash-leaflet.herokuapp.com/)            | Responsive maps              |
| [Plotly](https://plotly.com/python)                            | Interactive Graphs   :bar_chart:        |
| [pyowm](https://pypi.org/project/pyowm/)                       | Connect to OpenWeatherMap    |
| [Geopy](https://pypi.org/project/geopy/)                       | Get coordinates of locations :round_pushpin: |
| [datetime](https://docs.python.org/3/library/datetime.html)    | display forecast dates  :date:     |
| [mapbox](https://www.mapbox.com/maps/)                         | create custom tile map       |

### Main Feature :pushpin:
User selects a location and gets all the latest weather information displayed in a visually pleasing manner. 

![Copy of FoRe MVP first look drawio (1)](https://user-images.githubusercontent.com/103201519/171530788-014f2353-f006-4bbd-829f-91fed1a5ec7d.png)

All this is made possible through Dash.
Dash has two main parts:
* Layout - the HTML and DCC components that design the static webpage
* Callbacks - Inputs and Outputs that define how the webpage becomes dynamic

### Installation :inbox_tray:

#### Prerequisites:

- [ ] An OpenWeatherMap free account which will give you access to an API key
- [ ] Choose a map tile layer of your choice either by creating a [mapbox free account](https://account.mapbox.com/auth/signup/) and designing your tiles in mapbox studio or choosing from the existing list of available [tile options](http://leaflet-extras.github.io/leaflet-providers/preview/)


         
              git clone this project into your machine
              pip install -r requirements.txt
 
### Licensing :lock:
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Her-o1/weather_project/blob/main/LICENSE) file for details.

### Future
I am looking forward to collecting more data and completing this project from a data science perspective. The main inspiration being that it is not enough to just present numbers to people. What does a forecast of 26 degrees celsius minimum temperatures really mean for a farmer or a traveller? I am keen on exploring weather variables and how they affect various demographies and how we can assimilate an informative product that shows forecasts and recommended activities.

If you have any ideas or suggestions or conributions feel free to reach out to me via [mail](joywanjiru879@gmail.com) :e-mail:


### Author :black_nib:
#### Joy Wanjiru

I am a data science enthusiast and a software engineer and I love working with Python especially because of it's vast pool of libraries for scientific computing




