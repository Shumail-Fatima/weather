from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):

    #city_name = 'Islamabad'
    API_key = '092575f84681c1fd4f2f6258d443790e'
    #url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'
        get_site_info = requests.get(url)
        if get_site_info.status_code == 200:
            data = get_site_info.json()
            #print(data)

        city_weather = {
        "city": city.name,
        "Weather_Description": data['weather'][0]['description'],
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "humididty": data['main']['humidity'],
        "Visibility": data['visibility'],
        "wind_speed": data['wind']['speed'],
        "icon" : data['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/weather.html', context)



