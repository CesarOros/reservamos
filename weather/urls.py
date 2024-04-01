from django.urls import path
from .views import get_weather_by_city_name

urlpatterns = [
    path('', get_weather_by_city_name, name='get_weather_by_city_name'),
]