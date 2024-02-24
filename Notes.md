# Weather-Station-Dashboard
<https://home.openweathermap.org/>

# .env
- Load env using load_dotenv() to access environment variables, also include that file in .gitignore

# Virtual environment 
- `python -m venv flask_env` --> will create folder flask_env
- Above will create python virtual environment using the version it was invoked with.
- To check version --> python --version
- inside flask_env folder run `Scripts\activate.bat` --> in vs code in terminal you will see (flask_env) indicationg virtual environment is activated. To deactivate just run `deactivate`

# Docker
- Make sure docker is running. 

## Build Image
- `docker build -t first_flask_docker .` command is used to build a Docker image from a Dockerfile and tag it with a name. for Dockerfile it will look in current working directory. And image will be stored in your local Docker image registry.
- Building image is like running instruction given in Dockerfile line by line. You can rebuild an image when there is some changes in code. Dcoker does layers caching of Dockerfile instructions.

## Run container using image
- `docker run -p 5000:5000 first_flask_docker` command is used to start a Docker container from the first_flask_docker image and map port 5000 of the container to port 5000 of the host machine.
- `docker start <docker_mame>` Above line will start a container from scracth and will give it a random name. This command can be used to run already existed containers. `docker container ls -a`


## Peak in container
- `docker exec -it <container_name_or_id> bash` --> will open a bash terminal. It's same as windows cmd as python base image I am using python:3.8-slim that's linux based image so bash will open. ls to list all files. 

## commands
`docker build -t self_image_name .`
`docker run -d -p 8000:8000 my_image`  --> run container, -d/-it
`docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter`
`docker exec -it <container_name> bash` --> run a bash terminal
`docker pull tensorflow/tensorflow:latest` --> pull image manually or run command will pull if not found

