import requests
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = 'nueva_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if "cities" not in session:
        session['cities'] = []
    cities = session['cities']

    if request.method == 'POST':
        new_city = request.form.get('city')
        cities.append(new_city)

    url = 'http://api.openweathermap.org/data/2.5/find?q={}&units=imperial&appid=6666786a40582534aa747dfab4d4c62d'
    weather_data = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        data = res['list'][0]

        weather = {
            'city' : data['name'],
            'temperature' : data['main']['temp'],
            'description' : data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon'],
        }
        weather_data.append(weather)

    session['cities'] = cities

    return render_template('index.html', weather_data=weather_data)