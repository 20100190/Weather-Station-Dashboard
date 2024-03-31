from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/weather/<city>')
def get_weather(city):
    api_key = '18f0b7f80970aa2219eb77591cbd1c33'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == '200':
        weather_data = response.json()
        # Process weather data as needed
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

# Create a model for the searches table
class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

# Create all database tables within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the weather search
@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']

        # Check if the city exists in the database
        search = Search.query.filter_by(city=city).first()

        if search:
            # If city exists in database, retrieve weather data from database
            return jsonify({'city': search.city,
                            'temperature': search.temperature,
                            'description': search.description,
                            'humidity': search.humidity})

        else:
            # If city not found in database, make API request to fetch weather data
            # After getting data from API, store it in database and return to user
            # Make sure to handle API request and response properly

            # Sample code to make API request (Replace with actual implementation)
            weather_data = {'city': 'City Name', 'temperature': 'Temperature', 'description': 'Description', 'humidity': 'Humidity'}

            new_search = Search(city=city, temperature=weather_data['temperature'], 
                                description=weather_data['description'], humidity=weather_data['humidity'])
            db.session.add(new_search)
            db.session.commit()

            return jsonify(weather_data)

    return render_template('weather.html')

# Route to display all records in the database
@app.route('/searches')
def all_searches():
    searches = Search.query.all()
    return render_template('searches.html', searches=searches)

if __name__ == '__main__':
    app.run(debug=True)

