from django.http import JsonResponse
from .api_client import get_cities_by_name, get_weather_by_cities


def get_weather_by_city_name(request):
    cityname = request.GET.get('cityname', None)
    
    if request.method == 'GET' and cityname:
        try:
            cityname = request.GET.get('cityname', None)
            cities = get_cities_by_name(cityname)
            weather_by_cities = get_weather_by_cities(cities)
            return JsonResponse({"data": weather_by_cities}, status=200)
        except Exception:
            return JsonResponse({"message": "Ocurrió un error con la petición"}, status=500)
    else:
        return JsonResponse({'message': 'Método no permitido o parametros invalidos'}, status=405)