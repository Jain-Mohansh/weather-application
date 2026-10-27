# Python Weather Application

A simple Python application that retrieves current weather information for a city using the Open-Meteo API.

## Features

- Search for a city by name
- Retrieve latitude and longitude using geocoding
- Display current temperature in Celsius
- Display wind speed in km/h
- Handle missing cities and API request errors

## Technologies Used

- Python
- Requests
- Open-Meteo Geocoding API
- Open-Meteo Forecast API

## Installation

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

## Run the Application

`python main.py`

Enter a city name when prompted to view its current weather.

## Future Improvements

- Display humidity and weather conditions
- Show a multi-day forecast
- Improve city selection when multiple places share a name
- Add automated tests
