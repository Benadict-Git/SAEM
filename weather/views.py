import requests
from django.shortcuts import render

API_KEY = "7e97e76e2742cb1988aa64e46ddf5d5c"

def weather_forecast(request):
    city = "Your City"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    
    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'humidity': weather_data['main']['humidity'],
        'weather': weather_data['weather'][0]['description'],
    }
    return render(request, 'weather/weather.html', context)
