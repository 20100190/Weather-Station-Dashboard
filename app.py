from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = "18f0b7f80970aa2219eb77591cbd1c33"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather/<city>')
def weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid="18f0b7f80970aa2219eb77591cbd1c33"&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    weather_data = weather(city)

    # Store queried cities in session
    if 'cities' not in session:
        session['cities'] = []
    session['cities'].append(city)

    return render_template('weather.html', weather_data=weather_data, cities=session['cities'])

if __name__ == '__main__':
    app.run(debug=True)
