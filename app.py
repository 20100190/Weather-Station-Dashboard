from dotenv import load_dotenv
import os
import requests
from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')    

    db.init_app(app)
    with app.app_context():
        from models import BasicInfo
        db.create_all()

    from models import BasicInfo

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/weather/<city>')
    def weather(city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=18f0b7f80970aa2219eb77591cbd1c33&units=metric'
        response = requests.get(url)
        data = response.json()
        basic_info = BasicInfo(time=datetime.now(), city=city, data=data)
        db.session.add(basic_info)
        db.session.commit()
        return data

    @app.route('/history')
    def history():
        '''Show all queruies from db
        '''
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    db.create_all(app=app)
    app.run(debug=True)