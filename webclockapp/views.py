from django.shortcuts import render

import requests, json
from decouple import config

# Create your views here.
def index(request):
    req = requests.get(f'https://api.weatherapi.com/v1/current.json?key={config("API_KEY")}&q=Chicago&aqi=no').json()
    fahrenheit = str(int(req['current']['temp_f'])) + '°F'
    # fahrenheit = '72°F'
    context = {'fahrenheit': fahrenheit}
    return render(request, 'index.html', context)