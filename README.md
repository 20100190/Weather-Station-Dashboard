# Weather-Station-Dashboard

- Load env using load_dotenv() to access environment variables, also include that file in .gitignore
# .env
- OPENWEATHERMAP_API_KEY = "your_api_key"

/Weather-Station-Dashboard
│
├── app.py         # Your main Flask application file
├── requirements.txt   # All required Python packages
├── Dockerfile     # Instructions for building the Docker image
├── .dockerignore  # (Optional) Exclude files from Docker build context
└── /templates     # (Optional) Folder for Jinja2 templates
    └── index.html 


- How to run?
git clone <URL-of-your-remote-repository>
cd myflaskapp  # Replace with the actual directory name of the cloned repository.

# without docker --> create venv and install req.txt and run app
- python -m venv venv --> Create and activate a virtual environment (Windows)
- venv\Scripts\activate
- pip install -r requirements.txt --> Install dependencies
- create .env file to populate your key, in docker that can be passed as cmd argument or you can pass it
- set FLASK_APP=app.py  # Or whichever file contains your Flask app
- flask run --> # Run the Flask app

# with docker --> create named image and then run a container using named image.
- docker build -t myflaskapp .
- docker run -e OPENWEATHERMAP_API_KEY=you_api_key -p 5000:5000 myflaskapp
- or pusblish docker image so people can use it directly

# online docker image
- create a repositry at --> <https://hub.docker.com/repositories/usman547>
- tag your local image with docker username and repositry name
- `docker tag local-image-name usman547/repo-name` --> this will point the image using pointer
- `docker push new-image-name-that-has-docker-username`

# docker compose
- It can be used to run multiple containers and can be set to which ports to expose
- and can set environemnt variables. 
- just run `docker compose up` in directory where we docker-compose.yml and do edit env variable in it.