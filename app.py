from dotenv import load_dotenv
import os
import requests
from flask import Flask, jsonify, render_template

load_dotenv()  # take environment variables from .env file
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
# decorator when someone hit root/above url then following function
# will handle that request
def index():
    return render_template('index.html')


@app.route('/weather/<city>', methods=['GET'])
# city is a parameter, will be captured from url and passed to this function
def get_weather(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    return jsonify(response.json())
