from dotenv import load_dotenv
import os
import requests
from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


# Create a model for the searches table
class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    data = db.Column(db.JSON, nullable=False)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('main/index.html')

    @app.route('/weather/<city>')
    def weather(city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=18f0b7f80970aa2219eb77591cbd1c33&units=metric'
        response = requests.get(url)
        data = response.json()
        if data['coord']:
            basic_info = Search(city=city, data=data)
            db.session.add(basic_info)
            db.session.commit()
        return data

    @app.route('/history')
    def history():
        '''Show all queruies from db
        '''
        searches = Search.query.all()
        return render_template('main/weather.html', all_data=searches)

    return app


if __name__ == '__main__':
    app = create_app()
    db.create_all(app=app)
    app.run(debug=True)
