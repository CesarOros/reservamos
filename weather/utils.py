from datetime import datetime
CITY = 'city'

def filter_by_cities(places):
    return list(filter(lambda place: place.get("result_type","") == CITY, places))

def get_max_min_temperature_by_days(weather_data):
    weather_data_daily = weather_data.get("daily", [])

    return [
        { 
            "min": daily.get("temp", {}).get("min", ""),
            "max": daily.get("temp", {}).get("max", ""),
            "date": datetime.fromtimestamp(daily.get("dt", None)).strftime("%Y-%m-%d %H:%M:%S")
        }  
        for daily in weather_data_daily
    ]


def filter_data(cities):
    return [ 
            {
                "city": city.get("name"), 
                "state": city.get("state"), 
                "country": city.get("country"),
                "lat": city.get("lat"),
                "long": city.get("long") 
            } 
        for city in cities 
    ]
