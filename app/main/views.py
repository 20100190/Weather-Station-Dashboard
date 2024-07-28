import os
from dotenv import load_dotenv

from flask import jsonify, render_template
import requests
from app.models import Search  # if it were a modul then we do not need app
from app import db
from . import main

load_dotenv()


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/weather/<city>')
def weather(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    data = response.json()
    if 'coord' in data:
        basic_info = Search(city=city, data=data)
        db.session.add(basic_info)
        db.session.commit()
    return jsonify(data)


@main.route('/history')
def history():
    searches = Search.query.all()
    return render_template('main/weather.html', all_data=searches)
