import os
import requests
from dotenv import load_dotenv
from .utils import filter_by_cities, get_max_min_temperature_by_days

load_dotenv()

API_KEY = os.getenv("API_KEY") 
BASE_URL_OPEN_WEATHER = os.getenv("BASE_URL_OPEN_WEATHER")
BASE_URL_RESERVAMOS = os.getenv("BASE_URL_RESERVAMOS")

SUCCESS_STATUS_CODE_OPENWEATHER = 200
SUCCESS_STATUS_CODE_RESERVAMOS = 201

def get_weather_data_by_location(lat, long):
    url = f'{BASE_URL_OPEN_WEATHER}?lat={lat}&lon={long}&appid={API_KEY}&exclude=minutely,current,hourly,alerts'
    try:
        response = requests.get(url)
        place_data = {}
        
        if response.status_code == SUCCESS_STATUS_CODE_OPENWEATHER:
            place_data = response.json()
        return place_data
    except requests.exceptions.RequestException as request_exception:
        # Manejar errores de solicitud HTTP
        print('Ocurrió un error al realizar la petición', request_exception)
    except Exception as e:
        print('Ocurrió un error en el metodo get_weather_data_by_location', e)
    return None
    
def get_cities_by_name(cityname):
    url = f'{BASE_URL_RESERVAMOS}?q={cityname}'    
    try:
        response = requests.get(url)

        cities = []
        if response.status_code == SUCCESS_STATUS_CODE_RESERVAMOS:
            places = response.json()
            cities = filter_by_cities(places)
        return cities
    except requests.exceptions.RequestException as e:
        print('Ocurrió un error al realizar la petición', e)
    except Exception as e:
        print('Ocurrió un error en el metodo get_cities_by_name()', e)
    return None


def get_weather_by_cities(cities):
    cities_parsed_data = []
    for city in cities:
        if "lat" in city and "long" in city:
            weather_by_location = get_weather_data_by_location(city["lat"], city["long"])
            temperature_by_days = get_max_min_temperature_by_days(weather_by_location)
            cities_parsed_data.append({
                "city": city.get("city_name"), 
                "state": city.get("state"), 
                "country": city.get("country"),
                "lat": city.get("lat"),
                "long": city.get("long"),
                "next_seven_days_weather": temperature_by_days
            } )
    return cities_parsed_data


