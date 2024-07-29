# Weather-Station-Dashboard

- Load env using load_dotenv() to access environment variables, 
- make sure to include that file in .gitignore
# .env
- OPENWEATHERMAP_API_KEY = "your_api_key"
- get your api key from <https://openweathermap.org/appid>

# App Structure
```plaintext
Weather-Station-Dashboard
your_project/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── views.py
│   ├── other_blueprint/
│   │   ├── __init__.py
│   │   ├── views.py
├── static/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── script.js
├── templates/
│   ├── main/
|   |   ├──index.html
│   |   ├── weather.html
│   ├── base.html
├── .env
├── run.py
├── requirements.txt        # All required Python packages
├── Dockerfile              # Instructions for building the Docker image
├── docker-compose.yml      # all instruction to run which container and port exposing just check environment section before run
├── .dockerignore           # (Optional) Exclude files from Docker build context
```


# How to run?

# Create .env file like below in root dir
OPENWEATHERMAP_API_KEY=your_key

# without docker 
## create venv and install requirements.txt and run 'python run.py' in cmd
Create and activate a virtual environment (Windows)
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt --> Install dependencies
- set FLASK_APP=run.py or simply python run.py in cmd

# with online docker image
- docker compose up
- docker run -it --env-file .env -p 5000:5000 usman547/weather-flask-app-repo
- docker run -d -p 5000:5000 -e OPENWEATHERMAP_API_KEY=your_api_key_here usman547/weather-flask-app-repo

# another way is to create docker image from Dockerfile and run a container
- docker build -t name_image .
- docker run -it -p 5000:5000 --env-file .env name_image

# Using github or other codespace
- codespace comes with running docker daemon so, you can do all of the above steps. Docker build, run, compose up after add .env file