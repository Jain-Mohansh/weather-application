import requests


def get_coordinates():
    city = input('Enter your city name : ').capitalize()
    params = {'name' : city,
            'language' : 'en',
            'format' : 'json'}
    try:
        response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=params, timeout=10)
        response.raise_for_status()
        json = response.json()
        
    except requests.RequestException as error:
        print(f"Unable to fetch weather data. Please check your internet connection and try again.")
        print(f"Error details: {error}")
        return 
    
    if json.get('results'):
        results = json['results'][0]
        latitude = results['latitude']
        longitude = results['longitude']
        return latitude, longitude

    else:
        print(f"Can't fetch data for {city}")


# get_coordinates()

def get_weather():
    location = get_coordinates()
    if location:
        try:
            params = {'latitude' : location[0], 'longitude' : location[1], 'timezone_abbreviation':	"GMT+5:30",'timezone':"Asia/Kolkata", 'current' : ['temperature_2m', 'wind_speed_10m']}
            response = requests.get('https://api.open-meteo.com/v1/forecast', params=params, timeout=10)
            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Unable to fetch weather data. Please check your internet connection and try again.")
            print(f"Error details: {error}")
            return
        
        data = response.json()
        print(f"Temperature : {data['current']['temperature_2m']}°C")
        print(f"Wind Speed : {data['current']['wind_speed_10m']} Km/h")
                


get_weather()
